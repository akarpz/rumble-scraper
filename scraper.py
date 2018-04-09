from urllib.request import urlopen
from bs4 import BeautifulSoup


root_booking_page = 'https://www.rumble-boxing.com/reserve/12900000002'
page = urlopen(root_booking_page)
parsed_page = BeautifulSoup(page, 'html.parser')

name_box = parsed_page.find('div', attrs={'data-classdate': '2018-04-09T06:00:00'})


class_id = name_box['id']

class_booking_page = 'https://www.rumble-boxing.com/book/' + class_id

booking_page = urlopen(class_booking_page)
parsed_booking_page = BeautifulSoup(booking_page, 'html.parser')

#print(parsed_booking_page)

loginForm = parsed_booking_page.find('form' , attrs = {'id': 'loginForm'})

loginKey = parsed_booking_page.find('input', attrs = {'name' : '_token'})['value']
loginUserName = 'adameast9000@live.com'
loginPassword = 'cloudNinePassword'

payload = {
  '_token': loginKey,
  'uid': loginUserName,
  'password': loginPassword
  }

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'RedditTesting')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib2.install_opener(opener)

# The action/ target from the form
authentication_url = 'https://www.rumble-boxing.com/authenticate'

print(loginKey)



#after login
spotcells = parsed_booking_page.find('div', attrs={'class': 'spotwrapper'})

#name = name_box.text.strip()
