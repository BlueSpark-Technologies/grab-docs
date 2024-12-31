# PS B-Stock Go-Live Preparation and Tests

## Release phases
### Phase 1: around October
* Step-by-step replacement of the DWH auto pricing in Exasol to the new microservice "Base Price Service", later called “Pricing Service”.
* Only some of the products per day are priced with the DWH auto pricing. These will continue to be played at around 8:30 a.m. after FTP / Cyberparts.
* The remaining prices are exported via microservice with the following export rhythm Hourly export from incl 6:00 a.m. to 20:00 p.m., a maximum of 500 updates / hour, except from 8:00 a.m. to 11:59 p.m. (because the DWH exports autopricing there)
* Export of all products that have not received a price update that day, but need one at 9:00 p.m. (after Amazon auto pricing), max 5000

Step-by-step replacement of the DWH auto pricing in Exasol to the new microservice "Base Price Service", later called “Pricing Service”.

Only some of the products per day are priced with the DWH auto pricing. These will continue to be played at around 8:30 a.m. after FTP / Cyberparts.

The remaining prices are exported via microservice with the following export rhythm Hourly export from incl 6:00 a.m. to 20:00 p.m., a maximum of 500 updates / hour, except from 8:00 a.m. to 11:59 p.m. (because the DWH exports autopricing there)

Export of all products that have not received a price update that day, but need one at 9:00 p.m. (after Amazon auto pricing), max 5000

### Phase 2: around Q1
* All prices are send out via the microservice, no more price updates from Exasol
* If possible / necessary price updates also at night
* If possible / necessary, depending on the Cyberparts capacity, more price updates per hour

All prices are send out via the microservice, no more price updates from Exasol

If possible / necessary price updates also at night

If possible / necessary, depending on the Cyberparts capacity, more price updates per hour

### Phase 3: no timeline yet
* Channel prices are calculated within Pricing Service as well.

Channel prices are calculated within Pricing Service as well.

## Screenplay Go-Live Day
| Date | Action |
|---|---|
| Monday, 18th Oct 2021 | define release date in Daily (Hannah / Nicu)Inform management, CMs, Stefan Teich, BI, SAP, SAP Pro, Cyberparts, Customer Happiness, Claudia (Hannah)Request correct b-stock article groups from Stefan Teich (Hannah)Give Nicu b-stock article groups from Stefan Teich (Hannah)Enable correct b-stock article groups (Nicu)Reduce DIS B-stock cache endpoint and monitor performance (Nicu) |
| Tuesday, 19th Oct 2021 | Meet with Ralph Friedberg and Torsten Liebig to discuss go-live, testing of SAP Pro FTP file format and extending FTP import time window (Hannah) |
| Wednesday, 20th Oct 2021 | test CM mail settings (Nicu), do we see when CMs didn’t subscribe? - yesmonitoring of quality of b-stock prices exported to SAP Pro (Hannah) - couldn’t be done because of Glue issues |
| Thursday, 21th Oct 2021 | monitoring of quality of b-stock prices exported to SAP Pro (Hannah) - couldn’t be finished because of Glue issues |
| Friday, 22th Oct 2021 | monitoring of quality of b-stock prices exported to SAP Pro (Hannah) tests passedremind CMs per mail to accept the subscription (Hannah) |
| Monday, 25th Oct 2021 | all times are DE time. after 10:00 before eob - Merge Exasol pull request to deactivate B Stock for chosen article groups in old autopricing - Hannahbefore 10:00 - Stop reprice-all command or stop it shortly after it has started - Nicubefore 10:30 - Cleanse SAP Pro queue - Nicu10:30 - tell Ralph Friedberg to activate export to production FTP Server in a group chat with Hannah, Nicu and Vasile. Tell them that they shouldn't expect messages before 12:00 German time - Nicuafter confirmation from Ralph Friedberg - Restart reprice-all command - Nicuafter 10:30 - double check we don't export anything until 12:00 German time - Nicu / Vasileafter repricing command finished - Make sure prices make sense - Hannahafter 12:00 - monitoring if messages are processed correctly - Nicu / Vasileafter 12:00 - monitoring if exported prices end up in Cyberparts - Hannah - not possible as no prices were exported until 21:00after successful go-live - send out mail to CMs with subscribing - Nicu- done on Tuesday instead |
| Tuesday, 26th Oct 2021 | monitoring of quality of b-stock prices exported to SAP Pro (Hannah)monitoring if exported prices end up in Cyberparts (Hannah) |
| Wednesday, 27th Oct 2021 | monitoring of quality of b-stock prices exported to SAP Pro (Hannah) |

Date

Action

Monday, 18th Oct 2021

