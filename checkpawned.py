# Simple script implementation of the https://haveibeenpwned.com/API/v3#PwnedPasswords API to check 
# if the password entered exists in the haveibeenpwned.com database

import hashlib
import getpass
import requests

url = "https://api.pwnedpasswords.com/range/"

pwd = getpass.getpass("Password to check: ")
res = hashlib.sha1(pwd.encode()).hexdigest()
prefix = res[:5]
postfix = res[5:].upper()
reqUrl = url+prefix

# Added padding header as recomended by Troy in his documentation. 
# Pads out responses to ensure all results contain a random number of records between 800 and 1,000.
req = requests.get(url = reqUrl, headers={"Add-Padding":"true"}, verify=True)
data = req.text

#print(f"Postfix: {res[5:]}")
#print(reqUrl)

for line in data.splitlines():
    if line.split(":")[0] == postfix:
        print ("CRAP! Your password is out in the wild, you should change it ASAP!")
        print (f"It's been found {line.split(':')[1]} times!")
        break