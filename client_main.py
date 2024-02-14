import ami
import os
import csv
import requests

# اطلاعات اتصال به سرور Asterisk را تنظیم کنید
host = "localhost"
port = 5038
username = "admin"
password = "password"

# به سرور Asterisk وصل شوید
client = ami.Client(host, port, username, password)

# دستوری را برای سرور Asterisk ارسال کنید تا لیست فایل ها را در /var/spool/asterisk/voicemail دریافت کنید
client.command("action: ListFiles dir=/var/spool/asterisk/voicemail")

# پاسخ سرور Asterisk را دریافت کنید
response = client.response()

# برای هر فایل در /var/spool/asterisk/voicemail
for line in response.splitlines():
    filename = os.path.basename(line)

    # URL دانلود فایل را بسازید
    url = f"http://{host}:{port}/voicemail/{filename}"

    # فایل را دانلود کنید
    response = requests.get(url)

    # فایل را در پوشه voicemail_files ذخیره کنید
    with open(f"voicemail_files/{filename}", "wb") as f:
        f.write(response.content)

    # نام فایل دانلود شده را در voicemail_files.csv ذخیره کنید
    with open("voicemail_files.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([filename])

# از سرور Asterisk جدا شوید
client.disconnect()