* define release date in Daily (Hannah / Nicu)
* Inform management, CMs, Stefan Teich, BI, SAP, SAP Pro, Cyberparts, Customer Happiness, Claudia (Hannah)
* Request correct b-stock article groups from Stefan Teich (Hannah)
* Give Nicu b-stock article groups from Stefan Teich (Hannah)
* Enable correct b-stock article groups (Nicu)
* Reduce DIS B-stock cache endpoint and monitor performance (Nicu)

define release date in Daily (Hannah / Nicu)

Inform management, CMs, Stefan Teich, BI, SAP, SAP Pro, Cyberparts, Customer Happiness, Claudia (Hannah)

Request correct b-stock article groups from Stefan Teich (Hannah)

Give Nicu b-stock article groups from Stefan Teich (Hannah)

Enable correct b-stock article groups (Nicu)

Reduce DIS B-stock cache endpoint and monitor performance (Nicu)

Tuesday, 19th Oct 2021

* Meet with Ralph Friedberg and Torsten Liebig to discuss go-live, testing of SAP Pro FTP file format and extending FTP import time window (Hannah)

Meet with Ralph Friedberg and Torsten Liebig to discuss go-live, testing of SAP Pro FTP file format and extending FTP import time window (Hannah)

Wednesday, 20th Oct 2021

* test CM mail settings (Nicu), do we see when CMs didn’t subscribe? - yes
* monitoring of quality of b-stock prices exported to SAP Pro (Hannah) - couldn’t be done because of Glue issues

test CM mail settings (Nicu), do we see when CMs didn’t subscribe? - yes

monitoring of quality of b-stock prices exported to SAP Pro (Hannah) - couldn’t be done because of Glue issues

Thursday, 21th Oct 2021

* monitoring of quality of b-stock prices exported to SAP Pro (Hannah) - couldn’t be finished because of Glue issues

monitoring of quality of b-stock prices exported to SAP Pro (Hannah) - couldn’t be finished because of Glue issues

Friday, 22th Oct 2021

* monitoring of quality of b-stock prices exported to SAP Pro (Hannah) tests passed
* remind CMs per mail to accept the subscription (Hannah)

monitoring of quality of b-stock prices exported to SAP Pro (Hannah) tests passed

remind CMs per mail to accept the subscription (Hannah)

Monday, 25th Oct 2021

all times are DE time.

* after 10:00 before eob - Merge Exasol pull request to deactivate B Stock for chosen article groups in old autopricing - Hannah
* before 10:00 - Stop reprice-all command or stop it shortly after it has started - Nicu
* before 10:30 - Cleanse SAP Pro queue - Nicu
* 10:30 - tell Ralph Friedberg to activate export to production FTP Server in a group chat with Hannah, Nicu and Vasile. Tell them that they shouldn't expect messages before 12:00 German time - Nicu
* after confirmation from Ralph Friedberg - Restart reprice-all command - Nicu
* after 10:30 - double check we don't export anything until 12:00 German time - Nicu / Vasile
* after repricing command finished - Make sure prices make sense - Hannah
* after 12:00 - monitoring if messages are processed correctly - Nicu / Vasile
* after 12:00 - monitoring if exported prices end up in Cyberparts - Hannah - not possible as no prices were exported until 21:00
* after successful go-live - send out mail to CMs with subscribing - Nicu- done on Tuesday instead

after 10:00 before eob - Merge Exasol pull request to deactivate B Stock for chosen article groups in old autopricing - Hannah

before 10:00 - Stop reprice-all command or stop it shortly after it has started - Nicu

before 10:30 - Cleanse SAP Pro queue - Nicu

10:30 - tell Ralph Friedberg to activate export to production FTP Server in a group chat with Hannah, Nicu and Vasile. Tell them that they shouldn't expect messages before 12:00 German time - Nicu

after confirmation from Ralph Friedberg - Restart reprice-all command - Nicu

after 10:30 - double check we don't export anything until 12:00 German time - Nicu / Vasile

after repricing command finished - Make sure prices make sense - Hannah

after 12:00 - monitoring if messages are processed correctly - Nicu / Vasile

after 12:00 - monitoring if exported prices end up in Cyberparts - Hannah - not possible as no prices were exported until 21:00

after successful go-live - send out mail to CMs with subscribing - Nicu- done on Tuesday instead

Tuesday, 26th Oct 2021

* monitoring of quality of b-stock prices exported to SAP Pro (Hannah)
* monitoring if exported prices end up in Cyberparts (Hannah)

monitoring of quality of b-stock prices exported to SAP Pro (Hannah)

monitoring if exported prices end up in Cyberparts (Hannah)

Wednesday, 27th Oct 2021

* monitoring of quality of b-stock prices exported to SAP Pro (Hannah)

monitoring of quality of b-stock prices exported to SAP Pro (Hannah)

## Dependencies and Stakeholders
Legend:

orange = roadblocker for going liveyellow = needs to be done after initial testing phasegreen = finishedgrey = needs to be done after Base Price Service is finished

