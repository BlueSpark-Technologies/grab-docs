# PS Escalation Scenarios & Tutorials

| Scenario | Action | who? | Ticket / Link to documentation |
|---|---|---|---|
| Due to Cyberparts maintenance price files can’t be imported | Export should be deactivated, but price calculation not Remove SAP Pro and BI SNS Queue credentials from Kubernetes. The simplest solution any member of our team can do is to simply delete the PRICE_EXPORT_SQS_URL environment variable stored in secrets manager and trigger a deployment (no need to rebuild the image, just deploy the last app image) and in less than 5 minutes no more prices will be pushed to the queue. If by any chance, at the same time this action needs to be performed and  some argo c-workflow which exports data in the base-price-orchestration-service namespace is also running, make sure that you manually Terminate or Delete it (otherwise it will continue exporting prices).→ exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instructionInform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke) After SAP Pro is up again, cleanse all messages on the SAP Pro queue and retrigger autopricing for all productsInform business stakeholders that the problem is resolved | Devs | https://bitbucket.org/devcst/pricing/src/master/README.md |
| SAP Pro is down | Export should be deactivated, but price calculation not Remove SAP Pro and BI SNS Queue credentials from Kubernetes. The simplest solution any member of our team can do is to simply delete the PRICE_EXPORT_SQS_URL environment variable stored in secrets manager and trigger a deployment (no need to rebuild the image, just deploy the last app image) and in less than 5 minutes no more prices will be pushed to the queue. If by any chance, at the same time this action needs to be performed and  some argo c-workflow which exports data in the base-price-orchestration-service namespace is also running, make sure that you manually Terminate or Delete it (otherwise it will continue exporting prices).→ exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instructionInform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke) After SAP Pro is up again, cleanse all messages on the SAP Pro queue and retrigger autopricing for all productsInform business stakeholders that the problem is resolved | Devs |  |
| More than 10.000 messages on the queue | Check if SAP Pro is still up and running and talk to Sebastian Moch or Ralph Friedberg. | Devs |  |
| Faulty data has flushed DIS, MPS or ECOMM → roll back prices, if the current ones don’t make sense | Deactivate regular price export jobs in Pricing Service (i.e. by pausing argo jobs)Figure out if prices are okay or not. If not, go to step 3. If not go to step 4. Fix the pricesPO: Find a point in time where we trusted the prices, talk to Stefan Rohne to discuss thisPO: communicate with Torsten Liebig when and how many price we maximally export → amount xDevs: call management command defined in the README of the repo with this point in time and export limit x as input parameters→ this exports most x important latest prices of all products that have been exported since then, have a non-null price and are exportable, to the Queue, save new rows in the db and in Athena with new exported_at timestamp and new updated_at fieldsInform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke) Inform DIS / MPS / ECOMM team that they need to inform us once all data is fresh again and correctWait until the broken service has successfully processed fresh data for all products (i.e. for DIS that would be from SAP Pro, for MPS that would be new feed data)Cleanse all three queues, MPS, ECOMM and DIS and empty the cacheRetrigger autopricing for all products with management command define in the README of the repoOnly after this trigger is 100% done, reactivate price export in Pricing ServiceInform business stakeholders that the problem is resolved |  | PA-459
                    -
            Getting issue details...
STATUS

