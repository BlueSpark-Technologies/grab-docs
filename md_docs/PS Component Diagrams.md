# PS Component Diagrams

See here for complete diagram CST Services

### ARIS
ARIS is the shared platform with Cyberport on which we add diagrams that are part of the Cyberport IT landscape. If you need access, please contact Hannah Winnes. If you see discrepancies between ARIS and our services, please contact you PO.

Current architecture: https://aris.cyberport.de/#default/item/c.default.Cyberport.xCMKoqDzEesVFgIWHWCwVA.-1/~AbBbIm1vZGVsVmlld2VyUmVwb3J0cyJd

Target architecture: https://aris.cyberport.de/#default/item/c.default.Cyberport.lwdzECs9EewVFgIWHWCwVA.-1/~AbBbIm1vZGVsVmlld2VyUmVwb3J0cyJ

### Lucidchart
Additional to ARIS we also have Lucid Chart Diagrams, that we can maintain ourselves.

# Components - Current Architecture
## Pricing Service
The purpose of the Pricing Service is to collect all necessary data in order to calculate the best base price of a product for the tenant’s webshop. This includes the price of a product, stock information, competitor data and various kinds of algorithm configuration. The algorithm configuration settings come from subscribing to certain topics on the E-commerce Cloud Service (ECS) and by calling respective API GET endpoint. Similarly competitor prices come from subscribing to a MPS topic on the Market Price Screening (MPS) and by again calling respective API GET endpoint. The third data source is the Data Integration Service (DIS), which provides all necessary Cyberport specific data.

After collecting this information it is parsed and used to calculate the optimal base price for a product. Certain price quality checks are also applied on this result and only if they are passed, it gets pushed to an SQS queue to be processed by SAP Pro and further distributed towards trailing external service until it finally appears on the webshop webpage itself.

# Components - Future Architecture
## Pricing Service
The purpose of the Pricing Service is to collect all necessary data in order to calculate the best base price and also channel prices of a product. This includes the price of a product, stock information, competitor data and various kinds of algorithm configuration. The algorithm configuration settings and manual prices come from subscribing to certain topics on the E-commerce Cloud Service (ECS) and by calling respective API GET endpoint. Similarly competitor prices come from subscribing to a MPS topic on the Market Price Screening (MPS) and by again calling respective API GET endpoint. The third data source is the Data Integration Service (DIS), which provides all necessary Cyberport specific data.

After collecting this information it is parsed first base prices are calculated and some price quality checks are made. Only if they are passed, channel prices are updated. Once channel prices are there as well, both base price and channel prices get pushed to an SQS queue to be processed by SAP Pro and further distributed towards trailing external service until it finally appears on the webshop webpage itself. Therefore the Pricing Service (PS) covers only the back-end part of the price calculation.

# Other Microservices
See here for Data Integration Service (DIS).

See here for Market Price Screening (MPS).

See here for E-commerce Cloud Service (ECS).

See here for Marketplace Service (MS).