| Dependency | Summary | Stakeholders | agreed to architecture | is implemented / finished | is tested before go-live | is informed about concrete release date | tested after go-live |
|---|---|---|---|---|---|---|---|
| Export to BI | Phase 1:Summary: Which columns of the PRODUCT_PRICE_RECOMMENDATION_HISTORY are actually used? -> @Schanzer Rainer We will provide BI with an S3 bucket to which we will send daily csv files with the same format at 6:00. This file should contain latest prices for each product that was priced in the Base Price Service. It also contains all columns that are relevant for Tableau dashboards 

 PA-314
                    -
            Getting issue details...
STATUS

 Artashes/Sritama will perform a daily import from S3 to a new table in PROD_DS. Stefan Berge said they will finish this until 24th of September, this includes Connector to S3 bucket -> issues with large columns, data type matching -> 1 weekHistorization part is built in Data Vault, for a part of the team Data Vault is new -> 2 weeksArtashes is on vacation for 2 weeks -> don't take anything live before he’s backView on the historization -> always last view per product -> 1 week Export from Data Vault to Exasol -> 1 week including release and testsHannah will change the DWH autopricing to fill up the table PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*) with data from this new table 

 TH-1136
                    -
            Getting issue details...
STATUS

AWS Glue Issues 

 PA-484
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-455
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-471
                    -
            Getting issue details...
STATUS

 Phase 2:Coordination with Artashes whether the SQS queue solution would work -> @Berge StefanInstead of a daily import of a csv file, we will eitherA) Push data on an SQS queue, where the data is contained within the message, one price per messageB) Push data regularly (e.g. hourly) to an S3 bucket and create a different SQS queue to inform you about new files. The message thus only say “there is a new file”, but doesn’t contain any data.Artashes will investigate this and inform us on what they preferArtashes will implement the BI side and import the incoming data to a new table.Switching off the FTP export / deactivating the price calculation part of the DWH autopricing after the complete move to the Pricing ServiceHannah will continue to fill up the table PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*), even if the DWH autopricing is not exporting any price anymore to Cyberparts, but only Base Price Calculation in Pricing ServicePhase 3:Rainer Schanzer (or someone else) will have to change Tableau Dashboards to use new data source and switch from “one price per day” logic to trigger based pricing logicAfterwards Hannah will deactivate filling up the PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*) tables and archive themDWH autopricing can be fully archived and deactivatedHistorical data in Exasol needs to be put to Data Historization Service → if Johannes Köhler-Landgraf still needs it | Artashes Hovasapyan (data engineering)Sritama Dutta (data engineering)Rainer Schanzer (will change dashboards)Stefan Berge (head of BI) | yes | no | no | yes | yes |
| Import Data Quality | Data Quality in MPSHandle article groups without relevant competitor handling

 PA-467
                    -
            Getting issue details...
STATUS

Duplicate handling 

 PA-469
                    -
            Getting issue details...
STATUS

 WIT spread offers on multiple product catalogues 

 PA-496
                    -
            Getting issue details...
STATUS

Error in merging of feed supplier data 

 PA-533
                    -
            Getting issue details...
STATUS

Changes on WIT have to be transferred to GZH too 

 PA-536
                    -
            Getting issue details...
STATUS

Unexpected error message shows up 

 PA-555
                    -
            Getting issue details...
STATUS

Fix this bug 

 PA-562
                    -
            Getting issue details...
STATUS

 Fix offer input window in DWH autopricingfurther unknown bugs?Data Quality in ECOMMMissing products because of missing article groups in DIS → resolvedMissing products because of lost messages between DIS and ECOMM 

 CEC-996
                    -
            Getting issue details...
STATUS

 (issue to be release soon, afterwards tests need to be made to re-trigger missing SKUs)Data Quality in DISMissing article groups (see ECOMM section above) → resolvedMissing SAP Pro data → already in clarification with SebastianMissing standard_purchase_priceWaiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious thresholdMissing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS

 Missing other fieldsSebastian has triggered them manually → Hannah, check again in Fr. 26th July | Sebastian Moch (SAP Pro)Camelia Topan (ECOMM / DIS)Jörg Kalesse (PIM)BI Team (Exasol)Jana Kempe (SAP)Hannah Winnes (MPS) | yes | no | no | - | no |
| Export schedule Cyberparts | Clarification with Tilo whether there are conflicts with the Amazon price export at 5:00 and 18:00 German time (Torsten will do this)Extension of import time window of FTP file to 22:00 German time (can be done quickly as soon as we tell Torsten that we will release soon), see ticket here https://devjira.cyberport.de/browse/CPARTS-1569 | Torsten Liebig (fall back during vacation Tilo Papke) | yes | yes | yes | yes | yes |
| Export to SAP Pro | Get SAP Pro access to our queue → done by Dragoș and NicuTake prices from QueueDelete prices from queuedetails see here PS Queue to SAP Pro | Sebastian Moch (SAP Pro) | yes | yes | yes | yes | yes |
| Export from SAP Pro to Cyberparts | Don’t update more than permitted prices (also after downtime)Build price prioritization (similar export schedule?)Stick to export windowImplement export to FTPtesting together with Ralph Friedberg 

 PA-499
                    -
            Getting issue details...
