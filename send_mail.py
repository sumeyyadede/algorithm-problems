import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#constant variables for body
JID = "47de74b5-8c7e-4e33-a55a-a7ba00f4ecdc"
CG = "Standart"
SBJ = "SM Engage Campaign"

#for xml create an object 
class Header(object):
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
        xml_file = "header.xml"
        with open(xml_file, 'w') as xml_file:
            xml_file.write("data=")
            tree.write(xml_file, xml_declaration = True)
            xml_file.close()
     
def postman(to_addr, from_addr, pwd, msg):
    # create and write body in the file
    head_file = Header()
    head_file.ta = to_addr
    head_file.user = from_addr
    head_file.pwd = pwd
    head_file.msg = msg 
    head_file.make_body()
    
    # define files and headers
    first_xml = "header.xml"
    second_xml = "return.xml"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # sending mail
    with open(first_xml) as first_xml:    
        response = requests.post('https://ppapi.smartmessage-engage.com/SENDEML', data = first_xml, headers = headers)

        # write the response.content in the file
        with open(second_xml, 'w') as second_xml:
            second_xml.write(response.content)
            second_xml.close()
            
            # take explanation  
            parser = ET.XMLParser(encoding = "utf-8")
            root = ET.parse("return.xml", parser = parser)
            exp = root.find('EXP').text
            return exp

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
