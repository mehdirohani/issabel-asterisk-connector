import ami
import os

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

# نام کامل هر فایل را در /var/spool/asterisk/voicemail چاپ کنید
for line in response.splitlines():
    filename = os.path.basename(line)
    print(filename)

# از سرور Asterisk جدا شوید
client.disconnect()
