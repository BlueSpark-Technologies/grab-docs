# MS Dashboard

# Content:
### 1. Historic Diagrams
* How many price changes per hour/day/week? - Every price change can be found in the logs (price not None).
* How does Buy Box relative rate / absolute amount change via time? - NO data
* Percentage of Amazon products split down to pricing category (reason) via time. There exist the following groups: capped by min_price - Message “The price is calculated from purchase price plus fee and VAT“capped webshop_price - Message “The price is calculated from webshop price plus markup“only competitor - Message “No competitor available, landed lowest competitive price is None”undercut competitors - Message “The calculated price is cheaper than the lowest offer“no Cyberport data available - Warning “Null values among aggregated warehouse info” https://cyber-solutions.atlassian.net/browse/PA-198 -> Per run (hourly) group by reasons above. Each product should fall into only one of those reasons above.
* capped by min_price - Message “The price is calculated from purchase price plus fee and VAT“
* capped webshop_price - Message “The price is calculated from webshop price plus markup“
* only competitor - Message “No competitor available, landed lowest competitive price is None”
* undercut competitors - Message “The calculated price is cheaper than the lowest offer“
* no Cyberport data available - Warning “Null values among aggregated warehouse info” https://cyber-solutions.atlassian.net/browse/PA-198 -> Per run (hourly) group by reasons above. Each product should fall into only one of those reasons above.
* Product price coverage (Amazon product skus which we could price (no errors) vs. products we couldn't price due to errors) via time We could price a product whenever there was a price change in the last hour - available in price change logsWe couldn’t price a product whenThere was a null value in Cyberport data - available in message “Null values among aggregated warehouse info”There is no Amazon fee data available - available in message “calculate_ms_fee_relative return value is None”There was a null value in Feed data because the SKU shared an ASIN with another SKU - No data
* We could price a product whenever there was a price change in the last hour - available in price change logs
* We couldn’t price a product whenThere was a null value in Cyberport data - available in message “Null values among aggregated warehouse info”There is no Amazon fee data available - available in message “calculate_ms_fee_relative return value is None”There was a null value in Feed data because the SKU shared an ASIN with another SKU - No data
* There was a null value in Cyberport data - available in message “Null values among aggregated warehouse info”
* There is no Amazon fee data available - available in message “calculate_ms_fee_relative return value is None”
* There was a null value in Feed data because the SKU shared an ASIN with another SKU - No data

How many price changes per hour/day/week? - Every price change can be found in the logs (price not None).

How does Buy Box relative rate / absolute amount change via time? - NO data

Percentage of Amazon products split down to pricing category (reason) via time. There exist the following groups:

* capped by min_price - Message “The price is calculated from purchase price plus fee and VAT“
* capped webshop_price - Message “The price is calculated from webshop price plus markup“
* only competitor - Message “No competitor available, landed lowest competitive price is None”
* undercut competitors - Message “The calculated price is cheaper than the lowest offer“
* no Cyberport data available - Warning “Null values among aggregated warehouse info” https://cyber-solutions.atlassian.net/browse/PA-198 -> Per run (hourly) group by reasons above. Each product should fall into only one of those reasons above.

capped by min_price - Message “The price is calculated from purchase price plus fee and VAT“

capped webshop_price - Message “The price is calculated from webshop price plus markup“

only competitor - Message “No competitor available, landed lowest competitive price is None”

undercut competitors - Message “The calculated price is cheaper than the lowest offer“

no Cyberport data available - Warning “Null values among aggregated warehouse info” https://cyber-solutions.atlassian.net/browse/PA-198 -> Per run (hourly) group by reasons above. Each product should fall into only one of those reasons above.

Product price coverage (Amazon product skus which we could price (no errors) vs. products we couldn't price due to errors) via time

* We could price a product whenever there was a price change in the last hour - available in price change logs
* We couldn’t price a product whenThere was a null value in Cyberport data - available in message “Null values among aggregated warehouse info”There is no Amazon fee data available - available in message “calculate_ms_fee_relative return value is None”There was a null value in Feed data because the SKU shared an ASIN with another SKU - No data
* There was a null value in Cyberport data - available in message “Null values among aggregated warehouse info”
* There is no Amazon fee data available - available in message “calculate_ms_fee_relative return value is None”
* There was a null value in Feed data because the SKU shared an ASIN with another SKU - No data

We could price a product whenever there was a price change in the last hour - available in price change logs

We couldn’t price a product when

* There was a null value in Cyberport data - available in message “Null values among aggregated warehouse info”
* There is no Amazon fee data available - available in message “calculate_ms_fee_relative return value is None”
* There was a null value in Feed data because the SKU shared an ASIN with another SKU - No data

There was a null value in Cyberport data - available in message “Null values among aggregated warehouse info”

There is no Amazon fee data available - available in message “calculate_ms_fee_relative return value is None”

There was a null value in Feed data because the SKU shared an ASIN with another SKU - No data

### 2. KPIs
* Amount products on Amazon ( 1 ) - count distinct by ASIN over all messages “Successfully saved ProductOffer” after this story https://cyber-solutions.atlassian.net/browse/PA-198 is done
* Amount Buy Box products ( 2 ) - count district by ASIN where we_won_buy_box = True over all messages “Successfully saved ProductOffer” after this story https://cyber-solutions.atlassian.net/browse/PA-198 is done
* Buy Box Rate - 2 / 1 in percent

Amount products on Amazon ( 1 ) - count distinct by ASIN over all messages “Successfully saved ProductOffer” after this story https://cyber-solutions.atlassian.net/browse/PA-198 is done

Amount Buy Box products ( 2 ) - count district by ASIN where we_won_buy_box = True over all messages “Successfully saved ProductOffer” after this story https://cyber-solutions.atlassian.net/browse/PA-198 is done

Buy Box Rate - 2 / 1 in percent

### 3. Tables
* Null values in DIS data (Purpose: Category managers want to be able to change change this data in CyberParts and increase the autopricing coverage): - Parse warning message “Null values among aggregated warehouse info”One row for each products for which the latest price calculation attempt resulted in an error because of null values in purchase_price, webshop_price, shipping_group or shipping_infoColumns SKUtimestamp of price calculation attemptpurchase_pricewebshop_price shipping_groupshipping_info
* One row for each products for which the latest price calculation attempt resulted in an error because of null values in purchase_price, webshop_price, shipping_group or shipping_info
* Columns SKUtimestamp of price calculation attemptpurchase_pricewebshop_price shipping_groupshipping_info
* SKU
* timestamp of price calculation attempt
* purchase_price
* webshop_price
* shipping_group
* shipping_info
* Null values in Feed data: - Parse warning message “calculate_ms_fee_relative return value is None”One row for each products for which the latest price calculation attempt resulted in an error because of null values in marketplace feeColumns SKUtimestamp of price calculation attemptmarketplace fee price = None - fixedmarketplace fee amount = None - fixed
* One row for each products for which the latest price calculation attempt resulted in an error because of null values in marketplace fee
* Columns SKUtimestamp of price calculation attemptmarketplace fee price = None - fixedmarketplace fee amount = None - fixed
* SKU
* timestamp of price calculation attempt
* marketplace fee price = None - fixed
* marketplace fee amount = None - fixed
* Duplicate SKU per ASIN: Table with SKUs that share an ASIN, together with first appearance of the SKU - NO data

Null values in DIS data (Purpose: Category managers want to be able to change change this data in CyberParts and increase the autopricing coverage): - Parse warning message “Null values among aggregated warehouse info”

* One row for each products for which the latest price calculation attempt resulted in an error because of null values in purchase_price, webshop_price, shipping_group or shipping_info
* Columns SKUtimestamp of price calculation attemptpurchase_pricewebshop_price shipping_groupshipping_info
* SKU
* timestamp of price calculation attempt
* purchase_price
* webshop_price
* shipping_group
* shipping_info

One row for each products for which the latest price calculation attempt resulted in an error because of null values in purchase_price, webshop_price, shipping_group or shipping_info

Columns

* SKU
* timestamp of price calculation attempt
* purchase_price
* webshop_price
* shipping_group
* shipping_info

SKU

timestamp of price calculation attempt

purchase_price

webshop_price

shipping_group

shipping_info

Null values in Feed data: - Parse warning message “calculate_ms_fee_relative return value is None”

* One row for each products for which the latest price calculation attempt resulted in an error because of null values in marketplace fee
* Columns SKUtimestamp of price calculation attemptmarketplace fee price = None - fixedmarketplace fee amount = None - fixed
* SKU
* timestamp of price calculation attempt
* marketplace fee price = None - fixed
* marketplace fee amount = None - fixed

One row for each products for which the latest price calculation attempt resulted in an error because of null values in marketplace fee

Columns

* SKU
* timestamp of price calculation attempt
* marketplace fee price = None - fixed
* marketplace fee amount = None - fixed

SKU

timestamp of price calculation attempt

marketplace fee price = None - fixed

marketplace fee amount = None - fixed

Duplicate SKU per ASIN: Table with SKUs that share an ASIN, together with first appearance of the SKU - NO data

# Logs analysis
### A. Marketplace Feed:
| # | Message | Comments | Payload |
|---|---|---|---|
| 1 | Successfully saved ProductOffer (containing 20 top_offers ): | add asinadd buy_box_winner | {
  "sales_rankings": [
    {"rank": 15160, "product_category_id": "pc_display_on_website"}, 
    {"rank": 120, "product_category_id": "430161031"}
  ], 
  "competitive_price_threshold": 518.0, 
  "offer_change_time": "2020-05-27T14:26:16Z", 
  "id": "ffb9b02b-58c5-413d-a5a1-cf6666a1c75d", 
  "suggested_lower_price_plus_shipping": 509.0, 
  "item_condition": "new", 
  "created_at": "2020-05-27T14:26:36Z", 
  "landed_ms_price": 568.9, 
  "landed_buy_box_price": 518.0, 
  "product_id": "33d2b1d1-89ad-4696-b93b-eae5ac325f3b",
  "updated_at": null
} |
| 2 | Processing "AnyOfferChanged" for Product: |  | {
  "merchant_id": "ba7c54cc-775c-4d06-b418-bca18bac8174", 
  "id": "33d2b1d1-89ad-4696-b93b-eae5ac325f3b", 
  "sku": "2E07-3IK", 
  "created_at": "2020-03-18T13:49:00Z", 
  "is_active": true, 
  "asin": "B081H4GX2F", 
  "updated_at": null
} |

#

Message

Comments

Payload

1

Successfully saved ProductOffer (containing 20 top_offers ):

add asin

add buy_box_winner

2

Processing "AnyOfferChanged" for Product:

### B. Marketplace Pricing
| # | Message | Namespace | Payload |
|---|---|---|---|
| 1 | No competitor available, landed lowest competitive price is None |  | {
  'vat': 0.19, 
  'buffer_to_competitor': 10,
   'cheap_shipping': 499, 
   'normal_shipping': 599, 
   'shipping_threshold': 20000, 
   'dhl_express_costs': 1899, 
   'haulier_low_costs': 1899, 
   'haulier_medium_costs': 2990, 
   'haulier_large_costs': 3999, 
   'markup_only_seller': 0.0, 
   'markup_webshop': 100, 
   'markup_min_price': 0.03
}; 

[Input Data]: 
{
  'product_sku': '1C33-1SS', 
  'mfs_fee_total': Decimal('11906.00'), 
  'mfs_fee_price': Decimal('170090.0'), 
  'landed_mfs_price': Decimal('170090.0'),
  'landed_lowest_comp_price': None, 
  'purchase_price': Decimal('122155.00'), 
  'webshop_price': Decimal('159900.0'), 
  'shipping_class': '1', 
  'shipping_group': '2'
}; 

[Derived Variables]: 
{
  'ms_fee_relative': Decimal('0.070'), 
  'min_price': Decimal('160206.160'), 
  'shipping_costs_min': Decimal('599'), 
  'landed_min_price': Decimal('160805.160'), 
  'shipping_costs_web': Decimal('599'), 
  'landed_web_shop_price': Decimal('160499.0')
} 

[Output Price]: 171834 |
| 2 | The calculated price is cheaper than the lowest offer; |  | [Algorithm Config]: 
{
  'vat': 0.19, 
  'buffer_to_competitor': 10, 
  'cheap_shipping': 499, 
  'normal_shipping': 599, 
  'shipping_threshold': 20000, 
  'dhl_express_costs': 1899, 
  'haulier_low_costs': 1899, 
  'haulier_medium_costs': 2990, 
  'haulier_large_costs': 3999, 
  'markup_only_seller': 0.0, 
  'markup_webshop': 100, 
  'markup_min_price': 0.03
}; 

[Input Data]: 
{
  'product_sku': 'Q535-017', 
  'mfs_fee_total': Decimal('1021.00'), 
  'mfs_fee_price': Decimal('14590.0'), 
  'landed_mfs_price': Decimal('13290.0'), 
  'landed_lowest_comp_price': Decimal('11989.00'), 
  'purchase_price': Decimal('8609.00'), 
  'webshop_price': Decimal('11290.0'), 
  'shipping_class': '1', 
  'shipping_group': '1'
}; 

[Derived Variables]: 
{
  'ms_fee_relative': Decimal('0.070'), 
  'min_price': Decimal('11290.695'), 
  'shipping_costs_min': Decimal('499'), 
  'landed_min_price': Decimal('11789.695'), 
  'shipping_costs_web': Decimal('499'), 
  'landed_web_shop_price': Decimal('11789.0')
} 

[Output Price]: 11979 |
| 3 | The price is calculated from webshop price plus markup; |  | [Algorithm Config]: 
{
  'vat': 0.19, 
  'buffer_to_competitor': 10, 
  'cheap_shipping': 499, 
  'normal_shipping': 599, 
  'shipping_threshold': 20000, 
  'dhl_express_costs': 1899, 
  'haulier_low_costs': 1899, 
  'haulier_medium_costs': 2990, 
  'haulier_large_costs': 3999, 
  'markup_only_seller': 0.0, 
  'markup_webshop': 100, 
  'markup_min_price': 0.03
}; 

[Input Data]: 
{
  'product_sku': '2303-99X', 
  'mfs_fee_total': Decimal('937.00'), 
  'mfs_fee_price': Decimal('13390.0'), 
  'landed_mfs_price': Decimal('14990.0'), 
  'landed_lowest_comp_price': Decimal('12947.00'), 
  'purchase_price': Decimal('9506.00'), 
  'webshop_price': Decimal('13490.0'), 
  'shipping_class': '1', 
  'shipping_group': '1'
}; 

[Derived Variables]: 
{
  'ms_fee_relative': Decimal('0.070'), 
  'min_price': Decimal('12467.109'), 
  'shipping_costs_min': Decimal('499'), 
  'landed_min_price': Decimal('12966.109'), 
  'shipping_costs_web': Decimal('499'), 
  'landed_web_shop_price': Decimal('13989.0')
} 
[Output Price]: 14089 |
| 4 | The price is calculated from purchase price plus fee and VAT; |  | [Algorithm Config]: 
{
  'vat': 0.19, 
  'buffer_to_competitor': 10, 
  'cheap_shipping': 499, 
  'normal_shipping': 599, 
  'shipping_threshold': 20000, 
  'dhl_express_costs': 1899, 
  'haulier_low_costs': 1899, 
  'haulier_medium_costs': 2990, 
  'haulier_large_costs': 3999, 
  'markup_only_seller': 0.0, 
  'markup_webshop': 100, 
  'markup_min_price': 0.03
}; 

[Input Data]: 
{
  'product_sku': '2E07-3IK', 
  'mfs_fee_total': Decimal('3891.00'), 
  'mfs_fee_price': Decimal('55590.0'), 
  'landed_mfs_price': Decimal('56890.0'), 
  'landed_lowest_comp_price': Decimal('51800.0'), 
  'purchase_price': Decimal('41544.00'), 
  'webshop_price': Decimal('53100.0'), 
  'shipping_class': '1', 
  'shipping_group': '1'
}; 

[Derived Variables]: 
{
  'ms_fee_relative': Decimal('0.070'), 
  'min_price': Decimal('54484.914'), 
  'shipping_costs_min': Decimal('599'), 
  'landed_min_price': Decimal('55083.914'), 
  'shipping_costs_web': Decimal('599'), 
  'landed_web_shop_price': Decimal('53699.0')
} 

[Output Price]: 55084 |
| 5 | calculate_min_price return value is None |  | [Algorithm Config]: 
{
  'vat': 0.19, 
  'buffer_to_competitor': 10, 
  'cheap_shipping': 499, 
  'normal_shipping': 599, 
  'shipping_threshold': 20000, 
  'dhl_express_costs': 1899, 
  'haulier_low_costs': 1899, 
  'haulier_medium_costs': 2990, 
  'haulier_large_costs': 3999, 
  'markup_only_seller': 0.0, 
  'markup_webshop': 100, 
  'markup_min_price': 0.03
} 

[Input Data]: 
{
  'product_sku': '1H62-03Q', 
  'purchase_price': Decimal('28725.00'), 
  'webshop_price': Decimal('32900.0'), 
  'shipping_class': '1', 
  'shipping_group': '99'
} |
| 6 | calculate_ms_fee_relative return value is None; |  | Algorithm Config]: 
{
  'vat': 0.19, 
  'buffer_to_competitor': 10, 
  'cheap_shipping': 499, 
  'normal_shipping': 599, 
  'shipping_threshold': 20000, 
  'dhl_express_costs': 1899, 
  'haulier_low_costs': 1899, 
  'haulier_medium_costs': 2990, 
  'haulier_large_costs': 3999, 
  'markup_only_seller': 0.0, 
  'markup_webshop': 100, 
  'markup_min_price': 0.03
}; 

[Input Data]: 
{
  'product_sku': '1H62-03Q', 
  'purchase_price': Decimal('28725.00'), 
  'webshop_price': Decimal('32900.0'), 
  'shipping_class': '1', 
  'shipping_group': '99'
} |
| 7 | calculate_shipping_costs_min return value is None: |  | [Algorithm Config]: 
{
  'vat': 0.19, 
  'buffer_to_competitor': 10, 
  'cheap_shipping': 499, 
  'normal_shipping': 599, 
  'shipping_threshold': 20000, 
  'dhl_express_costs': 1899, 
  'haulier_low_costs': 1899, 
  'haulier_medium_costs': 2990, 
  'haulier_large_costs': 3999, 
  'markup_only_seller': 0.0, 
  'markup_webshop': 100, 
  'markup_min_price': 0.03
}; 

[Input Data]: 
{
  'product_sku': '3F53-01M', 
  'webshop_price': Decimal('3500000.0'), 
  'purchase_price': Decimal('2867386.00'), 
  'shipping_class': '2',
  'shipping_group': '2'
} |
| 8 | Null value in at least one of the following fields: web shop price, purchase price, MS fee amount, shipping group, shipping class; | not a price change | [Algorithm Config]: 
{
  'vat': 0.19, 
  'buffer_to_competitor': 10, 
  'cheap_shipping': 499, 
  'normal_shipping': 599, 
  'shipping_threshold': 20000, 
  'dhl_express_costs': 1899, 
  'haulier_low_costs': 1899, 
  'haulier_medium_costs': 2990, 
  'haulier_large_costs': 3999, 
  'markup_only_seller': 0.0, 
  'markup_webshop': 100, 
  'markup_min_price': 0.03
}; 
[Input Data]: 
{
  'product_sku': '1H53-0A7', 
  'mfs_fee_total': Decimal('4475.00'), 
  'mfs_fee_price': Decimal('47190.0'), 
  'landed_mfs_price': Decimal('47190.0'), 
  'landed_lowest_comp_price': Decimal('39992.00'), 
  'purchase_price': Decimal('34491.00'), 
  'webshop_price': Decimal('43900.0'), 
  'shipping_class': None, 
  'shipping_group': None
}; 

[Derived Variables]: 
{
  'ms_fee_relative': Decimal('0.095'), 
  'min_price': Decimal('46291.802'), 
  'shipping_costs_min': None, 
  'landed_min_price': None, 
  'shipping_costs_web': None, 
  'landed_web_shop_price': None
} 

[Output Price]: None |

#

Message

Namespace

Payload

1

No competitor available, landed lowest competitive price is None

2

The calculated price is cheaper than the lowest offer;

3

The price is calculated from webshop price plus markup;

4

The price is calculated from purchase price plus fee and VAT;

5

calculate_min_price return value is None

6

calculate_ms_fee_relative return value is None;

7

calculate_shipping_costs_min return value is None:

8

Null value in at least one of the following fields: web shop price, purchase price, MS fee amount, shipping group, shipping class;

not a price change

