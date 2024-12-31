# Shipping Costs

As we often discuss about shipping strategies, we want to summarize open and answered questions and collect information and data driven arguments on this page.

You can enter a question even if you think it is hard or impossible to answer right now.

The calculation matrix for shipping costs can be found here Shipping Cost Calculation.

| Question | Status | Answer |
|---|---|---|
| Do customers tend to buy more or less if we split the price in listed_price + shipping_costs or keep listed_price = landed_price and set shipping_costs = 0? | DONE | Proposal: we randomly select an evenly distributed representatively large set of all products we consider being affected by this psychological effect we divide this set into two subsets A and Bset A we will remain priced like beforeset B will have shipping costs included in landed_price and configured to have free shippingAfter a predefined period of time the order/billing numbers are compared to set A and we check how significant (if at all) the difference issee here for more details: A/B-Test Free Shipping |
| How are customers affected by shipping costs? | PARTLY ANSWERED | A statistic from statista.de returns this result, part of the poll were also non electronics B2C-ecommerce companies. However this statistic doesn’t differ between electronic webshops and e.g. fashion webshops. Also it doesn’t specify if the a customer in the first bar would have also cancelled his/her if shipping was included in the listed price and thus the total price wasn’t competitive anymore.Parts of this question is answered here as well A/B-Test Free Shipping. |
| How do customers mostly select prices on Geizhals.de? Cheapest price including or excluding shipping costs? | PARTLY ANSWERED | Looking at the results of the A/B test customers that allow tracking probably tend to not compare landed, but only listed price. A/B-Test Free Shipping |
| What are the technical possibilities of distributed shipping costs automatically right now? | OPEN |  |
| Where will shipping cost configuration be after Cyberparts deactivation? SAP or microservice landscape or somewhere else? | OPEN |  |
| How do competitors like Amazon, Notebooksbilliger, Saturn & Mediamarkt handle shipping costs? | ANSWERED | A statistic from statista.de returns this result, part of the poll were also non electronics B2C-ecommerce companies.The strategy from direct electronics competitors still need to be analyzed. notebooksbilliger.deSimilar shipping configuration model as we have. No minimum order value. Products below 250€ cost 3.99€ (less than our model) and above 7.99€ (more than our model)see here for details https://www.notebooksbilliger.de/infocenter/section/shippingamazon.deStrongly depends on merchantMost products from amazon.de are free of shipping for prime members and free of shipping above 29€ for non-prime membersCompetitors usually don’t differ between one-position or multi-position orders. (In multi-position orders usually shipping costs are therefore applied multiple times)mediamarkt.deFor CDs, games, blurays and DVDs shipping is 3.99€For all other non-haulier and non FSK18 products shipping is 4.99€For orders above 59€, non-haulier and non FSK18 products are shipped for freeIn multi-position orders shipping is only applied once==> This is significantly cheaper than our modelsee here for details https://faq.mediamarkt.de/app/answers/detail/a_id/7379/~/wie-hoch-sind-die-versandkosten-%2F-lieferkosten%3Fsaturn.deSame as mediamarkt.dealternate.deProducts that are shipped via DHL (up to 31kg) all cost 6.99€ unless marked a free shippingOnly toys are shipped cheaper 4.99€, haulier costs similar to ourssee here for details https://www.alternate.de/html/help/contentBig.html?docId=7114&showTree=118&showTree=2450 |
| How do customers choose a webshop to buy unspecific non-brand products like USB-cables? | OPEN | For products like this Geizhals often collects related offers in categories. Example USB-cables: https://geizhals.de/?cat=kabusb |
| What restrictions do exist regarding configuring products to have free shipping? | ANSWERED | https://wiki.cyberport.de/display/spl/0+Regelungen+zu+Versandkostenfreiheit |
| Provided the order behaviour of our customers would stay the same, what profit impacts could we have? That means: if we include the shipping costs in the product price and don’t separate it anymore we would earn the equivalent of 2x the sipping costs instead of 1x if a customers has two articles in his order. | OPEN | Probably it would be advisable to keep shipping costs separate for article groups that are often bought together with other products (cables, adapters computer mouses, …). Because if such a product is bought separately and as for shipping costs we make sure, we cover internal shipping expenses.if such a product is bought together with a more expensive product like a notebook that has free shipping costs the complete order is free of shipping. However we could analyze applying latent shipping costs twice also in a subsequent second A-B test, after we performed the one above to see if the free shipping via listed price is desirable at all. |
| Would customers buy more if there was a “free shipping above x EUR” policy in order to get over this price threshold? | OPEN |  |

Question

Status

Answer

Do customers tend to buy more or less if we split the price in listed_price + shipping_costs or keep listed_price = landed_price and set shipping_costs = 0?

DONE

Proposal:

* we randomly select an evenly distributed representatively large set of all products we consider being affected by this psychological effect
* we divide this set into two subsets A and B
* set A we will remain priced like before
* set B will have shipping costs included in landed_price and configured to have free shipping
* After a predefined period of time the order/billing numbers are compared to set A and we check how significant (if at all) the difference is

we randomly select an evenly distributed representatively large set of all products we consider being affected by this psychological effect

we divide this set into two subsets A and B

set A we will remain priced like before

set B will have shipping costs included in landed_price and configured to have free shipping

