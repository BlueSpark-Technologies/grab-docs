# PSE Technical Dependencies

* PSE Component DiagramsThe PSE Voucher Service consists of two sub-services that communicate with other micro-services in the Cybersolutions Tech microservice landscape.PSE Orchestration ServiceThe purpose of the PSE Orchestration Service is to collect all necessary data in order to calculate the best voucher of a product for a price search engine (PSE) as www.geizhals.de. This includes the price of a product, stock information, competitor data and black-/whitelist configuration.
* PSE Core Service
* PSE Orchestration ServiceThis service doesn’t exist yet, but is in planning.
* PSE External SystemsThe PSE Voucher Service deals with only one external service, which is SAP Pro. SAP Pro needs to be extended so that product vouchers are bound to a specific product. This is necessary so customers on the webshop can't expoit Geizhals vouchers by swapping the bought product. Changes here are planned in the following demand: https://devjira.cyberport.de/browse/CPDM2-3154?filter=23051
* PSE Internal Integration PointsCurrently there are no service internal integration points to be documented.
* PSE PrototypeRequirementsTechnical ImplementationUser Handling
* Requirements
* Technical Implementation
* User Handling

The PSE Voucher Service consists of two sub-services that communicate with other micro-services in the Cybersolutions Tech microservice landscape.

## PSE Orchestration Service
The purpose of the PSE Orchestration Service is to collect all necessary data in order to calculate the best voucher of a product for a price search engine (PSE) as www.geizhals.de. This includes the price of a product, stock information, competitor data and black-/whitelist configuration.

This service doesn’t exist yet, but is in planning.

The PSE Voucher Service deals with only one external service, which is SAP Pro.

SAP Pro needs to be extended so that product vouchers are bound to a specific product. This is necessary so customers on the webshop can't expoit Geizhals vouchers by swapping the bought product. Changes here are planned in the following demand: https://devjira.cyberport.de/browse/CPDM2-3154?filter=23051

Currently there are no service internal integration points to be documented.

* Requirements
* Technical Implementation
* User Handling

