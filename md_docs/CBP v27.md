# CBP v2.7

## Releases
In comparison to the Coverage Based Pricing v2.6 method, we made some changes:

| Release version | Release notes | Release date |
|---|---|---|
| v2.7 | Make expected order rate on a certain day dependent on seasonal changes. During Christmas weeks we expect more sales than in summer holidays. This might shift the weight of the target demand from being distributed evenly on all days in a time frame to have different more realistic weights | 13.01.2021 |

Release version

Release notes

Release date

v2.7

* Make expected order rate on a certain day dependent on seasonal changes. During Christmas weeks we expect more sales than in summer holidays. This might shift the weight of the target demand from being distributed evenly on all days in a time frame to have different more realistic weights

Make expected order rate on a certain day dependent on seasonal changes. During Christmas weeks we expect more sales than in summer holidays. This might shift the weight of the target demand from being distributed evenly on all days in a time frame to have different more realistic weights

13.01.2021

## Configuration
An example configuration entry looks like the following:

| Product Id | Target quantity | Start date | End date |
|---|---|---|---|
| ABCD-123 | 60 | 2020-06-06 | 2020-09-06 |

Product Id

Target quantity

Start date

End date

ABCD-123

60

2020-06-06

2020-09-06

## Algorithm
The result is the following method:

The procedure to calculate a starting value is the following:

In addition to that there are some price cap business rules to avoid outliers in both directions. These are currently the same as in the Merchant Based Stream.

| Strategy "COVERAGE BASED PRICING" |
|---|
| Selection of all relevant products(see also here BPS Algorithm: Stream Selection) | Product ismerchandise articlenot “ausgelistet” and not “Bestand Zentrallager > 0” and not “Inventory Store > 0” and not “offene Einkaufsaufträge”no bundle on the auto pricing list, not excluded from auto pricing, not manually deactivatedactivated for COVERAGE BASED PRICING (entries for coverage based pricing exist)no PRICE SUCCESSOR (related items) pricingno NEW_PRODUCT and no MERCHANT BASED or no valid RRP |
| Price Calculation | Preparation configuration: (deal) quantity: target quantity of items that should be sold within the selling (target) time frame start date: beginning of the selling time frame (day 1)end date: end of the selling time frame (day D)season_factor_d: how does the sell out deviate from average sell out because of seasonPreparation calculations (more details see below):order quantity := total orders since start dateseason_impact := season_factor_1 + …. + season_factor_Dtarget-sellout per day d := target_quantity * (d + season_factor_1 + … + season_factor_d) / ((end date - current date) + season_impact) current-sellout per day := sellout last seven days / 7average-price := average selling price over the last seven daysRecommended landed price if current_day == start_day==> reco price := starting price (more info see below)if order quantity >= (deal) quantity==> reco price := RRPif End date < heute==> reco price := margin floor priceif |1 - current sellout per day / target-sellout per day| < 5%==> reco price := average-priceif current sellout per day < target-sellout per day==> reco price := average-price - average-price- margin floor price) / 4Otherwise==> reco price := average + (RRP - average-price) / 4 |
| Price quality checks(see also here BPS Algorithm: Price Quality Check) | Preparation for margin calculation:if standard purchase price < average purchase price==> product costs := standard purchase priceif inventory > 0 ==> product costs := average purchase priceotherwise==> product costs := standard purchase priceDetermine margin floor per product according to the following priority:configuration for article group according to price rangeconfiguration for article group totalconfiguration for shared flat according to price rangeconfiguration for WG totalconfiguration for default by price rangeconfiguration for default totalDetermine margin cap per product according to the following priority:Configuration for article groupConfiguration for WGConfiguration for defaultMax price := 1.19 * product costs / (1-margin cap)Min price := 1.19 * products costs / (1-margin floor)Store limit:If the product is available in at least two stores and is not listed by ePOP==> Store limit: = 1Otherwise==> Store limit: = 0 |
|  | a) Lowest Product Price: if reco landed price - shipping costs < lowest product price==> reco landed price := lowest product price + 1 + shipping costs |
|  | b) UVP/RRP Cap:    i) RRP Check:At Tier1: ==> use RRPAt Tier2+Tier3: Are there merchants with price ≤ UVP?==> Use UVP, otherwise no UVP/RRP Cap    ii) if reco landed price > UVP + shipping costs        ==> reco landed price := UVP + shipping costsIf SALE flag is set==> Cap at RRP - 5% |
|  | c) Margin Cap:if reco landed price - shipping costs > max price==> reco landed price := max_price + shipping costsotherwise==> no change |
|  | d) Price Change Threshold    If Last pricing stream != 'UNHEALTHY INVENTORY':if (reco landed price - last landed price) / landed price > 0.3==> reco landed price := landed price * 1.3if (reco landed price - last landed price) / landed price < -0.3==> reco landed price := landed price * 0.7 |
|  | e) Margin Floorreco landed price - shipping costs < min price==> reco landed price := min_price + shipping costssonst: no change |
|  | f) Final reco price roundedif reco landed price - shipping costs < 0.5==> final reco price := reco landed price - shipping costsif reco landed price - shipping costs < 200==> final reco price := round(reco landed price - shipping costs;0) + 0.90otherwise==> final reco price := round(reco landed price - shipping costs;0) |
|  | if no price change==> NEEDS_TO_BE_UPDATE := 0change reason "Margin Floor"==> NEEDS_TO_BE_UPDATED := 1change reason "Unhealthy Inventory Reset"==> NEEDS_TO_BE_UPDATED := 1change reason not "Unhealthy Inventory Reset" and store limit = 1 and (reco landed price > 100 or price change > 4)==> NEEDS_TO_BE_UPDATED := 1change reason not "Unhealthy Inventory Reset" and store limit = 1 and last price change was less then 7 days ago (changed to 3 days in 2.4)==> NEEDS_TO_BE_UPDATED := 0if second price change upwards or downwards in a row and reason not "Margin Floor"==> NEEDS_TO_BE_UPDATED := 0otherwise==> NEEDS_TO_BE_UPDATED := 1 Consequence:NEEDS_TO_BE_UPDATE = 1==> price changeotherwise==> no price change |

