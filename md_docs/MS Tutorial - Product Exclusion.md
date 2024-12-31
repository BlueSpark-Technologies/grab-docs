# MS Tutorial - Product Exclusion

In some cases manual pricing is necessary for products on Amazon. Therefore we have an exclusion list that avoids unwanted automatic price changes from the MS Pricing Service. Setting a manual price row will not be sufficient as the automatic export via FTP server (see here MS FTP Server) will delete manual prices rows. This is implemented within Cyberparts and outside of our control.

After putting a product on the exclusion list, the Amazon channel price can be changed in Cyberparts. It is important that the respective user keeps this manual price up to date, as it is not monitored by the Marketplace Service anymore.

## Access to the Exclusion List
If you need access to the exclusion list, please contact Aleksander Meier .

## Tutorial
This tutorial explains how you can add or remove a product to the Amazon autopricing exclusion list.

The exclusion list is available in the marketplace-pricing-configuration-prod s3 bucket of the production account (328072401551) accessible via the following link https://s3.console.aws.amazon.com/s3/buckets/marketplace-pricing-configuration-prod.

Open the console and you will see the following page:

2. Mark the file (check the box on the left) and click on Actions → Open or Download

3. On your local machine, add new products or remove products that should not be excluded anymore.

The format of the file is as follows:

a one-column csv with EXCLUDED_PRODUCT_SKU as header and the next lines will contain the desired excluded product skus, one per row.Just to be consistent with the csv files that the service is exporting, the csv separator is ; but there is no need to provide one, since it’s a one column csv.

If no product is desired to be on the excluded list, just leave the csv file empty (containing the header or without it), but DON’T delete this file because the application is expecting it to be there (as long as the application is running with the --use-exclusion-list flag set to True).

Also make sure to not have duplicates if you add products, and to delete all instances of a product when you want to remove it from the list. The script will only check if the current product is in the list and not how often.

4. Save the file and upload it to S3 by either drag and drop or by clicking the orange Upload button. You will see this page, on which you can add your file and overwrite the existing one.

The name of the file is important to be precisely exclusion_list.csv , so be careful at any typos.

5. Next please confirm the upload and see if it has worked:

6. After confirming the upload operation, you can also double check the “Last modified” attribute, to be extra sure.

## Technical Details
* S3 URI: s3://marketplace-pricing-configuration-prod/exclusion_list.csv
* ARN: arn:aws:s3:::marketplace-pricing-configuration-prod/exclusion_list.csv

S3 URI: s3://marketplace-pricing-configuration-prod/exclusion_list.csv

ARN: arn:aws:s3:::marketplace-pricing-configuration-prod/exclusion_list.csv

