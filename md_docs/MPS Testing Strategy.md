# MPS Testing Strategy

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

## Types of Testing (applicable to MPS)
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

Market Price Screening Algorithm Validation Test

As developer I want to be able to easily spot bugs in the Market Price Screening algorithm. Therefore we need an end-to-end data validation test using real files and real data and checking the accuracy of the results.

We have multiple files needed for the test:

* real GZH file from a past date
* real WIT file incl Idealo data from a past date
* csv for relevant competitors in ECOMM
* csv for global competitor configuration in ECOMM
* csv for hierarchy item in ECOMM
* csv for link between competitors and products in ECOMM
* csv for item info in DIS
* csv for expected results

real GZH file from a past date

real WIT file incl Idealo data from a past date

csv for relevant competitors in ECOMM

csv for global competitor configuration in ECOMM

csv for hierarchy item in ECOMM

csv for link between competitors and products in ECOMM

csv for item info in DIS

csv for expected results

Steps:

Parse testing csvs and create entries for relevant competitors + global competitor + hierarchy item configuration in ECOMM data base using randomized uuids

Parse testing csvs and create entries for item info in DIS data base using randomized uuids

Empty ECS and DIS API endpoint caches in MPS for all affected SKUs

Trigger file import in MPS using GZH and WIT file from the test set above

After processing has finished assert results of MPS table latest_offers with the expected results csv from Exasol.

You can assert the fields my_price, my_availability, my_shipping_cost per SKU by filtering the csv on merchant_name == 'Cyberport'

For getting all others offers per SKU and asserting the completeness of feed_item_merchants and the fields merchant_name, merchant_short_name, price, availability, shipping_cost, you have to filter on merchant_name != 'Cyberport'. The other columns like ean and provider_item_name can’t be asserted because we don’t have these columns in Exasol.

Aim is to get 100%. If it's not 100% we should look at each row in the csv and if it's for example floating point errors in Exasol we can change the rows in the csv for expected results.

This is how you can create new files if necessary: Performed this shortly after the feed processing in Exasol ran through at 08:00 UTC+1.

Run this after file processing in DWH autopricing has finished (use a different path on your machine)

Select latest two feed files, one for GZH and one for WIT incl Idealo data. Make sure you select the latest files at the time at which Exasol ran (usually 8:20 German time) for each supplier from this production S3 bucket https://s3.console.aws.amazon.com/s3/buckets/feedservice.

Query latest results from DIS

Query latest results from ECOMM

