# anopesendmailpy
Send Mail from Anope IRC Services using Python 3 </br>
</br>
# Info

This was created for Anope IRC Services as replacement of sendmail</br>
But it may work with other software that uses /usr/sbin/sendmail -t</br>

# How to install
</br>
Download sendmail.py and requirements.txt</br>
pip/pip3 install -r requirements.txt</br>
Change in sendmail.py </br>
smtp_hostname</br>
smtp_port</br>
smtp_username</br>
smtp_password</br>
smtp_security</br>
chmod +x sendmail.py</br>
Set in anope services.conf sendmailpath= to script location</br>
