# MPS Release Notes

# Release Notes before 2023
Please enter here the release notes of the Market Price Screening.

# Austrian Version
## MPS-AT-0.1.0 - 25.02.2021
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10163

Description: This is the first release of the Austrian Market Price Screening. It stores only the unprocessed csvs in S3, nothing more. Uses code from MPS-1.3.1.

Bug

* [PA-344] - Create Austrian Market Price Screening version MPS AT from German MPS

[PA-344] - Create Austrian Market Price Screening version MPS AT from German MPS

# German Version
## MPS-2.9.1 - 03.01.2023
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10430/tab/release-report-all-issues

Description: Due to a bug we couldn't process some WorkIT files. This should be fixed now.

Story

* PA-902 Investigate and fix AttributeError: 'NoneType' object has no attribute 'iterchildren'

PA-902 Investigate and fix AttributeError: 'NoneType' object has no attribute 'iterchildren'

## MPS-2.9.0 - 17.10.2022
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10378/

Description: Consuming and saving in db the ASIN field of the Workit feed file.

Story

* PA-864 Check if new feed has the same structure
* PA-865 [MPS] Parse data from feed and store ASIN number in MPS DB

PA-864 Check if new feed has the same structure

PA-865 [MPS] Parse data from feed and store ASIN number in MPS DB

## MPS-2.8.0 - 24.05.2022
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10347

Description: This release brings performance improvements by enabling SKU caching while checking SKU validity. It also adds Time To Leave (TTL) strategy to Argo workflows.

Story

* PA-714 Add TTL Strategy for all Argo Cron Workflows
* PA-689 Review caching approach used by MPS when determining whether a sku is valid
* PA-727 Remove SKU validation logic when receiving a request for merged feed item details
* PA-695 Disable newrelic distributed tracing in preprod

PA-714 Add TTL Strategy for all Argo Cron Workflows

PA-689 Review caching approach used by MPS when determining whether a sku is valid

PA-727 Remove SKU validation logic when receiving a request for merged feed item details

PA-695 Disable newrelic distributed tracing in preprod

## MPS-2.7.0 - 29.03.2022
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10314

Description: This release enables parallel processing of GZH data in csv file, WIT is unchanged.

Story

* PA-541 Optimize file processing in MPS

PA-541 Optimize file processing in MPS

## MPS-2.6.0 - 27.01.2022
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10305

Description: From this release on our offer gets not only taken from GZH, but when it's null gets overwritten by WIT and IDL. Therefore we now have more often than not a my_price feed_item object returned in the API.

Story

* PA-636 Coalesce our own offer from GZH, WIT + IDL

PA-636 Coalesce our own offer from GZH, WIT + IDL

## MPS-2.5.0 - 20.01.2022
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10300

Description: Now again our own offer is included in the outlier detection, S3 bucket names have uniform names and data is only returned from API endpoints if processing was successful for both feed suppliers.

Bug

* PA-613 Fix cleanup-db command failing when a batch contains only one item

PA-613 Fix cleanup-db command failing when a batch contains only one item

Story

* PA-625 Include our own offer in outlier detection
* PA-623 Prepare, assist and test release MPS-2.5.0
* PA-620 Ensure uniform naming in MPS S3 buckets
* PA-604 Check latest successful export for all providers

PA-625 Include our own offer in outlier detection

PA-623 Prepare, assist and test release MPS-2.5.0

PA-620 Ensure uniform naming in MPS S3 buckets

PA-604 Check latest successful export for all providers

Task

* PA-619 Enable Newrelic Distributed Tracing Feature
* PA-609 Enforce Flake8 checks to be made when tests are ran in CI for all Pricing Projects

PA-619 Enable Newrelic Distributed Tracing Feature

PA-609 Enforce Flake8 checks to be made when tests are ran in CI for all Pricing Projects

## MPS-2.4.1 - 16.12.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10301

Description: After making changes in Exasol as well we need to increase the offer filter in all places from 24h to 48h.

