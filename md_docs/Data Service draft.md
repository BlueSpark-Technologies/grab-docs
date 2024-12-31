# Data Service draft

In the first phase of the implementation it was decided to have o bigger application consisting of multiple components:

* Exasol importer - runs once a day
* Whitelist/Blacklist importer - runs every hour; it will cache the lists; it will get the latest feed service data for each product from the final list; it will send this data to DataService API
* Voucher codes importer - runs every hour
* DataService API - it will receive data from FeedService once a new price feed is imported
* Vouchers csv file distributor - should run after all the previous jobs had run.

TODO:

* Make a clear data workflow.
* Technical approval.
* Business approval.

## "Data flow" proposal:
https://www.lucidchart.com/documents/edit/b38f99d8-f112-4e20-b669-e97517e9fd26/0

### A) Importing white list, black list, voucher code data and computing eligible product list
* Should run as frequently as possible/reasonable (maybe every few minutes)
* Should run as a separate application container (possibly lambda function) which will poll the FTP server with the indicated frequency and will retrieved the latest versions of the white list, black list and voucher code CSV files
* The same process will compute the eligible product list with/without (TBD) looking at the Product DB table and will:identify whether there are any changes to the previously computed eligible product listsave the new product listcall (async) a Data Service API endpoint with the PRODUCT_ID for every PRODUCT_ID which is an addition to the previous list – the endpoint will trigger a voucher computation (to be detailed below) – ENDPOINT 2remove any vouchers from the computed vouchers DB table if they were previously in the eligible product list and they were removed after the update – TBD
* identify whether there are any changes to the previously computed eligible product list
* save the new product list
* call (async) a Data Service API endpoint with the PRODUCT_ID for every PRODUCT_ID which is an addition to the previous list – the endpoint will trigger a voucher computation (to be detailed below) – ENDPOINT 2
* remove any vouchers from the computed vouchers DB table if they were previously in the eligible product list and they were removed after the update – TBD

### B) Importing Products from Exasol
* Should run once a day
* Should run as a separate application container (possibly lambda function) which will import all the products (using the existing query written by Christian) to the Data Service DB
* Once the import is finished the same process will:remove any vouchers from the computed vouchers DB table if they were previously in the vouchers DB table but the products were not imported this time; the imported_at field in the DB can be used for this – TBDcall (async) a Data Service API endpoint with the PRODUCT_ID for every PRODUCT_ID which was imported AND is in the list of eligible products currently stored – the endpoint will trigger a voucher computation (to be detailed below) – ENDPOINT 2
* remove any vouchers from the computed vouchers DB table if they were previously in the vouchers DB table but the products were not imported this time; the imported_at field in the DB can be used for this – TBD
* call (async) a Data Service API endpoint with the PRODUCT_ID for every PRODUCT_ID which was imported AND is in the list of eligible products currently stored – the endpoint will trigger a voucher computation (to be detailed below) – ENDPOINT 2

### C) Computing vouchers
* The original endpoint from Voucher 0.2 Service Architecture diagram (Tech. Discussion)
* Will be triggered by Feed Service updates
* Will accept the POST method and a Feed Item object in the payload
* Will do the following:Will look up the product for which the Feed Item is relevant in the eligible product list – which is permanently updated as described in section AWill look up the product for which the Feed Item is relevant in the Product table of the DB – which is updated once a day as described in section BIf the product is missing from either the product list or the products DB, then there should be no voucher calculation and, if it exists, the voucher code for the current product should be removed from the vouchers DB tableIf the product exists and is eligible, a voucher computation will be triggered for this element only (call to Voucher Service)If a voucher was not retrieved then, if it exists, the voucher code for the current product should be removed from the vouchers DB tableIf a voucher is retrieved then it should be saved to the Voucher table (will be described below) w/ "distributed" == False
* Will look up the product for which the Feed Item is relevant in the eligible product list – which is permanently updated as described in section A
* Will look up the product for which the Feed Item is relevant in the Product table of the DB – which is updated once a day as described in section B
* If the product is missing from either the product list or the products DB, then there should be no voucher calculation and, if it exists, the voucher code for the current product should be removed from the vouchers DB table
* If the product exists and is eligible, a voucher computation will be triggered for this element only (call to Voucher Service)
* If a voucher was not retrieved then, if it exists, the voucher code for the current product should be removed from the vouchers DB table
* If a voucher is retrieved then it should be saved to the Voucher table (will be described below) w/ "distributed" == False

