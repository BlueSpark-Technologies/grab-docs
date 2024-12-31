# Stream: Merchant Based Pricing

## Motivation
The purpose of the pricing stream Merchant Based Pricing is to adapt the price of a product to the prices of the competition. In this stream are only products with competing merchant offers available in our price feed data. Prices get chosen according to a configured percentile per product. A percentile value of 0.3 means that 30% of the landed competitor offers are cheaper than our own offer. The percentiles can be configured per category group or article group.

On the calculated prices then price caps are applied. We don’t want to be more expensive than the recommended retails price for example and don’t want to undercut the minimal margin. Also we don’t want to be cheaper than the lowest competitor offer.

Currently price changes only apply daily although feed information is updated multiple times a day. Pricing Service tackles that issue because it enables pricing more than once daily.

## Configuration
There are multiple configurations for this stream:

* Global Merchant Selection (which merchants are considered relevant in general): This is not configurable in the UI, but only in Exasol PROD_DS.PROD_STAGING_PRC_MAP_MERCHANTS_MV
* Product Merchant Selection Configuration (which of the globally admitted merchants are relevant for a product / article group / category level 3): This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications.Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and category level 3 null
* This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications.
* Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and category level 3 null
* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and category level 3 null
* Tiering configuration (which percentile should be used for a product / article group / category level 3):This can be configured in the Pricing UI section Basic Settings. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and product hierarchy null
* This can be configured in the Pricing UI section Basic Settings. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .
* Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and product hierarchy null
* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and product hierarchy null

Global Merchant Selection (which merchants are considered relevant in general): This is not configurable in the UI, but only in Exasol PROD_DS.PROD_STAGING_PRC_MAP_MERCHANTS_MV

Product Merchant Selection Configuration (which of the globally admitted merchants are relevant for a product / article group / category level 3):

* This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications.
* Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and category level 3 null
* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and category level 3 null

This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications.

Each product has exactly one matching row in this table:

* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and category level 3 null

if for the product's article group there is a row specified use that row,

if not and there is a row for the product hierarchy use that row,

if not use the general row with article group and category level 3 null

Tiering configuration (which percentile should be used for a product / article group / category level 3):

* This can be configured in the Pricing UI section Basic Settings. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .
* Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and product hierarchy null
* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and product hierarchy null

This can be configured in the Pricing UI section Basic Settings. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .

Each product has exactly one matching row in this table:

* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and product hierarchy null

if for the product's article group there is a row specified use that row,

if not and there is a row for the product hierarchy use that row,

if not use the general row with article group and product hierarchy null

## Algorithm
* Pricing for each product is based on the prices of selected providers.
* The more providers there are for a product, the more our price is oriented towards the cheapest provider; the fewer providers there are, the more it is oriented towards the most expensive provider. This typically puts us on the first page of price search engines.

Pricing for each product is based on the prices of selected providers.

The more providers there are for a product, the more our price is oriented towards the cheapest provider; the fewer providers there are, the more it is oriented towards the most expensive provider. This typically puts us on the first page of price search engines.

Terms:

* product price: VK1 Gross
* landed price: product price + shipping costs
* WG: commodity group
* AG: article group

product price: VK1 Gross

landed price: product price + shipping costs

WG: commodity group

AG: article group

Sequence:

Tier allocation; the quantiles per tier can be configured at WG/AG level

at least one competitor, then set landed price

* ≤ 3 Competitor à 30% Quantil (Tier 1)
* 4-6 Competitor à 40% Quantil (Tier 2)
* ≥ 7 Competitor à 50% Quantil (Tier 3)

≤ 3 Competitor à 30% Quantil (Tier 1)

4-6 Competitor à 40% Quantil (Tier 2)

≥ 7 Competitor à 50% Quantil (Tier 3)

No automatic price change if no competitor exists

