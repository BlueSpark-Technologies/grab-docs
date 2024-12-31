# MPS Project Artifacts & Deployments

Please contact DevOps or Pricing team, if you miss some information.

| Name | Url | Details |
|---|---|---|
| MPS GIT Repository | https://bitbucket.org/devcst/market-price-screening/src/master/ | All users under CST group have access |
| MPS Jira - Backlog | https://cyber-solutions.atlassian.net/secure/RapidBoard.jspa?projectKey=PA&quickFilter=92 | Classical Jira Workflow |
| MPS Jira - Kanban | https://cyber-solutions.atlassian.net/secure/RapidBoard.jspa?rapidView=50&projectKey=PA | Kanban Board |
| MPS CI/CD | STG: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screeningPREproduction: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening-preprodPRODUCTION: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening-productionMPS Austrian: STG: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-autPREproduction: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut-preprodPRODUCTION: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut-prod | Default deployment to stagingMPS Austrian: default deployment to staging |
| MPS Secrets access | to be filled | Programmatic access only. WIP |
| MPS SNS topic | STG: mp-screening-notifications-stg.fifoPREproduction: mp-screening-notifications-preprod.fifoPRODUCTION:  mp-screening-notifications.fifoMPS Austrian: no SNS topic yet |  |
| MPS S3 | STG: https://s3.console.aws.amazon.com/s3/buckets/pse-feed/ for staging PREproduction: https://s3.console.aws.amazon.com/s3/buckets/pse-feed-preprod PRODUCTION: https://s3.console.aws.amazon.com/s3/buckets/feedservice/ MPS Austrian: STG: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-stgPREproduction: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-preprodPRODUCTION: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-prod | for staging use the cst-staging environment.for production use the cst-staging environment and Read-Development role. |
| MPS Data base | cst-staging-1.ci5gbargqglm.eu-central-1.rds.amazonaws.com/mpscreening for stagingmkpscreening.cec62psb7xip.eu-central-1.rds.amazonaws.com/mkpscreening for productionmpscreening-preprod.cykeabspibse.eu-central-1.rds.amazonaws.com/mpscreening for preprodMPS Austrian: no DB yetSee here for tutorial to get latest host name in case it has changed (e.g. on preprod after importing production data base snap shop) Find out data base host name of microservices. | Check out this tutorial to figure out how to access postgres microservice data bases via PyCharm Add DB and data lake connections in PyCharm. |
| MPS Sumologic dashboards | to be filled |  |
| MPS New relic | https://one.eu.newrelic.com/launcher/nr1-core.explorer?pane=eyJuZXJkbGV0SWQiOiJhcG0tbmVyZGxldHMub3ZlcnZpZXciLCJlbnRpdHlJZCI6Ik1qY3dNREV4TVh4QlVFMThRVkJRVEVsRFFWUkpUMDU4TnpRMk9UUTRORGMifQ==&sidebars[0]=eyJuZXJkbGV0SWQiOiJucjEtY29yZS5hY3Rpb25zIiwiZW50aXR5SWQiOiJNamN3TURFeE1YeEJVRTE4UVZCUVRFbERRVlJKVDA1OE56UTJPVFE0TkRjIiwic2VsZWN0ZWROZXJkbGV0Ijp7Im5lcmRsZXRJZCI6ImFwbS1uZXJkbGV0cy5vdmVydmlldyJ9fQ==&platform[accountId]=2666361&platform[timeRange][duration]=1800000&platform[$isFallbackTimeRange]=true |  |
| MPS Swagger / API Definition | production: https://market-price-screening.service.cybersolutions-tech.com/api/docs/pre-production: https://market-price-screening.preprod.cybersolutions-tech.com/api/docs/staging: https://market-price-screening.stg.cybersolutions-tech.com/api/docs/ |  |
| MPS Elastic / Kibana | https://cst-monitoring.kb.eu-west-1.aws.found.io:9243/app/discover# | Tutorial on how to use it Log drilling in Kibana |

Name

Url

Details

MPS GIT Repository

https://bitbucket.org/devcst/market-price-screening/src/master/

All users under CST group have access

MPS Jira - Backlog

https://cyber-solutions.atlassian.net/secure/RapidBoard.jspa?projectKey=PA&quickFilter=92

Classical Jira Workflow

MPS Jira - Kanban

https://cyber-solutions.atlassian.net/secure/RapidBoard.jspa?rapidView=50&projectKey=PA

Kanban Board

MPS CI/CD

