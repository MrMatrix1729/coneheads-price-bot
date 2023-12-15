import requests
import praw
import json
import time
from datetime import *
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
	user_agent= ,
	client_secret= ,
	client_id= ,
	username= ,
	password=
)

tokens = {
	"cone": "polygon/0xba777ae3a3c91fcd83ef85bfe65410592bdd0f7c",
	"plunger":"polygon/0x43ff18fa32e10873fd9519261004a85ae2c7a65d",
	"taco": "polygon/0x7ea837454e3c425e01a8432234140755fc2add1c",
	"donut": "ether/0xc0f9bd5fa5698b6505f643900ffa515ea5df54a9",
	"moons": "arbitrumnova/0x0057ac2d777797d31cd3f8f13bf5e927571d6ad0"
}

def priceFetch():

	d = {}
	output={}

	headers = {
  		"X-BLOBR-KEY": 
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


def tokenread(token):
	with open('test.json') as f: 
   		data = f.read() 
	js = json.loads(data)

	if token not in js['tokens']:
		return 6969696
	else:
		return js['tokens'][token]

def ts():
	with open('test.json') as f: 
   		data = f.read() 
	js = json.loads(data)
	return js['timestamp']


subreddit = reddit.subreddit("test")

print("Starting script....\n")
print("Waiting for comments...\n")

for comment in subreddit.stream.comments(skip_existing=True):
	print("Comment: " + comment.body)
	if comment.body.startswith("!value"):
		tsFormat = '%Y-%m-%d %H:%M:%S.%f'
		timestampCurrent = datetime.now()
		timestampFile = datetime.strptime(ts(), tsFormat)
		diff = timestampCurrent - timestampFile
		ago = diff.seconds // 60

		if(ago > 15):
			print("Refetching prices...")
			priceFetch()
			ago = 0

		splitedcom = comment.body.split()
		
		try:
			amount = int(splitedcom[1])
			coin1price = float(tokenread(splitedcom[2]))
			coin2price = float(tokenread(splitedcom[3]))
		except:
			print("Reply: ")
			comment.reply("Please Enter a valid format. Format: `!value amount token1 token2`")
			continue

		print(coin1price, coin2price, amount)

		if(coin1price == 6969696 or coin2price == 6969696):
			supported = ','.join(list(tokens.keys()))
			print("Reply: ")
			comment.reply("Coin not supported. Currently " + supported + " are supported")
			continue
		else:
			finalamount = coin1price/coin2price*amount
		

		reply = splitedcom[1] + " " + splitedcom[2] + " = " + str(finalamount) + " " + splitedcom[3] + "\n\n ^(Fetched: " + str(ago) + "min ago)"
		print("Reply: ")
		comment.reply(reply)
