import unittest
import send_mail

TO = "dedesuemyya"
FROM = "training_user"
PWD = "P@ssw0rd"
MSG = "new message"

def test_mail():
   	response = send_mail.postman(TO, FROM, PWD, MSG)
   	assert(response == "OK")

# class TestMail(unittest.TestCase):
# 	def setUp(self):
# 		pass

# 	def test_mail(self):
#     	response = send_mail.postman(TO, FROM, PWD, MSG)
#     	self.assertEqual(response, "OK")
    	# assert(response == "OK")

def main():
    test_mail.main()

if __name__ == '__main__':
	main()
