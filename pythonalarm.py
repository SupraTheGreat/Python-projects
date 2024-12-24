import os
print (os.getcwd())


# import required module
from datetime import datetime
import pytz
from plyer import notification
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

# URL of the web page
url = 'http://chickenisthebest.s3-website-us-east-1.amazonaws.com'

# Fetch the HTML content of the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # List to store the extracted text
    extracted_text = []

    # Extract text from <h1>, <h2>, <h3>, and <p> tags
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        extracted_text.append(tag.get_text(strip=True))

    # Display the extracted text
    print(extracted_text)
else:
    print(f"Failed to retrieve the page. HTTP Status Code: {response.status_code}")

result = '0'

print('Enter a 12-hour format time like this: 12:45 PM')
inptim = "12:45 PM"

if inptim[1] == ':':
    result += inptim
else:
    result = inptim

aware_us_central = datetime.now(pytz.timezone('US/Central'))
now = aware_us_central.strftime("%I:%M")
print(now)

while now != result:
  aware_us_central = datetime.now(pytz.timezone('US/Central'))
  now = aware_us_central.strftime("%I:%M %p")

print('ALARM ALARM ALARM ALARM')


notification.notify(
    title="ALARM ALARM ALARM ALARM",
    message="It worked!",
    app_name="Alarm App",  # Optional
    timeout=5  # Notification stays for 10 seconds
)
print()
fo.close()