| Strategy "MERCHANT BASED PRICING" |
|---|
| Selection of all relevant products(see also here Base Price Algorithm: Stream Selection) | Product ismerchandise article (no voucher or software license or similar)no B-stock productactive, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”no bundleon the auto pricing list, not excluded from auto pricing, not manually deactivatednot activated for COVERAGE BASED PRICINGno ENFORCE RRP pricingno unhealthy inventoryno activated for Price Relations Pricingamount of considered competing merchants is > 0 (even if product is not available for them)is either no new product or has no valid recommended retail price (because then new product pricing can’t be applied)has neither price nor purchase_price quality issues |
| Price Calculation | a) Selection Tier: x := amount of configured competing merchants with stockif x = 0: ==> Percentile Tier 1 without stockif 1 ≤ x ≤ 3: ==> Percentile Tier 1if 4 ≤ x ≤ 6: ==> Percentile Tier 2if 7 ≤ x: ==> Percentile Tier 3b) Selection "tier price" Let’s define price(percentile, list of landed prices) as ==> the price that you get when you sort the list of n prices in a descending order and take the floor(percentile*n)-th price.Take the correct percentile value from the tiering configuration tables and calculate the tier price via==> reco landed price := price(percentile, list of competitor offers) |
| Price quality checks(see also here Base Price Algorithm: Price Quality Check) | Preparation for margin calculation:if standard purchase price < average purchase price==> product costs := standard purchase priceif inventory > 0 ==> product costs := average purchase priceotherwise==> product costs := standard purchase priceGet Margin Floor configuration for a product according to the following prioritization:Configuration for article group for a price rangeConfiguration for whole article groupConfiguration for category level 3 for a price rangeConfiguration for whole category level 3Default Configuration for a price rangeDefault ConfigurationGet Margin Cap configuration for a product according to the following prioritization:Configuration for article groupConfiguration for category level 3Default ConfigurationMax price := 1.19 * product costs / (1-margin cap)Min price := 1.19 * products costs /(1-margin floor)store limit:if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1otherwise ==> Store limit := 0a) Lowest Product Price: if reco landed price - shipping costs < lowest product price: ==> reco landed price := lowest product price + 1 + shipping costsotherwise ==> no changeb) RRP Cap:If Tier1: Use RRPIf Tier2 or Tier3: If there is competitor with price ≤ RRP: ==> use RRPotherwise if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price changec) Margin Cap: if reco landed price - shipping costs > max price ==> reco landed price := max_price + shipping costsd) Price Change Threshold    Letzter Pricing Stream != 'UNHEALTHY INVENTORY':if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7e) Margin Floorif reco landed price - shipping costs < min price ==> reco landed price := min_price + shipping costsf) Rounding rulesif reco landed price - shipping costs < 0.5 ==> reco listed price := reco landed price - shipping costsif reco landed price - shipping costs < 200 ==> reco listed price := round(reco landed price - shipping costs; 0) + 0.90otherwise ==> reco listed price := round(reco landed price - shipping costs; 0)Price change:if no price change ==> NEEDS_TO_BE_UPDATED := 0if price cap due to margin floor ==> NEEDS_TO_BE_UPDATED := 1if price cap due to unhealthy inventory reset ==> NEEDS_TO_BE_UPDATED := 1if no price cap due to unhealthy inveentory reset and store limit = 1 and (reco_landed_price > 100 or price difference > 4)==> NEEDS_TO_BE_UPDATED := 1if no price cap due to unhealthy inventory reset and store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0otherwise==> NEEDS_TO_BE_UPDATED := 1Execution:if NEEDS_TO_BE_UPDATE = 1==> distribute new priceotherwise ==> don’t distribute price |

Strategy "MERCHANT BASED PRICING"

Selection of all relevant products

(see also here Base Price Algorithm: Stream Selection)

Product is

* merchandise article (no voucher or software license or similar)
* no B-stock product
* active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”
* no bundle
* on the auto pricing list, not excluded from auto pricing, not manually deactivated
* not activated for COVERAGE BASED PRICING
* no ENFORCE RRP pricing
* no unhealthy inventory
* no activated for Price Relations Pricing
* amount of considered competing merchants is > 0 (even if product is not available for them)
* is either no new product or has no valid recommended retail price (because then new product pricing can’t be applied)
* has neither price nor purchase_price quality issues

merchandise article (no voucher or software license or similar)

no B-stock product

active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”

no bundle

on the auto pricing list, not excluded from auto pricing, not manually deactivated

not activated for COVERAGE BASED PRICING

no ENFORCE RRP pricing

no unhealthy inventory

no activated for Price Relations Pricing

amount of considered competing merchants is > 0 (even if product is not available for them)

is either no new product or has no valid recommended retail price (because then new product pricing can’t be applied)

has neither price nor purchase_price quality issues

Price Calculation

a) Selection Tier: x := amount of configured competing merchants with stock

* if x = 0: ==> Percentile Tier 1 without stock
* if 1 ≤ x ≤ 3: ==> Percentile Tier 1
* if 4 ≤ x ≤ 6: ==> Percentile Tier 2
* if 7 ≤ x: ==> Percentile Tier 3

if x = 0: ==> Percentile Tier 1 without stock

if 1 ≤ x ≤ 3: ==> Percentile Tier 1

if 4 ≤ x ≤ 6: ==> Percentile Tier 2

if 7 ≤ x: ==> Percentile Tier 3

b) Selection "tier price"

Let’s define price(percentile, list of landed prices) as ==> the price that you get when you sort the list of n prices in a descending order and take the floor(percentile*n)-th price.

Take the correct percentile value from the tiering configuration tables and calculate the tier price via==> reco landed price := price(percentile, list of competitor offers)

