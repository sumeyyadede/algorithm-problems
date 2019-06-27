import smtplib

server = smtplib.SMTP("dedesumeyya@gmail.com", 587)
server.starttls()
server.login("dedesumeyya@gmail.com", "1993smyyadd1997")

message = "Hello!!"
server.sendmail("dedesumeyya@gmail.com", "sumeyyadede6@gmail.com", message)
server.quit()


if __name__ == "__main__":
	main()