* An additional endpoint for computing vouchers, to be used in case trigger is not Feed Service
* Will be triggered by either scenarios A or B, as described above
* Will not require a payload, just a PRODUCT_ID
* Will do the following:Will look up the product for which the Feed Item is relevant in the eligible product list – which is permanently updated as described in section AWill look up the product for which the Feed Item is relevant in the Product table of the DB – which is updated once a day as described in section BIf the product is missing from either the product list or the products DB, then there should be no voucher calculation and, if it exists, the voucher code for the current product should be removed from the vouchers DB tableWill fetch the latest available Feed Service information for the given PRODUCT_ID via an HTTP call to Feed ServiceIf no Feed Service information is available for the given PRODUCT_ID then, if it exists, the voucher code for the current product should be removed from the vouchers DB table ??? - TBDIf the product exists and is eligible, a voucher computation will be triggered for this element only (call to Voucher Service)If a voucher was not retrieved then, if it exists, the voucher code for the current product should be removed from the vouchers DB tableIf a voucher is retrieved then it should be saved to the Voucher table (will be described below) w/ "distributed" == False
* Will look up the product for which the Feed Item is relevant in the eligible product list – which is permanently updated as described in section A
* Will look up the product for which the Feed Item is relevant in the Product table of the DB – which is updated once a day as described in section B
* If the product is missing from either the product list or the products DB, then there should be no voucher calculation and, if it exists, the voucher code for the current product should be removed from the vouchers DB table
* Will fetch the latest available Feed Service information for the given PRODUCT_ID via an HTTP call to Feed Service
* If no Feed Service information is available for the given PRODUCT_ID then, if it exists, the voucher code for the current product should be removed from the vouchers DB table ??? - TBD
* If the product exists and is eligible, a voucher computation will be triggered for this element only (call to Voucher Service)
* If a voucher was not retrieved then, if it exists, the voucher code for the current product should be removed from the vouchers DB table
* If a voucher is retrieved then it should be saved to the Voucher table (will be described below) w/ "distributed" == False
* Notice how just steps 4-5 differ from the flow of ENDPOINT 1

### D) Distributing vouchers
* Should run as often as necessary for business reasons (once every 30 minutes seems like a good candidate if that's how often the data is ingested by Geizhals) – TBD
* Should run as a separate application container (possibly lambda function)
* Will do the following:Will LOCK the Voucher table (will be described below)Will fetch all the information from the Voucher table (will be described below)Will compute the CSV fileWill send the file via FTPWill update all the records in the Voucher table w/ "distributed" == TrueWill UNLOCK the Voucher table
* Will LOCK the Voucher table (will be described below)
* Will fetch all the information from the Voucher table (will be described below)
* Will compute the CSV file
* Will send the file via FTP
* Will update all the records in the Voucher table w/ "distributed" == True
* Will UNLOCK the Voucher table
* Once an item in the Voucher table is "distributed == True", then it should be considered an active voucher

VOUCHER CODES TABLE

| PRODUCT_ID | VOUCHER_ID | VOUCHER_VALUE | VOUCHER_CODE | DISTRIBUTED | Notes |
|---|---|---|---|---|---|
| KT03-005 | XXX | 200 | SOME_CODE | True | this means that this voucher has already been distributed at least once and, therefore, is an "active" voucherthis information will help us to identify the current voucher value as described in section 2) of Second phase solution for data aggregation and distribution service |
| A409-1LX | YYY | 100 | SOME_OTHER_CODE | False | this means that this voucher has not yet been distributed at all and, therefore, is an "inactive" voucherthe value of this voucher should not be included in the price described in section 2) of Second phase solution for data aggregation and distribution service |

* this means that this voucher has already been distributed at least once and, therefore, is an "active" voucher
* this information will help us to identify the current voucher value as described in section 2) of Second phase solution for data aggregation and distribution service

* this means that this voucher has not yet been distributed at all and, therefore, is an "inactive" voucher
* the value of this voucher should not be included in the price described in section 2) of Second phase solution for data aggregation and distribution service

