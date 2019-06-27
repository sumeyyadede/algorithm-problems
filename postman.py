import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#constant variables for body
JID = "47de74b5-8c7e-4e33-a55a-a7ba00f4ecdc"
CG = "Standart"
SBJ = "SM Engage Campaign"
    
# define files and headers
REQUEST_XML = "header.xml"
RESPONSE_XML = "return.xml"
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}

#for xml create an object 
class RequestBuilder(object):
    def __init__(self):    
        self.user = None
        self.pwd = None
        self.msg = None
        self.ta = None

    def make_body(self):
        root = ET.Element("SENDEML")
        ET.SubElement(root, "USR").text = self.user 
        ET.SubElement(root, "PWD").text = self.pwd 
        ET.SubElement(root, "JID").text = JID 
        ET.SubElement(root, "CG").text = CG
        ET.SubElement(root, "SBJ").text = SBJ
        rcpt_list = ET.SubElement(root, "RCPT_LIST")
        rcpt = ET.SubElement(rcpt_list, "RCPT")
        ET.SubElement(rcpt, "MSG").text = self.msg
        ET.SubElement(rcpt, "TA").text = self.ta
        tree = ET.ElementTree(root) 
        
        # write the body in the file 
        try:        
            with open(REQUEST_XML, 'w') as request_file:
                request_file.write("data=")
                tree.write(request_file, xml_declaration = True)
            return REQUEST_XML
        except IOError:
            print('An error occured trying to write the return file.')

def postman(to_addr, from_addr, pwd, msg):
    # create and write body in the file
    request_builder = RequestBuilder()
    request_builder.ta = to_addr
    request_builder.user = from_addr
    request_builder.pwd = pwd
    request_builder.msg = msg 
    request_xml = request_builder.make_body()

    # sending mail
    try:
        with open(request_xml) as request_file: 
            response = requests.post('https://ppapi.smartmessage-engage.com/SENDEML', data = request_file, headers = HEADERS)

            # write the response.content in the file
            try:
                with open(RESPONSE_XML, 'w') as response_file:
                    response_file.write(response.content)
            except IOError:
                return 'An error occured in header file.'       

            # take explanation  
            parser = ET.XMLParser(encoding = "utf-8")
            root = ET.parse(RESPONSE_XML, parser = parser)
            exp = root.find('EXP').text
            return exp
    except:
        return 'An error occured.'       

def main():
    # take inputs from user
    to_addr = raw_input("Please enter the target address: ")    
    from_addr = raw_input("Please enter the your address: ")
    pwd = raw_input("Please enter the your password: ")
    msg = raw_input("Please enter your message: \n")

    sm = postman(to_addr, from_addr, pwd, msg)
    print(sm)

if __name__ == "__main__":
    main()
