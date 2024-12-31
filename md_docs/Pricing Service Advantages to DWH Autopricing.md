# Pricing Service Advantages to DWH Autopricing

In the following two tables we have collected general advantages of the new Pricing Service  compared to the existing Data Warehouse Autopricing in Exasol as well as minor issues that should not go fully unnoticed.

| Advantages Pricing Service | Reason |
|---|---|
| Near-time pricing instead of once a day → more up to date prices | In DWH autopricing we receive fresh data at most daily, in some cases even only from day before yesterdayIn PS most fields are delivered in near-real time from SAP Pro day and night. |
| Step towards replacing Cyberparts | In accordance to agreed target architecture for price flow: Pricing Service communicates with SAP Pro and not Cyberparts anymoreHaving the base price in the microservice landscape sets the way for channel pricing (eBay, Stores, Mercateo, B2B, …) |
| Product can be more easily given to new tenants (Computer Universe, Silkes Weinkeller) | python code is universal, not every tenant has Exasol as a data base and SQL flavorcode only needs to be maintained in one place, since Rest APIs are common standard across industry |
| More sophisticated and Machine Learning algorithms possible | In Exasol we were limited to mostly SQL built in functionsSince the new code is in Python we can use open source Machine Learning librariesuse more complicated mathematical functions availableimport data from multiple data bases and data lakes, not just Exasol |
| Increased code quality → less bugs → better price quality | code review by professional python developersautomation tests using python libraries by QAarchitecture reviewed by software architect |
| We expect reduce price discrepancies between Webshop and SAP → less man power needed by CRM | Export from SAP Pro to web shop and to SAP takes differently long (difference up to multiple hours)Due to more distributed price exports across the whole day (up to 500 changes per hour) the differing export duration should be less of an issue |
| Reduced maintenance time in the long run | We have a uniform documentation structure in Confluence and code structure in a central microservice libraryJira structure for new requirementsthat is the same across all microservices.Well documented code makes it easier for new developers to onboard on of our projects |
| Fully automatic up-/downscaling depending on changes in data | Using Keda and AWS the Pricing Service automatically increases resources and computation power if many incoming price triggers and data changes are. This is important after down times from SAP Pro, changed configuration by CMs, Christmas, black weekend.This scaling works day and night without human intervention which is great for weekends |
| More data is stored than in DWH autopricing | Merchant data is stored whenever a new file is created, whereas in Exasol data is processed less often → great for collecting training data for Machine Learning models |
| Exasol performance increases if DWH autopricing is done solely in PS | The DWH autopricing and dependent scripts take resources from Exasol that are freed after full go-live. |
| Higher security measurements | Every user who has access to Exasol can view and extract our pricing algorithms. Also the connection to Cyberparts via FTP is insecure because of the FTP settings, therefore it wouldn’t be hard to hack the system. The Pricing Service repositories and data base are under security audits and are protected via Single-Sign-On login. Only team members can access it. |

Advantages Pricing Service

Reason

Near-time pricing instead of once a day → more up to date prices

* In DWH autopricing we receive fresh data at most daily, in some cases even only from day before yesterday
* In PS most fields are delivered in near-real time from SAP Pro day and night.

In DWH autopricing we receive fresh data at most daily, in some cases even only from day before yesterday

In PS most fields are delivered in near-real time from SAP Pro day and night.

Step towards replacing Cyberparts

* In accordance to agreed target architecture for price flow: Pricing Service communicates with SAP Pro and not Cyberparts anymore
* Having the base price in the microservice landscape sets the way for channel pricing (eBay, Stores, Mercateo, B2B, …)

In accordance to agreed target architecture for price flow: Pricing Service communicates with SAP Pro and not Cyberparts anymore

Having the base price in the microservice landscape sets the way for channel pricing (eBay, Stores, Mercateo, B2B, …)

Product can be more easily given to new tenants (Computer Universe, Silkes Weinkeller)

* python code is universal, not every tenant has Exasol as a data base and SQL flavor
* code only needs to be maintained in one place, since Rest APIs are common standard across industry

python code is universal, not every tenant has Exasol as a data base and SQL flavor

code only needs to be maintained in one place, since Rest APIs are common standard across industry

More sophisticated and Machine Learning algorithms possible

* In Exasol we were limited to mostly SQL built in functions
* Since the new code is in Python we can use open source Machine Learning librariesuse more complicated mathematical functions availableimport data from multiple data bases and data lakes, not just Exasol
* use open source Machine Learning libraries
* use more complicated mathematical functions available
* import data from multiple data bases and data lakes, not just Exasol

In Exasol we were limited to mostly SQL built in functions

Since the new code is in Python we can

* use open source Machine Learning libraries
* use more complicated mathematical functions available
* import data from multiple data bases and data lakes, not just Exasol

use open source Machine Learning libraries

use more complicated mathematical functions available

import data from multiple data bases and data lakes, not just Exasol

Increased code quality → less bugs → better price quality

* code review by professional python developers
* automation tests using python libraries by QA
* architecture reviewed by software architect

code review by professional python developers

automation tests using python libraries by QA

architecture reviewed by software architect

We expect reduce price discrepancies between Webshop and SAP → less man power needed by CRM

* Export from SAP Pro to web shop and to SAP takes differently long (difference up to multiple hours)
* Due to more distributed price exports across the whole day (up to 500 changes per hour) the differing export duration should be less of an issue

Export from SAP Pro to web shop and to SAP takes differently long (difference up to multiple hours)

Due to more distributed price exports across the whole day (up to 500 changes per hour) the differing export duration should be less of an issue

Reduced maintenance time in the long run

