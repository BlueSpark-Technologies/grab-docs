# PS Data Model

## PS Data Base Contents
For more info on each fields see section below.

| Table name | Field | Data type | Description | Source field |
|---|---|---|---|---|
| base_price_calculation | id | string | primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one price calculation (attempt). Thus there can be multiple ids for the same product. | internal |
| sku | string | the sku of the product | - |
| selected_stream | string | the stream which was selected for the price calculation using the stream selection algorithm from here Base Price Algorithm: Stream Selection | internal |
| recommended_price_listed_gross | int | is the unchecked recommended price calculated by the Pricing Service using the selected_stream Base Price Algorithm: Pricing Streams in cents | internal |
| checked_recommended_price_listed_gross | int | is the recommended price after the Price Check algorithm Base Price Algorithm: Price Quality Check in cents | internal |
| product_views_band | string | All products on our webshop are put in one of 6 product views bands on a scale from A to E. A contains the most clicked products on the webshop, E contains least clicked products. | see below |
| is_export_allowed | boolean | Export of product prices is only allowed if the last price was not too long ago or is very urgent. Background is that we don’t want employees in non-online Cyberport stores to have to change price too often. | internal |
| updated_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was updated. | internal |
| created_at | datetime | is the creation timestamp of the row in the data base in UTC+0. | internal |
| exported_at | datetime | is the timestamp from when the price for the sku was exported to the queue. If it is null the price was not exported (yet). Timestamp is in UTC+0 as well. | internal |
| inventory_health_strategy | string | the correct inventory_health_strategy is the strategy that should be applied to a product if it is unhealthy. (For calculation details, see below). We use this field also as an indicator if the product currently is unhealthy, which is the case if the strategy is not “Regular”. We need the history of this field within PS to see if our pricing methods have changed the unhealthy status of a product and if so how much. | see below |
| current_price_listed_gross | int | see below | internal |
| category_manager | string | see below | see below |
| shipping_class | string | see below | see below |
| shipping_group | string | see below | see below |
| lowest_competitor_price_landed_gross | int | see below | internal |
| vat_rate | float | see below | see below |
| product_description | string | see below | see below |
| purchase_price_listed_net | int | see below | see below |
| is_price_suspicious | boolean | see below | internal |
| reason_is_price_suspicious | string | see below | internal |
| avg_purchase_price_listed_net | int | see below | internal |
| avg_current_price_listed_gross | int | see below | internal |
| merchant_offers_verbose | text | see below | internal |
| lowest_competitor_price_listed_gross | int | the lowest price in a list of relevant competitors | internal |
| product_id | string | foreign key, id of the product in product table, represented using UUID | internal |
| is_auto_pricing_activated | boolean | This flag is configured in Cyberparts to allow automatic price imports for a product | before release PS-4.0.0 - DIS - has_auto_price field after release PS-4.0.0 - ECS - is_auto_pricing_activated field |
|  |  |  |  |  |
| product | id | string | primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one product. | internal |
| sku | string | product sku | - |
| manual_base_price_listed_gross | int | manual base price in cents set by the CMs in the Pricing Cockpit to overwrite the automatic base price. | ECS → /v0/pricing-cockpit/product-manual-pricing/[product_sku]/?channels__campaigns__isnull=false → manual_base_price |
| current_base_price_listed_gross | int | This is the latest base price in cents that was exported by Pricing Service for a product. This could be either the automatic base price calculation which was exported OR a manual price from ECS which was exported. | currently: DIS → /api/v2/product/[product-sku]/price → base_pricefuture: internal |
| markup_pct | float | This value is the average profit markup on top of the gross listed internal costs compared tot he gross retail price of products that are similar in category and / or price level and have competitors. This value is used to calculate prices for products, that don’t have competitor offers and thus a market level to orient prices on. See Stream: No Merchants Pricing for more details. It can take values between 0 and 1, a value of 0.3 means that 30% needs to be added to the internal costs (vat + purchasing) to obtain a price. | currently: DHS → bpsorch.v_ps_markup_pct(in the past: from Exasol PROD_DS.V_PS_MARKUP_PCT → MARKUP_PCT) |
| created_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was created. | internal |
| updated_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was updated. | internal |
| selling_unit | string | The measuring unit of the package e.g. kg, l, m etc. | DIS → /api/v2/product/[product_sku]/product-info |
| selling_unit_factor | float | Mandatory determination of the price per kg or l. If a product is sold by a selling unit, this field describes the factor of the unit at which the product is sold. I.e. a selling_unit_factor value of 0.4 for a selling_unit='kg' means, that the product is sold in 400g packages. | DIS → /api/v2/product/[product_sku]/product-info |
| exported_at | datetime | This field contains the UTC+0 timestamp of when the product data has been exported to SAP Pro. It is only applies for manual prices. | internal |
| vat_rate | decimal | This field contains the vat rate used to calculate the net prices for a product. | DIS → /api/v2/product/[product_sku]/product-info |
|  |  |  |  |  |
| channel_price | id | string | primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one channel and product combination. | internal |
| product_id | string | the id of the product in the product table, foreign key | internal |
| sales_channel_code | string | Most tenants not only sell merchandise on their webshop but also on marketplaces, stores or in special B2B shops. Each of these are called a (sales) channels and each channel has a short name or a channel code to identify it across services. | ECS |
| manual_channel_price_listed_gross | decimal | This is the manual channel price in cents added manually by a CM via a possibly temporary price campaign in the ECS Pricing Cockpit. There can only be once manual channel price at a time that is valid even though there might be future price campaigns already planned by the CMs in the Cockpit. ECS sends us the currently active one, if there is any. This manual_channel_price_listed_gross overwrites the internal default_channel_price_listed_gross suggested by the Pricing Service and an optional external_channel_price_listed_gross provided by third party pricing add-ons like the Marketplace Service. | ECS |
| default_channel_price_listed_gross | decimal | The Pricing Service uses price calculation formulas provided by CMs in the Channel Strategies UI of the E-commerce Cloud (EC) to calculated default prices in cents for the case that neither a manual channel price is provided in the Pricing Cockpit nor an external price system provides a price for a channel and a product. Sometimes you might hear people refer to this price as “channel autopricing price”, “standard channel price” or similar. This default_channel_price_listed_gross is only exported to the subscribing IT systems whenever it changes and if neither a manual nor an external channel price (manual_channel_price_listed_gross and external_channel_price_listed_gross) are available. | internal |
| external_channel_price_listed_gross | decimal | The Pricing Service supports the addition of external price sources for selected channels that can overwrite the simple channel pricing supported in the Channel Strategies UI in the E-commerce Cloud (EC). One example is the Marketplace Service (MS) which supports a live Amazon Pricing based on real-time competitor data provided by Amazon itself. For channels like this we import an external_channel_price_listed_gross in cents into the Pricing Service and prefer this over the default_channel_price_listed_gross. It is only exported when no manual_channel_price_listed_gross exists. For some channels the price in cents which comes from an external shop eg. Amazon marketplace | MS → api/v1/products/[product_sku]/price → new_price |
| operation_id | string | id of the channel price calculation, represented using UUID | internal |
| created_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was created. | internal |
| updated_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was updated. | internal |
| exported_at | datetime | This field contains the UTC+0 timestamp of when the product data has been exported to SAP Pro. | internal |
| channel_strategy_formula | string | the formula used to calculate the default_channel_price_listed_gross | ECS |
|  |
| default_channel_price_calculation | id | string | primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one product. | internal |
| sku | string | product sku from product table | - |
| sales_channel_code | string | see channel_price db table above | ECS |
| product_description | string | see below | see below |
| default_channel_price_listed_gross | string | see channel_price db table above | see above |
| channel_strategy_formula | string | see channel_price db table above | see above |
| price_per_unit_listed_gross |  | see channel_price db table above | see above |
| selling_unit | string | see product db table above | see above |
| selling_unit_factor | float | see product db table above | see above |
| vat_rate | float | see channel_price below | see below |
| free_quantity_central_warehouse | integer | can be part of the formula, computed from quantity and reservedQuantity, both values coming from DIS | DIS |
| purchase_price_listed_net | float | see channel_price below | see below |
| average_purchase_price_listed_net | float | see channel_price below | see below |
| standard_purchase_price_listed_net | float | see channel_price below | see below |
| decision_purchase_price_listed_net | float | see channel_price below | see below |
| base_price_listed_gross | float |  |  |
| lowest_competitor_offer | float | see channel_price below | see below |
| recommended_retail_price | float | see channel_price below | see below |
| shipping_cost | float | see channel_price below | see below |
| created_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was created. | internal |
| exported_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was updated. | internal |
| is_export_allowed | boolean | weather the channel price can be exported or not. Only the channels which are part of the EXPORTABLE_CHANNEL_CODES list can be exported. EXPORTABLE_CHANNEL_CODES is an env variable set in AWS Secrets | internal |
| channel_price_id | string | foreign key, points to the channel_price id | internal |

Table name

Field

Data type

Description

Source field

base_price_calculation

id

string

primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one price calculation (attempt). Thus there can be multiple ids for the same product.

internal

sku

string

the sku of the product

-

selected_stream

string

the stream which was selected for the price calculation using the stream selection algorithm from here Base Price Algorithm: Stream Selection

internal

recommended_price_listed_gross

int

