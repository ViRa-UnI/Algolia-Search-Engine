# Installation Guide for Algolia Search Integration Module

## Prerequisites
Before you begin the installation of the Algolia Search Integration Module, ensure that you have the following prerequisites in place:

- Odoo Version 16 Community Edition installed and running.
- Administrative access to your Odoo instance.
- An active Algolia account with API credentials (Application ID, Admin API Key, and Search-Only API Key).

## Step 1: Download the Module
Download the latest version of the Algolia Search Integration Module from the Odoo app store or the repository where it is hosted.

## Step 2: Add the Module to Odoo
Place the downloaded module into the Odoo addons directory. The default path is usually `/odoo/addons`.

## Step 3: Update the Module List
Log in to your Odoo instance as an administrator and navigate to `Apps > Update Apps List`. Click on 'Update' to refresh the list of available modules.

## Step 4: Install the Module
In the Odoo Apps menu, search for 'Algolia Search Integration'. When you find the module, click on the 'Install' button to begin the installation process.

## Step 5: Configure Algolia Credentials
After installation, go to `Settings > Algolia Search Configuration` to open the Algolia Config Wizard located at `wizard/views/algolia_config_wizard_view.xml`. Enter your Algolia Application ID, Admin API Key, and Search-Only API Key.

## Step 6: Index Your Products
Navigate to `Inventory > Products` and use the action `Update Algolia Index` to synchronize your product catalog with Algolia. This process can also be automated using scheduled actions.

## Step 7: Customize Search Settings
Customize the search settings according to your business needs by going to `Website > Configuration > Search Settings`. Here you can define the attributes for faceting, ranking, and other search behaviors.

## Step 8: Verify the Integration
Check the integration by going to your website's search bar and typing a query. You should see instant search results powered by Algolia.

## Step 9: Set Up Analytics (Optional)
To set up the analytics dashboard, navigate to `Website > Algolia Search > Analytics Dashboard` as defined in `views/analytics_dashboard_view.xml`. This dashboard will help you track and analyze search queries and user interactions.

## Troubleshooting
If you encounter any issues during the installation or configuration, refer to the `README.md` and `doc/administrator_guide.md` for troubleshooting tips and contact support if necessary.

## Conclusion
You have successfully installed and configured the Algolia Search Integration Module for Odoo Version 16 Community Edition. Enjoy the enhanced search capabilities on your eCommerce platform!