We have a uniform

* documentation structure in Confluence and
* code structure in a central microservice library
* Jira structure for new requirements

documentation structure in Confluence and

code structure in a central microservice library

Jira structure for new requirements

that is the same across all microservices.

Well documented code makes it easier for new developers to onboard on of our projects

Fully automatic up-/downscaling depending on changes in data

* Using Keda and AWS the Pricing Service automatically increases resources and computation power if many incoming price triggers and data changes are.
* This is important after down times from SAP Pro, changed configuration by CMs, Christmas, black weekend.
* This scaling works day and night without human intervention which is great for weekends

Using Keda and AWS the Pricing Service automatically increases resources and computation power if many incoming price triggers and data changes are.

This is important after down times from SAP Pro, changed configuration by CMs, Christmas, black weekend.

This scaling works day and night without human intervention which is great for weekends

More data is stored than in DWH autopricing

Merchant data is stored whenever a new file is created, whereas in Exasol data is processed less often → great for collecting training data for Machine Learning models

Exasol performance increases if DWH autopricing is done solely in PS

The DWH autopricing and dependent scripts take resources from Exasol that are freed after full go-live.

Higher security measurements

* Every user who has access to Exasol can view and extract our pricing algorithms.
* Also the connection to Cyberparts via FTP is insecure because of the FTP settings, therefore it wouldn’t be hard to hack the system.
* The Pricing Service repositories and data base are under security audits and are protected via Single-Sign-On login. Only team members can access it.

Every user who has access to Exasol can view and extract our pricing algorithms.

Also the connection to Cyberparts via FTP is insecure because of the FTP settings, therefore it wouldn’t be hard to hack the system.

The Pricing Service repositories and data base are under security audits and are protected via Single-Sign-On login. Only team members can access it.

| Watch outs |  |
|---|---|
| No ad-hoc development | Adding new fields into our algorithms might require adding them in the Data Integration Service first, which envolves two more teams (SAP Pro and Integration) and therefore needs longer timeBut this is mainly an issue until most relevant fields are added to SAP Pro and the Data Integration Servicechanges can’t and shouldn’t be released by a single person due to quality assurance process and distributed architectureBut we have escalation scenarios for downtimes, incoming data errorsBut multiple people were onboarded to perform emergency operations regarding down-timesBut we reduce the room for errors if processes are followed |
| Reporting gets a bit more complicated | BI needs to adapt general assumption that a product has exactly one product price per day and build different dashboards.But this is only a temporary issue until BI changes theseSince Tableau currently doesn’t work in real time, there might be price discrepancies over the day between webshop and pricing dashboardsBut we are already in conversation with BI to find a better update schedule for dashbaordsDebugging of a price might take longer as prices might change quicklyBut we are already planning an improved Pricing Cockpit to visualize data errors and bad configuration |

Watch outs

No ad-hoc development

* Adding new fields into our algorithms might require adding them in the Data Integration Service first, which envolves two more teams (SAP Pro and Integration) and therefore needs longer timeBut this is mainly an issue until most relevant fields are added to SAP Pro and the Data Integration Service
* But this is mainly an issue until most relevant fields are added to SAP Pro and the Data Integration Service
* changes can’t and shouldn’t be released by a single person due to quality assurance process and distributed architectureBut we have escalation scenarios for downtimes, incoming data errorsBut multiple people were onboarded to perform emergency operations regarding down-timesBut we reduce the room for errors if processes are followed
* But we have escalation scenarios for downtimes, incoming data errors
* But multiple people were onboarded to perform emergency operations regarding down-times
* But we reduce the room for errors if processes are followed

Adding new fields into our algorithms might require adding them in the Data Integration Service first, which envolves two more teams (SAP Pro and Integration) and therefore needs longer time

* But this is mainly an issue until most relevant fields are added to SAP Pro and the Data Integration Service

But this is mainly an issue until most relevant fields are added to SAP Pro and the Data Integration Service

changes can’t and shouldn’t be released by a single person due to quality assurance process and distributed architecture

* But we have escalation scenarios for downtimes, incoming data errors
* But multiple people were onboarded to perform emergency operations regarding down-times
* But we reduce the room for errors if processes are followed

But we have escalation scenarios for downtimes, incoming data errors

But multiple people were onboarded to perform emergency operations regarding down-times

But we reduce the room for errors if processes are followed

Reporting gets a bit more complicated

* BI needs to adapt general assumption that a product has exactly one product price per day and build different dashboards.But this is only a temporary issue until BI changes these
* But this is only a temporary issue until BI changes these
* Since Tableau currently doesn’t work in real time, there might be price discrepancies over the day between webshop and pricing dashboardsBut we are already in conversation with BI to find a better update schedule for dashbaords
* But we are already in conversation with BI to find a better update schedule for dashbaords
* Debugging of a price might take longer as prices might change quicklyBut we are already planning an improved Pricing Cockpit to visualize data errors and bad configuration
* But we are already planning an improved Pricing Cockpit to visualize data errors and bad configuration

BI needs to adapt general assumption that a product has exactly one product price per day and build different dashboards.

* But this is only a temporary issue until BI changes these

But this is only a temporary issue until BI changes these

Since Tableau currently doesn’t work in real time, there might be price discrepancies over the day between webshop and pricing dashboards

* But we are already in conversation with BI to find a better update schedule for dashbaords

But we are already in conversation with BI to find a better update schedule for dashbaords

Debugging of a price might take longer as prices might change quickly

* But we are already planning an improved Pricing Cockpit to visualize data errors and bad configuration

But we are already planning an improved Pricing Cockpit to visualize data errors and bad configuration

