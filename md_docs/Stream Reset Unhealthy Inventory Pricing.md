# Stream: Reset Unhealthy Inventory Pricing

## Motivation
The purpose of the pricing stream Reset Unhealthy Inventory is to avoid to offer a product on a too low price, if an unhealthy product gets sold out and then for some reason re-bought and therefore re-offered again after some time. This stream makes sure to set the price to the recommended retail price (RRP) again, after the last item was sold. Consider this stream as a safety net only.

## Configuration
We have some configuration variables for this stream in our global configuration:

| Configuration parameter | What does it control? | Current value |
|---|---|---|
| UNHEALTHY_INVENTORY_RESET_MARGIN_MARKUP | What should our minimum margin be, if we can't price with RRP in this stream? | see here for the currently used configuration value PS Configuration |
| RRP_SHIPPING_THRESHOLD | Up until which price should shipping be included in RRP? | -”- |

Configuration parameter

What does it control?

Current value

UNHEALTHY_INVENTORY_RESET_MARGIN_MARKUP

What should our minimum margin be, if we can't price with RRP in this stream?

see here for the currently used configuration value PS Configuration

RRP_SHIPPING_THRESHOLD

Up until which price should shipping be included in RRP?

-”-

## Algorithm
Here is a flow chart of this algorithm.

| Strategy "UNHEALTHY INVENTORY RESET" |
|---|
| Selection of all relevant products(see also here Base Price Algorithm: Stream Selection) | Product ismerchandise article (no voucher or software license or similar)no B-stock productactive, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”no bundleon the auto pricing list, not excluded from auto pricing, not manually deactivatednot activated for COVERAGE BASED PRICINGnot activated for PRICE SUCCESSORhas neither price nor purchase_price quality issuesactivated for UNHEALTHY INVENTORY RESET |
| Price Calculation | Price calculation: Use RRP if possibleif RRP is available and larger than zero and if competition available larger than lowest competitor offerif we have less than 4 competitor offers that have the product available==> reco listed price := RRP + shipping costsif RRP < 9999==> reco listed price := RRPelse ==> reco listed price := RRP + shipping costsif is no valid RRP but valid margin floor==> reco listed price := min_price * 1.15otherwise==> keep old price: reco listed price := current landed price |
| Price quality checks(see also here Base Price Algorithm: Price Quality Check) | Store limit:if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1otherwise ==> Store limit := 0Price change:if no price change ==> NEEDS_TO_BE_UPDATED := 0otherwise==> NEEDS_TO_BE_UPDATED := 1Execution:if NEEDS_TO_BE_UPDATE = 1==> distribute new priceotherwise ==> don’t distribute price |

Strategy "UNHEALTHY INVENTORY RESET"

Selection of all relevant products

(see also here Base Price Algorithm: Stream Selection)

Product is

* merchandise article (no voucher or software license or similar)
* no B-stock product
* active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”
* no bundle
* on the auto pricing list, not excluded from auto pricing, not manually deactivated
* not activated for COVERAGE BASED PRICING
* not activated for PRICE SUCCESSOR
* has neither price nor purchase_price quality issues
* activated for UNHEALTHY INVENTORY RESET

merchandise article (no voucher or software license or similar)

no B-stock product

active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”

no bundle

on the auto pricing list, not excluded from auto pricing, not manually deactivated

not activated for COVERAGE BASED PRICING

not activated for PRICE SUCCESSOR

has neither price nor purchase_price quality issues

activated for UNHEALTHY INVENTORY RESET

Price Calculation

Price calculation: Use RRP if possible

* if RRP is available and larger than zero and if competition available larger than lowest competitor offerif we have less than 4 competitor offers that have the product available==> reco listed price := RRP + shipping costsif RRP < 9999==> reco listed price := RRPelse ==> reco listed price := RRP + shipping costs
* if we have less than 4 competitor offers that have the product available==> reco listed price := RRP + shipping costs
* if RRP < 9999==> reco listed price := RRP
* else ==> reco listed price := RRP + shipping costs
* if is no valid RRP but valid margin floor==> reco listed price := min_price * 1.15
* otherwise==> keep old price: reco listed price := current landed price

if RRP is available and larger than zero and if competition available larger than lowest competitor offer

* if we have less than 4 competitor offers that have the product available==> reco listed price := RRP + shipping costs
* if RRP < 9999==> reco listed price := RRP
* else ==> reco listed price := RRP + shipping costs

if we have less than 4 competitor offers that have the product available==> reco listed price := RRP + shipping costs

if RRP < 9999==> reco listed price := RRP

else ==> reco listed price := RRP + shipping costs

if is no valid RRP but valid margin floor==> reco listed price := min_price * 1.15

otherwise==> keep old price: reco listed price := current landed price

Price quality checks

(see also here Base Price Algorithm: Price Quality Check)

Store limit:

* if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1
* otherwise ==> Store limit := 0

if product is available in at least 2 stores and not marked via ePOP then==> Store limit := 1

otherwise ==> Store limit := 0

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

