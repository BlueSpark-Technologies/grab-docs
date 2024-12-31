# Stream: BTO Pricing

## Motivation
BTO products (build to order) are products that often are made specifically for the customer who ordered it. They usually don’t have a good EAN and can therefore only difficultly be matched with offers from other merchants. Also if they get matched the matching often is inaccurate. Therefore it is hard to price them with the merchant based pricing.

The purpose of this stream is to price BTO products using the purchase price (which includes the raised purchase costs compared to the default configuration of the product) together with a percentage markup that covers the desired CM-margin.

## Configuration
In the future we would like to have

* a flag that defines an article in PIM as BTO → therefore we don’t need to filter on product description
* an update to the Pricing UI tab basic settings to contain two extra columns for BTO markup: (1) BTO markup for products with stock, (2) BTO markup for products without stock. (exact design needs to be defined)
* we don’t need the configuration “Anwendung bestehender Preisrundungsregeln?” (should the product be rounded), instead we will just round all the product prices to have a pretty format.
* unchanged we will only allow relative (percentage) markups, not absolute. Both columns should be configurable to two digits in steps of 0.01 increments.

a flag that defines an article in PIM as BTO → therefore we don’t need to filter on product description

an update to the Pricing UI tab basic settings to contain two extra columns for BTO markup: (1) BTO markup for products with stock, (2) BTO markup for products without stock. (exact design needs to be defined)

we don’t need the configuration “Anwendung bestehender Preisrundungsregeln?” (should the product be rounded), instead we will just round all the product prices to have a pretty format.

unchanged we will only allow relative (percentage) markups, not absolute. Both columns should be configurable to two digits in steps of 0.01 increments.

## Algorithm
The algorithm behind BTO products will not change, just the place where it is calculated (microservice instead of VKPA Tool).

| Strategy "BTO MARKUP" |
|---|
| Selection of all relevant products(see also here Base Price Algorithm: Stream Selection) | Product ismerchandise article (no voucher or software license or similar)no B-stock productactive, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”no bundlenot excluded from auto pricing, not manually deactivatednot activated for COVERAGE BASED PRICINGnot activated for ENFORCE RRP pricingnot activated for PRICE SUCCESSOR PRICINGhas BTO flag or (until BTO flag is not available in PIM yet) contains the phrase “BTO” in product descriptionthere is BTO configuration available for this product or its article group or its category level 3has no purchase_price quality issues |
| Price Calculation | Recommended priceIf standard purchase price, VAT and BTO configuration are availableIf product has free stock (all stock ids, disregarding open purchase orders)==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_in_stock)Else==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_no_stock)otherwise keep old price:==> reco listed price := current listed price |
| Price quality checks(see also here Base Price Algorithm: Price Quality Check) | Not more than 30% price change check: if reco listed price > 1.3 * current listed price ==> reco listed price := 1.3 * current listed price if reco listed price < 0.7 * current listed price ==> reco listed price := 0.7 * current listed priceelse keep it at it isFinal reco price roundedif reco listed price  < 0.5€==> final reco price := reco listed priceif reco listed price < 200€==> final reco price := floor(reco listed price) + 0.90€otherwise ==> final reco price := ceil(reco listed price)Price change:if no price change ==> NEEDS_TO_BE_UPDATED := 0, don’t distribute new priceotherwise==> NEEDS_TO_BE_UPDATED := 1, distribute new price |

Strategy "BTO MARKUP"

Selection of all relevant products

(see also here Base Price Algorithm: Stream Selection)

Product is

* merchandise article (no voucher or software license or similar)
* no B-stock product
* active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”
* no bundle
* not excluded from auto pricing, not manually deactivated
* not activated for COVERAGE BASED PRICING
* not activated for ENFORCE RRP pricing
* not activated for PRICE SUCCESSOR PRICING
* has BTO flag or (until BTO flag is not available in PIM yet) contains the phrase “BTO” in product description
* there is BTO configuration available for this product or its article group or its category level 3
* has no purchase_price quality issues

merchandise article (no voucher or software license or similar)

no B-stock product

active, aka. not “ausgelistet” or “Bestand Zentrallager > 0” or “Inventory Store > 0” or “offene Einkaufsaufträge”

no bundle

not excluded from auto pricing, not manually deactivated

not activated for COVERAGE BASED PRICING

not activated for ENFORCE RRP pricing

not activated for PRICE SUCCESSOR PRICING

has BTO flag or (until BTO flag is not available in PIM yet) contains the phrase “BTO” in product description

there is BTO configuration available for this product or its article group or its category level 3

has no purchase_price quality issues

Price Calculation

Recommended price

* If standard purchase price, VAT and BTO configuration are availableIf product has free stock (all stock ids, disregarding open purchase orders)==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_in_stock)Else==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_no_stock)
* If product has free stock (all stock ids, disregarding open purchase orders)==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_in_stock)
* Else==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_no_stock)
* otherwise keep old price:==> reco listed price := current listed price

If standard purchase price, VAT and BTO configuration are available

* If product has free stock (all stock ids, disregarding open purchase orders)==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_in_stock)
* Else==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_no_stock)

If product has free stock (all stock ids, disregarding open purchase orders)==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_in_stock)

Else==> reco listed price := standard purchase price * (1 + VAT) * (1 + BTO_markup_no_stock)

otherwise keep old price:==> reco listed price := current listed price

Price quality checks

(see also here Base Price Algorithm: Price Quality Check)

Not more than 30% price change check:

* if reco listed price > 1.3 * current listed price ==> reco listed price := 1.3 * current listed price
* if reco listed price < 0.7 * current listed price ==> reco listed price := 0.7 * current listed price
* else keep it at it is

if reco listed price > 1.3 * current listed price ==> reco listed price := 1.3 * current listed price

if reco listed price < 0.7 * current listed price ==> reco listed price := 0.7 * current listed price

else keep it at it is

Final reco price rounded

* if reco listed price  < 0.5€==> final reco price := reco listed price
* if reco listed price < 200€==> final reco price := floor(reco listed price) + 0.90€
* otherwise ==> final reco price := ceil(reco listed price)

if reco listed price  < 0.5€==> final reco price := reco listed price

if reco listed price < 200€==> final reco price := floor(reco listed price) + 0.90€

otherwise ==> final reco price := ceil(reco listed price)

Price change:

* if no price change ==> NEEDS_TO_BE_UPDATED := 0, don’t distribute new price
* otherwise==> NEEDS_TO_BE_UPDATED := 1, distribute new price

if no price change ==> NEEDS_TO_BE_UPDATED := 0, don’t distribute new price

otherwise==> NEEDS_TO_BE_UPDATED := 1, distribute new price

## Release plan
* Until autumn: Integration of BTO config in Pricing UI
* Until beginning of 2022: Integration of BTO Stream in Base Price Service using BTO product filtering via product description
* Until beginning of 2022: Integration of BTO Flag in PIM and communication towards Base Price Service via SAP Pro
* Afterwards: change of BTO filtering using new flag in PIM instead of product description

Until autumn: Integration of BTO config in Pricing UI

Until beginning of 2022: Integration of BTO Stream in Base Price Service using BTO product filtering via product description

Until beginning of 2022: Integration of BTO Flag in PIM and communication towards Base Price Service via SAP Pro

Afterwards: change of BTO filtering using new flag in PIM instead of product description

## Tasks
* Stefan Rohne talk to Claudia for integration BTO field in PIM