is the unchecked recommended price calculated by the Pricing Service using the selected_stream Base Price Algorithm: Pricing Streams in cents

internal

checked_recommended_price_listed_gross

int

is the recommended price after the Price Check algorithm Base Price Algorithm: Price Quality Check in cents

internal

product_views_band

string

All products on our webshop are put in one of 6 product views bands on a scale from A to E. A contains the most clicked products on the webshop, E contains least clicked products.

see below

is_export_allowed

boolean

Export of product prices is only allowed if the last price was not too long ago or is very urgent. Background is that we don’t want employees in non-online Cyberport stores to have to change price too often.

internal

updated_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was updated.

internal

created_at

datetime

is the creation timestamp of the row in the data base in UTC+0.

internal

exported_at

datetime

is the timestamp from when the price for the sku was exported to the queue. If it is null the price was not exported (yet). Timestamp is in UTC+0 as well.

internal

inventory_health_strategy

string

the correct inventory_health_strategy is the strategy that should be applied to a product if it is unhealthy. (For calculation details, see below). We use this field also as an indicator if the product currently is unhealthy, which is the case if the strategy is not “Regular”. We need the history of this field within PS to see if our pricing methods have changed the unhealthy status of a product and if so how much.

see below

current_price_listed_gross

int

see below

internal

category_manager

string

see below

see below

shipping_class

string

see below

see below

shipping_group

string

see below

see below

lowest_competitor_price_landed_gross

int

see below

internal

vat_rate

float

see below

see below

product_description

string

see below

see below

purchase_price_listed_net

int

see below

see below

is_price_suspicious

boolean

see below

internal

reason_is_price_suspicious

string

see below

internal

avg_purchase_price_listed_net

int

see below

internal

avg_current_price_listed_gross

int

see below

internal

merchant_offers_verbose

text

see below

internal

lowest_competitor_price_listed_gross

int

the lowest price in a list of relevant competitors

internal

product_id

string

foreign key, id of the product in product table, represented using UUID

internal

is_auto_pricing_activated

boolean

This flag is configured in Cyberparts to allow automatic price imports for a product

before release PS-4.0.0 - DIS - has_auto_price field

after release PS-4.0.0 - ECS - is_auto_pricing_activated field

product

id

string

primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one product.

internal

sku

string

product sku

-

manual_base_price_listed_gross

int

manual base price in cents set by the CMs in the Pricing Cockpit to overwrite the automatic base price.

ECS → /v0/pricing-cockpit/product-manual-pricing/[product_sku]/?channels__campaigns__isnull=false → manual_base_price

current_base_price_listed_gross

int

This is the latest base price in cents that was exported by Pricing Service for a product. This could be either the automatic base price calculation which was exported OR a manual price from ECS which was exported.

currently: DIS → /api/v2/product/[product-sku]/price → base_price

future: internal

markup_pct

float

This value is the average profit markup on top of the gross listed internal costs compared tot he gross retail price of products that are similar in category and / or price level and have competitors. This value is used to calculate prices for products, that don’t have competitor offers and thus a market level to orient prices on. See Stream: No Merchants Pricing for more details. It can take values between 0 and 1, a value of 0.3 means that 30% needs to be added to the internal costs (vat + purchasing) to obtain a price.

currently: DHS → bpsorch.v_ps_markup_pct(in the past: from Exasol PROD_DS.V_PS_MARKUP_PCT → MARKUP_PCT)

created_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was created.

internal

updated_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was updated.

internal

selling_unit

string

The measuring unit of the package e.g. kg, l, m etc.

DIS → /api/v2/product/[product_sku]/product-info

selling_unit_factor

float

Mandatory determination of the price per kg or l. If a product is sold by a selling unit, this field describes the factor of the unit at which the product is sold. I.e. a selling_unit_factor value of 0.4 for a selling_unit='kg' means, that the product is sold in 400g packages.

DIS → /api/v2/product/[product_sku]/product-info

exported_at

datetime

This field contains the UTC+0 timestamp of when the product data has been exported to SAP Pro. It is only applies for manual prices.

internal

vat_rate

decimal

This field contains the vat rate used to calculate the net prices for a product.

DIS → /api/v2/product/[product_sku]/product-info

channel_price

id

string

primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one channel and product combination.

internal

product_id

string

the id of the product in the product table, foreign key

internal

sales_channel_code

string

Most tenants not only sell merchandise on their webshop but also on marketplaces, stores or in special B2B shops. Each of these are called a (sales) channels and each channel has a short name or a channel code to identify it across services.

ECS

manual_channel_price_listed_gross

decimal

This is the manual channel price in cents added manually by a CM via a possibly temporary price campaign in the ECS Pricing Cockpit. There can only be once manual channel price at a time that is valid even though there might be future price campaigns already planned by the CMs in the Cockpit. ECS sends us the currently active one, if there is any. This manual_channel_price_listed_gross overwrites the internal default_channel_price_listed_gross suggested by the Pricing Service and an optional external_channel_price_listed_gross provided by third party pricing add-ons like the Marketplace Service.

ECS

default_channel_price_listed_gross

decimal

The Pricing Service uses price calculation formulas provided by CMs in the Channel Strategies UI of the E-commerce Cloud (EC) to calculated default prices in cents for the case that neither a manual channel price is provided in the Pricing Cockpit nor an external price system provides a price for a channel and a product. Sometimes you might hear people refer to this price as “channel autopricing price”, “standard channel price” or similar. This default_channel_price_listed_gross is only exported to the subscribing IT systems whenever it changes and if neither a manual nor an external channel price (manual_channel_price_listed_gross and external_channel_price_listed_gross) are available.

internal

external_channel_price_listed_gross

decimal

The Pricing Service supports the addition of external price sources for selected channels that can overwrite the simple channel pricing supported in the Channel Strategies UI in the E-commerce Cloud (EC). One example is the Marketplace Service (MS) which supports a live Amazon Pricing based on real-time competitor data provided by Amazon itself. For channels like this we import an external_channel_price_listed_gross in cents into the Pricing Service and prefer this over the default_channel_price_listed_gross. It is only exported when no manual_channel_price_listed_gross exists.

For some channels the price in cents which comes from an external shop eg. Amazon marketplace

MS → api/v1/products/[product_sku]/price → new_price

operation_id

string

id of the channel price calculation, represented using UUID

internal

created_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was created.

internal

updated_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was updated.

internal

exported_at

datetime

This field contains the UTC+0 timestamp of when the product data has been exported to SAP Pro.

internal

channel_strategy_formula

string

the formula used to calculate the default_channel_price_listed_gross

ECS

default_channel_price_calculation

id

string

