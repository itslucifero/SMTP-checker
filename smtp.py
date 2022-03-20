from datetime import date
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

today = date.today()
print(f"""
        
                             SMTP CHECKER         Coded By :       
                                                                                      
██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚══███╔╝
███████║██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║  ███╔╝ 
██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║ ███╔╝  
██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
              Date :  {today}
              Contact : https://t.me/kickflap                                                 """)


smtp_server = input('Enter your smtp server : ')
smtp_port = input('Enter your SMTP port :')
smtp_user = input('Please enter your SMTP USERNAME : ')
smtp_pass = input('Enter your SMTP password : ')
smtp_reciever = input('Enter reciever email (YOUR EMAIL) FOR TEST : ')




message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: HrackeDZ SMTP e-mail test

This is a test e-mail message.
Your SMTP WORKS.
"""


context = ssl.create_default_context()

def smtp(smtp_server, port, user, receiver_email, password, message):
    
    if port == '587':
        
        with smtplib.SMTP(smtp_server, port) as server:
            try:
                 
             
                 server.ehlo()  # Can be omitted
                 server.starttls()
                 server.ehlo()  # Can be omitted
                 server.login(user, password)
                 server.sendmail(user, receiver_email, message)
                 print(f'''\n\n\nSMTP ALIVE :\n SERVER : {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n MESSAGE SENT! ''')
            except smtplib.SMTPAuthenticationError:
                 print('Dead SMTP')    
    elif port == '465':
        with smtplib.SMTP_SSL(smtp_server, port) as server:
           
            try:
                
                 server.login(user, password)
                 server.sendmail(user, receiver_email, message)
                 print(f'''\n\n\nSMTP ALIVE :\n SERVER :  {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n MESSAGE SENT!''')
            except smtplib.SMTPAuthenticationError:
                 print('Dead SMTP')    

    else:
        print('PORT NOT SUPPORTED')
        quit()
    


smtp(smtp_server=smtp_server, port=smtp_port, user=smtp_user, receiver_email=smtp_reciever, password=smtp_pass, message=message)