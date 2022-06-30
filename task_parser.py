import xml.dom.minidom
import xml.etree.cElementTree as ET
import xmltodict
def main():
    data = xmltodict.parse("task.xml")
    # use the parse() function to load and parse an XML file
    # tree = ET.parse("task.xml")
    #
    # # get root element
    # root = tree.getroot()
    #
    # # print out the document node and the name of the first child tag
    # print (doc.nodeName)
    # print (doc.firstChild.tagName)
    #
    # # get a list of XML tags from the document and print each one
    # field = doc.getElementsByTagName("field")
    # print ("%d field:" % field.length)
    #
    # for i in field:
    #     print(i.getAttribute("name"))


print("Calling parser...")
main()