https://bitbucket.org/devcst/pricing/src/master/README.md |
| DIS / ECOMM / MPS is / was down | Deactivate regular price export jobs in Pricing Service (i.e. by pausing argo jobs), because even if DIS gets up again, at first it will only respond with outdated data. Figure out if prices are okay or not, i.e if faulty data has been processed by DIS. If not, go to step 3. If data is just outdated but not faulty, go to step 4. Fix the pricesPO: Find a point in time where we trusted the prices, talk to Stefan Rohne to discuss this - usually prices are okay if e.g. was just down. PO: communicate with Torsten Liebig when and how many price we maximally export → amount xDevs: call management command defined in the README of the repo with this point in time and export limit x as input parameters→ this exports most x important latest prices of all products that have been exported since then, have a non-null price and are exportable, to the Queue, save new rows in the db and in Athena with new exported_at timestamp and new updated_at fieldsInform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke) Inform DIS / ECOMM team that they need to inform us once all data is fresh again and correctWait until the broken service has successfully processed fresh data for all products (i.e. for DIS that would be from SAP Pro)Cleanse all three queues, MPS, ECOMM and DIS and empty the cacheRetrigger autopricing for all products with management command define in the README of the repoOnly after this trigger is 100% done, reactivate regular price export in Pricing ServiceInform business stakeholders that the problem is resolved | Devs |  |
| PS is / was down | PO: Inform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke) Dev: Get PS running againPause regular price export argo jobs as soon as possibleClear MPS and DIS queues and invalidate cache for all products. Don’t clear ECS queue. Reimport latest base prices from DIS. Retrigger autopricing for all products with management command define in the README of the repoOnly after this trigger is 100% done, reactivate regular price export in Pricing ServiceInform business stakeholders that the problem is resolved | Devs | https://bitbucket.org/devcst/pricing/src/master/README.md |
| Maintaining mail addresses of CMs for suspicious price alerts | (There is a more detailed version of what needs to be done in the linked page.)Delete old CSV file from S3 bucketUpload updated CSV file to S3 bucketAsk a dev with access to the Kubernetes cluster to log on, and run the flask command which will download the csv and add CM data to the category_manager table in the database. This command will also automatically subscribe CMs to the topicAfter the cm data is added to the table, ask a dev to get the id of the default CM. The id must than be added to the Secrets Manager in AWS and a new deploy must be done for it to take effectLet the CMs know they will get an email from AWS and that they should confirm the subscription to the suspicious prices topic | Devs | How to manage CM emails table 

 PA-373
                    -
            Getting issue details...
STATUS

 

 PA-476
                    -
            Getting issue details...
STATUS |
|  |  |  |  |

Scenario

Action

who?

Ticket / Link to documentation

Due to Cyberparts maintenance price files can’t be imported

Export should be deactivated, but price calculation not

Remove SAP Pro and BI SNS Queue credentials from Kubernetes. The simplest solution any member of our team can do is to simply delete the PRICE_EXPORT_SQS_URL environment variable stored in secrets manager and trigger a deployment (no need to rebuild the image, just deploy the last app image) and in less than 5 minutes no more prices will be pushed to the queue. If by any chance, at the same time this action needs to be performed and  some argo c-workflow which exports data in the base-price-orchestration-service namespace is also running, make sure that you manually Terminate or Delete it (otherwise it will continue exporting prices).→ exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instruction

Inform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke)

After SAP Pro is up again, cleanse all messages on the SAP Pro queue and retrigger autopricing for all products

Inform business stakeholders that the problem is resolved

Devs

https://bitbucket.org/devcst/pricing/src/master/README.md

SAP Pro is down

Export should be deactivated, but price calculation not

Remove SAP Pro and BI SNS Queue credentials from Kubernetes. The simplest solution any member of our team can do is to simply delete the PRICE_EXPORT_SQS_URL environment variable stored in secrets manager and trigger a deployment (no need to rebuild the image, just deploy the last app image) and in less than 5 minutes no more prices will be pushed to the queue. If by any chance, at the same time this action needs to be performed and  some argo c-workflow which exports data in the base-price-orchestration-service namespace is also running, make sure that you manually Terminate or Delete it (otherwise it will continue exporting prices).→ exports will fail → data is pushed to Athena, but exported_at will always be empty → can be done within 5min after instruction

Inform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke)

After SAP Pro is up again, cleanse all messages on the SAP Pro queue and retrigger autopricing for all products

Inform business stakeholders that the problem is resolved

Devs

More than 10.000 messages on the queue

Check if SAP Pro is still up and running and talk to Sebastian Moch or Ralph Friedberg.

Devs

