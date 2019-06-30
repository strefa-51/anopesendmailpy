#!/usr/bin/python3
"""
MIT License

Copyright (c) 2019 Strefa 51

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys
from flanker import mime
from sender import Message
from sender import Mail
import time
#SETTINGS
smtp_hostname = ""
smtp_port = 25
smtp_username = ""
smtp_password = ""
smtp_security = "SSL"
#END SETTINGS

input = sys.stdin.read()
text = mime.from_string(input)


msg = Message(text.headers['subject'])
msg.fromaddr = text.headers['from']
msg.to = text.headers['to']
msg.body = text.body
msg.date = time.time()
msg.charset = "utf-8"
#Check SSL or TLS
smtp_ssl_use = False
smtp_tls_use = False

if smtp_security == "SSL":
	smtp_ssl_use = True
elif smtp_security == "TLS":
	smtp_tls_use = True
else:
	smtp_ssl_use = False
	smtp_tls_use = False

mail = Mail(smtp_hostname, port=smtp_port, username=smtp_username, password=smtp_password, use_tls=smtp_tls_use, use_ssl=smtp_ssl_use, debug_level = None)
mail.send(msg)