STATUS

 details see here PS Queue to SAP Pro and here SAP Pro to FTP | Sebastian Moch (SAP Pro)Torsten Liebig (Cyberparts) | yes | yes | yes | yes | yes |
| Price discrepancies between SAP and Webshop | As can be seen here there might be price discrepancies between SAP and the webshop if the speed of processing from SAP Pro to either of those two takes different amount of time. See also here for PS Component Diagrams. If that happens CRM will have to resolve these issues, which takes roughly 4min per case. We have to make sure that the amount of price discrepancies doesn’t increase. Therefore we need to agree on a monitoring and test scheme | Jana Kempe (SAP)Haupt Michael (Head of CRM)Patrick Mike Österreich (responsible for resolving discrepancies) | yes | no | no, how do we test this? | no | no |
| Category Management | Inform CM about BTO in SAP Text instead of Artikelbezeichnung - Arian Teßmann will be responsible for BTO prices → Claudia, Stefan and Arian are informed, they take care of it. Inform CM about changed schedule of pricesInform CM about change in mail schedule / structure in Double Check → emphasize that they have to confirm the mail subscription | Arian Teßmann (BTO prices)Stefan Rohne (Head of CM, will inform all other CMs) | yes | - | - | yes | - |
| Escalation scenarios (Plan B) | Have plan B if certain steps don’t work, this includes having a documented and easy process to shut down the service and reinstall DWH autopricing → Tutorial can be found here PS Escalation Scenarios & Tutorialsremove the secret or queue name from environment variable → exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instruction roll back prices, if the current ones don’t make sense 

 PA-459
                    -
            Getting issue details...
STATUS

 recover from a down timeBPS is down → clear outgoing SAP Pro SQS Queue → cache invalidation for all products → retrigger autopricing for all products | Nicolae Natrapeiu (Python lead in this project)Hannah Winnes (old DWH autopricing) | yes | yes | yes | yes | yes |
| Monitoring | Who monitors what?Technical Does the service work as it should? 

 PA-440
                    -
            Getting issue details...
STATUS

 / 

 DOPS-917
                    -
            Getting issue details...
STATUS

 → first look should be from Devops → Hannah: clarify with Razvan and Dragos for first response, come to dev if necessary

 DOPS-979
                    -
            Getting issue details...
STATUS

At the beginning Nicu will have a look whenever we get an alertMonitoringAWS Glue Issues 

 PA-484
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-455
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-471
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-484
                    -
            Getting issue details...
STATUS

How do we make sure prices make sense? → HannahIs the allowed amount of price changes enough? → HannahDo any products get stuck and never updated? → HannahCheck dead-letter queue → We need to get an email in the morning (Hannah added a comment 

 DOPS-917
                    -
            Getting issue details...
STATUS

 here)  → Nicu will be first responder and contact others for help | Dragoș Malene (DevOps lead in this project)Nicolae Nătrăpeiu (Python lead in this project)Hannah Winnes (business monitoring) | yes | yes | yes | yes | yes |
| Further prototyping | How will be be able to do further prototyping? → we need a workshop with Nicu, Sebi, Christian and Horatiu | Christian Flegel (prototyping autopricing)Hannah Winnes (prototyping autopricing) | - | no | no | no |  |
| Performant reports | Analytical database (e.g. redshift) in DHS for performant reports and business monitoring | Horatiu Maieranu (Data Historization Service)Dragoș Malene (DevOps lead in this project) |  |  |  |  |  |
| Management Approval | They like to be informed about changes and risks | Laszlo KovacsSimon FrankRené Bittner | - | - | - | yes | - |

Dependency

Summary

Stakeholders

agreed to architecture

is implemented / finished

is tested before go-live

is informed about concrete release date

tested after go-live

Export to BI

Phase 1:

* Summary: Which columns of the PRODUCT_PRICE_RECOMMENDATION_HISTORY are actually used? -> @Schanzer Rainer
* We will provide BI with an S3 bucket to which we will send daily csv files with the same format at 6:00. This file should contain latest prices for each product that was priced in the Base Price Service. It also contains all columns that are relevant for Tableau dashboards 

 PA-314
                    -
            Getting issue details...
