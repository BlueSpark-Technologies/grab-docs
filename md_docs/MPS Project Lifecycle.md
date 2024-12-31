# MPS Project Lifecycle

The Market Price Screening was previously called Price Feed Service or PSE Feed Service and was one of the first microservices to be built by CyberSolutions Tech.

See here for Release Notes MPS Release Notes and here for who worked on the project at which times MPS Team Information.

## Version 0
It released in 2019 in a first iteration and contained merely a filtering for relevant competitors and available products. Product specific filtering was not implemented yet. Also there didn't exist and SNS topic and subscription possibility yet.

## Version 1
Version 1 is about to be released in 2020 and contains an SNS topic to notify subscribing services of new incoming and parsed market price data. Also it has a more profound product specific filtering based on the configuration coming from the E-Commerce Cloud Service. That way Category Managers can change the configuration in a comfortable UI and see the changes walk through the E-Commerce Cloud Service to the Market Price Screening to the PSE Voucher Service and the Base Price Service to Cyberparts and finally the Cyberport Webshop.

