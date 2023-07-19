# SMTP Checker v 0.2 (Added Bulk Checker)


Contact me for it : https://t.me/itslucifero


Script in python uses smtplib to chek if your smtp server works or dead.

In version 0.1 , it was a sngle checker , by that i mean single smtp checker .

Now i have added lot of features to it :D

You can check in bulk now 
make sure ur list txt file is like this :

SMTPSERVER|PORT|SMTPUSER|SMTPPASS

My script can scan millions of smtps ; and also i didn't delete the old version of single checker i just made it as an option in the script.

Result will be saved to :
AliveSMTP.txt
DeadSMTP.txt

USE : 

python smtp.py

Req :

- pip install crayons
- pip install smtplib

enter your smtp host and port and logins
it will detect SSL or TLS by port number so don't worry.