primary key, represented using UUID (see https://starkandwayne.com/blog/uuid-primary-keys-in-postgresql/ ). One id represents exactly one product.

internal

sku

string

product sku from product table

-

sales_channel_code

string

see channel_price db table above

ECS

product_description

string

see below

see below

default_channel_price_listed_gross

string

see channel_price db table above

see above

channel_strategy_formula

string

see channel_price db table above

see above

price_per_unit_listed_gross

see channel_price db table above

see above

selling_unit

string

see product db table above

see above

selling_unit_factor

float

see product db table above

see above

vat_rate

float

see channel_price below

see below

free_quantity_central_warehouse

integer

can be part of the formula, computed from quantity and reservedQuantity, both values coming from DIS

DIS

purchase_price_listed_net

float

see channel_price below

see below

average_purchase_price_listed_net

float

see channel_price below

see below

standard_purchase_price_listed_net

float

see channel_price below

see below

decision_purchase_price_listed_net

float

see channel_price below

see below

base_price_listed_gross

float

lowest_competitor_offer

float

see channel_price below

see below

recommended_retail_price

float

see channel_price below

see below

shipping_cost

float

see channel_price below

see below

created_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was created.

internal

exported_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was updated.

internal

is_export_allowed

boolean

weather the channel price can be exported or not. Only the channels which are part of the EXPORTABLE_CHANNEL_CODES list can be exported. EXPORTABLE_CHANNEL_CODES is an env variable set in AWS Secrets

internal

channel_price_id

string

foreign key, points to the channel_price id

internal

## DHS Pricing Data Model
Documentation for historic data that is stored in Data Historization Service can also be found here DHS Data Model.

| Table name | Field | Data Type | Description | Source of field |
|---|---|---|---|---|
| all tables | operation_id | uuid | primary key that uniquely identifies one price calculation (attempt), represented using UUID. This is the same id as the one used in PS data base base_price_calculation table. | internal |
| base_price_input_data | article_group | string | Every SKU has exactly an article_group, it is one level above the SKU itself in the hierarchy tree. One article_group belongs to exactly one cat_lvl_3 and has usually multiple products in it. | ECOMM → /v0/product-pricing-configurations/{sku}/ → Article Group |
| base_price_input_data | assortment_status | string | The listing status of this product, can take values EOL, ACTIVE, INACTIVE | DIS → /v2/product/{sku}/product-info → status |
| base_price_input_data | average_purchase_price_listed_net | decimal | current inventory purchase price is based on the past purchase costs in EUR per unit in the stock (how much did we pay for the stock we have in average). But careful, this can be different to the actual price we have to way if we want to reorder the product today. | DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → averagePurchasePrice |
| base_price_input_data | b_stock_abs_devaluation_gross | decimal | This is the EUR amount the b-stock product is worth less than the parent product. | DIS → /v2/product-b-stock/{sku} → abs_devaluation |
| base_price_input_data | b_stock_parent_id | string | Every B-stock product is linked to a new version of the same product. This is the SKU of that parent product. | DIS → /v2/product-b-stock/{sku} → parent_id |
| base_price_input_data | b_stock_parent_price_listed_gross | decimal | This is the price of the b-stock parent product. E.g. how much would the current product cost if it was new. Note: to get the newest parent price we request it from the price endpoint, using the parent_id as the sku | DIS → /v2/product/{parent_id}/price → price |
| base_price_input_data | bto_markup_in_stock | decimal | If a product is selected for BTO pricing and it has free stock left in any stock_id this is the markup that should be used added to the gross purchase_price_listed_net plus VAT. | ECOMM → /v0/product-pricing-configurations/{sku}/ → bto_markup_in_stock |
| base_price_input_data | bto_markup_no_stock | decimal | If a product is selected for BTO pricing and it has no free stock left in any stock_id this is the markup that should be used added to the gross purchase_price_listed_net plus VAT. | ECOMM → /v0/product-pricing-configurations/{sku}/ → bto_markup_no_stock |
| base_price_input_data | cat_lvl_3 | string | Every SKU has exactly an cat_lvl_3, it is two levels above the sku itself in the hierarchy tree and is the highest level below global which just contains all products. One cat_lvl_3 usually has multiple article_groups and products in it. | ECOMM → /v0/product-pricing-configurations/{sku}/ → Cat Lvl 3 |
| base_price_input_data | category_manager | string | The name of the category manager who is responsible for a product | DIS → api/v2/item/[product-sku]/info→ category_manager |
| base_price_input_data | cbp_end_date | date | see cbp_target_quantity | ECOMM → /v0/product-pricing-configurations/{sku}/ → end_date |
| base_price_input_data | cbp_start_date | date | see cbp_target_quantity | ECOMM → /v0/product-pricing-configurations/{sku}/ → start_date |
| base_price_input_data | cbp_target_quantity | integer | In the Coverage Based Pricing method you can define a target_quantity, eg. amount of units you want to sell within time frame cbp_start_date and cbp_end_date. The autopricing will try to find prices to achieve this. | ECOMM → /v0/product-pricing-configurations/{sku}/ → target_quantity |
| base_price_input_data | current_base_price_listed_gross | decimal | current base price without shipping of the product in EUR | DIS → /api/v2/product/{sku}/price → base_price |
| base_price_input_data | current_webshop_price_listed_gross | decimal | current webshop price without shipping of the product in EUR | DIS → /api/v2/product/{sku}/price → price |
| base_price_input_data | description | string | Human readable product description as displayed on the webshop from Data Integr. Service | DIS → /v2/product/{sku}/product-info → name |
| base_price_input_data | end_exclusion_at | datetime | This is the timestamp in UTC+0 until which on the product should not be priced with the autopricing. If it is null it means, it will be excluded indefinitely. | ECOMM → /v0/product-pricing-configurations/{sku}/ → end_exclustion_at |
| base_price_input_data | exclusion_reason | string | This string is an explanation that a CM can set when adding a product or an article group or a category level 3 to the exclusion list in the Pricing UI | ECOMM → /v0/product-pricing-configurations/{sku}/ → exclusion_reason |
| base_price_input_data | inventory_health_bucket | string | The classification of products in the Unhealthy Inventory scheme is based on the combination of the weighted duration of the inventory (aging) and the range of the inventory quantity predicted from previous sales figures until it is sold (coverage). These two metrics are used to categorize products every day into so called inventory health buckets. Where A0, A1, A2, A3, A4 stand for aging classes (lower number means younger aging) and C0, C1, C2, C3, C4 stand for coverage classes (lower number means shorter coverage and is therefore better). Thus A0-C0 is the healthiest and A4-C4 is the unhealthiest bucket.See Inventory Health Service (IHS) and Stream: Unhealthy Inventory Pricing for details. | DIS → /v2/product/{sku}/product-info → inventory_health_demand |
| base_price_input_data | inventory_health_config = list of tuples (range_min, range_max, inventory_health_bucket, inventory_health_strategy, markdown_parameter). One for each combination of range and bucket ==> currently 4 ranges * 25 buckets = 100 tuples per sku) | string | The inventory health strategy, that should be applied to a product with depending on the aging class and coverage class as configured in the E-Commerce Cloud Service. | ECOMM → /v0/product-pricing-configurations/{sku}/ → inventory_health |
| base_price_input_data | inventory_quantity_central_warehouse | integer | The amount of units with this product_id, that are available in the central warehouse | DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → quantity |
| base_price_input_data | is_auto_pricing_activated | boolean | This flag if the product is configured in Cyberparts to allow automatic price imports, meaning when the flat "DWH Import deakt." to false (yes, the logic is reversed) | DIS → /v2/product/{sku}/product-info → has_auto_price |
| base_price_input_data | is_on_exclusion_list | boolean | This flag has to be set to true, if the product is on exclusion list in Ecommerce Cloud Service. | ECOMM → /v0/product-pricing-configurations/{sku}/ → is_autopricing_excluded |
| base_price_input_data | is_rrp_enforced | boolean | This flag describes if the product is configured to be offered with the recommended retail price in the Ecommerce Cloud Service | ECOMM → /v0/product-pricing-configurations/{sku}/ → enforced_rrp |
| base_price_input_data | margin_cap | decimal | maximal profit margin that was be manually configured by CMs in the ECOMM Pricing UI.Values range (as DECIMAL(2)): 0.1 to 1 | ECOMM → /v0/product-pricing-configurations/{sku}/ → margin_cap |
| base_price_input_data | margin_floor | decimal | minimal profit margin that was be manually configured by CMs in the ECOMM Pricing UI.Values range (as DECIMAL(2)): -0.5 to 0.5 | ECOMM → /v0/product-pricing-configurations/{sku}/ → margin_floor |
| base_price_input_data | margin_floor_range = list of values | string |  | ECOMM → /v0/product-pricing-configurations/{sku}/ → margin_floor_range |
| base_price_input_data | margin_impact | decimal | Often when we sell a product we get money back from manufacturers, something like "rewards" for selling a certain number of product of course or for complying with their advertising strategy. This amount in Euro can be deduced from the original purchase price when it comes to internal costs. | DIS → we don’t know yet the data source for this field. this currently has a constant value of None until is origin is sorted out. |
| base_price_input_data | marketing_attribute | string | The marketing decision made for this product, can take values BUNDLE, NEW, SALE. If and only if a product has the marketing_attribute NEW, we price it with the stream Stream: New Products Pricing, i.e. a higher price than usual. If a product is on SALE, we know that it is promoted on the webshop, it reaches more product views and customers expect a lower price than the competitor offers. Therefore we have a lower maximal price in the price check steps described in Base Price Algorithm: Price Quality Check. | DIS → /v2/product/{sku}/product-info → marketing_attribute |
| base_price_input_data | mbp_percentile_tier | JSON | This field contains a JSON that contains the percentiles that are used to price a product in the Stream: Merchant Based Pricing according to our competitors. A percentile of value 1.0 means we aim to be the cheapest competitor, a value of 0.0 means we’re aim to have the same price as the most expensive competitor offer. There are three values: percentile tier 1 (value of index 1), percentile tier 2 (value of index 2) and percentile tier 3 (value of index 3). Which one is used for a product at a certain point in time depends on the amount of competitors. if there are less or equal than 0 (in the default configuration) merchant competitor offers, we are in Tier1 without stock and use percentile_tier_1if there are less or equal than 3 (in the default configuration) merchant competitor offers,we are in Tier1 with stock and use percentile_tier_1if there are less or equal than 6 (in the default configuration) merchant competitor offers,we are in Tier2 and use percentile_tier_2otherwise we are in Tier3 and use percentile_tier_3 | ECOMM → /v0/product-pricing-configurations/{sku}/ → percentile_tier→ value / index |
| base_price_input_data | mps_merchant_offers list of tuples (availability, price, shipping_cost , named_price) | string | A list of other competitor offer infos for this product even though they might not have it in stock right now.named_price is a easily readable string which is formatted as such:  <merchant_short_name> (<price> {'*' if availability in [1,2]} ) examples: Amzn (19.90*) - A merchant offer from Amazon Amznwith a price of 19.90 eur and stock available *Otto (20.50) A merchant offer from Otto Otto with a price of 20.50 eur  and no stock available (note missing *) | MPS /v0/merged-feed-items-details/{sku} → feed_item_merchants → price, availability, shipping_cost, merchant_short_name |
| base_price_input_data | open_purchase_order_quantity | integer | The amount of units with this product_id, that are ordered but not available yet | DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → openPurchaseOrderQuantity |
| base_price_input_data | price_relations_base_product | string | The purpose of the pricing stream Price Successor is to define a price for a product that is in some way linked or descendant to another product (for example a grey notebook that should have the same price as its black twin). This field describes the product which should be used as a reference (in this example the black product). See here for details Stream: Price Successor Pricing. | ECOMM → /v0/product-pricing-configurations/{sku}/ → base_product → code |
| base_price_input_data | price_relations_value | decimal | This is the discount that should be subtracted from the price of the base product to get the price successor price. It can be positive or negative and either a relative or absolute value. See here for details Stream: Price Successor Pricing. | ECOMM → /v0/product-pricing-configurations/{sku}/ → if value_type = “relative” then relative_valueelif value_type = “absolute” then absolute_valueelse Null |
| base_price_input_data | price_relations_value_type | string | If this field is “absolute” we add a fixed Euro positive or negative discount to the price of a base price, if it’s “relative” we substract a positive or negative percentage discount from the price of the base price. See here for details Stream: Price Successor Pricing. | ECOMM → /v0/product-pricing-configurations/{sku}/ → value_type |
| base_price_input_data | product_sku | string |  |  |
| base_price_input_data | product_type | string | This describes the kind of article we have, can take the values PHYSICAL, USED, SPARE, BUNDLE, SERVICE, DISCOUNT, INSURANCE, SHIPPING | DIS → /v2/product/{sku}/product-info → type |
| base_price_input_data | product_views_band | string | Takes values A to E. A is in the top percent of clicked products on the webshop, E contains least clicked products | DIS → /v2/product/{sku}/product-info → product_views_band |
| base_price_input_data | reserved_quantity_central_warehouse | integer | The amount of units with this product_id, that are in the central warehouse, but reserved | DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → reserved_quantity |
| base_price_input_data | rrp_listed_gross | decimal | The recommended retail price provided by the manufacturers themselves in EUR | DIS → /v2/product/{sku}/price → retail_price |
| base_price_input_data | shipping_class | string | The shipping class is part of shipping information that defines the shipping costs of a product depending on its listed price | DIS → /v2/product/{sku}/shipping → shipping_class |
| base_price_input_data | shipping_group | string | The shipping group is part of shipping information that defines the shipping costs of a product depending on its listed price | DIS → /v2/product/{sku}/shipping → shipping_group |
| base_price_input_data | standard_purchase_price_listed_net | decimal | current purchase price cost in EUR if we would decide to buy the product again today at the default supplier | DIS → /api/v2/product/{product_sku}/price → standard_purchase_price |
| base_price_input_data | start_exclusion_at | datetime | This is the timestamp in UTC+0 from which on the product should not be priced with the autopricing anymore. If everything works as planned, it should not be null. | ECOMM → /v0/product-pricing-configurations/{sku}/ → start_exclusion_at |
| base_price_input_data | stock_quantity | integer | One value of stock for each product and each stock_id. | DIS → /v2/product/{sku}/stock → quantity |
| base_price_input_data | vat_rate | decimal | current tax rate as a fraction that we have to pay after selling the product to a B2C customer | DIS → /v2/product/{sku}/product-info → vat_rate |
| base_price_input_data | date_only | date | this is a field only used for as a dynamic partitioning key (used for internal performance and storage of data in AWS Kinesis/Glue). should not be used for any business purposes | computed by AWS Kinesis based on created field |
|  |
| base_price_meta_data | avg_current_base_price_listed_gross | decimal | This is an average value of the last current_price_listed_gross value. We use this to check if the current checked_recommended_price_listed_gross seems suspicious, e.g. we suspect a data errors in fields that affected the current price calculation. Then we mark is_price_suspicious is True and send a mail to the CM. | calculated within PS |
| base_price_meta_data | avg_purchase_price_listed_net | decimal | This is an average value of the last purchase_price_listed_net values. We use this to check if the current purchase_price_listed_net seems suspicious, e.g. we suspect a data error. Then we mark is_price_suspicious is True and send a mail to the CM. | calculated within PS |
| base_price_meta_data | bundle_components | string | List of product skus which make up a bundle product (if the bundle product is a computer, the bundle components would consist of mouse, keyboard, headphones etc.) | DIS → api/v2/pricing-product-bundle-list?bundle_sku={product_sku} → bundle_components |
| base_price_meta_data | free_quantity | integer | This is the total free quantity, e.g. total_stock_quantity - reserved_quantity. | calculated within PS |
| base_price_meta_data | inventory_health_markdown_parameter | decimal | See description for field inventory_health_strategy. | calculated within PS |
| base_price_meta_data | inventory_health_strategy | string | The correct inventory_health_strategy for a product is calculated as: Filter elements in list inventory_health_config for 5-tuples that have the correct range range_min < current_price <= range_max → 25 items remainingFilter elements in list to fit for the current inventory_health_bucket (filter list such that inventory_health_config->inventory_health_bucket = inventory_health_bucket from DIS) → 1 item remainingNow we should have exactly one entry and one value for inventory_health_strategy and in some cases a non-null markdown_parameter, which we shall rename to inventory_health_markdown_parameter. | calculated within PS |
| base_price_meta_data | is_export_allowed | boolean | On some occasions we don’t allow exports, eg. when stores would have to manually change price tags but the last update was less than 7 days ago. | calculated within PS |
| base_price_meta_data | is_store_affected | boolean | If a product is available in a store in which there is no digital price tag (ePop), the product is considered is_store_affected = True. That means that we don't want to annoy our employees at the stores by forcing them to have to replace price tags on the shelves all the time. Therefore we have to check if the previous price change was less than a certain time ago and only update then (currently once a week). | calculated within PS |
| base_price_meta_data | last_pricing_stream | string | the pricing selected_stream of the previous successful base price calculation | calculated within PS |
| base_price_meta_data | last_unhealthy_cont_markdown_export | date | The time of the last continuous markdown price export from Pricing Service for this product using unhealthy inventory stream | calculated within PS |
| base_price_meta_data | lowest_competitor_price_listed_gross | decimal | This is the lowest listed competitor offer in EUR that is available in the Market Price Screening Service for this product. Availability doesn't matter here. | calculated within PS |
| base_price_meta_data | lowest_competitor_price_with_stock_listed_gross | decimal | This lowest relevant competitor offer from Market Price Screening, more specifically it is the minimum value of merchant_offers_with_stock. | calculated within PS |
| base_price_meta_data | lowest_competitor_price_landed_gross | decimal | This lowest relevant competitor offer including shipping_costs from Market Price Screening, more specifically it is the minimum value of landed_merchant_offers_without_stock. | calculated within PS |
| base_price_meta_data | lowest_competitor_price_with_stock_landed_gross | decimal | This lowest relevant competitor offer including shipping_costs from Market Price Screening ignoring stock availabilites, more specifically it is the minimum value of landed_merchant_offers_with_stock. | calculated within PS |
| base_price_meta_data | max_price_listed_gross | decimal | This is round(purchase_price_listed_net / (1 - min(margin_cap, 0.99)) * (1 + vat_rate), 2) unless null values prevent this calculation from happening. | calculated within PS |
| base_price_meta_data | min_price_listed_gross | decimal | This is round(purchase_price_listed_net / (1 - min(margin_floor, 0.99)) * (1 + vat_rate), 2) unless null values prevent this calculation from happening. | calculated within PS |
| base_price_meta_data | markup_pct | decimal | The target margin extracted by taking the average margin of similar products that we offer as a fraction of the internal costs | calculated in DHS based on base_price_input_data and base_price_calculation table data in v_ps_markup_pct |
| base_price_meta_data | merchant_offers_with_stock_listed_gross | string | This is a field derived from mps_merchant_offers, it contains a list of competitor prices without shipping_costs from offers that have the unit in stock (availability = 2). | calculated within PS |
| base_price_meta_data | merchant_offers_without_stock_listed_gross | string | This is a field derived from mps_merchant_offers, it contains a list of competitor prices without shipping_costs from all offers regardless of availability. | calculated within PS |
| base_price_meta_data | merchant_offers_without_stock_landed_gross | string | This is a field derived from mps_merchant_offers, it contains a list of competitor prices including shipping_costs from all offers that have the unit in stock (availability = 2). | calculated within PS |
| base_price_meta_data | merchant_offers_without_stock_landed_gross | string | This is a field derived from mps_merchant_offers, it contains a list of competitor prices including shipping_costs from all offers regardless of availability. | calculated within PS |
| base_price_meta_data | merchant_offers_verbose | string | This is a field derived from mps_merchant_offers,  it’s just a concatenation of all named_price values, comma separated. When the offer is available for the customer to buy at the merchant’s site, the offer gets an asterisk attached to it. example: Amzn (19.90*), Otto (20.50), PCKing(22.30*) | calculated within PS |
| base_price_meta_data | product_sku | string |  | - |
| base_price_meta_data | purchase_price_listed_net | decimal | The processed purchase costs from the Integration Service in EUR. The logic is the following. If both avg_purchase_price_listed_net and standard_purchase_price are null → assume nullElse if none are null and non-zero → we take the minimum of bothElse if avg_purchase_price_listed_net is non-null and non-zero → avg_purchase_price_listed_netElse if standard_purchase_price_listed_net is non-null and non-zero → standard_purchase_price_listed_netIf we have margin_impact data we subtract this from the interim results before returning the purchase_price_listed_net.More info can be found here https://cyber-solutions.atlassian.net/wiki/spaces/IS/pages/2260729857/DIS+purchase+price+calculation. | DIS → /api/v2/product/{product_sku}/price → purchase_price |
| base_price_meta_data | reason_price | string | This a string that describes why was the current price chosen, e.g. which part of the algorithm lead to the current recommended_price_listed_gross. | calculated within PS |
| base_price_meta_data | reason_price_check | string | This a string that describes which price checks were passed and which cappings were applied before returning checked_recommended_price_listed_gross. | calculated within PS |
| base_price_meta_data | reason_stream | string | This a string that describes why the current autopricing selected_stream chosen. | calculated within PS |
| base_price_meta_data | timestamp_last_export | datetime | When was the last successful price export for this product? | calculated within PS |
| base_price_meta_data | total_free_quantity | integer | This is the total free quantity, e.g. stock_quantity - reserved_quantity aggregated over all stock_ids sent by DIS stock. | calculated within PS |
| base_price_meta_data | total_stock_quantity | integer | This is the stock_quantity aggregated over all stock_ids sent by DIS stock. | calculated within PS |
| base_price_meta_data | trigger_reason | string | what changed field / which service triggered the repricing withing the Pricing Service | calculated within PS |
| base_price_meta_data | date_only | date | this is a field only used for as a dynamic partitioning key (used for internal performance and storage of data in AWS Kinesis/Glue). should not be used for any business purposes | computed by AWS Kinesis based on created field |
| base_price_meta_data | exported_at | datetime | This is the creation timestamp of the row in the data base in UTC+0. | calculated within PS |
|  |
| base_price_calculation | category_manager | string | Category manager name to which the product belongs. | DIS → api/v2/item/[product-sku]/info → category_manager |
| base_price_calculation | checked_recommended_price_listed_gross | decimal | This is the recommended price after the Base Price Algorithm: Price Quality Check was executed. | calculated within PS |
| base_price_calculation | created_at | datetime | timestamp at which the calculation was performed | calculated within PS |
| base_price_calculation | current_base_price_listed_gross | decimal | the current base price value, received by PS from DIS service, | DIS → /api/v2/product/[product-sku]/price → base_price |
| base_price_calculation | description | string | Human readable product description as displayed on the webshop from Data Integr. Service | DIS → /api/v2/product/[product-sku]/product-info → base_price |
| base_price_calculation | inventory_health_strategy | string | calculated based on the  inventory_health_config,  inventory_health_bucket | calculated within PS |
| base_price_calculation | is_price_suspicious | boolean | If a price is suspicious, the price is not exported, but only a mail is sent to the respective CM. The logic for suspicious prices can be found here Base Price Algorithm: Price Quality Check. | calculated within PS |
| base_price_calculation | lowest_competitor_price_landed_gross | decimal | This lowest relevant competitor offer including shipping_costs from Market Price Screening, more specifically it is the minimum value of landed_merchant_offers_without_stock. | calculated within PS |
| base_price_calculation | product_sku | string |  | - |
| base_price_calculation | product_views_band | string | Takes values A to E. A is in the top percent of clicked products on the webshop, E contains least clicked products | DIS → /api/v2/product/[product-sku]/product-info → product_views_band |
| base_price_calculation | purchase_price_listed_net | decimal |  | DIS → /api/v2/product/[product-sku]/price → purchase_price |
| base_price_calculation | reason_is_price_suspicious | string | This is a string that explains what exactly made this product suspicious (is_price_suspicious is True), if it is. | calculated within PS |
| base_price_calculation | recommended_price_listed_gross | decimal | This price is the unchecked recommended price calculated by the Pricing Service using the selected_stream Base Price Algorithm: Pricing Streams before Base Price Algorithm: Price Quality Check have been executed. | calculated within PS |
| base_price_calculation | selected_stream | string | The stream which was selected for the price calculation using the stream selection algorithm from here Base Price Algorithm: Stream Selection | calculated within PS |
| base_price_calculation | shipping_class | string |  |  |
| base_price_calculation | shipping_group | string |  |  |
| base_price_calculation | updated_at | datetime | This field contains the UTC+0 timestamp of when the row in the data base was updated. | calculated within PS |
| base_price_calculation | vat_rate | decimal | current tax rate as a fraction that we have to pay after selling the product to a B2C customer | DIS → /v2/product/{sku}/product-info → vat_rate |
| base_price_calculation | date_only | date | this is a field only used for as a dynamic partitioning key (used for internal performance and storage of data in AWS Kinesis/Glue). should not be used for any business purposes | computed by AWS Kinesis based on created field |
| base_price_calculation | exported_at | datetime | This is the timestamp from when the price for the sku was exported to the queue. If it is null the price was not exported (yet). Timestamp is in UTC+0 as well. | calculated within PS |
|  |
| channel_price | channel_price_id | string | foreign key to channel_price table in PS data base |  |
| channel_price | product_id | string | foreign key to product table in PS data base |  |
| channel_price | sku | string | the sku of the product |  |
| channel_price | sales_channel_code | string | see channel_price db table above |  |
| channel_price | manual_channel_price_listed_gross | decimal | see channel_price db table above |  |
| channel_price | default_channel_price_listed_gross | decimal | see channel_price db table above |  |
| channel_price | external_channel_price_listed_gross | decimal | see channel_price db table above |  |
| channel_price | price_per_unit_listed_gross | decimal | see channel_price db table above |  |
| channel_price | created_at | datetime | see channel_price db table above |  |
| channel_price | updated_at | datetime | see channel_price db table above |  |
| channel_price | exported_at | datetime | see channel_price db table above |  |
| channel_price | channel_strategy_name | string |  |  |
| channel_price | channel_strategy_formula | string | the formula used to calculate the default_channel_price_listed_gross |  |
| channel_price | selling_unit | string | see product db table above |  |
| channel_price | selling_unit_factor | decimal | see product db table above |  |
| channel_price | vat_rate | decimal | can be part of the formula |  |
| channel_price | decision_purchase_price_listed_net | decimal | can be part of the formula.The decision purchase price in EUR contains the net standard purchase price minus sell-in and sell-out backend discount conditions that reduce the effective costs of a product to a value lower than the listed standard purchase price. The price itself is specific per supplier, thus we operate on the chosen default standard supplier. If the standard supplier, their selling price or their backend conditions changes, so will the value of this price. It's called decision purchase price, because it's a more realistic portrayal of the operative costs than the standard_supplier_price. |  |
| channel_price | standard_purchase_price_listed_net | decimal | can be part of the formula |  |
| channel_price | average_purchase_price_listed_net | decimal | can be part of the formula |  |
| channel_price | purchase_price_listed_net | decimal | can be part of the formula |  |
| channel_price | recommended_retail_price_listed_gross | decimal | can be part of the formula |  |
| channel_price | shipping_costs | decimal | can be part of the formula |  |
| channel_price | lowest_competitor_offer_listed_gross | decimal | can be part of the formula |  |
| channel_price | reason_channel_price_trigger | string | a message that contains what changed fields triggered the repricing |  |
| channel_price | currency | string | EUR as a constant for now |  |
| channel_price | channel_prices | array | TBD ? |  |
|  |
| base_price_meta_data | is_coverage_based_pricing | boolean | This flag describes if the product is configured to be price within Coverage Based Pricing in the Ecommerce Cloud Service | calculated within PS |
| base_price_meta_data | has_unhealthy_inventory | boolean | A product is unhealthy if all the following conditions are trueif inventory_health_strategy is available and not ‘Regular’ andif assortment_status != ‘ACTIVE’ or (product_views_band = 'A' and free_quantity_central_warehouse > 5) or(product_views_band = 'B' and free_quantity_central_warehouse > 3) or(product_views_band = 'C' and free_quantity_central_warehouse > 2) or(free_quantity_central_warehouse > 1) | calculated within PS |
| base_price_calculation | is_price_successor | boolean | This flag describes if the product is configured as a price successor of another product in the Ecommerce Cloud Service | calculated within PS |