Faulty data has flushed DIS, MPS or ECOMM → roll back prices, if the current ones don’t make sense

Deactivate regular price export jobs in Pricing Service (i.e. by pausing argo jobs)

Figure out if prices are okay or not. If not, go to step 3. If not go to step 4.

Fix the prices

PO: Find a point in time where we trusted the prices, talk to Stefan Rohne to discuss this

PO: communicate with Torsten Liebig when and how many price we maximally export → amount x

Devs: call management command defined in the README of the repo with this point in time and export limit x as input parameters→ this exports most x important latest prices of all products that have been exported since then, have a non-null price and are exportable, to the Queue, save new rows in the db and in Athena with new exported_at timestamp and new updated_at fields

Inform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke)

Inform DIS / MPS / ECOMM team that they need to inform us once all data is fresh again and correct

Wait until the broken service has successfully processed fresh data for all products (i.e. for DIS that would be from SAP Pro, for MPS that would be new feed data)

Cleanse all three queues, MPS, ECOMM and DIS and empty the cache

Retrigger autopricing for all products with management command define in the README of the repo

Only after this trigger is 100% done, reactivate price export in Pricing Service

Inform business stakeholders that the problem is resolved

PA-459
                    -
            Getting issue details...
STATUS

https://bitbucket.org/devcst/pricing/src/master/README.md

DIS / ECOMM / MPS is / was down

Deactivate regular price export jobs in Pricing Service (i.e. by pausing argo jobs), because even if DIS gets up again, at first it will only respond with outdated data.

Figure out if prices are okay or not, i.e if faulty data has been processed by DIS. If not, go to step 3. If data is just outdated but not faulty, go to step 4.

Fix the prices

PO: Find a point in time where we trusted the prices, talk to Stefan Rohne to discuss this - usually prices are okay if e.g. was just down.

PO: communicate with Torsten Liebig when and how many price we maximally export → amount x

Devs: call management command defined in the README of the repo with this point in time and export limit x as input parameters→ this exports most x important latest prices of all products that have been exported since then, have a non-null price and are exportable, to the Queue, save new rows in the db and in Athena with new exported_at timestamp and new updated_at fields

Inform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke)

Inform DIS / ECOMM team that they need to inform us once all data is fresh again and correct

Wait until the broken service has successfully processed fresh data for all products (i.e. for DIS that would be from SAP Pro)

Cleanse all three queues, MPS, ECOMM and DIS and empty the cache

Retrigger autopricing for all products with management command define in the README of the repo

Only after this trigger is 100% done, reactivate regular price export in Pricing Service

Inform business stakeholders that the problem is resolved

Devs

PS is / was down

PO: Inform business stakeholders (Stefan Rohne or Claudia Esterl or Philipp Gambke)

Dev: Get PS running again

Pause regular price export argo jobs as soon as possible

Clear MPS and DIS queues and invalidate cache for all products. Don’t clear ECS queue.

Reimport latest base prices from DIS.

Retrigger autopricing for all products with management command define in the README of the repo

Only after this trigger is 100% done, reactivate regular price export in Pricing Service

Inform business stakeholders that the problem is resolved

Devs

https://bitbucket.org/devcst/pricing/src/master/README.md

Maintaining mail addresses of CMs for suspicious price alerts

(There is a more detailed version of what needs to be done in the linked page.)

Delete old CSV file from S3 bucket

Upload updated CSV file to S3 bucket

Ask a dev with access to the Kubernetes cluster to log on, and run the flask command which will download the csv and add CM data to the category_manager table in the database. This command will also automatically subscribe CMs to the topic

After the cm data is added to the table, ask a dev to get the id of the default CM. The id must than be added to the Secrets Manager in AWS and a new deploy must be done for it to take effect

Let the CMs know they will get an email from AWS and that they should confirm the subscription to the suspicious prices topic

Devs

How to manage CM emails table

PA-373
                    -
            Getting issue details...
STATUS

PA-476
                    -
            Getting issue details...
STATUS