Strategy "COVERAGE BASED PRICING"

Selection of all relevant products

(see also here BPS Algorithm: Stream Selection)

Product is

* merchandise article
* not “ausgelistet” and not “Bestand Zentrallager > 0” and not “Inventory Store > 0” and not “offene Einkaufsaufträge”
* no bundle
* on the auto pricing list, not excluded from auto pricing, not manually deactivated
* activated for COVERAGE BASED PRICING (entries for coverage based pricing exist)
* no PRICE SUCCESSOR (related items) pricing
* no NEW_PRODUCT and no MERCHANT BASED or no valid RRP

merchandise article

not “ausgelistet” and not “Bestand Zentrallager > 0” and not “Inventory Store > 0” and not “offene Einkaufsaufträge”

no bundle

on the auto pricing list, not excluded from auto pricing, not manually deactivated

activated for COVERAGE BASED PRICING (entries for coverage based pricing exist)

no PRICE SUCCESSOR (related items) pricing

no NEW_PRODUCT and no MERCHANT BASED or no valid RRP

Price Calculation

Preparation configuration:

* (deal) quantity: target quantity of items that should be sold within the selling (target) time frame
* start date: beginning of the selling time frame (day 1)
* end date: end of the selling time frame (day D)
* season_factor_d: how does the sell out deviate from average sell out because of season

(deal) quantity: target quantity of items that should be sold within the selling (target) time frame

start date: beginning of the selling time frame (day 1)

end date: end of the selling time frame (day D)

season_factor_d: how does the sell out deviate from average sell out because of season

Preparation calculations (more details see below):

* order quantity := total orders since start date
* season_impact := season_factor_1 + …. + season_factor_D
* target-sellout per day d := target_quantity * (d + season_factor_1 + … + season_factor_d) / ((end date - current date) + season_impact)
* current-sellout per day := sellout last seven days / 7
* average-price := average selling price over the last seven days

order quantity := total orders since start date

season_impact := season_factor_1 + …. + season_factor_D

target-sellout per day d := target_quantity * (d + season_factor_1 + … + season_factor_d) / ((end date - current date) + season_impact)

current-sellout per day := sellout last seven days / 7

average-price := average selling price over the last seven days

Recommended landed price

* if current_day == start_day==> reco price := starting price (more info see below)
* if order quantity >= (deal) quantity==> reco price := RRP
* if End date < heute==> reco price := margin floor price
* if |1 - current sellout per day / target-sellout per day| < 5%==> reco price := average-price
* if current sellout per day < target-sellout per day==> reco price := average-price - average-price- margin floor price) / 4
* Otherwise==> reco price := average + (RRP - average-price) / 4

