from datetime import date
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter.font import BOLD
import crayons
import platform
import os

platform.system()
if platform.system() == 'Linux':

    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')    


today = date.today()
print (crayons.red(f"""
        
                             SMTP CHECKER v 0.2         Coded By :       
                                                                                      
██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚══███╔╝
███████║██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║  ███╔╝ 
██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║ ███╔╝  
██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
              Date :  {today}
              Contact : https://t.me/kickflap 
              Website : https://www.hrackedz.com
              Discord for premium tools here :
                 https://discord.gg/E3jWdM5k        \n\n                                        """))

try:

    

            smtp_reciever = input('Enter reciever email (YOUR EMAIL) FOR TEST : ')


            clear()

            print(crayons.blue('''

            ==> 1 - Single SMTP checker
            ==> 2 - Bulk SMTP checker

            '''))

            entry = input(crayons.red('root@hrackedz# : ==>'))

            message = """From: From Person <from@fromdomain.com>
            To: To Person <to@todomain.com>
            Subject: HrackeDZ SMTP e-mail test

            This is a test e-mail message.
            Your SMTP WORKS.
            """


            if entry == '1':
                clear()
                smtp_server = input(crayons.red('Enter your SMTP server : '))
                smtp_port = input(crayons.red('Enter your SMTP port : '))
                smtp_user = input(crayons.red('Enter your SMTP USERNAME : '))
                smtp_pass = input(crayons.red('Enter your SMTP password : '))
                context = ssl.create_default_context()

                def smtp(smtp_server, port, user, receiver_email, password, message):
                
                    if port == '587':
                    
                       with smtplib.SMTP(smtp_server, port) as server:
                        try:
                            
                        
                            server.ehlo()
                            server.starttls()
                            server.ehlo()  
                            server.login(user, password)
                            server.sendmail(user, receiver_email, message)
                            print(crayons.green(f'''\n\nSMTP ALIVE :\nSERVER : {smtp_server}\nUser: {user}\nPass: {password}\nPORT : {port} \nMESSAGE SENT! '''))
                        except smtplib.SMTPAuthenticationError:
                            print(crayons.red(f'''Dead SMTP \nSERVER : {smtp_server}\nUser: {user}\nPass: {password}\nPORT : {port} \n'''))   
                    elif port == '465':
                        with smtplib.SMTP_SSL(smtp_server, port) as server:
                        
                         try:

                            server.login(user, password)
                            server.sendmail(user, receiver_email, message)
                            print(crayons.green(f'''\n\nSMTP ALIVE :\nSERVER : {smtp_server}\nUser: {user}\nPass: {password}\nPORT : {port} \nMESSAGE SENT! '''))
                         except smtplib.SMTPAuthenticationError:
                            print(crayons.red(f'''Dead SMTP \n SERVER : {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n'''))     

                    else:
                         print(crayons.red('PORT NOT SUPPORTED'))
                         quit()
                


                smtp(smtp_server=smtp_server, port=smtp_port, user=smtp_user, receiver_email=smtp_reciever, password=smtp_pass, message=message)




            elif entry== '2':
                context = ssl.create_default_context()
                print(crayons.blue('''
                Your list myst be like this
                smtpserver|port|user|pass

                Check your list before posting it 

                Result will be saved to :
                AliveSMTP.txt
                DeadSMTP.txt
                In the script Path
                '''))

                def checker(file):
                    with open(file, "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            smtp_server, smtp_port, smtp_user, smtp_pass = line.rstrip('\n').split("|")      
                            def smtp(smtp_server, port, user, password):
                                    if port == '587':
                                               with smtplib.SMTP(smtp_server, port) as server:
                                                try:
                                    
                                
                                                    server.ehlo()  
                                                    server.starttls()
                                                    server.ehlo()  
                                                    server.login(user, password)
                                                    server.sendmail(user, smtp_reciever, message)
                                                    res = open('AliveSMTP.txt', 'a')
                                                    print(crayons.green(f'''\n\nSMTP ALIVE :\nSERVER : {smtp_server}\nUser: {user}\nPass: {password}\nPORT : {port} \nMESSAGE SENT! '''))
                                                    res.write(f"{smtp_server}|{smtp_port}|{smtp_user}|{smtp_pass}\n")
                                                    res.close()
                                                    
                                                except smtplib.SMTPException:
                                                        res1 = open('DeadSMTP.txt', 'a')
                                                        print(crayons.red(f'''\n\nDead SMTP \nSERVER : {smtp_server}\nUser: {user}\nPass: {password}\nPORT : {port} \n'''))    
                                                        res1.write(f"{smtp_server}|{smtp_port}|{smtp_user}|{smtp_pass}\n")
                                                        res1.close()
                                    elif port == '465':
                                                with smtplib.SMTP_SSL(smtp_server, port) as server:
                                                    try:
                                    
                                                        server.login(user, password)
                                                        server.sendmail(user, smtp_reciever, message)
                                                        res = open('AliveSMTP.txt', 'a')
                                                        print(crayons.green(f'''\n\nSMTP ALIVE :\nSERVER : {smtp_server}\nUser: {user}\nPass: {password}\nPORT : {port} \nMESSAGE SENT! '''))
                                                        res.write(f"{smtp_server}|{smtp_port}|{smtp_user}|{smtp_pass}\n")
                                                        res.close()
                                                    except smtplib.SMTPException:
                                                        res1 = open('DeadSMTP.txt', 'a')
                                                        print(crayons.red(f'''\n\nDead SMTP \nSERVER : {smtp_server}\nUser: {user}\nPass: {password}\nPORT : {port} \n'''))     
                                                        res1.write(f"{smtp_server}|{smtp_port}|{smtp_user}|{smtp_pass}\n")
                                                        res1.close()
                                    else:
                                        print(crayons.red('PORT NOT SUPPORTED'))
                                        quit()
                            smtp(smtp_server=smtp_server, port=smtp_port, user=smtp_user, password=smtp_pass)        



                checker(input('Enter your smtp list path Ex(c:/users/admin/list.txt) : '))



            else:
                print(crayons.red('!!!!! Please choose a valid entry !!!!!'))
                quit() 
                        
except KeyboardInterrupt:
            print(crayons.red('CTRL + C DETECTED LEAVING BYEEEE!'))
            quit()






                