Table name

Field

Data Type

Description

Source of field

all tables

operation_id

uuid

primary key that uniquely identifies one price calculation (attempt), represented using UUID. This is the same id as the one used in PS data base base_price_calculation table.

internal

base_price_input_data

article_group

string

Every SKU has exactly an article_group, it is one level above the SKU itself in the hierarchy tree. One article_group belongs to exactly one cat_lvl_3 and has usually multiple products in it.

ECOMM → /v0/product-pricing-configurations/{sku}/ → Article Group

base_price_input_data

assortment_status

string

The listing status of this product, can take values EOL, ACTIVE, INACTIVE

DIS → /v2/product/{sku}/product-info → status

base_price_input_data

average_purchase_price_listed_net

decimal

current inventory purchase price is based on the past purchase costs in EUR per unit in the stock (how much did we pay for the stock we have in average). But careful, this can be different to the actual price we have to way if we want to reorder the product today.

DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → averagePurchasePrice

base_price_input_data

b_stock_abs_devaluation_gross

decimal

This is the EUR amount the b-stock product is worth less than the parent product.

DIS → /v2/product-b-stock/{sku} → abs_devaluation

base_price_input_data

b_stock_parent_id

string

Every B-stock product is linked to a new version of the same product. This is the SKU of that parent product.

