# PS Testing Strategy

## Objectives
The standard objectives of the testing activity are:

* Prevent and find defects
* Make sure the software meets the business requirements
* Gain confidence in the level of quality of the products we deliver

Prevent and find defects

Make sure the software meets the business requirements

Gain confidence in the level of quality of the products we deliver

## Implementation and Execution
* Develop and prioritize test cases
* Create test data
* Execute the test cases
* Compare expected and actual results
* Re-test in order to confirm a fix

Develop and prioritize test cases

Create test data

Execute the test cases

Compare expected and actual results

Re-test in order to confirm a fix

## Types of Testing (applicable to PS)
### Functional Testing
* Feature testing - This is done on a ticket base. Every Jira story is a feature and it needs to be tested individually in order to make sure it complies with the acceptance criteria. After that, a risk analysis should be done and see if further testing is needed - see Regression testing. Generally, this type of testing can be automated but we need to make sure we don't end up with very long test runs. It is generally a “back box“ type of testing, because we don’t have access to the application code
* Unit testing - The earliest type of testing. Mainly done by the development team(but testing team members can also help), it basically tests the units of code. This is “white box“ testing. While it can ensure a specific piece of code works well it cannot test its integration with the system. It is always automated
* Integration testing - It is relevant both in case of a micro service’s internal components, and in case of its interaction with the other micro services. This is what we call End to End tests. The aim here is to ensure our microservices work well as a system. It can be automated - we should make this one of our priorities. However, given the nature of our products, it will most likely never be fully automated(i.e integration with the Marketplace)
* Regression testing - Type of testing that ensures the implementation of a feature, or a bug fix, does not break other functionalities. This needs to be done for every ticket that we implement. Regression testing complexity is directly dependent on the system-under-test complexity. It can be automated.
* Smoke testing - Tests that ensure the basic functionality of a system. A smoke test suite contains only the essential tests that we need to run in order to decide if a system is up or down. This is fully automated and is done for any production release, but also on staging
* Contract testing - Is a way to ensure that services can communicate with each other as expected. The contract is between a consumer (a client who wants to receive some data from an app) and a provider (an API that provides the data the client needs). When a provider API is changed the developers need a way to know if those changes will affect the services which are using that provider, this is the case when contract-testing needs to be performed.

Feature testing - This is done on a ticket base. Every Jira story is a feature and it needs to be tested individually in order to make sure it complies with the acceptance criteria. After that, a risk analysis should be done and see if further testing is needed - see Regression testing. Generally, this type of testing can be automated but we need to make sure we don't end up with very long test runs. It is generally a “back box“ type of testing, because we don’t have access to the application code

Unit testing - The earliest type of testing. Mainly done by the development team(but testing team members can also help), it basically tests the units of code. This is “white box“ testing. While it can ensure a specific piece of code works well it cannot test its integration with the system. It is always automated

Integration testing - It is relevant both in case of a micro service’s internal components, and in case of its interaction with the other micro services. This is what we call End to End tests. The aim here is to ensure our microservices work well as a system. It can be automated - we should make this one of our priorities. However, given the nature of our products, it will most likely never be fully automated(i.e integration with the Marketplace)

Regression testing - Type of testing that ensures the implementation of a feature, or a bug fix, does not break other functionalities. This needs to be done for every ticket that we implement. Regression testing complexity is directly dependent on the system-under-test complexity. It can be automated.

Smoke testing - Tests that ensure the basic functionality of a system. A smoke test suite contains only the essential tests that we need to run in order to decide if a system is up or down. This is fully automated and is done for any production release, but also on staging

Contract testing - Is a way to ensure that services can communicate with each other as expected. The contract is between a consumer (a client who wants to receive some data from an app) and a provider (an API that provides the data the client needs). When a provider API is changed the developers need a way to know if those changes will affect the services which are using that provider, this is the case when contract-testing needs to be performed.

