import requests
from bs4 import BeautifulSoup as bs
from random import randint
from twilio.rest import Client

proxies = ["45.76.20.147:8888",
"66.175.83.156:8080",
"216.198.170.70:8080",
"70.169.141.247:48678",
"47.17.62.181:808",
"54.236.59.57:80"]
proxy_len = len(proxies) - 1

client = Client("foo", "foo")

headers = {'user-agent':"Safari/537.36"}
proxy = proxies[randint(0,proxy_len)]

ip = {'http':proxy}
r = requests.get("https://www.reddit.com/r/buildapcsales/new/",headers=headers,proxies=ip,timeout=10)
if r.status_code == 200:
	soup = bs(r.text, "html.parser")
	latest_post = soup.find('a',{'class':'title may-blank outbound'})

	msg = "{} \n{}".format(latest_post.text.strip(),latest_post.get('href'))
	client.api.account.messages.create(
	    to="+123123123",
	    from_="+123123123",
	    body=msg)
	print("- SENT -")
else:
	print("- ERROR -")
