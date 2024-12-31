# PS Base Price Calculation

## Algorithm
Is there a manual base price for this product?

Use that price

Else calculate the price automatically

Select the correct base price calculation strategy (called "price stream") evaluating the data in 1. → more documentation here Base Price Algorithm: Stream Selection

Calculate the base price using the chosen stream in 2 b). and the data in 1. → We have 9 active streams Base Price Algorithm: Pricing Streams, meaning price strategies or algorithms to calculate the price of a product.

Before distributing a base price of a product to the webshop it needs to pass quality checks (price change not too high, not too many price changes in a row) and apply rounding if necessary. → more documentation here Base Price Algorithm: Price Quality Check

A visualization of this algorithm can be found here

