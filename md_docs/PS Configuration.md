# PS Configuration

# 1. Pricing UI
## Basic Settings
https://app.cybersolutions-tech.com/pricing/basic-settings

## Relevant Competitors
https://app.cybersolutions-tech.com/pricing/relevant-competitors

## Price Relations
https://app.cybersolutions-tech.com/pricing/price-relations

## Inventory Health
https://app.cybersolutions-tech.com/pricing/inventory-health

## Coverage Based Pricing
https://app.cybersolutions-tech.com/pricing/coverage-based-pricing

# 2. Product Exclusion
see here for tutorial ECS Escalation Scenarios & Tutorials

# 3. Environment Variables and Configuration File
Within the service we have a set of configuration values that can be adjusted to the current market situation and tenant.

* Configuration that is in environment variables can be set individually for each tenant and environment.
* Configuration that is within the https://bitbucket.org/devcst/bps-orchestration/src/master/src/bpsorch/config.py of the code repository can only be changed for all tenants at once. Moving parameters to environment variables can be done easily though on request.

Configuration that is in environment variables can be set individually for each tenant and environment.

Configuration that is within the https://bitbucket.org/devcst/bps-orchestration/src/master/src/bpsorch/config.py of the code repository can only be changed for all tenants at once. Moving parameters to environment variables can be done easily though on request.

A selection of parameters that can be adjusted within the service can be found here. The list is not exhaustive:

