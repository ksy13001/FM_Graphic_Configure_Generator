import os
import xml.etree.ElementTree as ET

apply_format = ["png", "jpeg"]
config = ET.parse("config.xml")
root = config.getroot()
maps_list = root.find(".//list[@id='maps']")


def indent(elem, level=0):
    """XML 들여쓰기를 적용하기 위한 재귀 함수."""
    i = "\n" + "    " * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        for child in elem:
            indent(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def get_path(name):
    return "graphics/pictures/person/"+name+"/portrait"


def add_new_record(img):
    file = img.split('.')
    img_name, img_format = file[0], file[1]
    if img_format not in apply_format:
        return
    for now in maps_list:
        if img_name == now.attrib.get("from"):
            return
    new_record = ET.Element("record")
    new_record.set("from", img_name)
    new_record.set("to", get_path(img_name))
    maps_list.append(new_record)
    print("새로운 record가 추가되었습니다." + img_name)


for file in os.listdir(os.getcwd()):
    add_new_record(file)

indent(root)
config.write("config.xml")