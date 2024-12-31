# PSE Voucher Roadmap & Estimation 2021

In the next iteration we want the PSE Voucher Service to work again for Cyberport. (stand Sep 2020 it only works for Computer Universe).

As customers exploited the previous versions of the PSE voucher service (see here for details PSE Project Lifecycle) we need some changes to be made in the legacy systems connected to the PSE Voucher Service. Therefore our Business Owner Ralph Andreeff created an official demand ticket https://devjira.cyberport.de/browse/CPDM2-3154 to change the Legacy Architecture in SAP / Cyberparts / Webshop. (If you don't have access communicate Dominik Eberlein please).

We wait until this is finished before we can reactivate and refurbish the PSE Voucher Core Service for Cyberport to use, so we don't need the prototype anymore.

Also for Cyberport we need to create the PSE Orchestration Service.

| Topic | Tasks | Dependencies | Python work estimate in man days | Comments / Questions |
|---|---|---|---|---|
| Technical Dept | Get service up to current standards (API pagination, endpoints, update libraries, we need swagger documentation) |  | 2d | unit test coverage is already more than 75%, Nicu already did some library updates |
| Initial set up | setting up the initial version of PSE Orchestration service |  | 1.5d |  |
| Data Import | API calls and subscription towards product_stock and product_price topics in DIS |  | 3.5d | we need two clients, one for fetching data on for listening to notifications |
|  | API calls and subscription towards MPS competitor data |  | 4d | we need two clients, one for fetching data on for listening to notifications |
|  | API calls for black / whitelisting on e-Commerce Cloud service | needs to be implemented in e-Commerce Cloud Service first (import from S3, storing in data base, create API endpoint) | 1.5d (+4d in CEC) | no queue, just an API call |
| PSE Orchestration Service internal | Parsing imported data, fetching data after notifications are triggered |  | 4d | if there are null values or data is not available, we just drop the product and give out a warning |
|  | making API request to PSE Core, responses are only stored in log messages |  | 1d | if anything goes wrong, we just drop the product and give out a warning |
| Algorithm (in PSE Core Service) | - | - | - | no changes in algorithm planned right now |
| Distribution | Creation distribution queue, messages should contain all relevant information | needs to be communicated with SAP Pro | 2d | essentially we can forward the response from PSE Core Service |
| Alerts | Default monitoring |  | 1d |  |
| End to end testing |  |  | 2d |  |
| SUM |  |  | 40 days=> 2 developers, 1 QA: 2 sprints=> 1 developer, 1QA: 4 sprints | Pure work PSE 22.5 days + CEC 4 days + 33% for meetings + 3days buffer, see here for (German) estimation communication towards other stakeholders: https://devjira.cyberport.de/browse/CPDM2-3154?filter=23051 |

Topic

Tasks

Dependencies

Python work estimate in man days

Comments / Questions

Technical Dept

Get service up to current standards (API pagination, endpoints, update libraries, we need swagger documentation)

2d

unit test coverage is already more than 75%, Nicu already did some library updates

Initial set up

setting up the initial version of PSE Orchestration service

1.5d

Data Import

API calls and subscription towards product_stock and product_price topics in DIS

3.5d

we need two clients, one for fetching data on for listening to notifications

API calls and subscription towards MPS competitor data

4d

we need two clients, one for fetching data on for listening to notifications

API calls for black / whitelisting on e-Commerce Cloud service

needs to be implemented in e-Commerce Cloud Service first (import from S3, storing in data base, create API endpoint)

1.5d (+4d in CEC)

no queue, just an API call

PSE Orchestration Service internal

Parsing imported data, fetching data after notifications are triggered

4d

if there are null values or data is not available, we just drop the product and give out a warning

making API request to PSE Core, responses are only stored in log messages

1d

if anything goes wrong, we just drop the product and give out a warning

Algorithm (in PSE Core Service)

-

-

-

no changes in algorithm planned right now

Distribution

Creation distribution queue, messages should contain all relevant information

needs to be communicated with SAP Pro

2d

essentially we can forward the response from PSE Core Service

Alerts

Default monitoring

1d

End to end testing

2d

SUM

40 days

=> 2 developers, 1 QA: 2 sprints

=> 1 developer, 1QA: 4 sprints

Pure work PSE 22.5 days + CEC 4 days + 33% for meetings + 3days buffer,

see here for (German) estimation communication towards other stakeholders: https://devjira.cyberport.de/browse/CPDM2-3154?filter=23051

| Non-Python Issue | Current solution | Target solution |
|---|---|---|
| business report: which vouchers are active?why were they calculated like that (source data) | Christian imports data from FTP server, creates report and exports csvs containing voucher data and Geizhals data. Runs automatically within a script on an ec2-instance. | Automated report or dashboard (Sumologic, extended report, export to S3 bucket). |

Non-Python Issue

Current solution

Target solution

business report:

* which vouchers are active?
* why were they calculated like that (source data)

which vouchers are active?

why were they calculated like that (source data)

Christian imports data from FTP server, creates report and exports csvs containing voucher data and Geizhals data. Runs automatically within a script on an ec2-instance.

Automated report or dashboard (Sumologic, extended report, export to S3 bucket).