| Section | Parameter | Explanation | Value |
|---|---|---|---|
| SHIPPING COSTS | SHIPPING_THRESHOLDCHEAP_SHIPPINGNORMAL_SHIPPINGDHL_EXPRESS_COSTSHAULIER_LOW_COSTSHAULIER_MEDIUM_COSTSHAULIER_LARGE_COSTSHAULIER_ANY_POINT = None | Until which price in EUR do we use the cheap shipping? | 199.99 EUR4.99 EUR5.99 EUR18.99 EUR18.99 EUR29.90 EUR39.90 EURNone EUR |
| STREAM SELECTION | UNHEALTHY_INVENTORY_PRICE_RANGE_1 | First unhealthy inventory configuration range is for products with prices between 0 EUR and the following value in EUR. | 10 EUR |
| UNHEALTHY_INVENTORY_PRICE_RANGE_2 | Second range is for products with prices higher than the previous value and smaller or equal to the following in EUR. | 100 EUR |
| UNHEALTHY_INVENTORY_PRICE_RANGE_3 | Third range is for products with prices higher than the previous value and smaller or equal to the following in EUR.Fourth range is for products with prices higher than this value without an upper value. | 500 EUR |
| AMOUNT_MERCHANT_THRESHOLD_TIER_1_WO_STOCK | if there are less or equal than this amount of merchant competitor offers and we have no merchants with stock, we are in Tier1 without stock and use percentile_tier_1 | 0 merchants |
| AMOUNT_MERCHANT_THRESHOLD_TIER_1 | if there are less or equal than this amount of merchant competitor offers, we are in Tier1 with stock and use percentile_tier_1 | 3 merchants |
| AMOUNT_MERCHANT_THRESHOLD_TIER_2 | if there are less or equal than this amount of merchant competitor offers, but more than in Tier1, we are in Tier2 and use percentile_tier_2otherwise we are in Tier3 and use percentile_tier_3 | 6 merchants |
| MIN_STOCK_UNHEALTHY_INVENTORY_BAND_AMIN_STOCK_UNHEALTHY_INVENTORY_BAND_BMIN_STOCK_UNHEALTHY_INVENTORY_BAND_CMIN_STOCK_UNHEALTHY_INVENTORY_GLOBAL | minimal amount of free stock in central warehouse before we consider a product in an unhealthy bucket to be unhealthy depending on product views band A to C and global | 5 units3 units2 units1 unit |
| NO MERCHANTS PRICING | NO_MERCHANTS_MARGIN_MARKUP | how many percent do we want to add to our default price because we're the only competitor? | 0.1 fraction |
| RRP ENFORCED PRICING | UNHEALTHY_INVENTORY_RESET_MARGIN_MARKUP | what should be our minimum margin, if we can't price with recommended retail price? | 0.15 fraction |
| UNHEALTHY INVENTORY PRICING | UNHEALTHY_BUCKETS | which health buckets are considered unhealthy? | ['Lowest_Merchant', 'Lowest_Merchant_Markdown','Continuous_Markdown', 'Continuous_Markdown_Aggressive'] |
| MIN_PRICE_FRACTION_UNHEALTHY_INVENTORY | what fraction of the default min price do we use when pricing with default unhealthy inventory? | 0.5 fraction |
| CONVERGENCE_TO_MIN_PRICE_UNHEALTHY_INVENTORY | during first phase of a product entering unhealthy inventory stream, how much should the current price be reduced to the min price? a value of 0.6 means that we will end up a little below the middle between min price and original price | 0.5 fraction |
| UNHEALTHY_NO_MERCHANTS_MARGIN_MARKUP | how many percent do we want to add for unhealthy products to our defaultprice because we're the only competitor? | 0.1 fraction |
| DAYS_UNTIL_NEXT_EXPORT_CONT_MD | we reduce prices in the strategy 'Continuous_Markdown' in regular here defined intervals, unit is days | 7 days |
| DAYS_UNTIL_NEXT_EXPORT_CONT_MD_AGR | we reduce prices in the strategy 'Continuous_Markdown_Aggressive' in regular here defined intervals, unit is days | 3 days |
| B STOCK | MIN_PRICE_BSTOCK_PARENT_PRICE | what is the smallest price of a b stock product's parent product in EUR that we require in order to perform a reduction of the b stock product's price? | 3 EUR |
| MIN_PRICE_CHANGE_BSTOCK | what is the smallest price change to the previous price that we allow in B stock pricing? | 3 EUR |
| MAX_FRACTION_PARENT_BSTOCK | which fraction of a b stock product's parent product price do we minimally allow? | 0.5 fraction |
| PRICE CHECKS | MAXIMAL_PRICE_REDUCTION | what is the maximal relative amount of price reduction that we allow per price change? | 0.3 fraction |
| MAXIMAL_PRICE_INCREASE | what is the maximal relative amount of price increase that we allow per price change? | 0.3 fraction |
| RRP_SHIPPING_THRESHOLD | Up until which price should shipping be included in RRP? | 9999 |
| SALE_RRP_REDUCTION | how much should the RRP capping be relatively reduced when the product is on sale? | 0.05 |
| UNHEALTHY_INVENTORY_REDUCTION | how much should the price be reduced at least if the pricing didn't work due to a mistakenly price increase? | 0 |
| UNCRITICAL_UNHEALTHY_BUCKETS | for which unhealthy inventory buckets do we allow a higher min price as a soft entry into unhealthy inventory reduction? | ['Lowest_Merchant', 'Lowest_Merchant_Markdown'] |
| BUFFER_TO_LOWEST_COMPETITOR_OFFER | how much should our offer be more expensive than lowest competitor offer? | 1 |
| ROUNDING | MIN_THRESHOLD_ROUNDING | how many euros can the product cost at most until we apply rounding? | 0.5 EUR |
| CEIL_THRESHOLD_ROUNDING | how many euros can the product cost at most until we don't round up or down, but always up? | 199.99 EUR |
| DECIMAL_MASK_ROUNDING | how should the decimal part of a price in EUR look like to look pretty? | 0.9 EUR |
| PRICE_THRESHOLD_STORE_CAPPING | if the product costs less than this parameter in EUR we apply store capping | 100 EUR |
| STORE CHECKS | PRICE_INCREASE_THRESHOLD_STORE_CAPPING | how much can the price increase be at least in EUR until we we ignore store capping? | 4 EUR |
| PRICE_REDUCTION_THRESHOLD_STORE_CAPPING | how much can the price reduction be at least in EUR until we we ignore store capping? | 4 days |
| PRICE_CHANGE_INTERVAL_STORE_CAPPING | how many days do we require to pass since the last price change until we change price of a store affected product? | 7 days |
| SUSPICIOUS RECOMMENDATIONS | SUSPICIOUS_PRICE_TREND | how much lower can the recommended price be compared to the average of the last week? maximal relative threshold of a price change compared to average price of the last week until we send an alert to CM. A value of 0.4 means that new price can only be 40% smaller than original value. | 0.4 fraction |
| SUSPICIOUS_MARGIN_THRESHOLD | how much price profit margin do we allow at most until we treat a price as suspicious? | 0 fraction |
| SUSPICIOUS_PURCHASE_PRICE_TREND | how much lower can the recommended price be compared to the average of the last week until we treat the recommended price as suspicious? | 0.4 fraction |