* STG: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening
* PREproduction: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening-preprod
* PRODUCTION: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening-production

STG: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening

PREproduction: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening-preprod

PRODUCTION: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/market-price-screening-production

MPS Austrian:

* STG: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut
* PREproduction: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut-preprod
* PRODUCTION: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut-prod

STG: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut

PREproduction: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut-preprod

PRODUCTION: https://concourse.ops.cybersolutions-tech.com/teams/dev-cst/pipelines/mps-aut-prod

Default deployment to staging

MPS Austrian:

default deployment to staging

MPS Secrets access

to be filled

Programmatic access only. WIP

MPS SNS topic

* STG: mp-screening-notifications-stg.fifo
* PREproduction: mp-screening-notifications-preprod.fifo
* PRODUCTION:  mp-screening-notifications.fifo

STG: mp-screening-notifications-stg.fifo

PREproduction: mp-screening-notifications-preprod.fifo

PRODUCTION:  mp-screening-notifications.fifo

MPS Austrian: no SNS topic yet

MPS S3

* STG: https://s3.console.aws.amazon.com/s3/buckets/pse-feed/ for staging
* PREproduction: https://s3.console.aws.amazon.com/s3/buckets/pse-feed-preprod
* PRODUCTION: https://s3.console.aws.amazon.com/s3/buckets/feedservice/

STG: https://s3.console.aws.amazon.com/s3/buckets/pse-feed/ for staging

PREproduction: https://s3.console.aws.amazon.com/s3/buckets/pse-feed-preprod

PRODUCTION: https://s3.console.aws.amazon.com/s3/buckets/feedservice/

MPS Austrian:

* STG: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-stg
* PREproduction: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-preprod
* PRODUCTION: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-prod

STG: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-stg

PREproduction: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-preprod

PRODUCTION: https://s3.console.aws.amazon.com/s3/buckets/mps-aut-prod

* for staging use the cst-staging environment.
* for production use the cst-staging environment and Read-Development role.

for staging use the cst-staging environment.

for production use the cst-staging environment and Read-Development role.

MPS Data base

cst-staging-1.ci5gbargqglm.eu-central-1.rds.amazonaws.com/mpscreening for staging

mkpscreening.cec62psb7xip.eu-central-1.rds.amazonaws.com/mkpscreening for production

mpscreening-preprod.cykeabspibse.eu-central-1.rds.amazonaws.com/mpscreening for preprod

MPS Austrian: no DB yet

See here for tutorial to get latest host name in case it has changed (e.g. on preprod after importing production data base snap shop) Find out data base host name of microservices.

Check out this tutorial to figure out how to access postgres microservice data bases via PyCharm Add DB and data lake connections in PyCharm.

MPS Sumologic dashboards

to be filled

MPS New relic

https://one.eu.newrelic.com/launcher/nr1-core.explorer?pane=eyJuZXJkbGV0SWQiOiJhcG0tbmVyZGxldHMub3ZlcnZpZXciLCJlbnRpdHlJZCI6Ik1qY3dNREV4TVh4QlVFMThRVkJRVEVsRFFWUkpUMDU4TnpRMk9UUTRORGMifQ==&sidebars[0]=eyJuZXJkbGV0SWQiOiJucjEtY29yZS5hY3Rpb25zIiwiZW50aXR5SWQiOiJNamN3TURFeE1YeEJVRTE4UVZCUVRFbERRVlJKVDA1OE56UTJPVFE0TkRjIiwic2VsZWN0ZWROZXJkbGV0Ijp7Im5lcmRsZXRJZCI6ImFwbS1uZXJkbGV0cy5vdmVydmlldyJ9fQ==&platform[accountId]=2666361&platform[timeRange][duration]=1800000&platform[$isFallbackTimeRange]=true

MPS Swagger / API Definition

* production: https://market-price-screening.service.cybersolutions-tech.com/api/docs/
* pre-production: https://market-price-screening.preprod.cybersolutions-tech.com/api/docs/
* staging: https://market-price-screening.stg.cybersolutions-tech.com/api/docs/

production: https://market-price-screening.service.cybersolutions-tech.com/api/docs/

pre-production: https://market-price-screening.preprod.cybersolutions-tech.com/api/docs/

staging: https://market-price-screening.stg.cybersolutions-tech.com/api/docs/

MPS Elastic / Kibana

https://cst-monitoring.kb.eu-west-1.aws.found.io:9243/app/discover#

Tutorial on how to use it Log drilling in Kibana