if current_day == start_day==> reco price := starting price (more info see below)

if order quantity >= (deal) quantity==> reco price := RRP

if End date < heute==> reco price := margin floor price

if |1 - current sellout per day / target-sellout per day| < 5%==> reco price := average-price

if current sellout per day < target-sellout per day==> reco price := average-price - average-price- margin floor price) / 4

Otherwise==> reco price := average + (RRP - average-price) / 4

Price quality checks

(see also here BPS Algorithm: Price Quality Check)

Preparation for margin calculation:

* if standard purchase price < average purchase price==> product costs := standard purchase price
* if inventory > 0 ==> product costs := average purchase price
* otherwise==> product costs := standard purchase price

if standard purchase price < average purchase price==> product costs := standard purchase price

if inventory > 0 ==> product costs := average purchase price

otherwise==> product costs := standard purchase price

Determine margin floor per product according to the following priority:

configuration for article group according to price range

configuration for article group total

configuration for shared flat according to price range

configuration for WG total

configuration for default by price range

configuration for default total

Determine margin cap per product according to the following priority:

Configuration for article group

Configuration for WG

Configuration for default

* Max price := 1.19 * product costs / (1-margin cap)
* Min price := 1.19 * products costs / (1-margin floor)

Max price := 1.19 * product costs / (1-margin cap)

Min price := 1.19 * products costs / (1-margin floor)

Store limit:

* If the product is available in at least two stores and is not listed by ePOP==> Store limit: = 1
* Otherwise==> Store limit: = 0

If the product is available in at least two stores and is not listed by ePOP==> Store limit: = 1

Otherwise==> Store limit: = 0

a) Lowest Product Price:

* if reco landed price - shipping costs < lowest product price==> reco landed price := lowest product price + 1 + shipping costs

if reco landed price - shipping costs < lowest product price==> reco landed price := lowest product price + 1 + shipping costs

b) UVP/RRP Cap:

i) RRP Check:

* At Tier1: ==> use RRP
* At Tier2+Tier3: Are there merchants with price ≤ UVP?==> Use UVP, otherwise no UVP/RRP Cap

At Tier1: ==> use RRP

At Tier2+Tier3: Are there merchants with price ≤ UVP?==> Use UVP, otherwise no UVP/RRP Cap

ii) if reco landed price > UVP + shipping costs        ==> reco landed price := UVP + shipping costs

If SALE flag is set==> Cap at RRP - 5%

c) Margin Cap:

* if reco landed price - shipping costs > max price==> reco landed price := max_price + shipping costs
* otherwise==> no change

if reco landed price - shipping costs > max price==> reco landed price := max_price + shipping costs

otherwise==> no change

d) Price Change Threshold

If Last pricing stream != 'UNHEALTHY INVENTORY':

* if (reco landed price - last landed price) / landed price > 0.3==> reco landed price := landed price * 1.3
* if (reco landed price - last landed price) / landed price < -0.3==> reco landed price := landed price * 0.7

if (reco landed price - last landed price) / landed price > 0.3==> reco landed price := landed price * 1.3

if (reco landed price - last landed price) / landed price < -0.3==> reco landed price := landed price * 0.7

e) Margin Floor

* reco landed price - shipping costs < min price==> reco landed price := min_price + shipping costs
* sonst: no change

reco landed price - shipping costs < min price==> reco landed price := min_price + shipping costs

sonst: no change

f) Final reco price rounded

* if reco landed price - shipping costs < 0.5==> final reco price := reco landed price - shipping costs
* if reco landed price - shipping costs < 200==> final reco price := round(reco landed price - shipping costs;0) + 0.90
* otherwise==> final reco price := round(reco landed price - shipping costs;0)

if reco landed price - shipping costs < 0.5==> final reco price := reco landed price - shipping costs

if reco landed price - shipping costs < 200==> final reco price := round(reco landed price - shipping costs;0) + 0.90

otherwise==> final reco price := round(reco landed price - shipping costs;0)

