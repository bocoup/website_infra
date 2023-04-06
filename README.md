# TODO: complete this

# Steps to run this tool
1. Add the ACF fields in WordPress
    - Make sure that **Show in REST API** is enabled in the group settings of the Field Group
2. Export your username and password in the command line
3. Run `python3 main.py` from the `tools/post_meta_converstion` folder 

## quick summary

tools --> anything that isn't directly wp related


wp --> wp copy content, currently only the wp-content folder is relevant
--> specifically the custom-post-types folder
--> and the initialization in the themes folder (./twentytwentythree/functions.php)

List of Current Plugins
- Advanced-custom-fields
- Akismet