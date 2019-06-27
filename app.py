import smtplib
import base64
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
def sendMail(): 
	# fromaddr = "dedesumeyya@gmail.com"
	# toaddr = "sumeyyadede6@gmail.com"
	# password = 1993smyyadd1997
	# body = "hello"

	toaddr = raw_input("Please enter the toaddr email address: ")
	fromaddr = raw_input("Please enter the fromaddr email address: ")
	password = raw_input("Please enter your password: ")
	body = raw_input("Please enter the message: \n")

	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "SM Engage Campaign"
		
	msg.attach(MIMEText(body, 'plain'))


	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, password)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

	return {'raw': base64.urlsafe_b64encode(msg.as_string())}


def main():

	print(sendMail())


if __name__ == "__main__":
	main()
	

