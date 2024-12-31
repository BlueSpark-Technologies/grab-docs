# PS Migration B-Stock from Exasol

As b-stock team member I want the pricing of b-stock products to be reliable and fast. Additionally as service owner I want the product to be usable for multiple clients independent from client specific data base formats. Therefore we want to move the b-stock pricing completely within the microservice landscape and make it independent from Exasol.

This will

* enable near real time pricing
* make prices more accurate and less susceptible to data errors in Exasol
* make b-stock pricing sellable to other clients, who don’t have an Exasol environment

enable near real time pricing

make prices more accurate and less susceptible to data errors in Exasol

make b-stock pricing sellable to other clients, who don’t have an Exasol environment

## Links to Documentation / Epics / Demands
| Project Demand Ticket in CP Jira | https://devjira.cyberport.de/browse/ECSP-795 |
|---|---|
| Epic in CST Jira | PA-868
                    -
            Getting issue details...
STATUS |
| current documentation for the B-Stock algorithm | Stream: B-Stock Pricing |
| Lucid Chart of B-Stock algorithm | https://lucidapp.eu/lucidchart/cd77f13e-58b0-40dd-88c8-02c383e22e10/edit?page=0_0&invitationId=inv_9a8a6d26-4fc1-4fd0-b28a-ad95a002bbf8# |
| Exasol view that needs to be migrated | https://bitbucket.org/devcst/microservice_import_sqls/src/master/dis_data_import/V_DIS_B_STOCK_BASE.sql |
| B-Stock code that’s already in Pricing Service | https://bitbucket.org/devcst/pricing/src/master/src/pricing/base_pricing/streams/b_stock_pricing.py |
| B-Stock documentation from B-Stock Team | https://wiki.cyberport.de/pages/viewpage.action?spaceKey=retouren&title=B-Ware+Pricinglogik |

Project Demand Ticket in CP Jira

https://devjira.cyberport.de/browse/ECSP-795

Epic in CST Jira

PA-868
                    -
            Getting issue details...
STATUS

current documentation for the B-Stock algorithm

Stream: B-Stock Pricing

Lucid Chart of B-Stock algorithm

https://lucidapp.eu/lucidchart/cd77f13e-58b0-40dd-88c8-02c383e22e10/edit?page=0_0&invitationId=inv_9a8a6d26-4fc1-4fd0-b28a-ad95a002bbf8#

Exasol view that needs to be migrated

https://bitbucket.org/devcst/microservice_import_sqls/src/master/dis_data_import/V_DIS_B_STOCK_BASE.sql

B-Stock code that’s already in Pricing Service

https://bitbucket.org/devcst/pricing/src/master/src/pricing/base_pricing/streams/b_stock_pricing.py

B-Stock documentation from B-Stock Team

https://wiki.cyberport.de/pages/viewpage.action?spaceKey=retouren&title=B-Ware+Pricinglogik

## Parts already in Pricing Service
Part of the microservices are currently:

* Stream selection of b-stock products
* Processing of abs_devaluation & parent price
* Price Checks

Stream selection of b-stock products

Processing of abs_devaluation & parent price

Price Checks

## Parts that need to be migrated
Both the data imports of relevant data need to be migrated into the microservice landscape as well as the calculation logic

### Data imports
Import of

| Data | Explanation | Example values | Current source | New source |
|---|---|---|---|---|
| b-stock grades | This field is set by logistics staff and describes the degradation status of a b-stock product compared to a new product. | VA1, VA2, VA3, null | PROD_DS.PROD_WAREHOUSE_V_PRODUCTS | DISProductsInfo endpoint bStockGrade |
| age of b-stock product | Time since the product was approved in Cyberparts, i.e. date the product was offered in the webshop the first time | 01.01.2022 | PROD_DS.PROD_WAREHOUSE_V_PRODUCTS | DISProductsInfo endpointapprovalDate |
| average b-stock age | average age (time since approval date) of related active b-stock children | 60 | PROD_DS.PROD_WAREHOUSE_V_PRODUCTS_MV | DISProductsInfo endpointapprovalDate ProductBStock endpoint to find all related b-stock products |
| order history | How often were b-stock products sold in the last 180 days? | ? | PROD_DS.PROD_WAREHOUSE_V_PRODUCT_SALES_MV | DHSexasol.ordersexasol.products |
| parent price | Current base price of the new parent product | 99.50€ | PROD_DS.V_CYBERPARTS_PRICES | PS product.current_base_price_listed_gross |
| current price | Current base price of the b stock  product | 89.50€ | PROD_DS.V_CYBERPARTS_PRICES | PS product.current_base_price_listed_gross |
| aggregated quantity | Total quantity of all b-stock products same parent product | 2 | PROD_DS.PROD_WAREHOUSE_V_PRODUCT_INVENTORY_MV | DIS ProductsStock endpointquantity |

Data