* if no price change==> NEEDS_TO_BE_UPDATE := 0
* change reason "Margin Floor"==> NEEDS_TO_BE_UPDATED := 1
* change reason "Unhealthy Inventory Reset"==> NEEDS_TO_BE_UPDATED := 1
* change reason not "Unhealthy Inventory Reset" and store limit = 1 and (reco landed price > 100 or price change > 4)==> NEEDS_TO_BE_UPDATED := 1
* change reason not "Unhealthy Inventory Reset" and store limit = 1 and last price change was less then 7 days ago (changed to 3 days in 2.4)==> NEEDS_TO_BE_UPDATED := 0
* if second price change upwards or downwards in a row and reason not "Margin Floor"==> NEEDS_TO_BE_UPDATED := 0
* otherwise==> NEEDS_TO_BE_UPDATED := 1

if no price change==> NEEDS_TO_BE_UPDATE := 0

change reason "Margin Floor"==> NEEDS_TO_BE_UPDATED := 1

change reason "Unhealthy Inventory Reset"==> NEEDS_TO_BE_UPDATED := 1

change reason not "Unhealthy Inventory Reset" and store limit = 1 and (reco landed price > 100 or price change > 4)==> NEEDS_TO_BE_UPDATED := 1

change reason not "Unhealthy Inventory Reset" and store limit = 1 and last price change was less then 7 days ago (changed to 3 days in 2.4)==> NEEDS_TO_BE_UPDATED := 0

if second price change upwards or downwards in a row and reason not "Margin Floor"==> NEEDS_TO_BE_UPDATED := 0

otherwise==> NEEDS_TO_BE_UPDATED := 1

Consequence:

* NEEDS_TO_BE_UPDATE = 1==> price change
* otherwise==> no price change

NEEDS_TO_BE_UPDATE = 1==> price change

otherwise==> no price change

| Variable | Calculation | Explanation |
|---|---|---|
| target quantity | comes from the configuration:T := target quantity of items that should be sold within the selling (target) time frame |  |
| start date | comes from the configuration:This is the first day d=1 in the target time frame |  |
| end date | comes from the configuration:This is the last day d=N in the target time frame |  |
| time frame duration | D := amount of active days in the time frame. Example: if start and end date are two consecutive days D = 2 |  |
| current day | d := number of the current day in target time frameExample: if the start date was yesterday, d=2 |  |
| starting price | Calculate an automated merchant based starting value:If there are merchants and price less than min priceStart price := min_price_1If there are merchants and price is greater than min price and less than RRPStart price := MERCHANT BASED priceIf there are merchants and price is greater than RRPStart price := RRPOtherwiseStart price := (RRP + min_price_1)/2 | The Category Managers don’t have the resources to evaluate good starting prices for each product manually. Hence we want to do it automatically. |
| margin floor | Calculate an automated margin floor: Margin floor := -(margin back)/(purchase price - back conditions), which results in a total profit rate of 0% | The Category Managers don’t have the resources to evaluate good margin floor values for each product manually. Hence we want to do it automatically. |
| season factor | season_factor_d = is the deviation in percent of the actual sell rate on a typical day this time during the year compared to the average sell rate in that product category per year broken down to a single day. Example: If we usually sell 182.500 notebooks per year, meaning 5.000 per day, but before Christmas we have sold in average 11.000 per day, the season factor for a day in that time would be 11/5 = 2.2 = 220%.The season factor gets updated and exported to a table in Exasol. | Depending on the season we naturally have more traffic on the webshop, therefore we can expect more orders in certain times compared to others. For example is order rate large before christmas and low during summer. If we would assume an even distribution of the target quantity of sold products over all days in the time frame this is likely not realistic. Therefore we use a season factor |
| season impact in time frame | season_impact = season_factor_1 + …. + season_factor_D | The season impact is the summarized factor of all days in the target time frame. During the summer this sum will be negative (consistently selling less than the yearly average, during Christmas it will be positive). |
| current-Sellout day d: | current_sellout_d := order_quantity from day 1 to day d |  |
| target-Sellout day d | target_sellout_d := target_quantity * (d + season_factor_1 + … + season_factor_d) / (D + season_impact)For the ones who are prone to math, here is why: Abbreviations: season_factor on day d: sf_dtarget quantity in time frame: T_Ddays in time frame: Dtarget sell out all year T_ytarget demand on day i: t_dtarget sell out until day d: T_dWe can’t just use the season factors sf_d directly on the average target demand per day in the target time frame to calculate t_d, which would be t_d = sf_d  * 1/D * T_D, because the integral over all season factors don’t add up to zero, therefore in summer the desired orders would be negative. Therefore we need to use the target demand T_D for the target time frame 1….D to estimate an artificial target quantity for the whole year T_Y:We just scale up the target quantity T_D of the portion D to the whole year including 365 days using the target quantity season impact. Then we can calculate the target demand: And then at last we need to aggregate the demand on all previous days 1,…,d in the target time frame, which is:The last sum in the denominator is the season impact defined above. | We are not only interested in the selling rate of the last week, even in case we met our target rate in that period. If didn’t sell enough in the past, we need to lower the price to recover the initial phase, even if we don’t make that much direct profit. Therefore we aggregate over all days until the current day 1,…,d. Also we weight target quantities depending on seasonal effects. |
| target rate comparison(first half of target frame) | In the first half for days d = 1,…,floor(D/2) we use the following condition for a price change: |1 - current_sellout_d / target_sellout_d| > 5% AND|target_sellout_d - current_sellout_d| > 3 * target_quantity / D AND|target_sellout_d - current_sellout_d| > 3 | We need a sensitive measure for the final period to see how far you are from the target. So we useda relative difference of 5% and in addition, we also demand for a price change that the deviation must be at least 3 daily sell out rates in order not to have to set the percentage limit too high in the first few days.Example: If we usually originally plan to sell 2 notebooks per day to cover the target of 200 in 100 days, but we sold only 4 until day 5, then we have a difference of 2*4 - 5 = 3 items difference to the target, which is smaller than 3*(2 notebooks per day) = 6. Hence we don’t allow a price change yet. |
| target rate comparison(second half of target frame) | In the second half for days d = floor(D/2)+1,…,D we use the following condition for a price change: |1 - (target_quantity-current_sellout_d) / (D-d) / (target_quantity / D)| > 10% AND|target_quantity - current_sellout_d| > 3 * target_quantity / D AND|target_sellout_d - current_sellout_d| > 3 | We need a more sensitive measure for the final period to see how far we are from the target. From the second half on, we want to look at it the other way round: What percentage do I have to sell more per day if I want to catch up? If the difference is more than 5%, change price.In addition, we again demand that the deviation must be at least 3 daily target sell out rates difference. |
| Lower boundary | Make the min_price flexible by creating a flexible min_price_d for each day d. min_price_d := min_price * (1-0.1(d-1)/(D-1))=> min_price_1 = min_price and min_price_D = 90% min_price | At first we want to see the min_price rather strict. Later if necessary we can lower this lower boundary up to 10% to recover from a bad starting phase even if we make less direct profit. |

