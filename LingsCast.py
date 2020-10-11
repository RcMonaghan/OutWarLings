import requests
from bs4 import BeautifulSoup
import re


# Fill in your details here to be posted to the login form.
payload = {
    'login_username': '',
    'login_password': ''
}


def Lings():
	with requests.Session() as s:
		p = s.post('https://sigil.outwar.com/login', data=payload)
		me = s.get('http://sigil.outwar.com/myaccount')
		soup = BeautifulSoup(me.content, 'html.parser')
		for Accounts in soup.findAll('a', attrs={'href': re.compile("^http://")}):
			Account = Accounts.get('href')
			AccountName = Accounts.get('target')
			pattern = 'PLAY!'
			result = re.match(pattern, AccountName)
			if Accounts.text != "PLAY!":
				me = s.get(Account)
				s.get("http://sigil.outwar.com/underlingtrust.php?claim=1")
			else:
				pass


Lings()