STATUS
* Artashes/Sritama will perform a daily import from S3 to a new table in PROD_DS. Stefan Berge said they will finish this until 24th of September, this includes Connector to S3 bucket -> issues with large columns, data type matching -> 1 weekHistorization part is built in Data Vault, for a part of the team Data Vault is new -> 2 weeksArtashes is on vacation for 2 weeks -> don't take anything live before he’s backView on the historization -> always last view per product -> 1 week Export from Data Vault to Exasol -> 1 week including release and tests
* Connector to S3 bucket -> issues with large columns, data type matching -> 1 week
* Historization part is built in Data Vault, for a part of the team Data Vault is new -> 2 weeks
* Artashes is on vacation for 2 weeks -> don't take anything live before he’s back
* View on the historization -> always last view per product -> 1 week
* Export from Data Vault to Exasol -> 1 week including release and tests
* Hannah will change the DWH autopricing to fill up the table PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*) with data from this new table 

 TH-1136
                    -
            Getting issue details...
STATUS
* AWS Glue Issues 

 PA-484
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-455
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-471
                    -
            Getting issue details...
STATUS

Summary: Which columns of the PRODUCT_PRICE_RECOMMENDATION_HISTORY are actually used? -> @Schanzer Rainer

We will provide BI with an S3 bucket to which we will send daily csv files with the same format at 6:00. This file should contain latest prices for each product that was priced in the Base Price Service. It also contains all columns that are relevant for Tableau dashboards 

 PA-314
                    -
            Getting issue details...
STATUS

Artashes/Sritama will perform a daily import from S3 to a new table in PROD_DS. Stefan Berge said they will finish this until 24th of September, this includes

* Connector to S3 bucket -> issues with large columns, data type matching -> 1 week
* Historization part is built in Data Vault, for a part of the team Data Vault is new -> 2 weeks
* Artashes is on vacation for 2 weeks -> don't take anything live before he’s back
* View on the historization -> always last view per product -> 1 week
* Export from Data Vault to Exasol -> 1 week including release and tests

Connector to S3 bucket -> issues with large columns, data type matching -> 1 week

Historization part is built in Data Vault, for a part of the team Data Vault is new -> 2 weeks

Artashes is on vacation for 2 weeks -> don't take anything live before he’s back

View on the historization -> always last view per product -> 1 week

Export from Data Vault to Exasol -> 1 week including release and tests

Hannah will change the DWH autopricing to fill up the table PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*) with data from this new table 

 TH-1136
                    -
            Getting issue details...
STATUS

AWS Glue Issues 

 PA-484
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-455
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-471
                    -
            Getting issue details...
STATUS

Phase 2:

* Coordination with Artashes whether the SQS queue solution would work -> @Berge Stefan
* Instead of a daily import of a csv file, we will eitherA) Push data on an SQS queue, where the data is contained within the message, one price per messageB) Push data regularly (e.g. hourly) to an S3 bucket and create a different SQS queue to inform you about new files. The message thus only say “there is a new file”, but doesn’t contain any data.
* A) Push data on an SQS queue, where the data is contained within the message, one price per message
* B) Push data regularly (e.g. hourly) to an S3 bucket and create a different SQS queue to inform you about new files. The message thus only say “there is a new file”, but doesn’t contain any data.
* Artashes will investigate this and inform us on what they prefer
* Artashes will implement the BI side and import the incoming data to a new table.
* Switching off the FTP export / deactivating the price calculation part of the DWH autopricing after the complete move to the Pricing Service
* Hannah will continue to fill up the table PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*), even if the DWH autopricing is not exporting any price anymore to Cyberparts, but only Base Price Calculation in Pricing Service

Coordination with Artashes whether the SQS queue solution would work -> @Berge Stefan

Instead of a daily import of a csv file, we will either

* A) Push data on an SQS queue, where the data is contained within the message, one price per message
* B) Push data regularly (e.g. hourly) to an S3 bucket and create a different SQS queue to inform you about new files. The message thus only say “there is a new file”, but doesn’t contain any data.

A) Push data on an SQS queue, where the data is contained within the message, one price per message

B) Push data regularly (e.g. hourly) to an S3 bucket and create a different SQS queue to inform you about new files. The message thus only say “there is a new file”, but doesn’t contain any data.

Artashes will investigate this and inform us on what they prefer

Artashes will implement the BI side and import the incoming data to a new table.

Switching off the FTP export / deactivating the price calculation part of the DWH autopricing after the complete move to the Pricing Service

Hannah will continue to fill up the table PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*), even if the DWH autopricing is not exporting any price anymore to Cyberparts, but only Base Price Calculation in Pricing Service

Phase 3:

* Rainer Schanzer (or someone else) will have to change Tableau Dashboards to use new data source and switch from “one price per day” logic to trigger based pricing logic
* Afterwards Hannah will deactivate filling up the PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*) tables and archive them
* DWH autopricing can be fully archived and deactivated
* Historical data in Exasol needs to be put to Data Historization Service → if Johannes Köhler-Landgraf still needs it

Rainer Schanzer (or someone else) will have to change Tableau Dashboards to use new data source and switch from “one price per day” logic to trigger based pricing logic

