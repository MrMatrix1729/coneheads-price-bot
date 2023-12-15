import time
import requests
import json
from datetime import datetime

tokens = {
	"cone": "polygon/0xba777ae3a3c91fcd83ef85bfe65410592bdd0f7c",
	"plunger":"polygon/0x43ff18fa32e10873fd9519261004a85ae2c7a65d",
	"taco": "polygon/0x7ea837454e3c425e01a8432234140755fc2add1c",
	"donut": "ether/0xc0f9bd5fa5698b6505f643900ffa515ea5df54a9",
	"moons": "arbitrumnova/0x0057ac2d777797d31cd3f8f13bf5e927571d6ad0"
}

d = {}
output={}

headers = {
  "X-BLOBR-KEY": "4t5FjpElAF3DjjwywkCKDWu3kMIvtE5G"
}



for key in tokens:
	tokenused = "https://open-api.dextools.io/free/v2/token/" + tokens[key] + "/price"
	print(key)
	price = (requests.get(tokenused,headers=headers).json())['data']['price']
	d[key] = price

output['timestamp']= str(datetime.now())
output['tokens']= d

with open("test.json", "w") as outfile: 
    json.dump(output, outfile)

