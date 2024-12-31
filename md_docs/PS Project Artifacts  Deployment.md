# PS Project Artifacts & Deployment

Please contact DevOps or Pricing team, if you miss some information.

| Name | Base Price Orchestration Service | Details |
|---|---|---|
| PS GIT Repository | https://bitbucket.org/devcst/bps-orchestration/src/master/ | All users under CST group have access |
| PS JIRA | https://cyber-solutions.atlassian.net/secure/RapidBoard.jspa?rapidView=32&projectKey=PAfilter on component = “Pricing Service” | Classical Jira Workflow |
| PS CI/CD | Staging: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/bps-orchestrationPreprod: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/bps-orchestration-preprodProd: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/bps-orchestration-production |  |
| PS Secrets access | - | programmatic |
| PS SQS | Staging:IN:https://sqs.eu-central-1.amazonaws.com/534195382396/dis-to-base-pricehttps://sqs.eu-central-1.amazonaws.com/534195382396/base-price-stg.fifoOUT:https://sqs.eu-central-1.amazonaws.com/534195382396/bps-computed-prices-stgPreprod:IN:https://sqs.eu-central-1.amazonaws.com/704701525355/mps-to-base-price.fifohttps://sqs.eu-central-1.amazonaws.com/704701525355/dis-to-base-priceOUT: https://sqs.eu-central-1.amazonaws.com/704701525355/bps-computed-prices-preprodProd:INhttps://sqs.eu-central-1.amazonaws.com/328072401551/mps-to-base-price.fifohttps://sqs.eu-central-1.amazonaws.com/328072401551/dis-to-base-priceOUT:https://sqs.eu-central-1.amazonaws.com/328072401551/bps-computed-prices-prod! each one of the IN queues above, has one Dead Letter Queue (DLQ) attached (their name is suffixed with -dlq ) |  |
| PS SNS | Staging: topic: arn:aws:sns:eu-central-1:534195382396:mp-screening-notifications-stg.fifo → sending messages with filter policy:{"resource_type": ["merged"]} → to queue arn:aws:sqs:eu-central-1:534195382396:base-price-stg.fifo&&topic: arn:aws:sns:eu-central-1:534195382396:cst-integration-stg-notifications  → sending messages with filter policy: {"resource_type": ["product_price","product_shipping","product_info"]} → to queue arn:aws:sqs:eu-central-1:534195382396:dis-to-base-pricePreprod:  topic: arn:aws:sns:eu-central-1:704701525355:mp-screening-notifications.fifo → sending messages with filter policy:{"resource_type": ["merged"]} → to queue arn:aws:sqs:eu-central-1:704701525355:mps-to-base-price.fifo&&topic: arn:aws:sns:eu-central-1:704701525355:cst-data-integration-preprod-notifications  → sending messages with filter policy: {"resource_type": ["product_price","product_shipping","product_info"]} → to queue arn:aws:sqs:eu-central-1:704701525355:dis-to-base-priceProd:topic: arn:aws:sns:eu-central-1:328072401551:mp-screening-notifications.fifo → sending messages with filter policy:{"resource_type": ["merged"]} → to queue arn:aws:sqs:eu-central-1:328072401551:mps-to-base-price.fifo&&topic: arn:aws:sns:eu-central-1:328072401551:cst-data-integration-notifications  → sending messages with filter policy: {"resource_type": ["product_price","product_shipping","product_info"]} → to queue arn:aws:sqs:eu-central-1:328072401551:dis-to-base-price |  |
| PS Data base | Staging: postgres://cst-staging-1.ci5gbargqglm.eu-central-1.rds.amazonaws.com:5432/bpsorchestrationPreprod:postgres://bpsorchestration-preprd.cykeabspibse.eu-central-1.rds.amazonaws.com/bpsorchestrationProd:postgres://bpsorchestration.cec62psb7xip.eu-central-1.rds.amazonaws.com/bpsorchestrationSee here for tutorial to get latest host name in case it has changed (e.g. on preprod after importing production data base snap shop) Find out data base host name of microservices. | Check out this tutorial to figure out how to access postgres microservice data bases via PyCharm Add DB and data lake connections in PyCharm. |
| PS Sumo Logic | Staging:_source=cst/default/staging AND _sourcecategory = "kubernetes/base/price/orchestration/stg/base/price/orchestration"Preprod:_source=cst/default/preprod AND _sourcecategory = "kubernetes/base/price/orchestration/preprod/base/price/orchestration"Prod:_source=cst/data/production AND _sourcecategory = "kubernetes/base/price/orchestration/service/base/price/orchestration" |  |
| MS New Relic |  |  |
| MS Swagger / API Definition | none yet |  |
| MS Elastic / Kibana | https://cst-monitoring.kb.eu-west-1.aws.found.io:9243/app/discover# | Tutorial on how to use it Log drilling in Kibana |