Variable

Calculation

Explanation

target quantity

comes from the configuration:

T := target quantity of items that should be sold within the selling (target) time frame

start date

comes from the configuration:

This is the first day d=1 in the target time frame

end date

comes from the configuration:

This is the last day d=N in the target time frame

time frame duration

D := amount of active days in the time frame.

Example: if start and end date are two consecutive days D = 2

current day

d := number of the current day in target time frame

Example: if the start date was yesterday, d=2

starting price

Calculate an automated merchant based starting value:

* If there are merchants and price less than min priceStart price := min_price_1
* If there are merchants and price is greater than min price and less than RRPStart price := MERCHANT BASED price
* If there are merchants and price is greater than RRPStart price := RRP
* OtherwiseStart price := (RRP + min_price_1)/2

If there are merchants and price less than min priceStart price := min_price_1

If there are merchants and price is greater than min price and less than RRPStart price := MERCHANT BASED price

If there are merchants and price is greater than RRPStart price := RRP

OtherwiseStart price := (RRP + min_price_1)/2

The Category Managers don’t have the resources to evaluate good starting prices for each product manually. Hence we want to do it automatically.

margin floor

Calculate an automated margin floor:

Margin floor := -(margin back)/(purchase price - back conditions),

which results in a total profit rate of 0%

The Category Managers don’t have the resources to evaluate good margin floor values for each product manually. Hence we want to do it automatically.

season factor

season_factor_d = is the deviation in percent of the actual sell rate on a typical day this time during the year compared to the average sell rate in that product category per year broken down to a single day.

Example: If we usually sell 182.500 notebooks per year, meaning 5.000 per day, but before Christmas we have sold in average 11.000 per day, the season factor for a day in that time would be 11/5 = 2.2 = 220%.

The season factor gets updated and exported to a table in Exasol.