After a predefined period of time the order/billing numbers are compared to set A and we check how significant (if at all) the difference is

see here for more details: A/B-Test Free Shipping

How are customers affected by shipping costs?

PARTLY ANSWERED

A statistic from statista.de returns this result, part of the poll were also non electronics B2C-ecommerce companies.

However this statistic doesn’t differ between electronic webshops and e.g. fashion webshops. Also it doesn’t specify if the a customer in the first bar would have also cancelled his/her if shipping was included in the listed price and thus the total price wasn’t competitive anymore.

Parts of this question is answered here as well A/B-Test Free Shipping.

How do customers mostly select prices on Geizhals.de? Cheapest price including or excluding shipping costs?

PARTLY ANSWERED

Looking at the results of the A/B test customers that allow tracking probably tend to not compare landed, but only listed price. A/B-Test Free Shipping

What are the technical possibilities of distributed shipping costs automatically right now?

OPEN

Where will shipping cost configuration be after Cyberparts deactivation? SAP or microservice landscape or somewhere else?

OPEN

How do competitors like Amazon, Notebooksbilliger, Saturn & Mediamarkt handle shipping costs?

ANSWERED

A statistic from statista.de returns this result, part of the poll were also non electronics B2C-ecommerce companies.

The strategy from direct electronics competitors still need to be analyzed.

notebooksbilliger.de

* Similar shipping configuration model as we have. No minimum order value.
* Products below 250€ cost 3.99€ (less than our model) and above 7.99€ (more than our model)
* see here for details https://www.notebooksbilliger.de/infocenter/section/shipping

Similar shipping configuration model as we have. No minimum order value.

Products below 250€ cost 3.99€ (less than our model) and above 7.99€ (more than our model)

see here for details https://www.notebooksbilliger.de/infocenter/section/shipping

amazon.de

* Strongly depends on merchant
* Most products from amazon.de are free of shipping for prime members and free of shipping above 29€ for non-prime members
* Competitors usually don’t differ between one-position or multi-position orders. (In multi-position orders usually shipping costs are therefore applied multiple times)

Strongly depends on merchant

Most products from amazon.de are free of shipping for prime members and free of shipping above 29€ for non-prime members

Competitors usually don’t differ between one-position or multi-position orders. (In multi-position orders usually shipping costs are therefore applied multiple times)

mediamarkt.de

* For CDs, games, blurays and DVDs shipping is 3.99€
* For all other non-haulier and non FSK18 products shipping is 4.99€
* For orders above 59€, non-haulier and non FSK18 products are shipped for free
* In multi-position orders shipping is only applied once==> This is significantly cheaper than our model
* see here for details https://faq.mediamarkt.de/app/answers/detail/a_id/7379/~/wie-hoch-sind-die-versandkosten-%2F-lieferkosten%3F

For CDs, games, blurays and DVDs shipping is 3.99€

For all other non-haulier and non FSK18 products shipping is 4.99€

For orders above 59€, non-haulier and non FSK18 products are shipped for free

In multi-position orders shipping is only applied once==> This is significantly cheaper than our model

see here for details https://faq.mediamarkt.de/app/answers/detail/a_id/7379/~/wie-hoch-sind-die-versandkosten-%2F-lieferkosten%3F

saturn.de

* Same as mediamarkt.de

Same as mediamarkt.de

alternate.de

* Products that are shipped via DHL (up to 31kg) all cost 6.99€ unless marked a free shipping
* Only toys are shipped cheaper 4.99€, haulier costs similar to ours
* see here for details https://www.alternate.de/html/help/contentBig.html?docId=7114&showTree=118&showTree=2450

Products that are shipped via DHL (up to 31kg) all cost 6.99€ unless marked a free shipping

Only toys are shipped cheaper 4.99€, haulier costs similar to ours

see here for details https://www.alternate.de/html/help/contentBig.html?docId=7114&showTree=118&showTree=2450

How do customers choose a webshop to buy unspecific non-brand products like USB-cables?

OPEN

For products like this Geizhals often collects related offers in categories. Example USB-cables: https://geizhals.de/?cat=kabusb

What restrictions do exist regarding configuring products to have free shipping?

ANSWERED

https://wiki.cyberport.de/display/spl/0+Regelungen+zu+Versandkostenfreiheit

Provided the order behaviour of our customers would stay the same, what profit impacts could we have? That means: if we include the shipping costs in the product price and don’t separate it anymore we would earn the equivalent of 2x the sipping costs instead of 1x if a customers has two articles in his order.

OPEN

Probably it would be advisable to keep shipping costs separate for article groups that are often bought together with other products (cables, adapters computer mouses, …). Because

* if such a product is bought separately and as for shipping costs we make sure, we cover internal shipping expenses.
* if such a product is bought together with a more expensive product like a notebook that has free shipping costs the complete order is free of shipping.

if such a product is bought separately and as for shipping costs we make sure, we cover internal shipping expenses.

if such a product is bought together with a more expensive product like a notebook that has free shipping costs the complete order is free of shipping.

However we could analyze applying latent shipping costs twice also in a subsequent second A-B test, after we performed the one above to see if the free shipping via listed price is desirable at all.

Would customers buy more if there was a “free shipping above x EUR” policy in order to get over this price threshold?

OPEN