Story

* PA-611 Increase offer filter from 24h to 48h and release to prod

PA-611 Increase offer filter from 24h to 48h and release to prod

## MPS-2.4.0 - 15.12.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10264

Description: This release handles down-times and ensures a better data quality for the Base Price Service by moving the outlier detection to after the merging of the feeds.

Story

* PA-610 Prepare, assist and test release MPS-2.4.0
* PA-600 Change sequence outlier detection after merging step
* PA-501 Only discard product catalogue in malformed XML files

PA-610 Prepare, assist and test release MPS-2.4.0

PA-600 Change sequence outlier detection after merging step

PA-501 Only discard product catalogue in malformed XML files

Task

* PA-601 Check if we still return data if offers haven't changed in 24 hours

PA-601 Check if we still return data if offers haven't changed in 24 hours

## MPS-2.3.0 - 07.12.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10274

Description: Again this release contains bug fixes for processing our offer from Geizhals files twice and thus ignoring it because of duplicate checks. Also we make sure not to price anything as no_merchant because of MPS downtimes.

Bug

* PA-562 Find cause of wrong offers for SKU QE04-006
* PA-555 Find cause of error messages "No fi_objs_prioritized found"

PA-562 Find cause of wrong offers for SKU QE04-006

PA-555 Find cause of error messages "No fi_objs_prioritized found"

Story

* PA-603 Prepare, assist and test release MPS-2.3.0
* PA-594 Argo cron workflows - uniform history and retry policy
* PA-486 Handle downtimes of depending services

PA-603 Prepare, assist and test release MPS-2.3.0

PA-594 Argo cron workflows - uniform history and retry policy

PA-486 Handle downtimes of depending services

Sub-task

* PA-591 Stop using data from "Mein..." columns to save own offer

PA-591 Stop using data from "Mein..." columns to save own offer

Task

* PA-571 Reduce cost on Aurora Instance for MPS

PA-571 Reduce cost on Aurora Instance for MPS

## MPS-2.2.0 - 18.10.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10255

Description: From this release on we ensure that GZH parsing follows the same changed rules as in WIT parsing.

Bug

* PA-482 Investigate root cause for cleanup-db command failing with a timeout

PA-482 Investigate root cause for cleanup-db command failing with a timeout

Story

* PA-536 Double check that Geizhals feed parsing follows the WIT/IDL newly implemented business rules

PA-536 Double check that Geizhals feed parsing follows the WIT/IDL newly implemented business rules

## MPS-2.1.5 - 13.10.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10268

Description: Fixes a major floating point accuracy bug.

Bug

* PA-550 Fix decimal / floating point accuracy in MPS data import

PA-550 Fix decimal / floating point accuracy in MPS data import

## MPS-2.1.4 - 08.10.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10268

Description: MPS patch to fix merging duplicates.

Bug

* PA-543 MPS patch to fix merging duplicates

PA-543 MPS patch to fix merging duplicates

## MPS-2.1.1-3 - 07.10.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10265

Description: For the last release a hotfix is necessary to enable file import again.

Bug

* PA-538 Hotfix key / value error in MPS after MPS-2.1.0 release

PA-538 Hotfix key / value error in MPS after MPS-2.1.0 release

## MPS-2.1.0 - 07.10.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10263

Description: This release contains a bug fix that we had in the merging of competitor offers from different files.

Story

* PA-533 Find bug in merging step in MPS

PA-533 Find bug in merging step in MPS

Bug

* PA-537 Prepare, release and test release-candidate MPS-2.1.0

PA-537 Prepare, release and test release-candidate MPS-2.1.0

## MPS-2.0.1 - 30.09.2021
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10262

Description: Patching any obvious bugs from the major 2.0.0 release

Story

* PA-513 Fix bugs found in 2.0.0 and release them as 2.0.1

PA-513 Fix bugs found in 2.0.0 and release them as 2.0.1

## MPS-2.0.0 - 29.09.2021
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10251

