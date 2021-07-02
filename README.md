# discogs_collection
Quick and dirty script to pull my and my husband's Discogs collections and combine them for display on a webpage. 
_This is a work in progress._ I will be adding some error handling and logging, as well as posting the simple HTML page that the data will be displayed in.

Discogs API documentation: https://www.discogs.com/developers

For this script you will need a developer key/secret only if you want to retreive the URL of the album cover image. If you just want basic collection info you don't need the key and secret. You can get a key and secret here: https://www.discogs.com/settings/developers. NOTE: these credentials do not identify you as a particular user. They just grant you access to the image URLs and increase your rate limit for API requests.

The main version of the script runs fine in Python 3 and I think it should be okay with 2.7.6 or higher. However it needs some slight modifications to run on 2.6.6. I have included a modified version. The differences are:
- disabling SSL verification for the API request (line XX)
- specifying the variable using the format method (line XX)