DIS → /v2/product-b-stock/{sku} → parent_id

base_price_input_data

b_stock_parent_price_listed_gross

decimal

This is the price of the b-stock parent product. E.g. how much would the current product cost if it was new. Note: to get the newest parent price we request it from the price endpoint, using the parent_id as the sku

DIS → /v2/product/{parent_id}/price → price

base_price_input_data

bto_markup_in_stock

decimal

If a product is selected for BTO pricing and it has free stock left in any stock_id this is the markup that should be used added to the gross purchase_price_listed_net plus VAT.

ECOMM → /v0/product-pricing-configurations/{sku}/ → bto_markup_in_stock

base_price_input_data

bto_markup_no_stock

decimal

If a product is selected for BTO pricing and it has no free stock left in any stock_id this is the markup that should be used added to the gross purchase_price_listed_net plus VAT.

ECOMM → /v0/product-pricing-configurations/{sku}/ → bto_markup_no_stock

base_price_input_data

cat_lvl_3

string

Every SKU has exactly an cat_lvl_3, it is two levels above the sku itself in the hierarchy tree and is the highest level below global which just contains all products. One cat_lvl_3 usually has multiple article_groups and products in it.

ECOMM → /v0/product-pricing-configurations/{sku}/ → Cat Lvl 3

base_price_input_data