Name

Base Price Orchestration Service

Details

PS GIT Repository

https://bitbucket.org/devcst/bps-orchestration/src/master/

All users under CST group have access

PS JIRA

https://cyber-solutions.atlassian.net/secure/RapidBoard.jspa?rapidView=32&projectKey=PA

filter on component = “Pricing Service”

Classical Jira Workflow

PS CI/CD

Staging: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/bps-orchestration

Preprod: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/bps-orchestration-preprod

Prod: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/bps-orchestration-production

PS Secrets access

-

programmatic

PS SQS

Staging:

* IN:https://sqs.eu-central-1.amazonaws.com/534195382396/dis-to-base-pricehttps://sqs.eu-central-1.amazonaws.com/534195382396/base-price-stg.fifo
* https://sqs.eu-central-1.amazonaws.com/534195382396/dis-to-base-price
* https://sqs.eu-central-1.amazonaws.com/534195382396/base-price-stg.fifo
* OUT:https://sqs.eu-central-1.amazonaws.com/534195382396/bps-computed-prices-stg
* https://sqs.eu-central-1.amazonaws.com/534195382396/bps-computed-prices-stg

IN:

* https://sqs.eu-central-1.amazonaws.com/534195382396/dis-to-base-price
* https://sqs.eu-central-1.amazonaws.com/534195382396/base-price-stg.fifo

https://sqs.eu-central-1.amazonaws.com/534195382396/dis-to-base-price

https://sqs.eu-central-1.amazonaws.com/534195382396/base-price-stg.fifo

OUT:

* https://sqs.eu-central-1.amazonaws.com/534195382396/bps-computed-prices-stg

https://sqs.eu-central-1.amazonaws.com/534195382396/bps-computed-prices-stg

Preprod:

* IN:https://sqs.eu-central-1.amazonaws.com/704701525355/mps-to-base-price.fifohttps://sqs.eu-central-1.amazonaws.com/704701525355/dis-to-base-price
* https://sqs.eu-central-1.amazonaws.com/704701525355/mps-to-base-price.fifo
* https://sqs.eu-central-1.amazonaws.com/704701525355/dis-to-base-price
* OUT: https://sqs.eu-central-1.amazonaws.com/704701525355/bps-computed-prices-preprod
* https://sqs.eu-central-1.amazonaws.com/704701525355/bps-computed-prices-preprod

IN:

* https://sqs.eu-central-1.amazonaws.com/704701525355/mps-to-base-price.fifo
* https://sqs.eu-central-1.amazonaws.com/704701525355/dis-to-base-price

https://sqs.eu-central-1.amazonaws.com/704701525355/mps-to-base-price.fifo

https://sqs.eu-central-1.amazonaws.com/704701525355/dis-to-base-price

OUT:

* https://sqs.eu-central-1.amazonaws.com/704701525355/bps-computed-prices-preprod

https://sqs.eu-central-1.amazonaws.com/704701525355/bps-computed-prices-preprod

Prod:

