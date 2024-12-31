# MS Pricing Distribution

Prices are currently exported to FTP (productive export to Amazon) and S3 (for debugging reasons only). In the future this will change and we will export via Pricing Service.

## Current Solution
### Current Schedule
Currently we export Amazon prices twice a day German time (in summer UTC+2 and in winter UTC+1)

* 5:00 in the morning
* 18:00 in the evening

5:00 in the morning

18:00 in the evening

### Current Architecture
Prices are currently exported to an S3 bucket and via an FTP-Server to Cyberparts and from there to the marketplace. However we already plan to change the export procedure in 2022/2023, which can be seen here MS External Systems.

| Component | Address | Contact person regarding credentials | Comment |
|---|---|---|---|
| AWS S3 Bucket | https://s3.console.aws.amazon.com/s3/buckets/marketplace-pricing/?region=eu-central-1&tab=overview | Cybersolutions Tech Dev-ops Team | We do this for debugging reasons |
| FTP Server | ftp://supplier.cyberport.de/ | Product Owner Hannah Winnes (Cybersolutions), Business Owner Malte Faßbach (Cyberport) | see also here MS FTP Server |

Component

Address

Contact person regarding credentials

Comment

AWS S3 Bucket

https://s3.console.aws.amazon.com/s3/buckets/marketplace-pricing/?region=eu-central-1&tab=overview

Cybersolutions Tech Dev-ops Team

We do this for debugging reasons

FTP Server

ftp://supplier.cyberport.de/

Product Owner Hannah Winnes (Cybersolutions), Business Owner Malte Faßbach (Cyberport)

see also here MS FTP Server

Prices get exported to Amazon via an FTP-Server which sends the data along to Cyberparts and from there to the marketplaces as described here MS FTP Server

Then the FTP Server takes the csv and messages the whole batch to Cyberparts, where it can be seen by category managers and business users.

Cyberparts does then two further exports.

Cyberparts export to SAP Pro. This is relevant for Cyberport to know how to handle billings and orders on Amazon and inventory information.

Cyberparts export to XML → Marketplace Application (aka. MPA, aka. Marketplace Connector) → Amazon.de and Amazon.at. The Cyperparts to Marketplace connector is maintained by Markus Paetzel from Cyberport.

Currently the connection between Cyberparts and XML is the bottleneck of the system preventing us from exporting more than 1000 prices rows in the morning and 1000 in the afternoon.

Therefore we plan a new architecture in which we communicate with Pricing Service and SAP Pro directly instead of the FTP → Cyberparts way.

### Current Content
We export all latest prices of products that were updated since the previous FTP export and that actually differ from the previous price. We get the prices by using the following algorithm:

Get timestamp of previous FTP export

Get export candidate list containing latest prices of products that were updated since the previous FTP export (just like before)

For each of the products in the list:

Check the latest price in the table product_price with created_at smaller or equal to the previous FTP export.

If the price of the product is the same as the export candidate, drop the product.

If not, add it to the final export list

Export this list to FTP server and S3 bucket

## Target Solution
### Target Schedule
Currently we export Amazon prices twice a day. In the future prices get exported in real time whenever they occur.

### Target Architecture
In collaboration with the EAM team (Enterprise Architects) the following architecture draft was created.

https://aris.cyberport.de/#default/item/c.default.Cyberport.ZnaLcQwdEehhDQIB92xRFw.-1/~AbBbIm1vZGVsVmlld2VyUmVwb3J0cyJd

It can be accessed using the credentials on this site https://wiki.cyberport.de/display/EAM/ARIS. If you don’t have access, please contact Hannah.

Essentially Cyberparts should not be able to export own Amazon price rows, not even when a new product is created and a very first price is published to Amazon.de. In all these cases only our Marketplace Service should export prices to Amazon via Pricing Service and SAP Pro.

### Target Content
Whenever we calculate a new price on Amazon, we check if it is different that the previous price and export it with the

* sales channel code = Amazon
* product  sku
* new price

sales channel code = Amazon

product  sku

new price

to the Pricing Service.

## Further reading
For the export format and requirements, please see here MS External Systems.

