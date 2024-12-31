# Stream: New Products Pricing

## Motivation
The purpose of the pricing stream New Products is to find a good starting price of a product that’s newly listed. However we only consider a product as new, if the relevant flag is set in Cyberparts and if there is no relevant competitor that currently has the same product on stock due to our price feed data.

## Configuration
There currently is no configuration for this pricing stream available.

## Algorithm
| Strategy "NEW PRODUCT" |
|---|
| Selection of all relevant products(see also here Base Price Algorithm: Stream Selection) | Product ismerchandise article (no voucher or software license or similar)is new productno B-stock productactive, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”no bundleon the auto pricing list, not excluded from auto pricing, not manually deactivatednot activated for COVERAGE BASED PRICINGno ENFORCE RRP pricingno activated for Price Relations Pricingamount of considered competing merchants with stock is 0has valid recommended retail price (called RRP)no data quality issues regarding purchase price |
| Price Calculation | Use the recommended retail price as new price==> reco landed price := recommended retail price + shipping costs |
| Price quality checks(see also here Base Price Algorithm: Price Quality Check) | Price change:if no price change ==> NEEDS_TO_BE_UPDATED := 0otherwise==> NEEDS_TO_BE_UPDATED := 1Execution:if NEEDS_TO_BE_UPDATE = 1==> distribute new priceotherwise ==> don’t distribute price |

Strategy "NEW PRODUCT"

Selection of all relevant products

(see also here Base Price Algorithm: Stream Selection)

Product is

* merchandise article (no voucher or software license or similar)
* is new product
* no B-stock product
* active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”
* no bundle
* on the auto pricing list, not excluded from auto pricing, not manually deactivated
* not activated for COVERAGE BASED PRICING
* no ENFORCE RRP pricing
* no activated for Price Relations Pricing
* amount of considered competing merchants with stock is 0
* has valid recommended retail price (called RRP)
* no data quality issues regarding purchase price

merchandise article (no voucher or software license or similar)

is new product

no B-stock product

active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”

no bundle

on the auto pricing list, not excluded from auto pricing, not manually deactivated

not activated for COVERAGE BASED PRICING

no ENFORCE RRP pricing

no activated for Price Relations Pricing

amount of considered competing merchants with stock is 0

has valid recommended retail price (called RRP)

no data quality issues regarding purchase price

Price Calculation

Use the recommended retail price as new price==> reco landed price := recommended retail price + shipping costs

Price quality checks

(see also here Base Price Algorithm: Price Quality Check)

Price change:

* if no price change ==> NEEDS_TO_BE_UPDATED := 0
* otherwise==> NEEDS_TO_BE_UPDATED := 1

if no price change ==> NEEDS_TO_BE_UPDATED := 0

otherwise==> NEEDS_TO_BE_UPDATED := 1

Execution:

* if NEEDS_TO_BE_UPDATE = 1==> distribute new price
* otherwise ==> don’t distribute price

if NEEDS_TO_BE_UPDATE = 1==> distribute new price

otherwise ==> don’t distribute price

