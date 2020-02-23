import sys
import requests


r = requests.get("https://www.facebook.com")
print(r.status_code)
