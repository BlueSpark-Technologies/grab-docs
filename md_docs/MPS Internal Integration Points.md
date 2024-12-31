# MPS Internal Integration Points

Currently we have one SNS fifo topic in MPS, that an external service can subscribe to. After that each subscribing client has its own SNS queue, from which messages can be processed and deleted - see MPS Component Diagram for details.

You can subscribe to supplier specific and merged data.

## Supplier specific
Contains data separated for each subscribed product feed supplier (GZH, WIT and/or IDL).

* After a new file is finished processing, for each sku it is checked if the list of competitors, their prices, availabilities, shipping costs and so on is different than in the previous entry in the data base based on provider_item_updated_at column for the same my_sku and the same product_feed_code.
* Only if that is the case a notification on the provider_feed_items topic is pushed containing the following body: 
{
  "Type": "Notification",
  "MessageId": "b6ea0428-399b-5567-80b2-5ca08654cdc7",
  "SequenceNumber": "10000000000002103757",
  "TopicArn": "arn:aws:sns:eu-central-1:534195382396:mp-screening-notifications-stg.fifo",
  "Message": "{\"feed_item\": {\"my_shipping_cost\": 599, \"provider_item_updated_at\": \"2021-01-25T01:29:09\", \"provider_item_name\": \"Lexmark 76C00K0 R\\u00fcckgabe-Toner Schwarz f\\u00fcr ca. 18.500 Seiten\", \"asin\":\"B03Z5NUG12\", \"my_price\": 22100, \"my_availability\": \"2\", \"id\": \"4c5721b8-96c6-4657-be8f-a1255d6d7c32\", \"ean\": \"734646635035\", \"created_at\": \"2021-01-25T12:46:07.148016\", \"provider_item_id\": \"1355006\", \"provider_id\": \"031fbbd1-f1d1-4472-a292-41857d16dae6\", \"my_ranking\": null, \"my_sku\": \"6703-6FY\", \"provider_file_created_at\": \"2021-01-25T12:07:00\"}, \"feed_item_merchants\": [{\"availability\": \"0\", \"merchant_id\": \"6293efae-cf81-4169-aa76-fc1023ecc8cd\", \"feed_item_id\": \"4c5721b8-96c6-4657-be8f-a1255d6d7c32\", \"price\": 16369, \"shipping_cost\": 0, \"created_at\": \"2021-01-25T12:46:07.154404\"}]}",
  "Timestamp": "2021-01-25T12:46:07.221Z",
  "UnsubscribeURL": "https://sns.eu-central-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-central-1:534195382396:mp-screening-notifications-stg.fifo:d235a8dc-c595-45bd-8133-400a732e0ec6",
  "MessageAttributes": {
    "business_unit_id": {
      "Type": "String",
      "Value": "CP"
    },
    "service_name": {
      "Type": "String",
      "Value": "market-price-screening"
    },
    "resource_type": {
      "Type": "String",
      "Value": "WIT"
    }
  }
}

After a new file is finished processing, for each sku it is checked if the list of competitors, their prices, availabilities, shipping costs and so on is different than in the previous entry in the data base based on provider_item_updated_at column for the same my_sku and the same product_feed_code.

Only if that is the case a notification on the provider_feed_items topic is pushed containing the following body:

## Merged
Contains data merged across all available and activated product feed suppliers.

Merged:

* After a new file is finished processing, the feed supplier merging algorithm is executed (see here for details https://cyber-solutions.atlassian.net/wiki/spaces/PSE/pages/369721360/MPS+Algorithm#Feed-Supplier-Merging-Algorithm).
* Only if the list of competitors, their prices, availabilities, shipping costs and so on is different than in the previous entry in the data base based on provider_item_updated_at column for an sku, a notification is pushed.
* It contains the following body: 
{
  "Type": "Notification",
  "MessageId": "d8d4b350-c94a-52a6-b3e7-ebd849e08c2e",
  "SequenceNumber": "10000000000002035523",
  "TopicArn": "arn:aws:sns:eu-central-1:534195382396:mp-screening-notifications-stg.fifo",
  "Message": "{\"feed_item\": {\"ean\": null, \"asin\":\"B03Z5NUG12\", \"id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"provider_file_created_at\": \"2021-01-25T08:00:04\", \"my_ranking\": 2, \"my_sku\": \"K758-103\", \"my_availability\": \"2\", \"provider_item_name\": \"Caso 01221 Folienrolle 20x600cm, 2 St\\u00fcck\", \"provider_id\": \"4c5644ed-0f95-433b-8ed4-2b45d84784a6\", \"provider_item_id\": \"894350\", \"my_price\": 1290, \"my_shipping_cost\": 0, \"provider_item_updated_at\": \"2021-01-25T08:18:00\", \"created_at\": \"2021-01-25T08:16:42.274413\"}, \"feed_item_merchants\": [{\"merchant_id\": \"6db8faef-369a-40e4-8526-b5c7c78345a8\", \"price\": 1115, \"availability\": \"1\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 599, \"created_at\": \"2021-01-25T08:16:42.276814\"}, {\"merchant_id\": \"259aee6a-8577-4474-8611-9f4003668d33\", \"price\": 1290, \"availability\": \"2\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 499, \"created_at\": \"2021-01-25T08:16:42.282028\"}, {\"merchant_id\": \"1ddd7bbf-9eb6-4a49-8bf8-06bee9a30b9d\", \"price\": 1290, \"availability\": \"0\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": null, \"created_at\": \"2021-01-25T08:16:42.283404\"}, {\"merchant_id\": \"6293efae-cf81-4169-aa76-fc1023ecc8cd\", \"price\": 1299, \"availability\": \"0\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 399, \"created_at\": \"2021-01-25T08:16:42.285052\"}, {\"merchant_id\": \"63958a6f-1c10-4c78-b0f8-f0da7f25b7b4\", \"price\": 1299, \"availability\": \"0\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 595, \"created_at\": \"2021-01-25T08:16:42.287488\"}, {\"merchant_id\": \"7a08eb51-a485-4863-b44a-41bf0cc6a4f2\", \"price\": 1311, \"availability\": \"1\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 499, \"created_at\": \"2021-01-25T08:16:42.288913\"}, {\"merchant_id\": \"3a6b697e-e359-4349-bd68-d18ce044ac58\", \"price\": 1311, \"availability\": \"1\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 595, \"created_at\": \"2021-01-25T08:16:42.290139\"}, {\"merchant_id\": \"53095635-ab1a-416e-b37b-2e9e73a23e76\", \"price\": 1313, \"availability\": \"2\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 299, \"created_at\": \"2021-01-25T08:16:42.296172\"}, {\"merchant_id\": \"c1bd0079-e4af-4c9d-b661-b8093e6e4111\", \"price\": 1313, \"availability\": \"2\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 299, \"created_at\": \"2021-01-25T08:16:42.297482\"}, {\"merchant_id\": \"b368e876-c19c-4af4-9cb5-db0ee6378f6c\", \"price\": 1399, \"availability\": \"1\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 665, \"created_at\": \"2021-01-25T08:16:42.300095\"}, {\"merchant_id\": \"7a78ab43-af9b-4a9d-8d08-2c5e78c9939d\", \"price\": 1499, \"availability\": \"2\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 899, \"created_at\": \"2021-01-25T08:16:42.302979\"}, {\"merchant_id\": \"a0be888b-b0e2-4cc1-892d-0b32a048ec47\", \"price\": 1621, \"availability\": \"0\", \"feed_item_id\": \"442e094a-0e15-475d-a8a4-a0772e3618cc\", \"shipping_cost\": 549, \"created_at\": \"2021-01-25T08:16:42.304595\"}]}",
  "Timestamp": "2021-01-25T08:16:42.386Z",
  "UnsubscribeURL": "https://sns.eu-central-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-central-1:534195382396:mp-screening-notifications-stg.fifo:f8dc8d13-a594-4707-b84e-d1539686d99f",
  "MessageAttributes": {
    "business_unit_id": {
      "Type": "String",
      "Value": "CP"
    },
    "service_name": {
      "Type": "String",
      "Value": "market-price-screening"
    },
    "resource_type": {
      "Type": "String",
      "Value": "merged"
    }
  }
}

After a new file is finished processing, the feed supplier merging algorithm is executed (see here for details https://cyber-solutions.atlassian.net/wiki/spaces/PSE/pages/369721360/MPS+Algorithm#Feed-Supplier-Merging-Algorithm).

Only if the list of competitors, their prices, availabilities, shipping costs and so on is different than in the previous entry in the data base based on provider_item_updated_at column for an sku, a notification is pushed.

It contains the following body:

Looking at the two message bodies from above, the main key in MessageAttributes is resource_type, which is the field based on which the AWS SNS filters the messages (while service_name and business_unit_id are just metadata, similar to the one Data Integration Service uses)The  Message  field, is a JSON-escaped object, identical to https://market-price-screening.service.cybersolutions-tech.com/v0/merged-feed-items-details/K758-103

