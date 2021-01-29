import re
import xml.etree.ElementTree as ET


rex = re.compile(r'''(?P<title>entity_relation
                               |entity
                               |Entity
                               |att_count
                               |attributes
                               
                               |relationship
                               
                     )
                     \s*:?\s*
                     (?P<value>.*)
                     ''', re.VERBOSE)
name = 0
count = 0
root = ET.Element('root')
root.text = '\n'    # newline before the celldata element
tempv = []
tempv1 = []

f = open("../users/Entity_attribute.txt","r" )
celldata = ET.SubElement(root, 'celldata')
celldata.text = '\n'    
celldata.tail = '\n\n'  
status = 0              
for line in f:
    if status == 0:     
            
        m = rex.search(line)
        if m:
                
            title = m.group('title')
            title = title.replace('&', '')
            title = title.replace(' ', '')

            if line.startswith('entity'):
                e = ET.SubElement(celldata, title.lower())
                e.text = m.group('value')
                e.tail = '\n'
                name = e.text

            elif line.startswith('entity_relation'):
                er = ET.SubElement(celldata, title.lower())
                er.text = m.group('value')
                er.tail = '\n'
                   

            elif line.startswith('relationship'):
                r = ET.SubElement(celldata, title.lower())
                r.text = m.group('value')
                r.tail = '\n'
                        
               
                    
            elif line.startswith('att_count'):
                count = int(m.group('value'))
                #print(count)
                    
            elif line.startswith('attributes'):
                attributes = ET.SubElement(celldata,'Entity' )
                attributes.text = '\n'
                attributes.attrib['name'] = name
                attributes.tail = '\n'
                    
                for i in range(0 , count):
                    tempv = line.split(':')[1]
                    tempv2 = tempv.split('\n')[0]
                    tempv1 = tempv2.split(',')
                    item = ET.SubElement(attributes, 'Attributes')
                    item.tail = '\n'
                    item.text = tempv1[i]
         
                    
            elif line.isspace():
                    celldata = ET.SubElement(root, 'celldata')
                    celldata.text = '\n'
                    celldata.tail = '\n\n'
                    status = 0
            else:
                raise LogicError('Unexpected status {}.'.format(status))
                break
                               


    tree = ET.ElementTree(root)
    tree.write("../users/cell.xml ", encoding='utf-8', xml_declaration=True)