Afterwards Hannah will deactivate filling up the PROD_DS.PRODUCT_PRICE_RECOMMENDATION_HISTORY(_*) tables and archive them

DWH autopricing can be fully archived and deactivated

Historical data in Exasol needs to be put to Data Historization Service → if Johannes Köhler-Landgraf still needs it

Artashes Hovasapyan (data engineering)

Sritama Dutta (data engineering)

Rainer Schanzer (will change dashboards)

Stefan Berge (head of BI)

yes

no

no

yes

yes

Import Data Quality

* Data Quality in MPSHandle article groups without relevant competitor handling

 PA-467
                    -
            Getting issue details...
STATUS

Duplicate handling 

 PA-469
                    -
            Getting issue details...
STATUS

 WIT spread offers on multiple product catalogues 

 PA-496
                    -
            Getting issue details...
STATUS

Error in merging of feed supplier data 

 PA-533
                    -
            Getting issue details...
STATUS

Changes on WIT have to be transferred to GZH too 

 PA-536
                    -
            Getting issue details...
STATUS

Unexpected error message shows up 

 PA-555
                    -
            Getting issue details...
STATUS

Fix this bug 

 PA-562
                    -
            Getting issue details...
STATUS

 Fix offer input window in DWH autopricingfurther unknown bugs?
* Handle article groups without relevant competitor handling

 PA-467
                    -
            Getting issue details...
STATUS
* Duplicate handling 

 PA-469
                    -
            Getting issue details...
STATUS
* WIT spread offers on multiple product catalogues 

 PA-496
                    -
            Getting issue details...
STATUS
* Error in merging of feed supplier data 

 PA-533
                    -
            Getting issue details...
STATUS
* Changes on WIT have to be transferred to GZH too 

 PA-536
                    -
            Getting issue details...
STATUS
* Unexpected error message shows up 

 PA-555
                    -
            Getting issue details...
STATUS
* Fix this bug 

 PA-562
                    -
            Getting issue details...
STATUS
* Fix offer input window in DWH autopricing
* further unknown bugs?
* Data Quality in ECOMMMissing products because of missing article groups in DIS → resolvedMissing products because of lost messages between DIS and ECOMM 

 CEC-996
                    -
            Getting issue details...
STATUS

 (issue to be release soon, afterwards tests need to be made to re-trigger missing SKUs)
* Missing products because of missing article groups in DIS → resolved
* Missing products because of lost messages between DIS and ECOMM 

 CEC-996
                    -
            Getting issue details...
STATUS

 (issue to be release soon, afterwards tests need to be made to re-trigger missing SKUs)
* Data Quality in DISMissing article groups (see ECOMM section above) → resolvedMissing SAP Pro data → already in clarification with SebastianMissing standard_purchase_priceWaiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious thresholdMissing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS

 Missing other fieldsSebastian has triggered them manually → Hannah, check again in Fr. 26th July
* Missing article groups (see ECOMM section above) → resolved
* Missing SAP Pro data → already in clarification with SebastianMissing standard_purchase_priceWaiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious thresholdMissing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS

 Missing other fieldsSebastian has triggered them manually → Hannah, check again in Fr. 26th July
* Missing standard_purchase_priceWaiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold
* Waiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.
* Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold
* Missing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS
* Missing other fieldsSebastian has triggered them manually → Hannah, check again in Fr. 26th July
* Sebastian has triggered them manually → Hannah, check again in Fr. 26th July

Data Quality in MPS

* Handle article groups without relevant competitor handling

 PA-467
                    -
            Getting issue details...
STATUS
* Duplicate handling 

 PA-469
                    -
            Getting issue details...
STATUS
* WIT spread offers on multiple product catalogues 

 PA-496
                    -
            Getting issue details...
STATUS
* Error in merging of feed supplier data 

 PA-533
                    -
            Getting issue details...
STATUS
* Changes on WIT have to be transferred to GZH too 

 PA-536
                    -
            Getting issue details...
STATUS
* Unexpected error message shows up 

 PA-555
                    -
            Getting issue details...
STATUS
* Fix this bug 

 PA-562
                    -
            Getting issue details...
STATUS
* Fix offer input window in DWH autopricing
* further unknown bugs?

Handle article groups without relevant competitor handling

 PA-467
                    -
            Getting issue details...
STATUS

Duplicate handling 

 PA-469
                    -
            Getting issue details...
STATUS

WIT spread offers on multiple product catalogues 

 PA-496
                    -
            Getting issue details...
STATUS

Error in merging of feed supplier data 

 PA-533
                    -
            Getting issue details...
STATUS

Changes on WIT have to be transferred to GZH too 

 PA-536
                    -
            Getting issue details...
STATUS

Unexpected error message shows up 

 PA-555
                    -
            Getting issue details...
STATUS

Fix this bug 

 PA-562
                    -
            Getting issue details...