category_manager

string

The name of the category manager who is responsible for a product

DIS → api/v2/item/[product-sku]/info→ category_manager

base_price_input_data

cbp_end_date

date

see cbp_target_quantity

ECOMM → /v0/product-pricing-configurations/{sku}/ → end_date

base_price_input_data

cbp_start_date

date

see cbp_target_quantity

ECOMM → /v0/product-pricing-configurations/{sku}/ → start_date

base_price_input_data

cbp_target_quantity

integer

In the Coverage Based Pricing method you can define a target_quantity, eg. amount of units you want to sell within time frame cbp_start_date and cbp_end_date. The autopricing will try to find prices to achieve this.

ECOMM → /v0/product-pricing-configurations/{sku}/ → target_quantity

base_price_input_data

current_base_price_listed_gross

decimal

current base price without shipping of the product in EUR

DIS → /api/v2/product/{sku}/price → base_price

base_price_input_data

current_webshop_price_listed_gross

decimal

current webshop price without shipping of the product in EUR

DIS → /api/v2/product/{sku}/price → price

base_price_input_data

description

string

Human readable product description as displayed on the webshop from Data Integr. Service

DIS → /v2/product/{sku}/product-info → name

base_price_input_data

end_exclusion_at

datetime

This is the timestamp in UTC+0 until which on the product should not be priced with the autopricing. If it is null it means, it will be excluded indefinitely.

ECOMM → /v0/product-pricing-configurations/{sku}/ → end_exclustion_at

base_price_input_data

exclusion_reason

string

This string is an explanation that a CM can set when adding a product or an article group or a category level 3 to the exclusion list in the Pricing UI

ECOMM → /v0/product-pricing-configurations/{sku}/ → exclusion_reason

base_price_input_data

inventory_health_bucket

string

The classification of products in the Unhealthy Inventory scheme is based on the combination of the weighted duration of the inventory (aging) and the range of the inventory quantity predicted from previous sales figures until it is sold (coverage). These two metrics are used to categorize products every day into so called inventory health buckets. Where A0, A1, A2, A3, A4 stand for aging classes (lower number means younger aging) and C0, C1, C2, C3, C4 stand for coverage classes (lower number means shorter coverage and is therefore better). Thus A0-C0 is the healthiest and A4-C4 is the unhealthiest bucket.

See Inventory Health Service (IHS) and Stream: Unhealthy Inventory Pricing for details.

DIS → /v2/product/{sku}/product-info → inventory_health_demand

base_price_input_data

inventory_health_config = list of tuples (range_min, range_max, inventory_health_bucket, inventory_health_strategy, markdown_parameter). One for each combination of range and bucket ==> currently 4 ranges * 25 buckets = 100 tuples per sku)

string

The inventory health strategy, that should be applied to a product with depending on the aging class and coverage class as configured in the E-Commerce Cloud Service.

ECOMM → /v0/product-pricing-configurations/{sku}/ → inventory_health

base_price_input_data

inventory_quantity_central_warehouse

integer

The amount of units with this product_id, that are available in the central warehouse

DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → quantity

base_price_input_data

is_auto_pricing_activated

boolean

This flag if the product is configured in Cyberparts to allow automatic price imports, meaning when the flat "DWH Import deakt." to false (yes, the logic is reversed)

DIS → /v2/product/{sku}/product-info → has_auto_price

base_price_input_data

is_on_exclusion_list

boolean

This flag has to be set to true, if the product is on exclusion list in Ecommerce Cloud Service.

ECOMM → /v0/product-pricing-configurations/{sku}/ → is_autopricing_excluded

base_price_input_data

is_rrp_enforced

boolean

This flag describes if the product is configured to be offered with the recommended retail price in the Ecommerce Cloud Service

ECOMM → /v0/product-pricing-configurations/{sku}/ → enforced_rrp

base_price_input_data

margin_cap

decimal

maximal profit margin that was be manually configured by CMs in the ECOMM Pricing UI.

Values range (as DECIMAL(2)): 0.1 to 1

ECOMM → /v0/product-pricing-configurations/{sku}/ → margin_cap

base_price_input_data

margin_floor

decimal

minimal profit margin that was be manually configured by CMs in the ECOMM Pricing UI.

Values range (as DECIMAL(2)): -0.5 to 0.5

ECOMM → /v0/product-pricing-configurations/{sku}/ → margin_floor

base_price_input_data

margin_floor_range = list of values

string

ECOMM → /v0/product-pricing-configurations/{sku}/ → margin_floor_range

base_price_input_data

margin_impact

decimal

Often when we sell a product we get money back from manufacturers, something like "rewards" for selling a certain number of product of course or for complying with their advertising strategy. This amount in Euro can be deduced from the original purchase price when it comes to internal costs.

DIS → we don’t know yet the data source for this field. this currently has a constant value of None until is origin is sorted out.

base_price_input_data

marketing_attribute

string

The marketing decision made for this product, can take values BUNDLE, NEW, SALE. If and only if a product has the marketing_attribute NEW, we price it with the stream Stream: New Products Pricing, i.e. a higher price than usual. If a product is on SALE, we know that it is promoted on the webshop, it reaches more product views and customers expect a lower price than the competitor offers. Therefore we have a lower maximal price in the price check steps described in Base Price Algorithm: Price Quality Check.

DIS → /v2/product/{sku}/product-info → marketing_attribute

base_price_input_data

mbp_percentile_tier

JSON

This field contains a JSON that contains the percentiles that are used to price a product in the Stream: Merchant Based Pricing according to our competitors. A percentile of value 1.0 means we aim to be the cheapest competitor, a value of 0.0 means we’re aim to have the same price as the most expensive competitor offer.

There are three values: percentile tier 1 (value of index 1), percentile tier 2 (value of index 2) and percentile tier 3 (value of index 3). Which one is used for a product at a certain point in time depends on the amount of competitors.

* if there are less or equal than 0 (in the default configuration) merchant competitor offers, we are in Tier1 without stock and use percentile_tier_1
* if there are less or equal than 3 (in the default configuration) merchant competitor offers,we are in Tier1 with stock and use percentile_tier_1
* if there are less or equal than 6 (in the default configuration) merchant competitor offers,we are in Tier2 and use percentile_tier_2
* otherwise we are in Tier3 and use percentile_tier_3

if there are less or equal than 0 (in the default configuration) merchant competitor offers, we are in Tier1 without stock and use percentile_tier_1

if there are less or equal than 3 (in the default configuration) merchant competitor offers,we are in Tier1 with stock and use percentile_tier_1

if there are less or equal than 6 (in the default configuration) merchant competitor offers,we are in Tier2 and use percentile_tier_2

otherwise we are in Tier3 and use percentile_tier_3

ECOMM → /v0/product-pricing-configurations/{sku}/ → percentile_tier→ value / index

base_price_input_data

mps_merchant_offers list of tuples (availability, price, shipping_cost , named_price)

string

A list of other competitor offer infos for this product even though they might not have it in stock right now.

named_price is a easily readable string which is formatted as such:  <merchant_short_name> (<price> {'*' if availability in [1,2]} ) examples: Amzn (19.90*) - A merchant offer from Amazon Amznwith a price of 19.90 eur and stock available *Otto (20.50) A merchant offer from Otto Otto with a price of 20.50 eur  and no stock available (note missing *)

MPS /v0/merged-feed-items-details/{sku} → feed_item_merchants → price, availability, shipping_cost, merchant_short_name

base_price_input_data

open_purchase_order_quantity

integer

The amount of units with this product_id, that are ordered but not available yet

DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → openPurchaseOrderQuantity

base_price_input_data

price_relations_base_product

string

The purpose of the pricing stream Price Successor is to define a price for a product that is in some way linked or descendant to another product (for example a grey notebook that should have the same price as its black twin). This field describes the product which should be used as a reference (in this example the black product). See here for details Stream: Price Successor Pricing.

ECOMM → /v0/product-pricing-configurations/{sku}/ → base_product → code

base_price_input_data

price_relations_value

decimal

This is the discount that should be subtracted from the price of the base product to get the price successor price. It can be positive or negative and either a relative or absolute value. See here for details Stream: Price Successor Pricing.

ECOMM → /v0/product-pricing-configurations/{sku}/ →

* if value_type = “relative” then relative_value
* elif value_type = “absolute” then absolute_value
* else Null

if value_type = “relative” then relative_value

elif value_type = “absolute” then absolute_value

else Null

base_price_input_data

price_relations_value_type

string

If this field is “absolute” we add a fixed Euro positive or negative discount to the price of a base price, if it’s “relative” we substract a positive or negative percentage discount from the price of the base price. See here for details Stream: Price Successor Pricing.

ECOMM → /v0/product-pricing-configurations/{sku}/ → value_type

