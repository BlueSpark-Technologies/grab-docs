# Stream: Unhealthy Inventory Pricing

# Motivation
The purpose of the pricing stream unhealthy inventory is to cheaply sell products, that are in storage for a long time (high age) or have a low selling rate vs. amount in storage (high coverage). For these products a low or even negative profit margin can be accepted as keeping the products in storage a for long time or not selling them at all can be more expensive than selling them under value.

For that pricing strategy each product is sorted into exactly one health bucket. (see Inventory Health Service (IHS) or table below for definition of buckets). A bucket is considered unhealthy, if for this product it is not configured as regular in the Pricing UI https://app.cybersolutions-tech.com/pricing/inventory-health . The configuration and therefore whether a product is in an unhealthy bucket also depends on the price range (Range 1 = 0€ - 10€, Range 2 = 10€ - 100€, Range 2 = 100€ - 500€, Range 2 > 500€). Only for a range of buckets (“unhealthy buckets”) the pricing stream Unhealthy Inventory is applied. Currently this is every bucket / strategy that is not labeled as “Regular”.

If no individual pattern is defined per product, its article group or cat level 3, the default (standard) pattern is used, which is:

The unhealthy pricing strategy gets activated automatically once a products gets unhealthy.

### General Strategy:
Each inventory health strategy has a lightly different logic, that can be found in the big table below.

However they all have a similar strategy in common:

First there is an initial price reduction on day 1.

If the product doesn’t turn healthy in the meantime, there is another reduction step after a certain period of time, which stays in place until the product is sold out, recovers into a more healthy bucket or until the next price reduction.

Details see in the big table below.

## Configuration
CM can change the unhealthy inventory configuration in the Pricing UI. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .

The configuration of this stream is also exported to this Exasol table:

SELECT * FROM PROD_DS.APP_AUTO_PRICING_CONF_INVENTORY_HEALTH;

Each product with each health bucket has exactly one row in this table:

first we filter on the current inventory health bucket. If it is A4-C2 all other rows with different INVENTORY_HEALTH_BUCKET aren’t relevant here.

Then we filter on product specific row

if for the product's article group there is a row specified with a matching resulting health bucket use that row

if not and there is a row for the product hierarchy and a matching health bucket use that row

if not use the general row with article group and product hierarchy null and the matching health bucket.

only the markdown parameter is applied in which the current base price is in the correct range.

Range 1: 0€ - 10€

Range 2: 10.01€ - 100€

Range 3: 100.01€ - 500€

Range 4: > 500.01€

| CAT_ID | PRODUCT_HIERARCHY | PRODUCT_ID | INV_HEALTH_BUCKET_POLICY | INVENTORY_HEALTH_BUCKET | MARKDOWN_PRICE_RANGE_1 | MARKDOWN_PRICE_RANGE_2 | MARKDOWN_PRICE_RANGE_3 | MARKDOWN_PRICE_RANGE_4 |
|---|---|---|---|---|---|---|---|---|
|  | K758 |  | Lowest_Merchant | A4-C2 | -0.1 | -0.05 | -0.025 | -0.015 |

CAT_ID

PRODUCT_HIERARCHY

PRODUCT_ID

INV_HEALTH_BUCKET_POLICY

INVENTORY_HEALTH_BUCKET

MARKDOWN_PRICE_RANGE_1

MARKDOWN_PRICE_RANGE_2

MARKDOWN_PRICE_RANGE_3

MARKDOWN_PRICE_RANGE_4

K758

Lowest_Merchant

A4-C2

-0.1

-0.05

-0.025

-0.015

