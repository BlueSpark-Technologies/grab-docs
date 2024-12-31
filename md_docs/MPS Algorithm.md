# MPS Algorithm

## Triggers
Whenever a new data set for a feed supplier comes in, store the data set and do the following processing steps. Afterwards push notifications on MPS Feed SNS topics for relevant SKUs in order to notify other subscribed microservices that there is new data available.

## Feed Supplier Processing Algorithm
Each feed supplier has a different customs of how merchants are named and which ones to include. Therefore we need to process the content into a unified format, only keep relevant merchants for a product (we don’t want our prices dictated by small garage sale like webshops) and filter out outliers as they might distort our prices into unwanted directions. We do it with the following procedure:

Get relevant feed supplier configuration from E-Commerce Cloud Services (for phase 1 this will be service internal configuration)

If the feed supplier in the trigger is considered relevant, continue, otherwise stop processing.

Filter on offers with positive non-null prices and filter out duplicate entries per merchantname, feed supplier and SKU. If there is conflicting data (multiple rows per SKU and merchantname), filter out all rows which have duplicates , keeping the lowest priced offer and dropping all other from the same merchant ,  loging also a message ==> only one offer per SKU, merchant left

Ask the Data Integration Service if the SKU is valid for Cyberport (product_info endpoint), if it isn’t drop all the offers for this SKU.

Get latest general merchant mapping configuration from E-Commerce Cloud Services

Map unified merchant name to raw merchant name. If there is no mapping, drop the offer.

Get product specific relevant competitors configuration for each SKU in the feed data from the E-Commerce Cloud Services.

Filter on SKU specific relevant competitors. → if nothing is specified for this SKU, we continue with the whole set of competitors without further filtering.

Compare resulting offers with previous offers and only keep changed or new offers

Push final merchant offer list for each remaining SKU on MPS Feed SNS Topics.

Comments:

In the old Exasol Price Feed calculations there was the option to choose which feed supplier was trusted more on certain merchants (table PROD_STAGING.PRC_CONF_FEED_MERCHANT_PRIORITIZATION in Exasol). However it was not used anyway, so we didn’t make the effort to implement it.

## Feed Supplier Merging Algorithm
As Pricing Service I don't want to bother with different feed suppliers or price search engines (e.g. product feed code). I only want to call the MPS service and get a trustworthy list of competitor prices for a product to choose a good webshop price accordingly. Therefore we need to merge GZH, WIT and IDL prices, after they were processed by the algorithm above.

Every time the Pricing Service requests a list of prices for a product, we want to do the following prioritization:

Take the latest data points for this product for of each feed supplier in the last 48 hours (based on provider_item_updated_at field) and check for duplicate merchant price (more than one price per merchant and product)

If we have more than one combination of product and merchant in the set we want to use Geizhals if possible, if there is no Geizhals, we want to use WorkIT, if there is no WorkIT, we want to use Idealo.

Filter on offers that deviate less than 50% of the median offer per product (outlier filtering). Base this outlier filtering based on landed price (price + zeroifnull(shipping_costs)).

If this list is empty as well return null value.

Comments:

* Analysis summer 2020 said that Geizhals data mostly is more accurate than WorkIT (crawled websites from competitors).
* On Geizhals or Idealo prices can be cheaper compared to prices on their website if merchants have vouchers.
* If we would use the latest price data point we might have alternating prices switching at the arrival of each new data file this is not tested yet, though.
* In Idealo data the matching between products can be off sometimes because they match over EAN instead of our SKU like on Geizhals.

Analysis summer 2020 said that Geizhals data mostly is more accurate than WorkIT (crawled websites from competitors).

On Geizhals or Idealo prices can be cheaper compared to prices on their website if merchants have vouchers.

If we would use the latest price data point we might have alternating prices switching at the arrival of each new data file this is not tested yet, though.

In Idealo data the matching between products can be off sometimes because they match over EAN instead of our SKU like on Geizhals.