Depending on the season we naturally have more traffic on the webshop, therefore we can expect more orders in certain times compared to others. For example is order rate large before christmas and low during summer. If we would assume an even distribution of the target quantity of sold products over all days in the time frame this is likely not realistic. Therefore we use a season factor

season impact in time frame

season_impact = season_factor_1 + …. + season_factor_D

The season impact is the summarized factor of all days in the target time frame. During the summer this sum will be negative (consistently selling less than the yearly average, during Christmas it will be positive).

current-Sellout day d:

current_sellout_d := order_quantity from day 1 to day d

target-Sellout day d

target_sellout_d := target_quantity * (d + season_factor_1 + … + season_factor_d) / (D + season_impact)

For the ones who are prone to math, here is why:

Abbreviations:

season_factor on day d: sf_dtarget quantity in time frame: T_Ddays in time frame: Dtarget sell out all year T_ytarget demand on day i: t_dtarget sell out until day d: T_d

We can’t just use the season factors sf_d directly on the average target demand per day in the target time frame to calculate t_d, which would be t_d = sf_d  * 1/D * T_D, because the integral over all season factors don’t add up to zero, therefore in summer the desired orders would be negative. Therefore we need to use the target demand T_D for the target time frame 1….D to estimate an artificial target quantity for the whole year T_Y:

We just scale up the target quantity T_D of the portion D to the whole year including 365 days using the target quantity season impact. Then we can calculate the target demand:

And then at last we need to aggregate the demand on all previous days 1,…,d in the target time frame, which is:

The last sum in the denominator is the season impact defined above.

We are not only interested in the selling rate of the last week, even in case we met our target rate in that period. If didn’t sell enough in the past, we need to lower the price to recover the initial phase, even if we don’t make that much direct profit. Therefore we aggregate over all days until the current day 1,…,d.

Also we weight target quantities depending on seasonal effects.

target rate comparison

(first half of target frame)

In the first half for days d = 1,…,floor(D/2) we use the following condition for a price change:

|1 - current_sellout_d / target_sellout_d| > 5% AND

|target_sellout_d - current_sellout_d| > 3 * target_quantity / D AND

|target_sellout_d - current_sellout_d| > 3

We need a sensitive measure for the final period to see how far you are from the target. So we useda relative difference of 5% and in addition, we also demand for a price change that the deviation must be at least 3 daily sell out rates in order not to have to set the percentage limit too high in the first few days.

Example: If we usually originally plan to sell 2 notebooks per day to cover the target of 200 in 100 days, but we sold only 4 until day 5, then we have a difference of 2*4 - 5 = 3 items difference to the target, which is smaller than 3*(2 notebooks per day) = 6. Hence we don’t allow a price change yet.

target rate comparison

(second half of target frame)

In the second half for days d = floor(D/2)+1,…,D we use the following condition for a price change:

|1 - (target_quantity-current_sellout_d) / (D-d) / (target_quantity / D)| > 10% AND

|target_quantity - current_sellout_d| > 3 * target_quantity / D AND

|target_sellout_d - current_sellout_d| > 3

We need a more sensitive measure for the final period to see how far we are from the target. From the second half on, we want to look at it the other way round: What percentage do I have to sell more per day if I want to catch up? If the difference is more than 5%, change price.

In addition, we again demand that the deviation must be at least 3 daily target sell out rates difference.

Lower boundary

Make the min_price flexible by creating a flexible min_price_d for each day d.

min_price_d := min_price * (1-0.1(d-1)/(D-1))

=> min_price_1 = min_price and min_price_D = 90% min_price

At first we want to see the min_price rather strict. Later if necessary we can lower this lower boundary up to 10% to recover from a bad starting phase even if we make less direct profit.

## Analysis
### Report Release v2.7:
| Releases | The report covers v2.7 |
|---|---|
| Time frame | 08.07.2020 - 30.09.2020 |
| Result | Goal reached in 35 / 48 cases |

Releases

The report covers v2.7

Time frame

08.07.2020 - 30.09.2020

Result

Goal reached in 35 / 48 cases

For further details look at the report here

### Report Release v2.7:
| Releases | The report covers v2.7 |
|---|---|
| Time frame | 02.02.2021 - 31.03.2021 |
| Result | Goal reached in 4 / 10 cases |

Releases

The report covers v2.7

Time frame

02.02.2021 - 31.03.2021

Result

Goal reached in 4 / 10 cases

For further details look at the report here

