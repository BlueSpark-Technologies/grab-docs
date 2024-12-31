# Go Live review of MS7

During the Go-Live process following problems/issues were faced:

27.07.2023. The webshop campaign didn’t start at the right moment.

Important campaign for Samsung products has been not started at the right moment because it was scheduled for the same time as Cyberparts started to mark channels as obsolete.

Lesson learned:

* don’t plan any activities when the release or change is going live.

don’t plan any activities when the release or change is going live.

28.07.2023. Consuming channel price notifications in the webshop took longer than expected

Webshop has finished consuming notifications only at the end of the next day. SAP / Algolia consumed notifications much faster and for this time there were price differences in these systems

Lesson learned:

* don’t take many activities on the same day
* no activities on Wednesday
* perfect day for taking any changes live is Monday
* find a way to send notifications to all consumers with different speeds so that the prices will stay the same everywhere

don’t take many activities on the same day

no activities on Wednesday

perfect day for taking any changes live is Monday

find a way to send notifications to all consumers with different speeds so that the prices will stay the same everywhere

28.07.2023. Price labels in stores can’t handle notifications with multiple prices in the notification and took only the last one which was not always the actual one.

There was no information about how Breece can handle price notifications

Lesson learned:

* Better documentation about all dependencies in all consumers for prices

Better documentation about all dependencies in all consumers for prices

