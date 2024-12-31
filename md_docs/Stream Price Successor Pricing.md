# Stream: Price Successor Pricing

## Motivation
The purpose of the pricing stream Price Successor is to define a price for a product that is in some way linked or descendant to another product (for example a grey notebook that should have the same price as its black twin).

## Configuration
There currently is a configuration in the Pricing UI available, in which products can be set as price successors of another product. See here for details Price Relations.

In Exasol it is persisted in the table PROD_DS.APP_AUTO_PRICING_CONF_PRICE_RELATIONS

| PRODUCT_ID1 | PRODUCT_ID2 | VAL_REL | VAL_ABS |
|---|---|---|---|
| AW04-0G9 | AW04-0G8 | NULL | 3 |

PRODUCT_ID1

PRODUCT_ID2

VAL_REL

VAL_ABS

AW04-0G9

AW04-0G8

NULL

3

## Algorithm
| Strategy "PRICE SUCCESSOR" |
|---|
| Selection of all relevant products(see also here BPS Algorithm: Stream Selection) | Product ismerchandise article (no voucher or software license or similar)no B-stock productactive, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”no bundleon the auto pricing list, not excluded from auto pricing, not manually deactivatedconfigured as Price Successors has neither price nor purchase_price quality issues |
| Price Calculation | Get price of the predecessor (base product to be used as reference for current successor product) from the configuration as well as the price factor val.If value_type = relative: ==> reco_landed_price = price_base_product * (1 + val_rel) + shipping costsIf value_type = absolute: ==> reco_landed_price = price_base_product + val_abs + shipping costs |
| Price quality checks(see also here BPS Algorithm: Price Quality Check) | Preparation for margin calculation:if current purchase price < average inventory value==> product costs := current purchase priceif inventory > 0 ==> product costs := average inventory valueotherwise==> product costs := current purchase pricestore limit:if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1otherwise ==> Store limit := 0Get Margin Floor configuration for a product according to the following prioritization:Configuration for article group for a price rangeConfiguration for whole article groupConfiguration for category group for a price rangeConfiguration for whole category groupDefault Configuration for a price rangeDefault ConfigurationGet Margin Cap configuration for a product according to the following prioritization:Configuration for article groupConfiguration for category groupDefault ConfigurationMax price := 1.19 * product costs / (1-margin cap)Min price := 1.19 * products costs /(1-margin floor)a) RRP Cap:If Tier1: Use RRPIf Tier2 or Tier3:If there is competitor with price ≤ RRP: ==> use RRPotherwiseif reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price changeb) Margin Cap:if reco landed price - shipping costs > max price ==> reco landed price := max_price + shipping costsc) Price Change Threshold    Letzter Pricing Stream != 'UNHEALTHY INVENTORY':if (reco landed price - letzter landed price) / landed price > 0.3 ==> reco landed price := landed price * 1.3if (reco landed price - letzter landed price) / landed price < -0.3 ==> reco landed price := landed price * 0.7d) Margin Floorif reco landed price - shipping costs < min price ==> reco landed price := min_price + shipping costsotherwise ==> keine Änderunge) Final reco price roundedif reco landed price - shipping costs < 0.5 ==> final reco price := reco landed price - shipping costsif reco landed price - shipping costs < 200 ==> final reco price := round(reco landed price - shipping costs; 0) + 0.90otherwise ==> final reco price := round(reco landed price - shipping costs; 0)Price change:if no price change ==> NEEDS_TO_BE_UPDATED := 0if price cap due to margin floor ==> NEEDS_TO_BE_UPDATED := 1if price cap due to unhealthy inventory reset ==> NEEDS_TO_BE_UPDATED := 1if no price cap due to unhealthy inventory reset and store limit = 1 and (reco_landed_price > 100 or price difference > 4)==> NEEDS_TO_BE_UPDATED := 1if no price cap due to unhealthy inventory reset and store limit = 1 and last price change less than 7 days ago ==> NEEDS_TO_BE_UPDATED := 0otherwise==> NEEDS_TO_BE_UPDATED := 1Execution:if NEEDS_TO_BE_UPDATE = 1==> distribute new priceotherwise ==> don’t distribute price |

Strategy "PRICE SUCCESSOR"

Selection of all relevant products

(see also here BPS Algorithm: Stream Selection)

Product is

* merchandise article (no voucher or software license or similar)
* no B-stock product
* active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”
* no bundle
* on the auto pricing list, not excluded from auto pricing, not manually deactivated
* configured as Price Successors
* has neither price nor purchase_price quality issues

merchandise article (no voucher or software license or similar)

no B-stock product

active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”

no bundle

on the auto pricing list, not excluded from auto pricing, not manually deactivated

configured as Price Successors

has neither price nor purchase_price quality issues

Price Calculation

Get price of the predecessor (base product to be used as reference for current successor product) from the configuration as well as the price factor val.

* If value_type = relative: ==> reco_landed_price = price_base_product * (1 + val_rel) + shipping costs
* If value_type = absolute: ==> reco_landed_price = price_base_product + val_abs + shipping costs

If value_type = relative: ==> reco_landed_price = price_base_product * (1 + val_rel) + shipping costs

If value_type = absolute: ==> reco_landed_price = price_base_product + val_abs + shipping costs

Price quality checks

(see also here BPS Algorithm: Price Quality Check)

Preparation for margin calculation:

* if current purchase price < average inventory value==> product costs := current purchase price
* if inventory > 0 ==> product costs := average inventory value
* otherwise==> product costs := current purchase price

if current purchase price < average inventory value==> product costs := current purchase price

if inventory > 0 ==> product costs := average inventory value

otherwise==> product costs := current purchase price

store limit:

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
* If Tier2 or Tier3:If there is competitor with price ≤ RRP: ==> use RRPotherwiseif reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price change
* If there is competitor with price ≤ RRP: ==> use RRP
* otherwiseif reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price change
* if reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costs
* If sales flag is set: ==> Cap bei RRP - 5%
* otherwise==> no price change

If Tier1: Use RRP

If Tier2 or Tier3:

* If there is competitor with price ≤ RRP: ==> use RRP
* otherwiseif reco landed price > RRP + shipping costs: ==> reco landed price := RRP + shipping costsIf sales flag is set: ==> Cap bei RRP - 5%otherwise==> no price change
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