### Automated testing
Automated testing is a core activity in agile development methodology. Next to preventing the introduction of defects in the application, it also serves as a way of getting quick feedback on the health of the application. The amount, scope and coverage of automated tests should be preliminarily decided based on requirements, budget, timeline etc

Core automation testing types are:

* Regression Testing
* Smoke Testing
* End-to-End Testing
* Unit Testing

Regression Testing

Smoke Testing

End-to-End Testing

Unit Testing

Automated testing should be done in order to replace the repetitive and time consuming testing tasks like regression testing and smoke testing. However, automation is very useful in case of testing new features and integration/end-to-end testing. However, the automation test suites need to look at quality over quantity, and not add thousands of tests that would take a long time to execute but add the tests that matter.

### End-to-end tests
The End-to-End tests for the Pricing Service can be found in this repository https://bitbucket.org/devcst/cst-tests/ in subfolder. This repository also contains tests for the Data Integration Service, ECOMM and the other projects.

There are 2 types of tests there: sanity tests and functional tests. The sanity tests are executed in case of a new production deployment or on demand in order to ensure the basic functionality of the product is still working - calls are made to the API to check the response content, algorithms etc. The functional tests test the base price calculation algorithm and its integration with the other microservices.

As developer I want to be able to easily spot bugs in the Base Price Autopricing algorithm. Also I would like to see which prices change when considering a change of the algorithm or the configuration of the unchanged algorithm. Therefore we need an end-to-end data validation test using real files and real data and checking the accuracy of the results.

We have a testing suite csv needed for the test:

* testing suite in form of csv, one row per SKU containing all input_data from DIS and ECS and MPS necessary for price calculation as well as meta_data and price_calculation data for products which are expected to have a valid price and repricing_stopped data for products which are supposed to not be priced successfully. This file should include all edge cases like null value combinations as well as normal products that cover all streams and scenarios that should be considered when tinkering with the auto pricing algorithms.

testing suite in form of csv, one row per SKU containing all input_data from DIS and ECS and MPS necessary for price calculation as well as meta_data and price_calculation data for products which are expected to have a valid price and repricing_stopped data for products which are supposed to not be priced successfully. This file should include all edge cases like null value combinations as well as normal products that cover all streams and scenarios that should be considered when tinkering with the auto pricing algorithms.

Steps:

Parse testing csv and create entries for different configuration types like coverage based pricing, basic settings, price successors, etc. in ECOMM data base via POST requests for all products in the suite using randomized uuids

Parse testing csv and create entries product stock, product price, product info and shipping info data in DIS data base via POST requests for all products in the suite using randomized uuids

Parse testing csv and create entries for competitor offers in MPS data base via new entries in the latest_offer table for all products in the suite using randomized uuids

Empty ECS, DIS and MPS API endpoint caches in Pricing Service for all affected SKUs

Trigger automatic base price calculation in Pricing Service for all products in the suite

After calculation has finished assert results of Pricing Service with the expected results csv from the testing suite. Check all three types of data meta_data, price_calculation and repricing_stopped.

Aim is to get 100%. If it's not 100% we should look at each row in the csv and if it's for example floating point errors in Exasol we can change the rows in the csv for expected results.