Section

Parameter

Explanation

Value

SHIPPING COSTS

SHIPPING_THRESHOLDCHEAP_SHIPPINGNORMAL_SHIPPINGDHL_EXPRESS_COSTSHAULIER_LOW_COSTSHAULIER_MEDIUM_COSTSHAULIER_LARGE_COSTSHAULIER_ANY_POINT = None

Until which price in EUR do we use the cheap shipping?

199.99 EUR4.99 EUR5.99 EUR18.99 EUR18.99 EUR29.90 EUR39.90 EURNone EUR

STREAM SELECTION

UNHEALTHY_INVENTORY_PRICE_RANGE_1

First unhealthy inventory configuration range is for products with prices between 0 EUR and the following value in EUR.

10 EUR

UNHEALTHY_INVENTORY_PRICE_RANGE_2

Second range is for products with prices higher than the previous value and smaller or equal to the following in EUR.

100 EUR

UNHEALTHY_INVENTORY_PRICE_RANGE_3

Third range is for products with prices higher than the previous value and smaller or equal to the following in EUR.

Fourth range is for products with prices higher than this value without an upper value.

500 EUR

AMOUNT_MERCHANT_THRESHOLD_TIER_1_WO_STOCK

if there are less or equal than this amount of merchant competitor offers and we have no merchants with stock, we are in Tier1 without stock and use percentile_tier_1

0 merchants

AMOUNT_MERCHANT_THRESHOLD_TIER_1

if there are less or equal than this amount of merchant competitor offers, we are in Tier1 with stock and use percentile_tier_1

3 merchants

AMOUNT_MERCHANT_THRESHOLD_TIER_2

if there are less or equal than this amount of merchant competitor offers, but more than in Tier1, we are in Tier2 and use percentile_tier_2

otherwise we are in Tier3 and use percentile_tier_3

6 merchants

MIN_STOCK_UNHEALTHY_INVENTORY_BAND_AMIN_STOCK_UNHEALTHY_INVENTORY_BAND_BMIN_STOCK_UNHEALTHY_INVENTORY_BAND_CMIN_STOCK_UNHEALTHY_INVENTORY_GLOBAL

minimal amount of free stock in central warehouse before we consider a product in an unhealthy bucket to be unhealthy depending on product views band A to C and global

5 units3 units2 units1 unit

NO MERCHANTS PRICING

NO_MERCHANTS_MARGIN_MARKUP

how many percent do we want to add to our default price because we're the only competitor?

0.1 fraction

RRP ENFORCED PRICING

UNHEALTHY_INVENTORY_RESET_MARGIN_MARKUP

what should be our minimum margin, if we can't price with recommended retail price?

0.15 fraction

UNHEALTHY INVENTORY PRICING

UNHEALTHY_BUCKETS

which health buckets are considered unhealthy?

['Lowest_Merchant', 'Lowest_Merchant_Markdown','Continuous_Markdown', 'Continuous_Markdown_Aggressive']

MIN_PRICE_FRACTION_UNHEALTHY_INVENTORY

what fraction of the default min price do we use when pricing with default unhealthy inventory?

