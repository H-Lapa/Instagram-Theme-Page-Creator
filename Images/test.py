import json
import os
accounts = json.load(open("Accounts.json"))
print(accounts)

new_string = json.dumps(accounts)


for x in accounts['accounts']:
    directory = x['Username']
    path = os.path.join("Images", directory)
    try:
        os.makedirs(path, exist_ok = True)
        print("Directory '%s' created successfully" % directory)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)


print("break")

"""
#load as python object
with open('Accounts.json') as f:
    data = json.load(f)

for accounts in data['accounts']:
    print(accounts['Username'])
    del accounts["ldp"]

with open('New_list.json', 'w') as f:
    json.dump(data, f)
"""
