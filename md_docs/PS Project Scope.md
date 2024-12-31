# PS Project Scope

The Pricing Service should import product data, competitor and configuration information from the Data Integration Service (DIS), Market Price Screening (MPS), Marketplace Service (MS) and E-commerce Cloud (EC) and calculate the base prices as well as channel prices of the product portfolio using a variety of strategies. Merchants can use it to continuously calculate optimized prices for their webshops, marketplaces and other sales channels according to the current market situation in order to optimize their profit. As this is done automatically the service is scalable to a big product portfolio.

As a (category) manager I want prices in stores and on marketplaces on which we also sell products to be slightly different than on the webshop, which uses primarily the base price from the Pricing Service (PS). Background is that for example in stores we have different types of costs like store employees, rent, cleaning personal, advertisement or that we have commission fees to pay if we sell products in eBay. Thus we need to consider these additional / varying costs in our prices on these so called channels. Currently this is done within Cyberparts and the so called “Multi-VK manager”. In the scope of replacing Cyberparts moving this logic into a separate microservice is a crucial step.

In the future the (category) management should be able to specify and change configuration and calculation strategies for these channels in a separate UI. In this UI CMs can also enter manual prices. Afterwards the Pricing Service (PS) should import manual prices, product data, configuration (and possibly competitor information) from the Data Integration Service, E-Commerce Cloud Service, the Market Price Screening Service and the Marketplace Service and if not set manually calculate the base prices and channel prices of the product portfolio using a variety of strategies for a variety of channels.

Current channels that Cyberport uses are

| Channel | in scope? | Contact person business side |  |
|---|---|---|---|
| Amazon | yes | Malte Faßbach | see also Marketplace Service (MS) |
| Ebay | yes | Malte Faßbach |  |
| Idealo | later phase | Malte Faßbach | to be discussed |
| Check 24 | later phase | Malte Faßbach | to be discussed |
| Synaxon | yes | Martin Gere, his supervisor Lars Gräper |  |
| B2B Mercato | yes | Martin Gere, his supervisor Lars Gräper |  |
| B2B Portale | yes | Martin Gere, his supervisor Lars Gräper |  |
| Burda Shop | yes | Philipp Fischer |  |
| Computer Universe | yes | Rene Bittner |  |
| Cyberport.at | yes | Stefan Rohne |  |
| Stores * | yes | Nico Gröger, Gerhard Poppenberger | different logic per store is necessary, amount of stores can change |
| gebraucht.de | no | Stefan Teich | according to Stefan Teich CP we had a cooperation with them about 6 years ago, but they don’t exist anymore |
| Apple Subscription | yes | Arian Teßmann |  |

Channel

in scope?

Contact person business side

Amazon

yes

Malte Faßbach

see also Marketplace Service (MS)

Ebay

yes

Malte Faßbach

Idealo

later phase

Malte Faßbach

to be discussed

Check 24

later phase

Malte Faßbach

to be discussed

Synaxon

yes

Martin Gere, his supervisor Lars Gräper

B2B Mercato

yes

Martin Gere, his supervisor Lars Gräper

B2B Portale

yes

Martin Gere, his supervisor Lars Gräper

Burda Shop

yes

Philipp Fischer

Computer Universe

yes

Rene Bittner

Cyberport.at

yes

Stefan Rohne

Stores *

yes

Nico Gröger, Gerhard Poppenberger

different logic per store is necessary, amount of stores can change

gebraucht.de

no

Stefan Teich

according to Stefan Teich CP we had a cooperation with them about 6 years ago, but they don’t exist anymore

Apple Subscription

yes

Arian Teßmann

## Algorithm
Calculating the base price and channel price of a product in the Pricing Service is done in four steps:

Collection of product information from different sources (including for example information about stock, purchase price, shipping, configurations, ... ) → more documentation can be found here PS Internal Integration Points and here PS External Systems

Calculate base price → more documentation PS Base Price Calculation

Is there a manual base price for this product?

Use that price

Else calculate the price automatically

Select the correct base price calculation strategy (called "price stream") evaluating the data in 1. → more documentation here Base Price Algorithm: Stream Selection

Calculate the base price using the chosen stream in 2 b). and the data in 1. → We have 9 active streams Base Price Algorithm: Pricing Streams, meaning price strategies or algorithms to calculate the price of a product.

Before distributing a base price of a product to the webshop it needs to pass quality checks (price change not too high, not too many price changes in a row) and apply rounding if necessary. → more documentation here Base Price Algorithm: Price Quality Check

Before distributing a base price we need to check if it’s important enough to use up our price change quota → more documentation Base Price Algorithm: Price Change Prioritization

Distribute the base price to SAP Pro

Calculate the channel prices for each channel → more documentation PS Channel Price Calculation

For the current channel is there a manual channel price?

Use that price

Else: Is there an automatic price from an external microservice (i.e. Marketplace Service for Amazon)?

Use that price

Else calculate the price automatically

Calculate price using channel strategy formula from E-Commerce Cloud Service Channel Strategies UI

Run the channel price through price quality checks (price change not too high, not too many price changes in a row) and apply rounding if necessary.

Distribute the prices to relevant destinations via SAP Pro → more documentation here PS External Systems.

There are also some trigger, that only trigger the channel pricing of some channels, but not the base price calculation. If the base price didn’t change, also the channel pricing isn’t triggered.

A visualization of this algorithm can be found here