## Algorithm
| Strategy "UNHEALTHY INVENTORY" |
|---|
| Selection of all relevant products(see also here Base Price Algorithm: Stream Selection) | Product ismerchandise articleactive, aka. not “ausgelistet” and not “Bestand Zentrallager > 0” and not “Inventory Store > 0” and not “offene Einkaufsaufträge”no bundleon the auto pricing list, not excluded from auto pricing, not manually deactivatednot activated for COVERAGE BASED PRICINGinventory is unhealthy |
| 1. Define Inventory Health Bucket | Age buckets:if weighted age <= 30 days: ==> Age bucket A0if weighted age <= 60 days: A1if weighted age <= 90 days: A2if weighted age <= 180 days: A3if weighted age > 180 days: A4coverage: if FREE_INV_QTY_CENTRAL_WH - open order quantity main storage < 0 ==> inventory := 0otherwise ==> inventory := FREE_INV_QTY_CENTRAL_WH - open order quantity main storageweighted turnover: without counting 'Team Key Account', 'Team Projektsales', 'Team B2B'==> weighted turnover := (14 * turnover last 7 days + 7 * turnover last 14 days + 3 *  turnover last 28 days + 1 * turnover last 84 days) / 52 / 7weighted Coverage: if weighted turnover <= 0 ==> weighted coverage := 9999otherwise weighted coverage := inventory / weighted turnoverCoverage buckets: if weighted coverage <= 30  days: C0if weighted coverage <= 60  days: C1if weighted coverage <= 90  days: C2if weighted coverage <= 180 days: C3if weighted coverage >   180 days: C4 |
| 2. Define pricing stream | if bucket is configured as “Regular”, use “MERCHANT BASED” pricing strategy (see here Stream: Merchant Based Pricing)if not listed and inventory >= 1, stay in “UNHEALTHY INVENTORY”if listed and band BU = A and inventory > 5, stay in “UNHEALTHY INVENTORY”if listed and band BU = B and inventory > 3, stay in “UNHEALTHY INVENTORY”if listed and band BU = C and inventory > 2, stay in “UNHEALTHY INVENTORY”if listed and band BU = D and inventory > 1, stay in “UNHEALTHY INVENTORY”otherwise, use “MERCHANT BASED” pricing strategy (see here Stream: Merchant Based Pricing) |
| Price Calculation | if INV_HEALTH_BUCKET_POLICY = Lowest Merchantifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stockwe have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stockif INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdownifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)if We have competitorsINV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown ==> reco landed price := lowest landed price * (1 + markdown price range)if INV_HEALTH_BUCKET_POLICY = Continuous Markdown and last price export in this strategy was at least 7 days ago==> reco landed price := landed price * (1 + markdown price range)if INV_HEALTH_BUCKET_POLICY = Continuous Markdown Aggressivelast price export in this strategy was at least 3 days ago==> reco landed price := landed price * (1 + markdown price range) |
| Price quality checks(see also here Base Price Algorithm: Price Quality Check) | Preparation for margin calculation:if standard purchase price < average purchase price==> product costs := standard purchase priceif inventory > 0 ==> product costs := average purchase priceotherwise==> product costs := standard purchase priceMin price is half the normal min price:min price := 1/2 * products costs / (1 - margin floor) * 1.19store limit:if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1otherwise ==> Store limit := 0Recommended landing price:1. check upper price cap / unwanted price riseif reco landed price > RRP * 0.95 - and RRP * 0.95 <= landed_price==> reco landed price := RRP * 0.95reco landed price > landed price==> reco landed price := landed price2. unwanted price increaseif reco landed price - shipping costs < current price==> reco landed price := current price3. min price capif reco landed price - shipping costs < min price==> reco landed price := min price4. Price Change Threshold    Letzter Pricing Stream != 'UNHEALTHY INVENTORY':if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.75. Rounding rulesif reco landed price - shipping costs < 0.5 ==> reco landed price := reco landed price - shipping costsif reco landed price - shipping costs < 200 ==> reco landed price := round(reco landed price - shipping costs;0) + 0.90otherwise ==> reco landed price := round(reco landed price - shipping costs;0) |
|  | Price change:if no price change ==> NEEDS_TO_BE_UPDATED := 0if (price increase and inventory health has improved) or reco_landed_price > 100 or price difference > 4 or capped by min_price==> NEEDS_TO_BE_UPDATED := 1if store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0otherwise==> NEEDS_TO_BE_UPDATED := 1Execution:if NEEDS_TO_BE_UPDATE = 1==> distribute new priceotherwise ==> don’t distribute price |

Strategy "UNHEALTHY INVENTORY"

Selection of all relevant products

(see also here Base Price Algorithm: Stream Selection)

Product is

* merchandise article
* active, aka. not “ausgelistet” and not “Bestand Zentrallager > 0” and not “Inventory Store > 0” and not “offene Einkaufsaufträge”
* no bundle
* on the auto pricing list, not excluded from auto pricing, not manually deactivated
* not activated for COVERAGE BASED PRICING
* inventory is unhealthy

merchandise article

active, aka. not “ausgelistet” and not “Bestand Zentrallager > 0” and not “Inventory Store > 0” and not “offene Einkaufsaufträge”

no bundle

on the auto pricing list, not excluded from auto pricing, not manually deactivated

not activated for COVERAGE BASED PRICING

inventory is unhealthy

1. Define Inventory Health Bucket

Age buckets:

* if weighted age <= 30 days: ==> Age bucket A0
* if weighted age <= 60 days: A1
* if weighted age <= 90 days: A2
* if weighted age <= 180 days: A3
* if weighted age > 180 days: A4

if weighted age <= 30 days: ==> Age bucket A0

if weighted age <= 60 days: A1

if weighted age <= 90 days: A2

if weighted age <= 180 days: A3

if weighted age > 180 days: A4

coverage:

* if FREE_INV_QTY_CENTRAL_WH - open order quantity main storage < 0 ==> inventory := 0
* otherwise ==> inventory := FREE_INV_QTY_CENTRAL_WH - open order quantity main storage

if FREE_INV_QTY_CENTRAL_WH - open order quantity main storage < 0 ==> inventory := 0

otherwise ==> inventory := FREE_INV_QTY_CENTRAL_WH - open order quantity main storage

weighted turnover:

* without counting 'Team Key Account', 'Team Projektsales', 'Team B2B'==> weighted turnover := (14 * turnover last 7 days + 7 * turnover last 14 days + 3 *  turnover last 28 days + 1 * turnover last 84 days) / 52 / 7

without counting 'Team Key Account', 'Team Projektsales', 'Team B2B'==> weighted turnover := (14 * turnover last 7 days + 7 * turnover last 14 days + 3 *  turnover last 28 days + 1 * turnover last 84 days) / 52 / 7

weighted Coverage:

* if weighted turnover <= 0 ==> weighted coverage := 9999
* otherwise weighted coverage := inventory / weighted turnover

if weighted turnover <= 0 ==> weighted coverage := 9999

otherwise weighted coverage := inventory / weighted turnover

Coverage buckets:

* if weighted coverage <= 30  days: C0
* if weighted coverage <= 60  days: C1
* if weighted coverage <= 90  days: C2
* if weighted coverage <= 180 days: C3
* if weighted coverage >   180 days: C4

if weighted coverage <= 30  days: C0

if weighted coverage <= 60  days: C1

if weighted coverage <= 90  days: C2

if weighted coverage <= 180 days: C3

if weighted coverage >   180 days: C4

2. Define pricing stream

* if bucket is configured as “Regular”, use “MERCHANT BASED” pricing strategy (see here Stream: Merchant Based Pricing)
* if not listed and inventory >= 1, stay in “UNHEALTHY INVENTORY”
* if listed and band BU = A and inventory > 5, stay in “UNHEALTHY INVENTORY”
* if listed and band BU = B and inventory > 3, stay in “UNHEALTHY INVENTORY”
* if listed and band BU = C and inventory > 2, stay in “UNHEALTHY INVENTORY”
* if listed and band BU = D and inventory > 1, stay in “UNHEALTHY INVENTORY”
* otherwise, use “MERCHANT BASED” pricing strategy (see here Stream: Merchant Based Pricing)

if bucket is configured as “Regular”, use “MERCHANT BASED” pricing strategy (see here Stream: Merchant Based Pricing)

if not listed and inventory >= 1, stay in “UNHEALTHY INVENTORY”

if listed and band BU = A and inventory > 5, stay in “UNHEALTHY INVENTORY”

if listed and band BU = B and inventory > 3, stay in “UNHEALTHY INVENTORY”

if listed and band BU = C and inventory > 2, stay in “UNHEALTHY INVENTORY”

if listed and band BU = D and inventory > 1, stay in “UNHEALTHY INVENTORY”

otherwise, use “MERCHANT BASED” pricing strategy (see here Stream: Merchant Based Pricing)

Price Calculation

* if INV_HEALTH_BUCKET_POLICY = Lowest Merchantifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stockwe have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stock
* INV_HEALTH_BUCKET_POLICY = Lowest Merchant
* ifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stockwe have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stock
* we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing
* we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stock
* we have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stock
* if INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdownifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)
* INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown
* ifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)
* we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing
* we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)
* we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)
* if We have competitorsINV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown ==> reco landed price := lowest landed price * (1 + markdown price range)
* We have competitors
* INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown ==> reco landed price := lowest landed price * (1 + markdown price range)
* if INV_HEALTH_BUCKET_POLICY = Continuous Markdown and last price export in this strategy was at least 7 days ago==> reco landed price := landed price * (1 + markdown price range)
* INV_HEALTH_BUCKET_POLICY = Continuous Markdown and
* last price export in this strategy was at least 7 days ago==> reco landed price := landed price * (1 + markdown price range)
* if INV_HEALTH_BUCKET_POLICY = Continuous Markdown Aggressivelast price export in this strategy was at least 3 days ago==> reco landed price := landed price * (1 + markdown price range)
* INV_HEALTH_BUCKET_POLICY = Continuous Markdown Aggressive
* last price export in this strategy was at least 3 days ago==> reco landed price := landed price * (1 + markdown price range)

if

* INV_HEALTH_BUCKET_POLICY = Lowest Merchant
* ifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stockwe have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stock
* we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing
* we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stock
* we have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stock

INV_HEALTH_BUCKET_POLICY = Lowest Merchant

if

* we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing
* we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stock
* we have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stock

we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing

we have competitors with available stock (short delivery time) ==> reco landed price := lowest landed competitor price with stock

