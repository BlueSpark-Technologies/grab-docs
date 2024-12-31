# Stream: No Merchants Pricing

## Motivation
The purpose of the pricing stream No Merchants is to price products that have no relevant competitors automatically. As there is no competitor that can be used for finding a good price level, product prices of similar products are used instead.

## Configuration
There are multiple configurations for this stream:

* Global Merchant Selection (which merchants are considered relevant in general): This is not configurable in the UI, but only in Exasol PROD_DS.PROD_STAGING_PRC_MAP_MERCHANTS_MV
* Product Merchant Selection Configuration (which of the globally admitted merchants are relevant for a product / article group / category level 3): This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .Also it is persisted in Exasol table PROD_DS.APP_AUTO_PRICING_CONF_MERCHANTSEach product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and category level 3 null
* This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .
* Also it is persisted in Exasol table PROD_DS.APP_AUTO_PRICING_CONF_MERCHANTS
* Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and category level 3 null
* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and category level 3 null

Global Merchant Selection (which merchants are considered relevant in general): This is not configurable in the UI, but only in Exasol PROD_DS.PROD_STAGING_PRC_MAP_MERCHANTS_MV

Product Merchant Selection Configuration (which of the globally admitted merchants are relevant for a product / article group / category level 3):

* This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .
* Also it is persisted in Exasol table PROD_DS.APP_AUTO_PRICING_CONF_MERCHANTS
* Each product has exactly one matching row in this table: if for the product's article group there is a row specified use that row, if not and there is a row for the product hierarchy use that row, if not use the general row with article group and category level 3 null
* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and category level 3 null

This can be configured in the Pricing UI section Relevant Competitors. Documentation for the UI can be found here Pricing UI - Software Requirements Specifications .

Also it is persisted in Exasol table PROD_DS.APP_AUTO_PRICING_CONF_MERCHANTS

Each product has exactly one matching row in this table:

* if for the product's article group there is a row specified use that row,
* if not and there is a row for the product hierarchy use that row,
* if not use the general row with article group and category level 3 null

if for the product's article group there is a row specified use that row,

if not and there is a row for the product hierarchy use that row,

if not use the general row with article group and category level 3 null

If there are no merchants that pass the configuration above a product is considered to have no merchants even though there are merchants visible on geizhals.de for example. Background is that we don’t consider all merchants relevant competitors.

## Algorithm
Here’s a visualization of the No Merchants Algorithm