STATUS

Fix offer input window in DWH autopricing

further unknown bugs?

Data Quality in ECOMM

* Missing products because of missing article groups in DIS → resolved
* Missing products because of lost messages between DIS and ECOMM 

 CEC-996
                    -
            Getting issue details...
STATUS

 (issue to be release soon, afterwards tests need to be made to re-trigger missing SKUs)

Missing products because of missing article groups in DIS → resolved

Missing products because of lost messages between DIS and ECOMM 

 CEC-996
                    -
            Getting issue details...
STATUS

 (issue to be release soon, afterwards tests need to be made to re-trigger missing SKUs)

Data Quality in DIS

* Missing article groups (see ECOMM section above) → resolved
* Missing SAP Pro data → already in clarification with SebastianMissing standard_purchase_priceWaiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious thresholdMissing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS

 Missing other fieldsSebastian has triggered them manually → Hannah, check again in Fr. 26th July
* Missing standard_purchase_priceWaiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold
* Waiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.
* Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold
* Missing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS
* Missing other fieldsSebastian has triggered them manually → Hannah, check again in Fr. 26th July
* Sebastian has triggered them manually → Hannah, check again in Fr. 26th July

Missing article groups (see ECOMM section above) → resolved

Missing SAP Pro data → already in clarification with Sebastian

* Missing standard_purchase_priceWaiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold
* Waiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.
* Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold
* Missing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS
* Missing other fieldsSebastian has triggered them manually → Hannah, check again in Fr. 26th July
* Sebastian has triggered them manually → Hannah, check again in Fr. 26th July

Missing standard_purchase_price

* Waiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.
* Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold

Waiting until 30th of August after Sebastians vacation -> manual load of missing values by Seb.

Manual load was not sufficient → Sebastian fixed it on Tuesday 14th of September and re-triggered the remaining products → now number is below suspicious threshold

Missing product views band → probably until Wednesday, 15th Sept 

 CEC-1376
                    -
            Getting issue details...
STATUS

Missing other fields

* Sebastian has triggered them manually → Hannah, check again in Fr. 26th July

Sebastian has triggered them manually → Hannah, check again in Fr. 26th July

Sebastian Moch (SAP Pro)

Camelia Topan (ECOMM / DIS)

Jörg Kalesse (PIM)

BI Team (Exasol)

Jana Kempe (SAP)

Hannah Winnes (MPS)

yes

no

no

-

no

Export schedule Cyberparts

* Clarification with Tilo whether there are conflicts with the Amazon price export at 5:00 and 18:00 German time (Torsten will do this)
* Extension of import time window of FTP file to 22:00 German time (can be done quickly as soon as we tell Torsten that we will release soon), see ticket here https://devjira.cyberport.de/browse/CPARTS-1569

Clarification with Tilo whether there are conflicts with the Amazon price export at 5:00 and 18:00 German time (Torsten will do this)

Extension of import time window of FTP file to 22:00 German time (can be done quickly as soon as we tell Torsten that we will release soon), see ticket here https://devjira.cyberport.de/browse/CPARTS-1569

Torsten Liebig

(fall back during vacation Tilo Papke)

yes

yes

yes

yes

yes

Export to SAP Pro

* Get SAP Pro access to our queue → done by Dragoș and Nicu
* Take prices from Queue
* Delete prices from queue

Get SAP Pro access to our queue → done by Dragoș and Nicu

Take prices from Queue

Delete prices from queue

details see here PS Queue to SAP Pro

Sebastian Moch (SAP Pro)

yes

yes

yes

yes

yes

Export from SAP Pro to Cyberparts

* Don’t update more than permitted prices (also after downtime)
* Build price prioritization (similar export schedule?)
* Stick to export window
* Implement export to FTP
* testing together with Ralph Friedberg 

 PA-499
                    -
            Getting issue details...
STATUS

Don’t update more than permitted prices (also after downtime)

Build price prioritization (similar export schedule?)

Stick to export window

Implement export to FTP

testing together with Ralph Friedberg 

 PA-499
                    -
            Getting issue details...
STATUS

details see here PS Queue to SAP Pro and here SAP Pro to FTP

Sebastian Moch (SAP Pro)

Torsten Liebig (Cyberparts)

yes

yes

yes

yes

yes

Price discrepancies between SAP and Webshop

As can be seen here there might be price discrepancies between SAP and the webshop if the speed of processing from SAP Pro to either of those two takes different amount of time. See also here for PS Component Diagrams.

If that happens CRM will have to resolve these issues, which takes roughly 4min per case. We have to make sure that the amount of price discrepancies doesn’t increase. Therefore we need to agree on a

* monitoring and test scheme

monitoring and test scheme

Jana Kempe (SAP)

Haupt Michael (Head of CRM)

Patrick Mike Österreich (responsible for resolving discrepancies)

yes

no

no, how do we test this?