we have competitors without available stock (long delivery times) ==> reco landed price := lowest landed competitor price without stock

if

* INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown
* ifwe don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)
* we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing
* we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)
* we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)

INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown

if

* we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing
* we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)
* we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)

we don’t have competitors==> reco landed price := product_costs * (1 + VAT) * 1 / (1 - markup_pct) + shipping_costs ==> for definition of markup_pct see Stream: No Merchants Pricing

we have competitors with available stock (short delivery time) ==> reco landed price := lowest competitor price with stock * (1 + markdown price range)

we have competitors without available stock (long delivery times ) ==> reco landed price := lowest competitor price without stock * (1 + markdown price range)

if

* We have competitors
* INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown ==> reco landed price := lowest landed price * (1 + markdown price range)

We have competitors

INV_HEALTH_BUCKET_POLICY = Lowest Merchant Markdown ==> reco landed price := lowest landed price * (1 + markdown price range)

if

* INV_HEALTH_BUCKET_POLICY = Continuous Markdown and
* last price export in this strategy was at least 7 days ago==> reco landed price := landed price * (1 + markdown price range)

INV_HEALTH_BUCKET_POLICY = Continuous Markdown and

last price export in this strategy was at least 7 days ago==> reco landed price := landed price * (1 + markdown price range)

if

* INV_HEALTH_BUCKET_POLICY = Continuous Markdown Aggressive
* last price export in this strategy was at least 3 days ago==> reco landed price := landed price * (1 + markdown price range)

INV_HEALTH_BUCKET_POLICY = Continuous Markdown Aggressive

last price export in this strategy was at least 3 days ago==> reco landed price := landed price * (1 + markdown price range)

Price quality checks

(see also here Base Price Algorithm: Price Quality Check)

Preparation for margin calculation:

* if standard purchase price < average purchase price==> product costs := standard purchase price
* if inventory > 0 ==> product costs := average purchase price
* otherwise==> product costs := standard purchase price

if standard purchase price < average purchase price==> product costs := standard purchase price

if inventory > 0 ==> product costs := average purchase price

otherwise==> product costs := standard purchase price

Min price is half the normal min price:

* min price := 1/2 * products costs / (1 - margin floor) * 1.19

min price := 1/2 * products costs / (1 - margin floor) * 1.19

store limit:

* if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1
* otherwise ==> Store limit := 0

if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1

otherwise ==> Store limit := 0

Recommended landing price:

1. check upper price cap / unwanted price rise

* if reco landed price > RRP * 0.95 - and RRP * 0.95 <= landed_price==> reco landed price := RRP * 0.95
* reco landed price > landed price==> reco landed price := landed price

if reco landed price > RRP * 0.95 - and RRP * 0.95 <= landed_price==> reco landed price := RRP * 0.95

reco landed price > landed price==> reco landed price := landed price

2. unwanted price increase

* if reco landed price - shipping costs < current price==> reco landed price := current price

if reco landed price - shipping costs < current price==> reco landed price := current price

3. min price cap

* if reco landed price - shipping costs < min price==> reco landed price := min price

if reco landed price - shipping costs < min price==> reco landed price := min price

4. Price Change Threshold    Letzter Pricing Stream != 'UNHEALTHY INVENTORY':

* if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3
* if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7

if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3

if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7

5. Rounding rules

* if reco landed price - shipping costs < 0.5 ==> reco landed price := reco landed price - shipping costs
* if reco landed price - shipping costs < 200 ==> reco landed price := round(reco landed price - shipping costs;0) + 0.90
* otherwise ==> reco landed price := round(reco landed price - shipping costs;0)

if reco landed price - shipping costs < 0.5 ==> reco landed price := reco landed price - shipping costs

if reco landed price - shipping costs < 200 ==> reco landed price := round(reco landed price - shipping costs;0) + 0.90

otherwise ==> reco landed price := round(reco landed price - shipping costs;0)

Price change:

* if no price change ==> NEEDS_TO_BE_UPDATED := 0
* if (price increase and inventory health has improved) or reco_landed_price > 100 or price difference > 4 or capped by min_price==> NEEDS_TO_BE_UPDATED := 1
* if store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0
* otherwise==> NEEDS_TO_BE_UPDATED := 1

if no price change ==> NEEDS_TO_BE_UPDATED := 0

if (price increase and inventory health has improved) or reco_landed_price > 100 or price difference > 4 or capped by min_price==> NEEDS_TO_BE_UPDATED := 1

if store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0

otherwise==> NEEDS_TO_BE_UPDATED := 1

Execution:

* if NEEDS_TO_BE_UPDATE = 1==> distribute new price
* otherwise ==> don’t distribute price

if NEEDS_TO_BE_UPDATE = 1==> distribute new price

otherwise ==> don’t distribute price