Description: This release contains some bug fixes to optimize data base clean up and filtering of competitor offers. Furthermore now we can now process offers spread across multiple catalogues in WIT and even if there is now offer by the tenant itself in the file.

Bug

* PA-485 Investigate Alternate.de merchant offer from WIT not being considered for product 1C22-1PV

PA-485 Investigate Alternate.de merchant offer from WIT not being considered for product 1C22-1PV

Story

* PA-502 Use v2 DIS API endpoints in MPS
* PA-497 Prepare assist and test release MPS-2.0.0
* PA-496 Implement solution for dealing with spread offers in WIT
* PA-495 Investigate solution for spread offers in WIT xml

PA-502 Use v2 DIS API endpoints in MPS

PA-497 Prepare assist and test release MPS-2.0.0

PA-496 Implement solution for dealing with spread offers in WIT

PA-495 Investigate solution for spread offers in WIT xml

## MPS-1.4.0 - 18.08.2021
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10198

Description: Old data is deleted from service after having been stored in DHS. Also we proceed with all globally relevant competitors if no relevant competitors are specified product wise in ECOMM.

Story

* PA-467 Use all competitors if no relevant competitors are specified.
* PA-458 Prepare assist and test release MPS-1.4.0
* PA-452 Extend merged_feed details endpoint by merchant names
* PA-450 Set timeout for Argo workflows in MPS
* PA-327 Create cron job to cleanse MPS from outdated data

PA-467 Use all competitors if no relevant competitors are specified.

PA-458 Prepare assist and test release MPS-1.4.0

PA-452 Extend merged_feed details endpoint by merchant names

PA-450 Set timeout for Argo workflows in MPS

PA-327 Create cron job to cleanse MPS from outdated data

## MPS-1.3.2 - 18.05.2021
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10198

Description: Fix two small bugs that cause MPS Workflow failures when caching and storing files.

Bug

* [PA-413] - Market Price Screening workflow failed twice in PROD

[PA-413] - Market Price Screening workflow failed twice in PROD

## MPS-1.3.1 - 10.02.2021
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10161

Description: Something causes MPS workflow failures. This release takes care of the according bug.

Bug

* [PA-336] - Check cause of MPS workflow failures

[PA-336] - Check cause of MPS workflow failures

## MPS-1.3.0 - 04.02.2021
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10154

Description: This release contains some bug fixes. Previously too many messages were pushed to the merged_feed_items topic and our own offers were deployed along with competitor offers.

Bug

* [PA-322] - feed_item_merchants section in MPS API endpoint for merged_feed_items endpoint shouldn't contain our offer
* [PA-323] - Too many notifications of type "merged" are sent to the SNS topic

[PA-322] - feed_item_merchants section in MPS API endpoint for merged_feed_items endpoint shouldn't contain our offer

[PA-323] - Too many notifications of type "merged" are sent to the SNS topic

## MPS-1.2.0 - 21.01.2021
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10123

Description: From this release on any service can extract the parsed and filtered data for a single feed supplier as well as a merged version of the latest feed data accross multiple feed suppliers using an API. Furthermore only valid SKUs get pushed to the MPS Topic.

Story

* [PA-175] - Push final merchant offer list for each remaining SKU on MPS Topic
* [PA-183] - Create API endpoint to return relevant offers for sku
* [PA-262] - Implement merging algorithm to combine WIT, GZH and IDL
* [PA-265] - Optimize argo cron jobs for importing and processing feed files
* [PA-266] - Check incoming SKUs for validity

[PA-175] - Push final merchant offer list for each remaining SKU on MPS Topic

[PA-183] - Create API endpoint to return relevant offers for sku

[PA-262] - Implement merging algorithm to combine WIT, GZH and IDL

[PA-265] - Optimize argo cron jobs for importing and processing feed files

[PA-266] - Check incoming SKUs for validity

## MPS-1.1.1 - 17.12.2020
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10146

Description: This release contains a hot fix for speeding up API endpoints

Story

