import xml.dom.minidom
from pathlib import Path

from models import Unit


def parse_unit_element(xml_element) -> Unit:
    description = ""
    try:
        description = xml_element.getElementsByTagName("Description")[0].childNodes[0].data
    except IndexError:
        pass
    full_name = ""
    try:
        full_name = xml_element.getElementsByTagName("НаименованиеПолное")[0].childNodes[0].data
    except IndexError:
        pass
    return Unit(identifier=xml_element.getElementsByTagName("Ref")[0].childNodes[0].data,
                is_deleted=xml_element.getElementsByTagName("DeletionMark")[0].childNodes[0].data,
                code=xml_element.getElementsByTagName("Code")[0].childNodes[0].data, description=description,
                full_name=full_name, is_discrete=xml_element.getElementsByTagName("Дискретная")[0].childNodes[0].data, )


def unit_parser(file: Path) -> [Unit]:
    tag_name = "CatalogObject.КлассификаторЕдиницИзмерения"
    xml_doc = xml.dom.minidom.parse(str(file))
    return [parse_unit_element(e) for e in xml_doc.getElementsByTagName(tag_name)]
