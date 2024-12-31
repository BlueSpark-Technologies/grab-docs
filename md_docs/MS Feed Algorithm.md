# MS Feed Algorithm

## AnyOfferChanged notification
The AnyOfferChanged subscription sends us a new offer for an ASIN, for which we offer at least one SKU.

We check if there is already a product in the product table that has the same ASIN:a) If yes, remember this sku and go to 3.b) If no get the SKU by calling the AMWS Api endpoint getMyPriceForASIN. Check how many SKUs the response contains:i) No SKU -> stop this routine with a warningii) One SKU -> remember this sku and go to 3.iii) Two SKUs or more, associate the ASIN with the internal dummy SKU 0000-000 and go to 3.

Store combination of ASIN and SKU in the product table.

Check if the offer contains our merchant price:a) If yes, go to 5.b) If no, check if the sku is the internal dummy SKU 0000-000:i) If yes, don't get a price.ii) If no, call the AMWS API endpoint getMyPriceForASIN and store the SKU go to 5.

Check if there is a fee in the product_fee table for this SKU:a) If yes, go to 5.b) If no, check if the sku is the internal dummy SKU 0000-000:i) If yes, don't get a fee.ii) If no, call the AMWS API endpoint getMyFeesEstimate for the SKU using the submitted price from the new offer and store the response in the product_fee table.

Store received product offer in the product_offer table.

If the SKU is not the internal dummy SKU 0000-000, notify the MS Pricing Service by pushing the information on the SQS Repricing Queue.

## ASIN ambiguity
How do I see, if there was a ambiguous ASIN SKU matching?-> It is linked to SKU 0000-000-> There is an SKU, which is in the GET_MERCHANT_LISTINGS_DATA_LITE file from Amazon, but it is not in the product table from the MS Feed Servive.

## Known issues
Assume we have an ASIN xyz and SKU sku1 in the product table. Now we get a new offer update for an ASIN that now is connected to a new SKU sku2. Just looking at the Amazon data we won't know which SKU this belongs to. Therefore we have to pretend that the new offer belongs to SKU sku1 as well. However this will not lead to submitting a price, that is too low, because the min price will be calculated on SKU sku2. The price recalculation for SKU sku2 however will never be triggered.

Here is a bigger example:

Assume we have an ASIN xyz and two product SKUs (blue and green notebook) that are matched to it. There are 21 offers for the same ASIN on Amazon. SKU_blue has rank 4 (4th cheapest offer) and costs 500€ and SKU_green has rank 21 and costs 600€.

Now we get an AnyOfferChanged notification. As SKU_green is not in the top 20 offers anymore we only get the price of SKU_blue, which is 500€. Note that the AnyOfferChanged notification does not contain the SKU of a product. So we get among all offers our own offer with [ ASIN = xyz | Price = 500€ | ... ].

Then we have to add an internal product_id in order to save the offer set with a new unique product_offer_id in the product_offer table in the data base. In the current implementation we extract all SKUs for ASIN xyz in the product table (in our case SKU_blue and SKU_green), and take the _first_ one, which is essentially a random and depends on when the product was added or the alphabetical order. Assume that in this process the wrong SKU (SKU_green) is chosen and match it to the internal product_id = product_id_green.

Then we store the following entry in the data base table product_offer with the matched internal product_id[ product_id = product_id_green | ms_landed_price = 500€ | ... ]

Now assume the MS Pricing Service calls the API and retrieves the ms_landed_price for SKU_green (remember, this had price 600€ on Amazon). The API takes the SKU and searches in the table product for the matching internal product_id which is product_id_green. Then it takes the latest offer_set in table product_offer and returns the field value ms_landed_price = 500€, which is wrong.=> Therefore in step 3, when we have to select a product_id to save the offer set, use a dummy product sku 0000-000 whenever there are multiple offers by Cyberport for the specific ASIN in question. Then an API call with an existing SKU will never touch offer_sets with multiple SKUs and in the worst case retrieve an outdated price. For each new ASIN with duplicate SKUs a dummy product with sku = 0000-000 with asin = xyz is added with its own product id.