base_price_input_data

product_sku

string

base_price_input_data

product_type

string

This describes the kind of article we have, can take the values PHYSICAL, USED, SPARE, BUNDLE, SERVICE, DISCOUNT, INSURANCE, SHIPPING

DIS → /v2/product/{sku}/product-info → type

base_price_input_data

product_views_band

string

Takes values A to E. A is in the top percent of clicked products on the webshop, E contains least clicked products

DIS → /v2/product/{sku}/product-info → product_views_band

base_price_input_data

reserved_quantity_central_warehouse

integer

The amount of units with this product_id, that are in the central warehouse, but reserved

DIS → /v2/product/{sku}/stock?stock-id=ZL_001 → reserved_quantity

base_price_input_data

rrp_listed_gross

decimal

The recommended retail price provided by the manufacturers themselves in EUR

DIS → /v2/product/{sku}/price → retail_price

base_price_input_data

shipping_class

string

The shipping class is part of shipping information that defines the shipping costs of a product depending on its listed price

DIS → /v2/product/{sku}/shipping → shipping_class

base_price_input_data

shipping_group

string

The shipping group is part of shipping information that defines the shipping costs of a product depending on its listed price

DIS → /v2/product/{sku}/shipping → shipping_group

base_price_input_data

standard_purchase_price_listed_net

decimal

current purchase price cost in EUR if we would decide to buy the product again today at the default supplier

DIS → /api/v2/product/{product_sku}/price → standard_purchase_price

base_price_input_data

start_exclusion_at

datetime

This is the timestamp in UTC+0 from which on the product should not be priced with the autopricing anymore. If everything works as planned, it should not be null.

ECOMM → /v0/product-pricing-configurations/{sku}/ → start_exclusion_at

base_price_input_data

stock_quantity

integer

One value of stock for each product and each stock_id.

DIS → /v2/product/{sku}/stock → quantity

base_price_input_data

vat_rate

decimal

current tax rate as a fraction that we have to pay after selling the product to a B2C customer

DIS → /v2/product/{sku}/product-info → vat_rate

base_price_input_data

date_only

date

this is a field only used for as a dynamic partitioning key (used for internal performance and storage of data in AWS Kinesis/Glue). should not be used for any business purposes

computed by AWS Kinesis based on created field

base_price_meta_data

avg_current_base_price_listed_gross

decimal

This is an average value of the last current_price_listed_gross value. We use this to check if the current checked_recommended_price_listed_gross seems suspicious, e.g. we suspect a data errors in fields that affected the current price calculation. Then we mark is_price_suspicious is True and send a mail to the CM.

calculated within PS

base_price_meta_data

avg_purchase_price_listed_net

decimal

This is an average value of the last purchase_price_listed_net values. We use this to check if the current purchase_price_listed_net seems suspicious, e.g. we suspect a data error. Then we mark is_price_suspicious is True and send a mail to the CM.

calculated within PS

base_price_meta_data

bundle_components

string

List of product skus which make up a bundle product (if the bundle product is a computer, the bundle components would consist of mouse, keyboard, headphones etc.)

DIS → api/v2/pricing-product-bundle-list?bundle_sku={product_sku} → bundle_components

base_price_meta_data

free_quantity

integer

This is the total free quantity, e.g. total_stock_quantity - reserved_quantity.

calculated within PS

base_price_meta_data

inventory_health_markdown_parameter

decimal

See description for field inventory_health_strategy.

calculated within PS

base_price_meta_data

inventory_health_strategy

string

The correct inventory_health_strategy for a product is calculated as:

Filter elements in list inventory_health_config for 5-tuples that have the correct range range_min < current_price <= range_max → 25 items remaining

Filter elements in list to fit for the current inventory_health_bucket (filter list such that inventory_health_config->inventory_health_bucket = inventory_health_bucket from DIS) → 1 item remaining

Now we should have exactly one entry and one value for inventory_health_strategy and in some cases a non-null markdown_parameter, which we shall rename to inventory_health_markdown_parameter.

calculated within PS

base_price_meta_data

is_export_allowed

boolean

On some occasions we don’t allow exports, eg. when stores would have to manually change price tags but the last update was less than 7 days ago.

calculated within PS

base_price_meta_data

is_store_affected

boolean

If a product is available in a store in which there is no digital price tag (ePop), the product is considered is_store_affected = True. That means that we don't want to annoy our employees at the stores by forcing them to have to replace price tags on the shelves all the time. Therefore we have to check if the previous price change was less than a certain time ago and only update then (currently once a week).

calculated within PS

base_price_meta_data

last_pricing_stream

string

the pricing selected_stream of the previous successful base price calculation

calculated within PS

base_price_meta_data

last_unhealthy_cont_markdown_export

date

The time of the last continuous markdown price export from Pricing Service for this product using unhealthy inventory stream

calculated within PS

base_price_meta_data

lowest_competitor_price_listed_gross

decimal

This is the lowest listed competitor offer in EUR that is available in the Market Price Screening Service for this product. Availability doesn't matter here.

calculated within PS

base_price_meta_data

lowest_competitor_price_with_stock_listed_gross

decimal

This lowest relevant competitor offer from Market Price Screening, more specifically it is the minimum value of merchant_offers_with_stock.

calculated within PS

base_price_meta_data

lowest_competitor_price_landed_gross

decimal

This lowest relevant competitor offer including shipping_costs from Market Price Screening, more specifically it is the minimum value of landed_merchant_offers_without_stock.

calculated within PS

base_price_meta_data

lowest_competitor_price_with_stock_landed_gross

decimal

This lowest relevant competitor offer including shipping_costs from Market Price Screening ignoring stock availabilites, more specifically it is the minimum value of landed_merchant_offers_with_stock.

calculated within PS

base_price_meta_data

max_price_listed_gross

decimal

This is round(purchase_price_listed_net / (1 - min(margin_cap, 0.99)) * (1 + vat_rate), 2) unless null values prevent this calculation from happening.

calculated within PS

base_price_meta_data

min_price_listed_gross

decimal

This is round(purchase_price_listed_net / (1 - min(margin_floor, 0.99)) * (1 + vat_rate), 2) unless null values prevent this calculation from happening.

calculated within PS

base_price_meta_data

markup_pct

decimal

The target margin extracted by taking the average margin of similar products that we offer as a fraction of the internal costs

calculated in DHS based on base_price_input_data and base_price_calculation table data in v_ps_markup_pct

base_price_meta_data

merchant_offers_with_stock_listed_gross

string

This is a field derived from mps_merchant_offers, it contains a list of competitor prices without shipping_costs from offers that have the unit in stock (availability = 2).

calculated within PS

base_price_meta_data

merchant_offers_without_stock_listed_gross

string

This is a field derived from mps_merchant_offers, it contains a list of competitor prices without shipping_costs from all offers regardless of availability.

calculated within PS

base_price_meta_data

merchant_offers_without_stock_landed_gross

string

This is a field derived from mps_merchant_offers, it contains a list of competitor prices including shipping_costs from all offers that have the unit in stock (availability = 2).

calculated within PS

base_price_meta_data

merchant_offers_without_stock_landed_gross

string

This is a field derived from mps_merchant_offers, it contains a list of competitor prices including shipping_costs from all offers regardless of availability.

calculated within PS

base_price_meta_data

merchant_offers_verbose

string

This is a field derived from mps_merchant_offers,  it’s just a concatenation of all named_price values, comma separated. When the offer is available for the customer to buy at the merchant’s site, the offer gets an asterisk attached to it. example: Amzn (19.90*), Otto (20.50), PCKing(22.30*)

calculated within PS

base_price_meta_data

product_sku

string

-

base_price_meta_data

purchase_price_listed_net

decimal

The processed purchase costs from the Integration Service in EUR. The logic is the following.

* If both avg_purchase_price_listed_net and standard_purchase_price are null → assume null
* Else if none are null and non-zero → we take the minimum of both
* Else if avg_purchase_price_listed_net is non-null and non-zero → avg_purchase_price_listed_net
* Else if standard_purchase_price_listed_net is non-null and non-zero → standard_purchase_price_listed_net

If both avg_purchase_price_listed_net and standard_purchase_price are null → assume null

Else if none are null and non-zero → we take the minimum of both

Else if avg_purchase_price_listed_net is non-null and non-zero → avg_purchase_price_listed_net

Else if standard_purchase_price_listed_net is non-null and non-zero → standard_purchase_price_listed_net

If we have margin_impact data we subtract this from the interim results before returning the purchase_price_listed_net.

More info can be found here https://cyber-solutions.atlassian.net/wiki/spaces/IS/pages/2260729857/DIS+purchase+price+calculation.

DIS → /api/v2/product/{product_sku}/price → purchase_price

base_price_meta_data

reason_price

string

This a string that describes why was the current price chosen, e.g. which part of the algorithm lead to the current recommended_price_listed_gross.

calculated within PS

base_price_meta_data

reason_price_check

string

This a string that describes which price checks were passed and which cappings were applied before returning checked_recommended_price_listed_gross.

calculated within PS

base_price_meta_data

reason_stream

string

This a string that describes why the current autopricing selected_stream chosen.

calculated within PS

base_price_meta_data

timestamp_last_export

datetime

When was the last successful price export for this product?

calculated within PS

base_price_meta_data

total_free_quantity

integer

