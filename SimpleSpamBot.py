#-*- coding: utf-8 -*-

############################################
# author: Krystian C.                      #
# 22.10.2017                               #
# SimpleSpamBot is made only for education #
# Made by 13 year old teenager             #
############################################

#### My github ######## My github ######## My github ######## My github ####
#
# My Github: https://github.com/Krystian-Cryhoo/SimpleSpamBot/
#
#### My github ######## My github ######## My github ######## My github ####


import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Send_Email(password, login, Semail, Subject, mess):
        
        #From, To, Subject - settings
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = Semail
        msg['Subject'] = Subject

        msg.attach(MIMEText(mess, 'plain'))
        text = msg.as_string()

        #Connectin2smtplib
        sendM = smtplib.SMTP('your_SMTP', 587) #Write smtp(SMTP must be in every spam-email same!
        sendM.starttls()
        sendM.login(login, password)

        #Send Mail && Quit
        sendM.sendmail(login, Semail, text)
        sendM.quit()
        
def Check_Email(email): #This def check whether e-mail exists 
        #Email login and pass
        email_user = 'your_login' 
        email_pass = 'your_pass'

        subject = 'check'
        #From, To, Subject - settings
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email
        msg['Subject'] = subject

        body = "."
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()

        #Connectin2smtplib
        sendM = smtplib.SMTP('your_SMTP', 587)
        sendM.starttls()
        sendM.login(email_user, email_pass)

        #Send Mail && Quit
        sendM.sendmail(email_user, email, text)
        sendM.quit()

#Take email to spam
yorn = True
while yorn:

    emailYorN = True
    while emailYorN:
            email = raw_input("Type email you want to spam: ")
            print 'Checking whether this email exists...\n'

            try:
                Check_Email(email)
                print 'Email exsist!'
                emailYorN = False
            except:
                print "Wrong email! Try again!"

    truorfalse = True

    print '\nExample: 10, 5, 8, 100'
    #How many times spam
    while truorfalse:
        Hmuch = raw_input("How many times you want spam: " )


        try: 
            print int(Hmuch)
            if int(Hmuch) <= 0:
                print 'Type another number!'
            else:
                truorfalse = False
        except:
            print 'Try again!'
    
    print "\n\nYour data:"
    print "E-mail: " + email
    print "How many times you want spam: " + Hmuch

    print "\nDo you want enter data again?"

    yorn2 = True
    while yorn2:
        yorn_question = raw_input("(Y/N): ")

        yorn_answer = str(yorn_question)

        if yorn_answer == "Y" or yorn_answer == "N" or yorn_answer == "y" or yorn_answer == "n":
            if yorn_answer == "Y" or yorn_answer == "y":
                print '\nOkay!\n'
                yorn2 = False
                yorn = True
            
            elif yorn_answer == "N" or yorn_answer == "n":
                print '\nOkay!\n'
                yorn2 = False
                yorn = False
        else:
            print 'Try again!'


#Take path to logins and passwords
print 'Type name txt with login e-mail'
print 'Remember! This txt must be in folder where is SimpleSpamBot!'
print 'Remember about .txt on end!'

yorn3 = True
while yorn3:
    txt_email = raw_input('Type path to txt: ')

    try:
        txt_path = str(txt_email)
        txt = open(txt_path, 'r')
        txt.read
        yorn3 = False
        print 'Good path!\n'
    except:
        print '\nWrong path! Try again!\n'

print '\nType name txt with password e-mail'
print 'Remember! This txt must be in folder where is SimpleSpamBot!'
print 'Remember about .txt on end!'
yorn4 = True
while yorn4:
    txt_pass = raw_input('Type path to txt: ')

    try:
        txt_path2 = str(txt_pass)
        txt2 = open(txt_path2, 'r')
        txt2.read
        yorn4 = False
        print 'Good path!\n'
    except:
        print '\nWrong path! Try again!\n'
#Get subject and message
yorn5 = True
while yorn5:

        subject1 = True
        while subject1:
                subject = raw_input("Write subject: ")
                print '\nDo you want write again?'
                answ = raw_input("(Y/N): ")

                if answ == 'Y' or answ == 'y':
                        subject1 = True
                if answ == 'N' or answ == 'n':
                        subject1 = False
                else:
                        print 'Try again!'

        msg1 = True
        while msg1:
                print '\n\nWirte a message or write "email.txt" and write in this txt'
                msg = raw_input("Write: ")

                if msg == "email.txt":
                                
                        Bcreate = open("email.txt", "a")
                        print '\n"email.txt" was created. Write in this txt a message'
                        Bcreate.close()
                        anykey = raw_input("Type any key to continue: ")

                        Bread = open("email.txt", "r")
                        msg = Bread.read()
                        Bread.close()
                print '\n\nYour message: \n' + str(msg)
                print '\nDo you want write again?'
                ansmsg = raw_input("(Y/N): ")
        
                if ansmsg == 'Y' or ansmsg == 'y':
                        msg1 = True
                if ansmsg == 'N' or ansmsg == 'n':
                        msg1 = False
                        yorn5 = False
                else:
                        print 'Try again!'
        
#Start Spam
print "\nStart spamming..."

SpamMuch = int(Hmuch)
login_txt = open(txt_path, 'r')
pwd_txt = open(txt_path2, 'r')
for i in range(0, SpamMuch):        
        line_txt = login_txt.readline()
        line_pwd = pwd_txt.readline()

        if line_txt == '' or line_pwd == '':
                login_txt.close() 
                login_txt = open(txt_path, 'r')
                line_txt = login_txt.readline()
                
                pwd_txt.close() 
                pwd_txt = open(txt_path2, 'r')
                line_pwd = pwd_txt.readline()
                
        print 'Login: ' + line_txt + ' Password: ' + line_pwd + ' trying send email...'

        password = str(line_pwd)
        login = str(line_txt)
        Semail = str(email)
        Subject = str(subject)
        mess = str(msg)
        #Sending Email
        try:         
                Send_Email(password, login, Semail, Subject, mess)
                print 'Sended'
        except:
                print 'Error'
        
        
print 'Di ent' 
