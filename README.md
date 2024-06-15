Before you start, make sure the following prerequisites are taken care of:

[System]
- Python 3
- The [Colorama Libary](https://pypi.org/project/colorama/) (pip3 install colorama)

[mosyle]
- You will need to generate a new token from the Mosyle Admin console: Organization--> Api integration
- Please note, with a recent update in Mosyle, an admin's username and password is now requrired in the call. You might want to create a new user for this.
- Also, just a fair warning. Be careful palying around with the Mosyle API. You can very much remove ADMIN rights from yourself.

[snipe-it]
- Snipe url is the full url of your Snipe-IT instance's api. EG: https://snipeit.example.com/api/v1 (do not add a slash at the end!)
- Generate the api key from the Snipe-IT seetings and for use in the configuration.ini
- Manufacturer Id should be set to the Apple Manufacturer entry in Snipe-IT. If you have not done this already, add apple as a manufacturer.
- If you have not done so already, you will need to create a category of devices for MacOS (we did "Computers"), iOS ( we did "Mobile/Tablets", and TVOS (we did "Media Players").
- The script will attempt to take device user assignments from Mosyle and "check out" the devices to the same user in Snipe-It. The two services should already have idential users for this to work. We have both Mosyle and Snipe-IT bound to our active directory/ldap for this reason.




[MosyleSnipeSync]
- Copy settings-example.ini to settings.ini
- Configure seetings.ini with the needed parameters.
- Each line has a comment above explaining the setting

[Questions/Comments/Concerns?]

You can best find me on the MacAdmin's slack as [Jake Garrison (Karpadiem)](https://macadmins.slack.com/team/U76DMNHT3)
