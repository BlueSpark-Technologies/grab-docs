# API Analysis

## 1. Syncronous requests
| # | Action | Type | Params | Data model |
|---|---|---|---|---|
| 1 | Get merchant product data | Report ( _GET_MERCHANT_LISTINGS_DATA_LITE_ ) | SellerId | Product data |
| 2 | Get fee estimate for product | Products.GetMyFeesEstimate(  ) | SellerIdMarketplaceIdIdType = SellerSKUIdValue = A415-1FVIsAmazonFulfilled = falseIdentifier - ???ListingPrice.Amount = 800 - ???ListingPrice.CurrencyCode = EURShipping.Amount = 0  - ???Shipping.CurrencyCode = EURPoints.PointsNumber = 0 - ??? | Product fee data |
| 3 | Get product competitor information | Products.GetLowestOfferListingsForSKU( ) | SellerSKU = A415-18QItemCondition = new | Product competitors data |

#

Action

Type

Params

Data model

1

Get merchant product data

Report ( _GET_MERCHANT_LISTINGS_DATA_LITE_ )

* SellerId

SellerId

Product data

2

Get fee estimate for product

Products.GetMyFeesEstimate(  )

* SellerId
* MarketplaceId
* IdType = SellerSKU
* IdValue = A415-1FV
* IsAmazonFulfilled = false
* Identifier - ???
* ListingPrice.Amount = 800 - ???
* ListingPrice.CurrencyCode = EUR
* Shipping.Amount = 0  - ???
* Shipping.CurrencyCode = EUR
* Points.PointsNumber = 0 - ???

SellerId

MarketplaceId

IdType = SellerSKU

IdValue = A415-1FV

IsAmazonFulfilled = false

Identifier - ???

ListingPrice.Amount = 800 - ???

ListingPrice.CurrencyCode = EUR

Shipping.Amount = 0  - ???

Shipping.CurrencyCode = EUR

Points.PointsNumber = 0 - ???

Product fee data

3

Get product competitor information

Products.GetLowestOfferListingsForSKU( )

* SellerSKU = A415-18Q
* ItemCondition = new

SellerSKU = A415-18Q

ItemCondition = new

Product competitors data

## 2. Subscriptions ( Notifications )
| # | Action | Method | Parameters | Data model | Assumptions |
|---|---|---|---|---|---|
| 1. | Register a Destination | Subscriptions.RegisterDestination() | Key = sqsQueueUrlValue = sqsUrlDeliveryChannel = SQS |  |  |
| 2. | Deregister a Destination | Subscriptions.DeregisterDestination() | Key = sqsQueueUrlValue = sqsUrlDeliveryChannel = SQS |  |  |
| 3. | Create a Subscription for the NotificationType | Subscriptions.CreateSubscription() | Key = sqsQueueUrlValue = sqsUrlDeliveryChannel = SQSIsEnabled = trueNotificationType = AnyOfferChanged |  | Method can be used to enable and disable notification type |
| 4 | Sent test notification | Subscriptions.SendTestNotificationToDestination() |  |  | Validates the sqs setup, by sending a test queue |
|  |  |  |  |  |  |
| 5 | Notification triggered on competitors data changes | AnyOfferChangedNotification (  ) | product_id | Product competitors data | ??? get update on merchant price updates |
| 6 |  |  |  |  |  |
| 7 |  |  |  |  |  |

#

Action

Method

Parameters

Data model

Assumptions

1.

Register a Destination

Subscriptions.RegisterDestination()

* Key = sqsQueueUrl
* Value = sqsUrl
* DeliveryChannel = SQS

Key = sqsQueueUrl

Value = sqsUrl

DeliveryChannel = SQS

2.

Deregister a Destination

Subscriptions.DeregisterDestination()

* Key = sqsQueueUrl
* Value = sqsUrl
* DeliveryChannel = SQS

Key = sqsQueueUrl

Value = sqsUrl

DeliveryChannel = SQS

3.

Create a Subscription for the NotificationType

Subscriptions.CreateSubscription()

* Key = sqsQueueUrl
* Value = sqsUrl
* DeliveryChannel = SQS
* IsEnabled = true
* NotificationType = AnyOfferChanged

Key = sqsQueueUrl

Value = sqsUrl

DeliveryChannel = SQS

IsEnabled = true

NotificationType = AnyOfferChanged

Method can be used to enable and disable notification type

4

Sent test notification

Subscriptions.SendTestNotificationToDestination()

Validates the sqs setup, by sending a test queue

5

Notification triggered on competitors data changes

AnyOfferChangedNotification (  )

* product_id

product_id

Product competitors data

??? get update on merchant price updates

6

7