| Strategy "NO MERCHANTS PRICING" |
|---|
| Selection of all relevant products(see also here Base Price Algorithm: Stream Selection) | Product ismerchandise article (no voucher or software license or similar)no B-stock productactive, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”no bundleno new producton the auto pricing list, not excluded from auto pricing, not manually deactivatednot activated for COVERAGE BASED PRICINGno RRP ENFORCED PRICINGno activated for PRICE SUCCESSOR PRICINGnot unhealthy inventoryamount of relevant competing merchants with or without stock is 0has neither price nor purchase_price quality issues |
| Price Calculation | Preparation for margin calculation:if standard purchase price < average purchase price==> product costs := standard purchase priceif inventory > 0 ==> product costs := average purchase priceotherwise==> product costs := standard purchase priceReference product prices: That are in Merchant Based PricingPrices of the last 7 days Price calculation:If there are at least 5 reference entries in (A) the same article group:==> markup_pct := median((A) reference price margins)If there are at least 5 reference entries in (B) the same commodity group with same price level (Preisband):==> markup_pct := median((B) reference price margins)If there are at least 5 reference entries in (C) the same commodity group with different price level (Preisband):==> markup_pct := median((C) reference price margins)If there are at least 5 reference entries with (D) the same price level (Preisband):==> markup_pct := median((D) reference price margins)If there are at least 5 reference entries:==> markup_pct := median(all reference price margins)markup_only_competitor := 1.1reco_landed_price = product_costs * 1 / (1 - markup_pct * markup_only_competitor) * 1.19 + shipping_costs |
| Price quality checks(see also here Base Price Algorithm: Price Quality Check) | Store limit:if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1otherwise ==> Store limit := 0Get Margin Floor configuration for a product according to the following prioritization:Configuration for article group for a price rangeConfiguration for whole article groupConfiguration for category group for a price rangeConfiguration for whole category groupDefault Configuration for a price rangeDefault ConfigurationGet Margin Cap configuration for a product according to the following prioritization:Configuration for article groupConfiguration for category groupDefault ConfigurationMax price := 1.19 * product costs / (1-margin cap)Min price := 1.19 * products costs /(1-margin floor)a) RRP Cap:If Tier1: Use RRPIf Tier2 or Tier3: If there is competitor with price ≤ RRP: ==> use RRPotherwise if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price changeb) Margin Cap: if reco landed price - shipping costs > max price ==> reco landed price := max_price + shipping costsc) Price Change Threshold    Letzter Pricing Stream != 'UNHEALTHY INVENTORY':if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7d) Margin Floorif reco landed price - shipping costs < min price ==> reco landed price := min_price + shipping costsotherwise ==> keine Änderunge) Final reco price roundedif reco landed price - shipping costs < 0.5 ==> final reco price := reco landed price - shipping costsif reco landed price - shipping costs < 200 ==> final reco price := round(reco landed price - shipping costs; 0) + 0.90otherwise ==> final reco price := round(reco landed price - shipping costs; 0)Price change:if no price change ==> NEEDS_TO_BE_UPDATED := 0if price cap due to margin floor ==> NEEDS_TO_BE_UPDATED := 1if price cap due to unhealthy inventory reset ==> NEEDS_TO_BE_UPDATED := 1if no price cap due to unhealthy inventory reset and store limit = 1 and (reco_landed_price > 100 or price difference > 4)==> NEEDS_TO_BE_UPDATED := 1if no price cap due to unhealthy inventory reset and store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0otherwise==> NEEDS_TO_BE_UPDATED := 1Execution:if NEEDS_TO_BE_UPDATE = 1==> distribute new priceotherwise ==> don’t distribute price |

Strategy "NO MERCHANTS PRICING"

Selection of all relevant products

(see also here Base Price Algorithm: Stream Selection)

Product is

* merchandise article (no voucher or software license or similar)
* no B-stock product
* active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”
* no bundle
* no new product
* on the auto pricing list, not excluded from auto pricing, not manually deactivated
* not activated for COVERAGE BASED PRICING
* no RRP ENFORCED PRICING
* no activated for PRICE SUCCESSOR PRICING
* not unhealthy inventory
* amount of relevant competing merchants with or without stock is 0
* has neither price nor purchase_price quality issues

merchandise article (no voucher or software license or similar)

no B-stock product

active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”

no bundle

no new product

on the auto pricing list, not excluded from auto pricing, not manually deactivated

not activated for COVERAGE BASED PRICING

no RRP ENFORCED PRICING

no activated for PRICE SUCCESSOR PRICING

not unhealthy inventory

amount of relevant competing merchants with or without stock is 0

has neither price nor purchase_price quality issues

Price Calculation

Preparation for margin calculation:

* if standard purchase price < average purchase price==> product costs := standard purchase price
* if inventory > 0 ==> product costs := average purchase price
* otherwise==> product costs := standard purchase price

if standard purchase price < average purchase price==> product costs := standard purchase price

if inventory > 0 ==> product costs := average purchase price

otherwise==> product costs := standard purchase price

Reference product prices:

* That are in Merchant Based Pricing
* Prices of the last 7 days

That are in Merchant Based Pricing

Prices of the last 7 days

Price calculation:

* If there are at least 5 reference entries in (A) the same article group:==> markup_pct := median((A) reference price margins)
* If there are at least 5 reference entries in (B) the same commodity group with same price level (Preisband):==> markup_pct := median((B) reference price margins)
* If there are at least 5 reference entries in (C) the same commodity group with different price level (Preisband):==> markup_pct := median((C) reference price margins)
* If there are at least 5 reference entries with (D) the same price level (Preisband):==> markup_pct := median((D) reference price margins)
* If there are at least 5 reference entries:==> markup_pct := median(all reference price margins)

