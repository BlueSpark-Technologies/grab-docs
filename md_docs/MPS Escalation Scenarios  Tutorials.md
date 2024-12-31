# MPS Escalation Scenarios & Tutorials

| Scenario | Action | who? | Ticket / Link to documentation |
|---|---|---|---|
| How can we add new short names to competitors to be used in the Pricing UI and BI Tableau dashboards? | If you don’t add a short name the long name will be used in the dashboards and cockpits.Tutorial on how to update the short_name field for merchants: With your DB tool of choice (mine is PyCharm) connect to the Screening Production Database through the ssh tunnel provided by DevOps (check the artifacts page for it’s URI).1. Pick the “merchant“ table 2. change the short_name attribute of the desired row AND commit the change 3. In order to double check that it actually worked: Do a http:GET request to https://market-price-screening.service.cybersolutions-tech.com/v0/gzh/feed-items-details/H101-101 (use here any sku which  has an offer from the merchant you’re interested in,  instead of H101-101) and you should see the value you updated at step 2 in the  merchant_short_name field | Business Users |  |
| How can we add new competitor to the competitor list to be considered by MPS? | See ECS Escalation Scenarios & Tutorials |  |  |
|  |  |  |  |

Scenario

Action

who?

Ticket / Link to documentation

How can we add new short names to competitors to be used in the Pricing UI and BI Tableau dashboards?

If you don’t add a short name the long name will be used in the dashboards and cockpits.Tutorial on how to update the short_name field for merchants:

With your DB tool of choice (mine is PyCharm) connect to the Screening Production Database through the ssh tunnel provided by DevOps (check the artifacts page for it’s URI).1. Pick the “merchant“ table

2. change the short_name attribute of the desired row AND commit the change

3. In order to double check that it actually worked: Do a http:GET request to https://market-price-screening.service.cybersolutions-tech.com/v0/gzh/feed-items-details/H101-101 (use here any sku which  has an offer from the merchant you’re interested in,  instead of H101-101) and you should see the value you updated at step 2 in the  merchant_short_name field

Business Users

How can we add new competitor to the competitor list to be considered by MPS?

See ECS Escalation Scenarios & Tutorials