This is the total free quantity, e.g. stock_quantity - reserved_quantity aggregated over all stock_ids sent by DIS stock.

calculated within PS

base_price_meta_data

total_stock_quantity

integer

This is the stock_quantity aggregated over all stock_ids sent by DIS stock.

calculated within PS

base_price_meta_data

trigger_reason

string

what changed field / which service triggered the repricing withing the Pricing Service

calculated within PS

base_price_meta_data

date_only

date

this is a field only used for as a dynamic partitioning key (used for internal performance and storage of data in AWS Kinesis/Glue). should not be used for any business purposes

computed by AWS Kinesis based on created field

base_price_meta_data

exported_at

datetime

This is the creation timestamp of the row in the data base in UTC+0.

calculated within PS

base_price_calculation

category_manager

string

Category manager name to which the product belongs.

DIS → api/v2/item/[product-sku]/info → category_manager

base_price_calculation

checked_recommended_price_listed_gross

decimal

This is the recommended price after the Base Price Algorithm: Price Quality Check was executed.

calculated within PS

base_price_calculation

created_at

datetime

timestamp at which the calculation was performed

calculated within PS

base_price_calculation

current_base_price_listed_gross

decimal

the current base price value, received by PS from DIS service,

DIS → /api/v2/product/[product-sku]/price → base_price

base_price_calculation

description

string

Human readable product description as displayed on the webshop from Data Integr. Service

DIS → /api/v2/product/[product-sku]/product-info → base_price

base_price_calculation

inventory_health_strategy

string

calculated based on the  inventory_health_config,  inventory_health_bucket

calculated within PS

base_price_calculation

is_price_suspicious

boolean

If a price is suspicious, the price is not exported, but only a mail is sent to the respective CM. The logic for suspicious prices can be found here Base Price Algorithm: Price Quality Check.

calculated within PS

base_price_calculation

lowest_competitor_price_landed_gross

decimal

This lowest relevant competitor offer including shipping_costs from Market Price Screening, more specifically it is the minimum value of landed_merchant_offers_without_stock.

calculated within PS

base_price_calculation

product_sku

string

-

base_price_calculation

product_views_band

string

Takes values A to E. A is in the top percent of clicked products on the webshop, E contains least clicked products

DIS → /api/v2/product/[product-sku]/product-info → product_views_band

base_price_calculation

purchase_price_listed_net

decimal

DIS → /api/v2/product/[product-sku]/price → purchase_price

base_price_calculation

reason_is_price_suspicious

string

This is a string that explains what exactly made this product suspicious (is_price_suspicious is True), if it is.

calculated within PS

base_price_calculation

recommended_price_listed_gross

decimal

This price is the unchecked recommended price calculated by the Pricing Service using the selected_stream Base Price Algorithm: Pricing Streams before Base Price Algorithm: Price Quality Check have been executed.

calculated within PS

base_price_calculation

selected_stream

string

The stream which was selected for the price calculation using the stream selection algorithm from here Base Price Algorithm: Stream Selection

calculated within PS

base_price_calculation

shipping_class

string

base_price_calculation

shipping_group

string

base_price_calculation

updated_at

datetime

This field contains the UTC+0 timestamp of when the row in the data base was updated.

calculated within PS

base_price_calculation

vat_rate

decimal

current tax rate as a fraction that we have to pay after selling the product to a B2C customer

DIS → /v2/product/{sku}/product-info → vat_rate

base_price_calculation

date_only

date

this is a field only used for as a dynamic partitioning key (used for internal performance and storage of data in AWS Kinesis/Glue). should not be used for any business purposes

computed by AWS Kinesis based on created field

base_price_calculation

exported_at

datetime

This is the timestamp from when the price for the sku was exported to the queue. If it is null the price was not exported (yet). Timestamp is in UTC+0 as well.

calculated within PS

channel_price

channel_price_id

string

foreign key to channel_price table in PS data base

channel_price

product_id

string

foreign key to product table in PS data base

channel_price

sku

string

the sku of the product

channel_price

sales_channel_code

string

see channel_price db table above

channel_price

manual_channel_price_listed_gross

decimal

see channel_price db table above

channel_price

default_channel_price_listed_gross

decimal

see channel_price db table above

channel_price

external_channel_price_listed_gross

decimal

see channel_price db table above

channel_price

price_per_unit_listed_gross

decimal

see channel_price db table above

channel_price

created_at

datetime

see channel_price db table above

channel_price

updated_at

datetime

see channel_price db table above

channel_price

exported_at

datetime

see channel_price db table above

channel_price

channel_strategy_name

string

channel_price

channel_strategy_formula

string

the formula used to calculate the default_channel_price_listed_gross

channel_price

selling_unit

string

see product db table above

channel_price

selling_unit_factor

decimal

see product db table above

channel_price

vat_rate

decimal

can be part of the formula

channel_price

decision_purchase_price_listed_net

decimal

can be part of the formula.

The decision purchase price in EUR contains the net standard purchase price minus sell-in and sell-out backend discount conditions that reduce the effective costs of a product to a value lower than the listed standard purchase price. The price itself is specific per supplier, thus we operate on the chosen default standard supplier. If the standard supplier, their selling price or their backend conditions changes, so will the value of this price. It's called decision purchase price, because it's a more realistic portrayal of the operative costs than the standard_supplier_price.

channel_price

standard_purchase_price_listed_net

decimal

can be part of the formula

channel_price

average_purchase_price_listed_net

decimal

can be part of the formula

channel_price

purchase_price_listed_net

decimal

can be part of the formula

channel_price

recommended_retail_price_listed_gross

decimal

can be part of the formula

channel_price

shipping_costs

decimal

can be part of the formula

channel_price

lowest_competitor_offer_listed_gross

decimal

can be part of the formula

channel_price

reason_channel_price_trigger

string

a message that contains what changed fields triggered the repricing

channel_price

currency

string

EUR as a constant for now

channel_price

channel_prices

array

TBD ?

base_price_meta_data

is_coverage_based_pricing

boolean

This flag describes if the product is configured to be price within Coverage Based Pricing in the Ecommerce Cloud Service

calculated within PS

base_price_meta_data

has_unhealthy_inventory

boolean

A product is unhealthy if all the following conditions are true

if inventory_health_strategy is available and not ‘Regular’ and

if

assortment_status != ‘ACTIVE’ or

(product_views_band = 'A' and free_quantity_central_warehouse > 5) or

(product_views_band = 'B' and free_quantity_central_warehouse > 3) or

(product_views_band = 'C' and free_quantity_central_warehouse > 2) or

(free_quantity_central_warehouse > 1)

calculated within PS

base_price_calculation

is_price_successor

boolean

This flag describes if the product is configured as a price successor of another product in the Ecommerce Cloud Service

calculated within PS

### Log / data Requirements
In the process of maintenance and monitoring we need to be able to do the following:

* Price calculation and export -> Store all data (or keep it in memory) that is needed for stream selection, price calculation and price checks until export price is calculated-> Store all data that is needed for price export until price is either discarded or exported (currently only field product_views_band is affected by this)
* Alerts and detection of down times-> is PS service working as expected? (Are the queue, data base, APIs all working)?-> do dependent service (DIS, MPS, ECOMM) work as expected or do we receive 500 errors?-> send out alert mails if there are incidents
* Visualization of Pricing KPIs-> how many price calculations per hour in last month?-> how often was a certain pricing stream chosen?-> which price checks were passed, which weren't? how often?-> how often did input data not pass null value checks -> aggregations of quality of input data-> export of this data to BI, so that they can make dashboards-> provision of this data to Pricing Cockpit so CMs can see why a price was chosen
* Debugging of puzzling calculation results → further algorithm improvement-> which service internal algorithm config was used?-> in which steps is the calculation different than what we intuitively have expected? Where would we have to change the logic in the future to get a different result?-> did faulty input data from DIS cause the unexpected price? was it the configuration from ECOMM? or weird competitor data?

Price calculation and export -> Store all data (or keep it in memory) that is needed for stream selection, price calculation and price checks until export price is calculated-> Store all data that is needed for price export until price is either discarded or exported (currently only field product_views_band is affected by this)

Alerts and detection of down times-> is PS service working as expected? (Are the queue, data base, APIs all working)?-> do dependent service (DIS, MPS, ECOMM) work as expected or do we receive 500 errors?-> send out alert mails if there are incidents

Visualization of Pricing KPIs-> how many price calculations per hour in last month?-> how often was a certain pricing stream chosen?-> which price checks were passed, which weren't? how often?-> how often did input data not pass null value checks -> aggregations of quality of input data-> export of this data to BI, so that they can make dashboards-> provision of this data to Pricing Cockpit so CMs can see why a price was chosen

Debugging of puzzling calculation results → further algorithm improvement-> which service internal algorithm config was used?-> in which steps is the calculation different than what we intuitively have expected? Where would we have to change the logic in the future to get a different result?-> did faulty input data from DIS cause the unexpected price? was it the configuration from ECOMM? or weird competitor data?

All issues listed above need to be done using either data base entries or logs in performant manner.

For example it shouldn’t take more than a couple of minutes to list products for which a certain price check failed or products that had in average more than x price changes per day. A rough estimation is that we Data Scientist spend roughly one hour a day analyzing this data and checking where we can improve data quality and business logic. If this would take significantly longer, it would impact our overall velocity rather much.

channel_price