Explanation

Example values

Current source

New source

b-stock grades

This field is set by logistics staff and describes the degradation status of a b-stock product compared to a new product.

VA1, VA2, VA3, null

PROD_DS.PROD_WAREHOUSE_V_PRODUCTS

DIS

ProductsInfo endpoint

bStockGrade

age of b-stock product

Time since the product was approved in Cyberparts, i.e. date the product was offered in the webshop the first time

01.01.2022

PROD_DS.PROD_WAREHOUSE_V_PRODUCTS

DIS

ProductsInfo endpoint

approvalDate

average b-stock age

average age (time since approval date) of related active b-stock children

60

PROD_DS.PROD_WAREHOUSE_V_PRODUCTS_MV

DIS

ProductsInfo endpoint

approvalDate

ProductBStock endpoint to find all related b-stock products

order history

How often were b-stock products sold in the last 180 days?

?

PROD_DS.PROD_WAREHOUSE_V_PRODUCT_SALES_MV

DHS

exasol.orders

exasol.products

parent price

Current base price of the new parent product

99.50€

PROD_DS.V_CYBERPARTS_PRICES

PS

product.current_base_price_listed_gross

current price

Current base price of the b stock  product

89.50€

PROD_DS.V_CYBERPARTS_PRICES

PS

product.current_base_price_listed_gross

aggregated quantity

Total quantity of all b-stock products same parent product

2

PROD_DS.PROD_WAREHOUSE_V_PRODUCT_INVENTORY_MV

DIS

ProductsStock endpoint

quantity

### Calculation of devaluation value
Can this part of the calculation be simplified?

## Project Plan - to be discussed
| Step | What? | Who? | Status |
|---|---|---|---|
| 1 | Understand each step of the current algorithm | Hannah, Alex with B-Stock Team | DONE |
| 2 | Reduce the algorithm and deploy it on Exasol | Hannah | CANCELEDwill be done in the next phase |
| 3 | Find out which input data the algorithm needs | Alex | DONE |
| 4 | Alignment with existing data in DIS, what is missing? | Alex | DONE |
| 5 | Locate the target system from which we can get the missing data | Alex with Mihai Mocanu & Horatiu & Sebastian Moch | DONE |
| 6 | Contact Python Lead to clarify where which subtopics should be calculated (e.g. aggregation of sales volumes) | Alex with Horatiu & Nicu | IN PROGRESS |

Step

What?

Who?

Status

1

Understand each step of the current algorithm

Hannah, Alex with B-Stock Team

DONE

2

Reduce the algorithm and deploy it on Exasol

Hannah

CANCELED

will be done in the next phase

3

Find out which input data the algorithm needs

Alex

DONE

4

Alignment with existing data in DIS, what is missing?

Alex

DONE

5

Locate the target system from which we can get the missing data

Alex with Mihai Mocanu & Horatiu & Sebastian Moch

DONE

6

Contact Python Lead to clarify where which subtopics should be calculated (e.g. aggregation of sales volumes)

Alex with Horatiu & Nicu

IN PROGRESS

## Open questions
| Question | Background info | Answer |
|---|---|---|
| What do the B-stock grade values mean?-> GA1, GA2, GA3 don’t seem to be used any more-> VA1, VA2, VA3 are still used for active b-stock products |  | The GA1, GA2 and GA3 values aren’t maintained anymore, only the V values are. V3 means highest degradation value and thus should involve highest price decrease. |
| What do the configuration values mean in the table PROD_DS.APP_AUTO_PRICING_CONF_B_STOCK? |  | COVERAGE can be set per hierarchy level, VAL represents the average amounts of days until the product should be sold out. DEVALUATION is the relative factor |
| Who is maintaining / checking the configuration values in PROD_DS.APP_AUTO_PRICING_CONF_B_STOCK? |  | They were initially set up and evaluated with Dominik Eberlein and haven’t been changed since |

Question

Background info

Answer

What do the B-stock grade values mean?

-> GA1, GA2, GA3 don’t seem to be used any more-> VA1, VA2, VA3 are still used for active b-stock products

The GA1, GA2 and GA3 values aren’t maintained anymore, only the V values are. V3 means highest degradation value and thus should involve highest price decrease.

What do the configuration values mean in the table PROD_DS.APP_AUTO_PRICING_CONF_B_STOCK?

* COVERAGE can be set per hierarchy level, VAL represents the average amounts of days until the product should be sold out.
* DEVALUATION is the relative factor

COVERAGE can be set per hierarchy level, VAL represents the average amounts of days until the product should be sold out.

DEVALUATION is the relative factor

Who is maintaining / checking the configuration values in PROD_DS.APP_AUTO_PRICING_CONF_B_STOCK?

* They were initially set up and evaluated with Dominik Eberlein and haven’t been changed since

They were initially set up and evaluated with Dominik Eberlein and haven’t been changed since

