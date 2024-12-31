# PSE Component Diagrams

The PSE Voucher Service consists of two sub-services that communicate with other micro-services in the Cybersolutions Tech microservice landscape.

## PSE Orchestration Service
The purpose of the PSE Orchestration Service is to collect all necessary data in order to calculate the best voucher of a product for a price search engine (PSE) as www.geizhals.de. This includes the price of a product, stock information, competitor data and black-/whitelist configuration.

After collecting this information it is parsed and distributed to the PSE Core Service for the calculation steps. After returning a voucher value the PSE Orchestration Service will distribute it to a queue for the Cyberport SAP Pro system, which processes and distributes it to trailing external service until it finally appears on the price search engine itself.

## PSE Core Service
The PSE Core Service takes preprocessed incoming data and calculates the optimal voucher value (absolute discount of a product in EUR) and gives it back to the PSE Orchestration Service for further distribution. For transparency and debugging it also stores the metadata and information on an internal data base.

## Other Microservices
See here for Data Integration Service Data Integration Service (DIS).

See here for Market Price Screening Service Market Price Screening (MPS).

See here for E-commerce Cloud Service (ECS) .

