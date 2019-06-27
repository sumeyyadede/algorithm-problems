import requests
import string
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def editFile(toaddr, fromaddr, password, msg):
    # edit header file 
    with open("header", "r") as file:
        line = file.readline()
        newLog = ''
        i = 0
        while line:
            if i == 1:
                newLine = '<USR>' + str(fromaddr) + '</USR>' + '\n'
            elif i == 2:
                newLine = '<PWD>' + str(password) + '</PWD>' + '\n'
            elif i == 8:
                newLine = '<MSG>' + str(msg) + '</MSG>' + '\n'
            elif i == 9:
                newLine = '<TA>' + str(toaddr) + '</TA>' + '\n'
            else:
                newLine = line
            newLog = newLog + newLine
            i = i + 1
            line = file.readline()

    with open('header','w') as file:
        file.write(newLog)

    sendMail()
    
def sendMail():
    txt_file = "header"
    xml_file = "return.xml"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # sending mail
    with open(txt_file) as txt_file:    
        response = requests.post('https://ppapi.smartmessage-engage.com/SENDEML', data = txt_file, headers = headers)

        #write the response.content in the xml_file
        with open(xml_file, 'w') as xml_file:
            xml_file.write(response.content)
            xml_file.close()

            #take the 'EXP' content
            parser = ET.XMLParser(encoding = "utf-8")
            root = ET.parse("return.xml", parser = parser)
            sh = root.find('EXP')
            print(sh.text)

def main():
    # take inputs from user
    toaddr = raw_input("Please enter the target address: ")    
    fromaddr = raw_input("Please enter the your address: ")
    password = raw_input("Please enter the your password: ")
    msg = raw_input("Please enter your message: \n")
    editFile(toaddr, fromaddr, password, msg)



if __name__ == "__main__":
    main()