* INhttps://sqs.eu-central-1.amazonaws.com/328072401551/mps-to-base-price.fifohttps://sqs.eu-central-1.amazonaws.com/328072401551/dis-to-base-price
* https://sqs.eu-central-1.amazonaws.com/328072401551/mps-to-base-price.fifo
* https://sqs.eu-central-1.amazonaws.com/328072401551/dis-to-base-price
* OUT:https://sqs.eu-central-1.amazonaws.com/328072401551/bps-computed-prices-prod
* https://sqs.eu-central-1.amazonaws.com/328072401551/bps-computed-prices-prod

IN

* https://sqs.eu-central-1.amazonaws.com/328072401551/mps-to-base-price.fifo
* https://sqs.eu-central-1.amazonaws.com/328072401551/dis-to-base-price

https://sqs.eu-central-1.amazonaws.com/328072401551/mps-to-base-price.fifo

https://sqs.eu-central-1.amazonaws.com/328072401551/dis-to-base-price

OUT:

* https://sqs.eu-central-1.amazonaws.com/328072401551/bps-computed-prices-prod

https://sqs.eu-central-1.amazonaws.com/328072401551/bps-computed-prices-prod

! each one of the IN queues above, has one Dead Letter Queue (DLQ) attached (their name is suffixed with -dlq )

PS SNS

Staging: topic: arn:aws:sns:eu-central-1:534195382396:mp-screening-notifications-stg.fifo → sending messages with filter policy:{"resource_type": ["merged"]} → to queue arn:aws:sqs:eu-central-1:534195382396:base-price-stg.fifo&&topic: arn:aws:sns:eu-central-1:534195382396:cst-integration-stg-notifications  → sending messages with filter policy: {"resource_type": ["product_price","product_shipping","product_info"]} → to queue arn:aws:sqs:eu-central-1:534195382396:dis-to-base-price

Preprod:  topic: arn:aws:sns:eu-central-1:704701525355:mp-screening-notifications.fifo → sending messages with filter policy:{"resource_type": ["merged"]} → to queue arn:aws:sqs:eu-central-1:704701525355:mps-to-base-price.fifo&&topic: arn:aws:sns:eu-central-1:704701525355:cst-data-integration-preprod-notifications  → sending messages with filter policy: {"resource_type": ["product_price","product_shipping","product_info"]} → to queue arn:aws:sqs:eu-central-1:704701525355:dis-to-base-price

Prod:topic: arn:aws:sns:eu-central-1:328072401551:mp-screening-notifications.fifo → sending messages with filter policy:{"resource_type": ["merged"]} → to queue arn:aws:sqs:eu-central-1:328072401551:mps-to-base-price.fifo&&topic: arn:aws:sns:eu-central-1:328072401551:cst-data-integration-notifications  → sending messages with filter policy: {"resource_type": ["product_price","product_shipping","product_info"]} → to queue arn:aws:sqs:eu-central-1:328072401551:dis-to-base-price

PS Data base

Staging: postgres://cst-staging-1.ci5gbargqglm.eu-central-1.rds.amazonaws.com:5432/bpsorchestrationPreprod:postgres://bpsorchestration-preprd.cykeabspibse.eu-central-1.rds.amazonaws.com/bpsorchestrationProd:postgres://bpsorchestration.cec62psb7xip.eu-central-1.rds.amazonaws.com/bpsorchestration

See here for tutorial to get latest host name in case it has changed (e.g. on preprod after importing production data base snap shop) Find out data base host name of microservices.

Check out this tutorial to figure out how to access postgres microservice data bases via PyCharm Add DB and data lake connections in PyCharm.

PS Sumo Logic

Staging:_source=cst/default/staging AND _sourcecategory = "kubernetes/base/price/orchestration/stg/base/price/orchestration"Preprod:_source=cst/default/preprod AND _sourcecategory = "kubernetes/base/price/orchestration/preprod/base/price/orchestration"Prod:_source=cst/data/production AND _sourcecategory = "kubernetes/base/price/orchestration/service/base/price/orchestration"

MS New Relic

MS Swagger / API Definition

none yet

MS Elastic / Kibana

https://cst-monitoring.kb.eu-west-1.aws.found.io:9243/app/discover#

Tutorial on how to use it Log drilling in Kibana

