# import lxml.etree as ET
# import xml.etree.ElementTree as ET

    xml_file = "header"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    with open(xml_file) as xml_file:    
        response = requests.post('https://ppapi.smartmessage-engage.com/SENDEML', data = xml_file, headers = headers)
    print(response.content)



    
    tree = ET.ElementTree(file = 'header.xml')
    root = tree.getroot()
    
    for elem in tree.iter(tag='USR'):
        elem.tag = fromaddr




    # xml_file = "header.xml"
    # xmltest = ET.fromstring(xml_file.encode("latin-1"))

    # parser = ET.XMLParser(encoding = "utf-8")
    # tree = ET.parse('header.xml', parser = parser)
    # sh = tree.find('TA')
    # sh.set(toaddr)
    
    # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # payload = {'USR': fromaddr,
    #            'PWD': password,
    #            'MSG': msg,
    #            'TA' : toaddr}
    # payld = json.dumps(payload)
    # ret = requests.post('https://ppapi.smartmessage-engage.com/SENDEML', headers = headers, data = payld)



    with open('header.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        
        for elem in root.getiterator():
            try:
                # elem.text = elem.text.replace('USR', fromaddr)
                # elem.text = elem.text.replace('PWD', password)
                elem.text = elem.text.replace('MSG', message)
                elem.text = elem.text.replace('TA', toaddr)
            except AttributeError:
                pass
        
    f.write(ET.tostring(tree, encoding = 'UTF-8', xml_declaration = True))        
    f.truncate()    
    
    # tree = et.parse('header.xml')
    # tree.find('USR').text = fromaddr
    # tree.find('PWD').text = password
    # tree.find('MSG').text = password
    # tree.write('header.xml')

    # with open('header.xml', 'rt') as xml_file:
    #     tree = ET.parse(xml_file)


    # parser = etree.XMLParser(encoding = "utf-8")
    # targetTree = etree.parse("./header.xml", parser = parser)
    # pageIds = targetTree.find("TA")

    # print "pageIds:",etree.tostring(pageIds)
    
    # with open('header.xml', 'rt') as xml_file:
    #     tree = ET.parse(xml_file)

    # parser = ET.XMLParser(encoding = "utf-8")
    # tree = ET.parse("header.xml", parser = parser)
    # tree = ET.ElementTree(file = 'header.xml')


    # root2 = ET.fromstring("header.xml", parser = parser)
    # root = ET.parse("header.xml", parser = parser)
    # sh = root.find('TA')
    # sh.set(toaddr)

    # parser = ET.XMLParser(encoding = "utf-8")
    # tree = ET.fromstring(open('header.xml').read())

    # tree = ET.fromstring(tree, parser = parser)
    # tree = ET.parse('header.xml')
    
    # r = requests.get('https://ppapi.smartmessage-engage.com/SENDEML', auth = (fromaddr, password))