Price quality checks

(see also here Base Price Algorithm: Price Quality Check)

Preparation for margin calculation:

* if standard purchase price < average purchase price==> product costs := standard purchase price
* if inventory > 0 ==> product costs := average purchase price
* otherwise==> product costs := standard purchase price

if standard purchase price < average purchase price==> product costs := standard purchase price

if inventory > 0 ==> product costs := average purchase price

otherwise==> product costs := standard purchase price

Get Margin Floor configuration for a product according to the following prioritization:

Configuration for article group for a price range

Configuration for whole article group

Configuration for category level 3 for a price range

Configuration for whole category level 3

Default Configuration for a price range

Default Configuration

Get Margin Cap configuration for a product according to the following prioritization:

Configuration for article group

Configuration for category level 3

Default Configuration

Max price := 1.19 * product costs / (1-margin cap)Min price := 1.19 * products costs /(1-margin floor)

store limit:

* if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1
* otherwise ==> Store limit := 0

if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1

otherwise ==> Store limit := 0

a) Lowest Product Price:

* if reco landed price - shipping costs < lowest product price: ==> reco landed price := lowest product price + 1 + shipping costs
* otherwise ==> no change

if reco landed price - shipping costs < lowest product price: ==> reco landed price := lowest product price + 1 + shipping costs

otherwise ==> no change

b) RRP Cap:

* If Tier1: Use RRP
* If Tier2 or Tier3: If there is competitor with price ≤ RRP: ==> use RRPotherwise if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price change
* If there is competitor with price ≤ RRP: ==> use RRP
* otherwise if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price change
* if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costs
* If sales flag is set: ==> Cap bei RRP - 5%
* otherwise==> no price change

If Tier1: Use RRP

If Tier2 or Tier3:

* If there is competitor with price ≤ RRP: ==> use RRP
* otherwise if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price change
* if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costs
* If sales flag is set: ==> Cap bei RRP - 5%
* otherwise==> no price change

If there is competitor with price ≤ RRP: ==> use RRP

otherwise

* if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costs
* If sales flag is set: ==> Cap bei RRP - 5%
* otherwise==> no price change

if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costs

If sales flag is set: ==> Cap bei RRP - 5%

otherwise==> no price change

c) Margin Cap:

* if reco landed price - shipping costs > max price ==> reco landed price := max_price + shipping costs

if reco landed price - shipping costs > max price ==> reco landed price := max_price + shipping costs

d) Price Change Threshold    Letzter Pricing Stream != 'UNHEALTHY INVENTORY':

* if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3
* if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7

if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3

if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7

e) Margin Floor

* if reco landed price - shipping costs < min price ==> reco landed price := min_price + shipping costs

if reco landed price - shipping costs < min price ==> reco landed price := min_price + shipping costs

f) Rounding rules

* if reco landed price - shipping costs < 0.5 ==> reco listed price := reco landed price - shipping costs
* if reco landed price - shipping costs < 200 ==> reco listed price := round(reco landed price - shipping costs; 0) + 0.90
* otherwise ==> reco listed price := round(reco landed price - shipping costs; 0)

if reco landed price - shipping costs < 0.5 ==> reco listed price := reco landed price - shipping costs

if reco landed price - shipping costs < 200 ==> reco listed price := round(reco landed price - shipping costs; 0) + 0.90

otherwise ==> reco listed price := round(reco landed price - shipping costs; 0)

Price change:

* if no price change ==> NEEDS_TO_BE_UPDATED := 0
* if price cap due to margin floor ==> NEEDS_TO_BE_UPDATED := 1
* if price cap due to unhealthy inventory reset ==> NEEDS_TO_BE_UPDATED := 1
* if no price cap due to unhealthy inveentory reset and store limit = 1 and (reco_landed_price > 100 or price difference > 4)==> NEEDS_TO_BE_UPDATED := 1
* if no price cap due to unhealthy inventory reset and store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0
* otherwise==> NEEDS_TO_BE_UPDATED := 1

if no price change ==> NEEDS_TO_BE_UPDATED := 0

if price cap due to margin floor ==> NEEDS_TO_BE_UPDATED := 1

if price cap due to unhealthy inventory reset ==> NEEDS_TO_BE_UPDATED := 1

if no price cap due to unhealthy inveentory reset and store limit = 1 and (reco_landed_price > 100 or price difference > 4)==> NEEDS_TO_BE_UPDATED := 1

if no price cap due to unhealthy inventory reset and store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0

otherwise==> NEEDS_TO_BE_UPDATED := 1

Execution:

* if NEEDS_TO_BE_UPDATE = 1==> distribute new price
* otherwise ==> don’t distribute price

if NEEDS_TO_BE_UPDATE = 1==> distribute new price

otherwise ==> don’t distribute price