### Pre-Go-Live tests
* Step 1: Write a PoC that returns the same as Exasol when fed with Exasol=> Status: DONE (tests on Hannah's machine)=> Result: we can trust the algorithms in the PoC to be the same as in Exasol
* => Status: DONE (tests on Hannah's machine)
* => Result: we can trust the algorithms in the PoC to be the same as in Exasol
* Step 2: Transform the PoC into a microservice and check if the microservice returns the same as Exasol when fed with Exasol data - CHECK (end-to-end tests)=> Status: DONE (tests on Hannah's machine)=> Result: we can trust the the algorithms in the microservice to be the same as in PoC and therefore in Exasol
* => Status: DONE (tests on Hannah's machine)
* => Result: we can trust the the algorithms in the microservice to be the same as in PoC and therefore in Exasol
* Step 3: Get the data quality from DIS, ECS and MPS to be the same (or better) than in Exasol=> Status: DONE for ECS and DIS, IN PROGRESS in MPS (DIS: data validation tests, ECS: tests on Hannah's machine, MPS: tests on Hannah's machine + Vasile's data validation tests in progress)=> Result:  we can trust the microservice data to be good enough for pricing
* => Status: DONE for ECS and DIS, IN PROGRESS in MPS (DIS: data validation tests, ECS: tests on Hannah's machine, MPS: tests on Hannah's machine + Vasile's data validation tests in progress)
* => Result:  we can trust the microservice data to be good enough for pricing
* Step 4: Check if the PoC returns the same (or better) prices as Exasol when fed with microservice data=> Status: IN PROGRESS  (tests on Hannah's machine), problems are that we can't get productive DIS data because of read-replica issues=> Result: technically it just double confirms step 3
* => Status: IN PROGRESS  (tests on Hannah's machine), problems are that we can't get productive DIS data because of read-replica issues
* => Result: technically it just double confirms step 3
* Step 5: Check if the BPS returns the same (or better) prices as Exasol=> Status: IN PROGRESS (tests on Hannah's machine, Vasile's data validation tests in progress)=> Result: we can trust that the data flow and price calculation triggers work well enough for pricing
* => Status: IN PROGRESS (tests on Hannah's machine, Vasile's data validation tests in progress)
* => Result: we can trust that the data flow and price calculation triggers work well enough for pricing

Step 1: Write a PoC that returns the same as Exasol when fed with Exasol

* => Status: DONE (tests on Hannah's machine)
* => Result: we can trust the algorithms in the PoC to be the same as in Exasol

=> Status: DONE (tests on Hannah's machine)

=> Result: we can trust the algorithms in the PoC to be the same as in Exasol

Step 2: Transform the PoC into a microservice and check if the microservice returns the same as Exasol when fed with Exasol data - CHECK (end-to-end tests)

* => Status: DONE (tests on Hannah's machine)
* => Result: we can trust the the algorithms in the microservice to be the same as in PoC and therefore in Exasol

=> Status: DONE (tests on Hannah's machine)

=> Result: we can trust the the algorithms in the microservice to be the same as in PoC and therefore in Exasol

Step 3: Get the data quality from DIS, ECS and MPS to be the same (or better) than in Exasol

* => Status: DONE for ECS and DIS, IN PROGRESS in MPS (DIS: data validation tests, ECS: tests on Hannah's machine, MPS: tests on Hannah's machine + Vasile's data validation tests in progress)
* => Result:  we can trust the microservice data to be good enough for pricing

=> Status: DONE for ECS and DIS, IN PROGRESS in MPS (DIS: data validation tests, ECS: tests on Hannah's machine, MPS: tests on Hannah's machine + Vasile's data validation tests in progress)

=> Result:  we can trust the microservice data to be good enough for pricing

Step 4: Check if the PoC returns the same (or better) prices as Exasol when fed with microservice data

* => Status: IN PROGRESS  (tests on Hannah's machine), problems are that we can't get productive DIS data because of read-replica issues
* => Result: technically it just double confirms step 3

=> Status: IN PROGRESS  (tests on Hannah's machine), problems are that we can't get productive DIS data because of read-replica issues

=> Result: technically it just double confirms step 3

Step 5: Check if the BPS returns the same (or better) prices as Exasol

* => Status: IN PROGRESS (tests on Hannah's machine, Vasile's data validation tests in progress)
* => Result: we can trust that the data flow and price calculation triggers work well enough for pricing

=> Status: IN PROGRESS (tests on Hannah's machine, Vasile's data validation tests in progress)

=> Result: we can trust that the data flow and price calculation triggers work well enough for pricing

