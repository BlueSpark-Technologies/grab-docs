# MPS Customer Expectation

# Customers
Customers of this service are via some levels of indirection Category Managers, Controlling and Mangers.

# Expectation
As the Market Price Screening collects real time data and uses the configuration from the E-Commerce Cloud Service the business users expect to change the configuration in a comfortable UI and see the changes walk through the E-Commerce Cloud Service to the Market Price Screening to the PSE Voucher Service and the Pricing Service to Cyberparts and finally to the Cyberport Webshop. That way they expect the prices in the Webshop to be based on current good quality competitor data reflecting their own knowledge about the market as they expressed via category group-wide or even product specific configuration.

# Target output format
In order to make the output for the PSE Core Service processable according to current logic, the feeds should be available in the following data format:

* PRODUCTFEEDCODE: provider id
* FEEDPRODUCTCODE: provider item id
* SKU: unit item id
* FEEDPOSITION: position in ranking
* MERCHANTNAME: merchant name (from mapping)
* MERCHANTNAME_SHORT: short version merchant name (added from mapping)
* SHIPPINGCOSTS: shipping costs in cent
* PRICE: price in cent
* DELIVERYTIME: merchant availability of product
* FEEDDATETIME: Date time of feed
* DATETIME: date and time of price

PRODUCTFEEDCODE: provider id

FEEDPRODUCTCODE: provider item id

SKU: unit item id

FEEDPOSITION: position in ranking

MERCHANTNAME: merchant name (from mapping)

MERCHANTNAME_SHORT: short version merchant name (added from mapping)

SHIPPINGCOSTS: shipping costs in cent

PRICE: price in cent

DELIVERYTIME: merchant availability of product

FEEDDATETIME: Date time of feed

DATETIME: date and time of price

Example:

| PRODUCTFEEDCODE | FEEDPRODUCTCODE | SKU | FEEDPOSITION | MERCHANTNAME | MERCHANTNAME_SHORT | SHIPPINGCOSTS | PRICE | DELIVERYTIME | FEEDDATETIME incl. TIMEZONE | PRICEDATETIMEincl. TIMEZONE |
|---|---|---|---|---|---|---|---|---|---|---|
| GZH | 619692 | 6711-28J | 10 | OfficePartner | OP | 43 | 5980 | 2 | 26.07.2017 13:53 | 26.07.2017 13:51 |
| GZH | 619692 | 6711-28J | 9 | Mindfactory | MF | 799 | 5974 | 1 | 26.07.2017 13:53 | 26.07.2017 13:51 |
| GZH | 619692 | 6711-28J | 8 | SurfFact | SurfFact | 0 | 5600 | 0 | 26.07.2017 13:53 | 26.07.2017 13:51 |
| GZH | 619692 | 6711-28J | 7 | DriveCity | DriveCity | 345 | 5425 | 0 | 26.07.2017 13:53 | 26.07.2017 13:51 |

PRODUCTFEEDCODE

FEEDPRODUCTCODE

SKU

FEEDPOSITION

MERCHANTNAME

MERCHANTNAME_SHORT

SHIPPINGCOSTS

PRICE

DELIVERYTIME

FEEDDATETIME incl. TIMEZONE

PRICEDATETIMEincl. TIMEZONE

GZH

619692

6711-28J

10

OfficePartner

OP

43

5980

2

26.07.2017 13:53

26.07.2017 13:51

GZH

619692

6711-28J

9

Mindfactory

MF

799

5974

1

26.07.2017 13:53

26.07.2017 13:51

GZH

619692

6711-28J

8

SurfFact

SurfFact

0

5600

0

26.07.2017 13:53

26.07.2017 13:51

GZH

619692

6711-28J

7

DriveCity

DriveCity

345

5425

0

26.07.2017 13:53

26.07.2017 13:51

