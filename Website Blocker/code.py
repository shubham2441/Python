import time
from datetime import datetime as dt

host+temp = "hosts"
redirect = '127.01.02'
website_list = [www.facebook.com, facebook.com]

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().date,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().date,16)):
        with open (host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " + website + '\n')