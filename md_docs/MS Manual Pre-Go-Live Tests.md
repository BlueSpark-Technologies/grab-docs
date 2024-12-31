# MS Manual Pre-Go-Live Tests

| Test | Service | Tasks CS and CST | Tasks CP (Malte Faßbach) | Scheduled testdate | Protocol | Result |
|---|---|---|---|---|---|---|
| Pipeline FTP-Server -> CyberParts | MS Pricing Service | Put existing product with a slightly changed on the FTP-Server -> Is the price row in CyberParts set to "manual" pricing? | Provide an SKU | Sprint 6 (2020-01-12) | Used SKU was Q535-013 with a price of 141.90. It was set to automatic in Cyberpart. After moving the testfile with only that SKU to the CP FTP-Server it appeared as changed less than 30 minutes later as a blue, manual price row with the defined price. This price was also transported to Amazon marketplace. Afterwards I changed it back. |  |
| List (add) new product on Amazon | MS Feed Service | We list a product on product and check, if the pipeline to the MS Feed Service works. | Provide an SKU and explain how to list a product (explained MS Escalation Scenarios & Tutorials). | Sprint 7 (2020-01-29) | New product:I added 4H20-043 (SKU) = B07SC7BZHR (ASIN) on Amazon in CyberParts at roughly 2020-01-29 13:10 Munich time on 118,90€. We saw it appear in the Amazon.de page on 13:29 Munich time. At 13:55 we did not see our change in the log files yet. We can not search in the notifications in the SQS for SKUs or ASINs. The notification was processed at about 17:00 Munich time. An increased speed in processing those notifications is already planned and shouldn’t be a problem in the future. |  |
| Delete products from Amazon, that are still on CP | MS Feed Service |  | Provide an SKU and explain how to unlist a product (explained MS Escalation Scenarios & Tutorials). | Sprint 7 |  |  |
| Change CP price of product that is listed on Amazon | MS Feed Service |  | Provide an SKU. | Sprint 7 (2020-01-29) | I added 1126-057 (SKU) = B07P9SKJ2Q (ASIN) on Amazon in CyberParts at roughly 2020-01-29 13:13-13:20 Munich time from 139,90€ to 142,90€. We saw it appear in the Amazon.de page on 13:35 Munich time. At 13:55 we did not see our change in the log files yet. We have a look at it later again.I changed the price of 1126-057 back to 139,90€ at 14:02, it appeared om Amazon at 14:11 in order to avoid having the wrong price too long.The notification was processed at about 17:00 Munich time. An increased speed in processing those notifications is already planned and shouldn’t be a problem in the future. |  |
| New price change offer competition | MS Feed Service | wait → should happen pretty often | nothing | Sprint 7 | Nicu and I saw updated prices regularly. There is no way to test however if all offers arrive at the queue though. |  |
| Amazon fee changes | MS Feed Service | wait → happens probably not much more than once a year | nothing | ? |  |  |
| Pipeline FTP-Server -> CyberParts | MS Pricing Service | Export new calculated prices hourly to FTP for all 4000 products | nothing | MS-PRICING-1.4.0 | The export of more than 1000 price rows per hour was too much for the Cyberparts Business connector. Therefore we reduced the export to only twice a day |  |
| Margin Strategy | MS Pricing Service | Deploy service with planned algorithm, monitor orders in Exasol and make a report | check Marketplace Dashboard in Tableau | MS-PRICING-1.4.0 and larger | Margin remains at the same level as before going live, which is good. |  |

Test

Service

Tasks CS and CST

Tasks CP (Malte Faßbach)

Scheduled testdate

Protocol

Result

Pipeline FTP-Server -> CyberParts

MS Pricing Service

Put existing product with a slightly changed on the FTP-Server -> Is the price row in CyberParts set to "manual" pricing?

Provide an SKU

Sprint 6 (2020-01-12)

Used SKU was Q535-013 with a price of 141.90. It was set to automatic in Cyberpart. After moving the testfile with only that SKU to the CP FTP-Server it appeared as changed less than 30 minutes later as a blue, manual price row with the defined price. This price was also transported to Amazon marketplace. Afterwards I changed it back.

List (add) new product on Amazon

MS Feed Service

We list a product on product and check, if the pipeline to the MS Feed Service works.

Provide an SKU and explain how to list a product (explained MS Escalation Scenarios & Tutorials).

Sprint 7 (2020-01-29)

New product:I added 4H20-043 (SKU) = B07SC7BZHR (ASIN) on Amazon in CyberParts at roughly 2020-01-29 13:10 Munich time on 118,90€. We saw it appear in the Amazon.de page on 13:29 Munich time. At 13:55 we did not see our change in the log files yet. We can not search in the notifications in the SQS for SKUs or ASINs. The notification was processed at about 17:00 Munich time. An increased speed in processing those notifications is already planned and shouldn’t be a problem in the future.

Delete products from Amazon, that are still on CP

MS Feed Service

Provide an SKU and explain how to unlist a product (explained MS Escalation Scenarios & Tutorials).

Sprint 7

Change CP price of product that is listed on Amazon

MS Feed Service

Provide an SKU.

Sprint 7 (2020-01-29)

