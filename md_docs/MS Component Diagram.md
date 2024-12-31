# MS Component Diagram

There are two sub services in the Marketplace Services:

MS Feed Service

MS Pricing Service

Integration diagram:

https://aris.cyberport.de/#default/item/c.default.Cyberport.5UAW0fOoEesVFgIWHWCwVA.-1/~AbBbIm1vZGVsVmlld2VyUmVwb3J0cyJd

## MS Feed Service
The purpose of the Marketplace Service is to collect competitor offers and fee information on Amazon on products that we offer as well.

## MS Pricing Service
The MS Pricing Service calculates optimal Amazon prices of our products according to a strategy based on webshop price, internal costs and competitor offers and exports them via Cyberparts back to Amazon.

The only internal microservice that the Marketplace Service depends on is the Data Integration Service.

## Other Microservices
See here for Data Integration Service Data Integration Service (DIS).