no

no

Category Management

* Inform CM about BTO in SAP Text instead of Artikelbezeichnung - Arian Teßmann will be responsible for BTO prices → Claudia, Stefan and Arian are informed, they take care of it.
* Inform CM about changed schedule of prices
* Inform CM about change in mail schedule / structure in Double Check → emphasize that they have to confirm the mail subscription

Inform CM about BTO in SAP Text instead of Artikelbezeichnung - Arian Teßmann will be responsible for BTO prices → Claudia, Stefan and Arian are informed, they take care of it.

Inform CM about changed schedule of prices

Inform CM about change in mail schedule / structure in Double Check → emphasize that they have to confirm the mail subscription

Arian Teßmann (BTO prices)

Stefan Rohne (Head of CM, will inform all other CMs)

yes

-

-

yes

-

Escalation scenarios (Plan B)

Have plan B if certain steps don’t work, this includes having a documented and easy process to

* shut down the service and reinstall DWH autopricing → Tutorial can be found here PS Escalation Scenarios & Tutorialsremove the secret or queue name from environment variable → exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instruction
* remove the secret or queue name from environment variable → exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instruction
* roll back prices, if the current ones don’t make sense 

 PA-459
                    -
            Getting issue details...
STATUS
* recover from a down timeBPS is down → clear outgoing SAP Pro SQS Queue → cache invalidation for all products → retrigger autopricing for all products
* BPS is down → clear outgoing SAP Pro SQS Queue → cache invalidation for all products → retrigger autopricing for all products

shut down the service and reinstall DWH autopricing → Tutorial can be found here PS Escalation Scenarios & Tutorials

* remove the secret or queue name from environment variable → exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instruction

remove the secret or queue name from environment variable → exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instruction

roll back prices, if the current ones don’t make sense 

 PA-459
                    -
            Getting issue details...
STATUS

recover from a down time

* BPS is down → clear outgoing SAP Pro SQS Queue → cache invalidation for all products → retrigger autopricing for all products

BPS is down → clear outgoing SAP Pro SQS Queue → cache invalidation for all products → retrigger autopricing for all products

Nicolae Natrapeiu (Python lead in this project)

Hannah Winnes (old DWH autopricing)

yes

yes

yes

yes

yes

Monitoring

Who monitors what?

Technical

* Does the service work as it should? 

 PA-440
                    -
            Getting issue details...
STATUS

 / 

 DOPS-917
                    -
            Getting issue details...
STATUS

 → first look should be from Devops → Hannah: clarify with Razvan and Dragos for first response, come to dev if necessary
* DOPS-979
                    -
            Getting issue details...
STATUS

At the beginning Nicu will have a look whenever we get an alert

Does the service work as it should? 

 PA-440
                    -
            Getting issue details...
STATUS

 / 

 DOPS-917
                    -
            Getting issue details...
STATUS

 → first look should be from Devops → Hannah: clarify with Razvan and Dragos for first response, come to dev if necessary

DOPS-979
                    -
            Getting issue details...
STATUS

At the beginning Nicu will have a look whenever we get an alert

Monitoring

* AWS Glue Issues 

 PA-484
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-455
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-471
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-484
                    -
            Getting issue details...
STATUS
* How do we make sure prices make sense? → Hannah
* Is the allowed amount of price changes enough? → Hannah
* Do any products get stuck and never updated? → Hannah
* Check dead-letter queue → We need to get an email in the morning (Hannah added a comment 

 DOPS-917
                    -
            Getting issue details...
STATUS

 here)  → Nicu will be first responder and contact others for help

AWS Glue Issues 

 PA-484
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-455
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-471
                    -
            Getting issue details...
STATUS

, 

    

            




    
 PA-484
                    -
            Getting issue details...
STATUS

How do we make sure prices make sense? → Hannah

Is the allowed amount of price changes enough? → Hannah

Do any products get stuck and never updated? → Hannah

Check dead-letter queue → We need to get an email in the morning (Hannah added a comment 

 DOPS-917
                    -
            Getting issue details...
STATUS

 here)  → Nicu will be first responder and contact others for help

Dragoș Malene (DevOps lead in this project)

Nicolae Nătrăpeiu (Python lead in this project)

Hannah Winnes (business monitoring)

yes

yes

yes

yes

yes

Further prototyping

How will be be able to do further prototyping? → we need a workshop with Nicu, Sebi, Christian and Horatiu

Christian Flegel (prototyping autopricing)

Hannah Winnes (prototyping autopricing)

-

no

no

no

Performant reports

Analytical database (e.g. redshift) in DHS for performant reports and business monitoring

Horatiu Maieranu (Data Historization Service)

Dragoș Malene (DevOps lead in this project)

Management Approval

They like to be informed about changes and risks

Laszlo Kovacs

Simon Frank

René Bittner

-

-

-

yes

-

