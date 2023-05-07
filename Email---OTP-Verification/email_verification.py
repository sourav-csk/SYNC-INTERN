import random
import smtplib

sender_mail = "sendermail"
password = "password"

#============ Head Line =====================================

print("=============OTP Verification===============")
receiver_mail = input("Enter your mail:- ")

#================================================
#================================================
#================================================
#================================================

#============== Server Login =====================

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_mail,password)

#=========== OTP Generate =======================================

otp = "".join([str(random.randint(0,9)) for i in range(4)])
msg = "Hello, your otp is " + str(otp)

#=============== Sending OTP in Receiver's Mail ==================

server.sendmail(sender_mail,receiver_mail,msg)
server.quit()

print("OTP sent successfully")

#============== User Input =======================================

user_otp = input("Enter the OTP sent to your email: ")
if user_otp == otp:
    print("OTP is verified successfully!")
else:
    print("Wrong OTP, enter correct OTP")
    print("Your OTP was:- " + str(otp))