# How to manage CM emails table

The CM email table in BPS Orchestration is used to notify CMs about suspicious prices.

Get the excel file and do the following:

Next, login to your AWS account using SSO, search for S3 and find the base-price-orch-export-bi bucket.

Next steps:

* connect to a pod via Lens or your preferred app and run the following flask command: flask populate-cm-table
* flask populate-cm-table
* after the command has finished importing the CM names and emails, delete the csv file from S3

connect to a pod via Lens or your preferred app and run the following flask command:

* flask populate-cm-table

flask populate-cm-table

after the command has finished importing the CM names and emails, delete the csv file from S3

IMPORTANT:Emails with suspicious prices are usually sent to the regular CM. If the regular CM is not subscribed to the email notifications than the email is sent to the default CM.

The default CM’s id must be copied from the production table and pasted into the secrets manager under the `DEFAULT_CM_ID` env variable. This step is mandatory if this is the first time the emails are being imported or if the default CM has changed.

This must be done by someone on the development team.

IMPORTANT 2:

If the production environment is ready to send emails with suspicious prices, make sure the env variable SUSPICIOUS_NOTIFICATION_ENABLED is set to true, otherwise emails will not be sent out.

IMPORTANT 3:

Please note that the name csv field contains a ,  which separates the First and Last name. Because of that, make sure that when you copy the name field, it’s properly quoted i.e.”Doe, John",john.doe@unknown.com   ✅ ok Doe, John,john.doe@unknown.com  😢 not ok

# Updating the email table
If a request comes regarding adding new names to the CM table follow these steps:

add the names and emails of the CMS in the category_manager table by hand

in a pod run the flask job flask subscribe-cms-to-email-alerts  which will subscribe the CMs to the SNS topic

follow the progress here https://eu-central-1.console.aws.amazon.com/sns/v3/home?region=eu-central-1#/topic/arn:aws:sns:eu-central-1:328072401551:bps-suspicious-prices