* [PA-289] - Deploy hotfix MPS-1.1.1 for Market Price Screening

[PA-289] - Deploy hotfix MPS-1.1.1 for Market Price Screening

## MPS-1.1.0 - 16.12.2020
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10080

Description: This release implements basic filtering and preprocessing of incoming merchant data necessary for Autopricing. It also implements the merging of multiple feeds.

Story

* [PA-84] - Create API call to retrieve offers per product_feed_code and sku
* [PA-170] - Get Configuration Relevant Feed Supplier
* [PA-171] - Get Configuration Merchant Mapping
* [PA-173] - Get Configuration Product Specific Relevant Competitors
* [PA-174] - Implement price feed filtering
* [PA-228] - Implement fail checks for data import
* [PA-272] - Release MPS-1.1.0 into production
* [PA-287] - Add database indices to fix data retrieval in API endpoints

[PA-84] - Create API call to retrieve offers per product_feed_code and sku

[PA-170] - Get Configuration Relevant Feed Supplier

[PA-171] - Get Configuration Merchant Mapping

[PA-173] - Get Configuration Product Specific Relevant Competitors

[PA-174] - Implement price feed filtering

[PA-228] - Implement fail checks for data import

[PA-272] - Release MPS-1.1.0 into production

[PA-287] - Add database indices to fix data retrieval in API endpoints

## MPS-1.0.1 - 29.10.2020
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10132

Description: Fix for PA-270 Gracefully fail when the ftp server is not available or hasn't yet published the file for the current day

Story

* [PA-270] - Gracefully fail when the ftp server is not available or hasn't yet published the file for the current day

[PA-270] - Gracefully fail when the ftp server is not available or hasn't yet published the file for the current day

## MPS-1.0.0 - 29.10.2020
Link to Jira: https://cyber-solutions.atlassian.net/projects/PA/versions/10064

Description: In this release the feed suppliers WorkIT and Idealo get integrated into the Market Price Screening.

Story

* [PA-82] - Import WorkIT XML file
* [PA-230] - MPS - Write deployment validation tests
* [PA-235] - Process and store WorkIT / Idealo data
* [PA-245] - Reduce log messages produced by MPS

[PA-82] - Import WorkIT XML file

[PA-230] - MPS - Write deployment validation tests

[PA-235] - Process and store WorkIT / Idealo data

[PA-245] - Reduce log messages produced by MPS

## MPS-0.7.0-0.7.3 - 18.-22.09.2020
Link to Jira: https://cyber-solutions.atlassian.net/browse/PA/fixforversion/10063

Description: This release updates the existing Market Price Screening to current standards in the CST microservice infrastructure.

Story

* [PA-167] - Drop client name from API
* [PA-168] - Update project structure
* [PA-169] - Update API filtering and pagination
* [PA-214] - Increase test coverage
* [PA-221] - Integrate test coverage plugin for Market Price Screening
* [PA-222] - Review MPS data model
* [PA-223] - Update general MPS documentation
* [PA-224] - Create Risk Analysis
* [PA-225] - Set up appropriate logging on Sumologic and New Relic
* [PA-242] - Fix release MPS-0.7.0 after incident 31

[PA-167] - Drop client name from API

[PA-168] - Update project structure

[PA-169] - Update API filtering and pagination

[PA-214] - Increase test coverage

[PA-221] - Integrate test coverage plugin for Market Price Screening

[PA-222] - Review MPS data model

[PA-223] - Update general MPS documentation

[PA-224] - Create Risk Analysis

[PA-225] - Set up appropriate logging on Sumologic and New Relic

[PA-242] - Fix release MPS-0.7.0 after incident 31

Subtask

* [PA-229] - Update application data model according to lucidchart diagram

[PA-229] - Update application data model according to lucidchart diagram

Release was spread over multiple days and version number because of 

    

            




    
 INCIDENT-31
                    -
            Getting issue details...
STATUS

## MPS-0.6.0 - 2019
No release notes available before 2019