0.5 fraction

CONVERGENCE_TO_MIN_PRICE_UNHEALTHY_INVENTORY

during first phase of a product entering unhealthy inventory stream, how much should the current price be reduced to the min price? a value of 0.6 means that we will end up a little below the middle between min price and original price

0.5 fraction

UNHEALTHY_NO_MERCHANTS_MARGIN_MARKUP

how many percent do we want to add for unhealthy products to our default

price because we're the only competitor?

0.1 fraction

DAYS_UNTIL_NEXT_EXPORT_CONT_MD

we reduce prices in the strategy 'Continuous_Markdown' in regular here defined intervals, unit is days

7 days

DAYS_UNTIL_NEXT_EXPORT_CONT_MD_AGR

we reduce prices in the strategy 'Continuous_Markdown_Aggressive' in regular here defined intervals, unit is days

3 days

B STOCK

MIN_PRICE_BSTOCK_PARENT_PRICE

what is the smallest price of a b stock product's parent product in EUR that we require in order to perform a reduction of the b stock product's price?

3 EUR

MIN_PRICE_CHANGE_BSTOCK

what is the smallest price change to the previous price that we allow in B stock pricing?

3 EUR

MAX_FRACTION_PARENT_BSTOCK

which fraction of a b stock product's parent product price do we minimally allow?

0.5 fraction

PRICE CHECKS

MAXIMAL_PRICE_REDUCTION

what is the maximal relative amount of price reduction that we allow per price change?

0.3 fraction

MAXIMAL_PRICE_INCREASE

what is the maximal relative amount of price increase that we allow per price change?

0.3 fraction

RRP_SHIPPING_THRESHOLD

Up until which price should shipping be included in RRP?

9999

SALE_RRP_REDUCTION

how much should the RRP capping be relatively reduced when the product is on sale?

0.05

UNHEALTHY_INVENTORY_REDUCTION

how much should the price be reduced at least if the pricing didn't work due to a mistakenly price increase?

0

UNCRITICAL_UNHEALTHY_BUCKETS

for which unhealthy inventory buckets do we allow a higher min price as a soft entry into unhealthy inventory reduction?

['Lowest_Merchant', 'Lowest_Merchant_Markdown']

BUFFER_TO_LOWEST_COMPETITOR_OFFER

how much should our offer be more expensive than lowest competitor offer?

1

ROUNDING

MIN_THRESHOLD_ROUNDING

how many euros can the product cost at most until we apply rounding?

0.5 EUR

CEIL_THRESHOLD_ROUNDING

how many euros can the product cost at most until we don't round up or down, but always up?

199.99 EUR

DECIMAL_MASK_ROUNDING

how should the decimal part of a price in EUR look like to look pretty?

0.9 EUR

PRICE_THRESHOLD_STORE_CAPPING

if the product costs less than this parameter in EUR we apply store capping

100 EUR

STORE CHECKS

PRICE_INCREASE_THRESHOLD_STORE_CAPPING

how much can the price increase be at least in EUR until we we ignore store capping?

4 EUR

PRICE_REDUCTION_THRESHOLD_STORE_CAPPING

how much can the price reduction be at least in EUR until we we ignore store capping?

4 days

PRICE_CHANGE_INTERVAL_STORE_CAPPING

how many days do we require to pass since the last price change until we change price of a store affected product?

7 days

SUSPICIOUS RECOMMENDATIONS

SUSPICIOUS_PRICE_TREND

how much lower can the recommended price be compared to the average of the last week? maximal relative threshold of a price change compared to average price of the last week until we send an alert to CM. A value of 0.4 means that new price can only be 40% smaller than original value.

0.4 fraction

SUSPICIOUS_MARGIN_THRESHOLD

how much price profit margin do we allow at most until we treat a price as suspicious?

0 fraction

SUSPICIOUS_PURCHASE_PRICE_TREND

how much lower can the recommended price be compared to the average of the last week until we treat the recommended price as suspicious?

0.4 fraction

