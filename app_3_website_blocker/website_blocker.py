import time
from datetime import  datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts_bu"
hosts_temp = "hosts"
redirect = "127.0.0.1 "
website_list = ["www.facebook.com", "facebook.com", "www.index.hr", "index.hr"]

while True:
    with open(hosts_temp, 'r+') as file:
        if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
            print("Working hours...")
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + website + "\n")
        else:
            print("Fun time!")
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                else:
                    pass
            file.truncate()
    time.sleep(5)