I added 1126-057 (SKU) = B07P9SKJ2Q (ASIN) on Amazon in CyberParts at roughly 2020-01-29 13:13-13:20 Munich time from 139,90€ to 142,90€. We saw it appear in the Amazon.de page on 13:35 Munich time. At 13:55 we did not see our change in the log files yet. We have a look at it later again.I changed the price of 1126-057 back to 139,90€ at 14:02, it appeared om Amazon at 14:11 in order to avoid having the wrong price too long.The notification was processed at about 17:00 Munich time. An increased speed in processing those notifications is already planned and shouldn’t be a problem in the future.

New price change offer competition

MS Feed Service

wait → should happen pretty often

nothing

Sprint 7

Nicu and I saw updated prices regularly. There is no way to test however if all offers arrive at the queue though.

Amazon fee changes

MS Feed Service

wait → happens probably not much more than once a year

nothing

?

Pipeline FTP-Server -> CyberParts

MS Pricing Service

Export new calculated prices hourly to FTP for all 4000 products

nothing

MS-PRICING-1.4.0

The export of more than 1000 price rows per hour was too much for the Cyberparts Business connector. Therefore we reduced the export to only twice a day

Margin Strategy

MS Pricing Service

Deploy service with planned algorithm, monitor orders in Exasol and make a report

check Marketplace Dashboard in Tableau

MS-PRICING-1.4.0 and larger

Margin remains at the same level as before going live, which is good.

### For functional and end-to-end testing of the re-pricing algorithm the following tests cases were created:
### Test results 2020-05-18
The results can be found in the attached file. There are comments for the failed and some of the the tests that could not be run

Remarks:

Test 36: we should change the reason. The null price was calculated using non-null values. The actual reason that was saved to the database, “null values“, does not reflect that

Test 37: we are calculating prices for products that are inactive in the Marketplace Feed Service database. We should avoid this

Observation during testing: for a single Data Integration Service update(price or stock), SNS might send duplicate notifications, causing several unnecessary price calculations. This might impact the performance as the Pricing Service is already under relatively heavy and constant load processing the AnyOfferChanged notifications

### Test results 2020-05-28
The results can be found in the attached file.

Issues 1 and 2 from the previous run were addressed as follows:

According to https://cyber-solutions.atlassian.net/browse/PA-189 , this failure is acceptable, so the tests were adjusted to pass.

Problems discovered were fixed with https://cyber-solutions.atlassian.net/browse/PA-185

### Test results 2020-06-25
The results can be found in the attached file.

Prices were changed due to the updates to the configuration values and the tests needed to be updated.

There were no failed tests

### Test results 2020-09-08
The results can be found in the attached file.

Prices were changed due to the updates made for this ticket https://cyber-solutions.atlassian.net/browse/PA-234

There were no failed tests

### Test results 2021-02-12
These are the changes:

| Parameter | current value | future value |
|---|---|---|
| markup_only_seller_absolute | 20€ | 10€ |
| markup_min_price | 15% | 13% |

Parameter

current value

future value

markup_only_seller_absolute

20€

10€

markup_min_price

15%

13%

The results can be found in the attached file. No failed tests

### Test results 2021-02-17
These are tje changes:

| Parameter | current value | future value |
|---|---|---|
| markup_min_price | 13% | 10% |

Parameter

current value

future value

markup_min_price

13%

10%

The results can be found in the attached file. No failed tests

### Test results 2021-03-01
These are tje changes:

| Parameter | current value | future value |
|---|---|---|
| markup_webshop_abs | 10 EUR | 1 EUR |

Parameter

current value

future value

markup_webshop_abs

10 EUR

1 EUR

The results can be found in the attached file. No failed tests

### Test results 2021-03-05
These are tje changes:

| Parameter | current value | future value |
|---|---|---|
| markup_min_price | 0.1 | 0.05 |

Parameter

current value

future value

markup_min_price

0.1

0.05

The results can be found in the attached file. No failed tests

### Test results 2021-04-09
These are tje changes:

| Parameter | current value | future value |
|---|---|---|
| markup_min_price | 0.05 | 0 |
| haulier_large_costs | 3999 | 3990 |

Parameter

current value

future value

markup_min_price

0.05

0

haulier_large_costs

3999

3990

The results can be found in the attached file. No failed tests

### Test results 2021-06-22
These are the changes:

| Parameter | current value | future value |
|---|---|---|
| markup_only_seller_abs | 1000 = 10€ | 100 = 1€ |

Parameter

current value

future value

markup_only_seller_abs

1000 = 10€

100 = 1€

The results can be found in the attached file. No failed tests

### Test results 2021-07-20
These are the changes:

| Parameter | current value | future value |
|---|---|---|
| markup_only_seller_rel | 0.00 = 0% | 0.01 = 1% |
| markup_only_seller_abs | 100 = 1.00EUR | 500 = 5.00EUR |

Parameter

current value

future value

markup_only_seller_rel

0.00 = 0%

0.01 = 1%

markup_only_seller_abs

100 = 1.00EUR

500 = 5.00EUR

The results can be found in the attached file. No failed tests

### Test results 2021-08-02
These are the changes:

| Parameter | current value | future value |
|---|---|---|
| markup_min_price | 0.00 = 0% | 0.03 = 3% |

Parameter

current value

future value

markup_min_price

0.00 = 0%

0.03 = 3%

The results can be found in the attached file. No failed tests