If there are at least 5 reference entries in (A) the same article group:==> markup_pct := median((A) reference price margins)

If there are at least 5 reference entries in (B) the same commodity group with same price level (Preisband):==> markup_pct := median((B) reference price margins)

If there are at least 5 reference entries in (C) the same commodity group with different price level (Preisband):==> markup_pct := median((C) reference price margins)

If there are at least 5 reference entries with (D) the same price level (Preisband):==> markup_pct := median((D) reference price margins)

If there are at least 5 reference entries:==> markup_pct := median(all reference price margins)

markup_only_competitor := 1.1

reco_landed_price = product_costs * 1 / (1 - markup_pct * markup_only_competitor) * 1.19 + shipping_costs

Price quality checks

(see also here Base Price Algorithm: Price Quality Check)

Store limit:

* if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1
* otherwise ==> Store limit := 0

if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1

otherwise ==> Store limit := 0

Get Margin Floor configuration for a product according to the following prioritization:

Configuration for article group for a price range

Configuration for whole article group

Configuration for category group for a price range

Configuration for whole category group

Default Configuration for a price range

Default Configuration

Get Margin Cap configuration for a product according to the following prioritization:

Configuration for article group

Configuration for category group

Default Configuration

Max price := 1.19 * product costs / (1-margin cap)Min price := 1.19 * products costs /(1-margin floor)

a) RRP Cap:

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

b) Margin Cap:

* if reco landed price - shipping costs > max price ==> reco landed price := max_price + shipping costs

if reco landed price - shipping costs > max price ==> reco landed price := max_price + shipping costs

c) Price Change Threshold    Letzter Pricing Stream != 'UNHEALTHY INVENTORY':

* if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3
* if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7

if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3

if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7

d) Margin Floor

* if reco landed price - shipping costs < min price ==> reco landed price := min_price + shipping costs
* otherwise ==> keine Änderung

if reco landed price - shipping costs < min price ==> reco landed price := min_price + shipping costs

otherwise ==> keine Änderung

e) Final reco price rounded

* if reco landed price - shipping costs < 0.5 ==> final reco price := reco landed price - shipping costs
* if reco landed price - shipping costs < 200 ==> final reco price := round(reco landed price - shipping costs; 0) + 0.90
* otherwise ==> final reco price := round(reco landed price - shipping costs; 0)

if reco landed price - shipping costs < 0.5 ==> final reco price := reco landed price - shipping costs

if reco landed price - shipping costs < 200 ==> final reco price := round(reco landed price - shipping costs; 0) + 0.90

otherwise ==> final reco price := round(reco landed price - shipping costs; 0)

Price change:

* if no price change ==> NEEDS_TO_BE_UPDATED := 0
* if price cap due to margin floor ==> NEEDS_TO_BE_UPDATED := 1
* if price cap due to unhealthy inventory reset ==> NEEDS_TO_BE_UPDATED := 1
* if no price cap due to unhealthy inventory reset and store limit = 1 and (reco_landed_price > 100 or price difference > 4)==> NEEDS_TO_BE_UPDATED := 1
* if no price cap due to unhealthy inventory reset and store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0
* otherwise==> NEEDS_TO_BE_UPDATED := 1

if no price change ==> NEEDS_TO_BE_UPDATED := 0

if price cap due to margin floor ==> NEEDS_TO_BE_UPDATED := 1

if price cap due to unhealthy inventory reset ==> NEEDS_TO_BE_UPDATED := 1

if no price cap due to unhealthy inventory reset and store limit = 1 and (reco_landed_price > 100 or price difference > 4)==> NEEDS_TO_BE_UPDATED := 1

if no price cap due to unhealthy inventory reset and store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0

otherwise==> NEEDS_TO_BE_UPDATED := 1

Execution:

* if NEEDS_TO_BE_UPDATE = 1==> distribute new price
* otherwise ==> don’t distribute price

if NEEDS_TO_BE_UPDATE = 1==> distribute new price

otherwise ==> don’t distribute price

