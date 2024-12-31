# DWH Autopricing

The DWH autopricing is in the process of being replaced by the Pricing Service (PS). If necessary it can be re-activated by following the tutorial here https://cyber-solutions.atlassian.net/wiki/pages/resumedraft.action?draftId=1791918083.

## Development Process
* We use the git repository mentioned below.
* Create a new branch for every new release / feature. Never develop on the master branch! We advise naming the branch according to the feature or release (for example CBP_v2.5 for a new release v2.5 in Coverage Based Pricing).
* After finishing the development, test your code thoroughly.
* Then create a merge request from your branch to the master branch and ask one of your colleagues to approve it. Only then it can be merged.
* Only after an approved an merge request, integrate the Code to Exasol permanently.

We use the git repository mentioned below.

Create a new branch for every new release / feature. Never develop on the master branch! We advise naming the branch according to the feature or release (for example CBP_v2.5 for a new release v2.5 in Coverage Based Pricing).

After finishing the development, test your code thoroughly.

Then create a merge request from your branch to the master branch and ask one of your colleagues to approve it. Only then it can be merged.

Only after an approved an merge request, integrate the Code to Exasol permanently.

## Mechanism
Every morning the following procedure is called STP_APP_AUTO_PRICING_BUILD_PRICING_UPDATE.

To put it simplified this script calls with some checks the following subscripts:

After that the calculated prices in PROD_MODEL.PRODUCT_PRICE_RECOMMENDATION_HISTORY gets exported via the FTP Server ftp://supplier.cyberport.de/ to SAP Pro, the Webshop and CyberParts. The last step takes roughly 2-2.5 hours. New prices in the webshop should hence be available during midtime every day.

## Code
Previously the SQL files had been in the folder https://teams.microsoft.com/_#/files/Allgemein?threadId=19%3Ad9b27334a06949f09bf082b741233d8b%40thread.skype&ctx=channel&context=AutoPricing%2FSQL%2FScripts_Tables_Views

This folder is now renamed to https://teams.microsoft.com/_#/files/Allgemein?threadId=19%3Ad9b27334a06949f09bf082b741233d8b%40thread.skype&ctx=channel&context=AutoPricing%2FSQL%2FScripts_Tables_Views_deprecated(use_git!).

Whenever a file was edited, a copy of the previous version was put into the Archive folder with a timestamp in the name.

We replaced this procedure by a git repository, so please use that instead.

Instead of a shared folder, we share a git repository, which can be cloned locally with the following command inserting your own Bitbucket user name:

git clone https://<bitbucket_username>@bitbucket.org/hannah_winnes_cs/pricing_sqls.gitThen it makes sense to tell git who you are.

git config --global user.name "Max Mustermann"git config --global user.email max.mustermann@cyber-solutions.com Tips:

* Run git pull before any new development otherwise you would put would integrate your changes to an old version of code and had to clean up any problems later. This call ensures you have the latest code versions of all branches.
* Create a new branch for every new release / feature by calling git checkout -b [name_of_your_new_branch] locally and push it to Bitbucket git push origin [name_of_your_new_branch]. We advise naming the branch according to the feature or release (for example CBP_v2.5 for a new release v2.5 in Coverage Based Pricing).
* If you want to add a new file that already exists but is not yet in the Git index, you can do so with git add <filename>
* After and during the further development of SQL files, the command git commit -m "<commit message>" the current status can be saved locally. The commit message shows what kind of change has just been made in the code. You can create as many commits as you want, so you can always go back one level if you mess up.
* So far, all changes are only visible locally in your own directory. If you plan to make the changes public, the current status should first be queried using git fetch origin master to ensure that no one else has changed one of the files that you are about to upload and, if in doubt, sets the changes to the current one Stand git rebase -i origin / branch_name.
* Only after the git push origin branch_name command are the new and / or changed visible to the rest of the team. A push should only be made after the modified SQL files have been tested.

Run git pull before any new development otherwise you would put would integrate your changes to an old version of code and had to clean up any problems later. This call ensures you have the latest code versions of all branches.

Create a new branch for every new release / feature by calling git checkout -b [name_of_your_new_branch] locally and push it to Bitbucket git push origin [name_of_your_new_branch]. We advise naming the branch according to the feature or release (for example CBP_v2.5 for a new release v2.5 in Coverage Based Pricing).

If you want to add a new file that already exists but is not yet in the Git index, you can do so with git add <filename>

After and during the further development of SQL files, the command git commit -m "<commit message>" the current status can be saved locally. The commit message shows what kind of change has just been made in the code. You can create as many commits as you want, so you can always go back one level if you mess up.

So far, all changes are only visible locally in your own directory. If you plan to make the changes public, the current status should first be queried using git fetch origin master to ensure that no one else has changed one of the files that you are about to upload and, if in doubt, sets the changes to the current one Stand git rebase -i origin / branch_name.

Only after the git push origin branch_name command are the new and / or changed visible to the rest of the team. A push should only be made after the modified SQL files have been tested.

## Tutorials
### Restart Autopricing manually
If there was a mistake in the pricing service, there could arise the necessity to update prices during the day, if we don't want to wait for another day. This should only be done after discussing with the rest of the Data Science team.

