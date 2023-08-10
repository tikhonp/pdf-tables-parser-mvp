import xml.dom.minidom
from pathlib import Path

from tqdm import tqdm

from models.ProductType import ProductType


def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default


def get_element_from(xml_element: xml.dom.minidom.Element, tag: str, python_type):
    element = safe_list_get(xml_element.getElementsByTagName(tag), 0, "")
    if isinstance(element, python_type):
        return element
    elif isinstance(element.childNodes, xml.dom.minicompat.NodeList):
        node = safe_list_get(element.childNodes, 0, "")
        if isinstance(node, str):
            return node
        else:
            return python_type(node.data)
    else:
        return element


def parse_product_type(xml_element) -> ProductType:
    return ProductType(
        identifier=get_element_from(xml_element, "Ref", str),
        is_folder=get_element_from(xml_element, "IsFolder", str),
        is_deleted=get_element_from(xml_element, "DeletionMark", str),
        parent=get_element_from(xml_element, "Parent", str),
        code=get_element_from(xml_element, "Code", str),
        description=get_element_from(xml_element, "Description", str),
        article=get_element_from(xml_element, "Артикул", str),
        basic_unit=get_element_from(xml_element, "БазоваяЕдиницаИзмерения", str),
        weight=get_element_from(xml_element, "Весовой", str),
        weight_factor_of_occurrence=get_element_from(xml_element, "ВесовойКоэффициентВхождения", str),
        keep_operational_records_of_balances=get_element_from(xml_element,
                                                         "ВестиОперативныйУчетОстатковНЗП", str),
        keep_batch_records_by_series=get_element_from(xml_element, "ВестиПартионныйУчетПоСериям", str),
        keep_records_by_series=get_element_from(xml_element, "ВестиУчетПоСериям", str),
        keep_records_by_series_VNZP=get_element_from(xml_element, "ВестиУчетПоСериямВНЗП", str),
        keep_records_by_characteristics=get_element_from(xml_element, "ВестиУчетПоХарактеристикам", str),
        type_of_reproduction=get_element_from(xml_element, "ВидВоспроизводства", str),
        type_of_nomenclature=get_element_from(xml_element, "ВидНоменклатуры", str),
        units_for_reports=get_element_from(xml_element, "ЕдиницаДляОтчетов", str),
        unit_of_storage_of_leftovers=get_element_from(xml_element, "ЕдиницаХраненияОстатков", str),
        is_set=get_element_from(xml_element, "Набор", str),
        purpose_of_use=get_element_from(xml_element, "НазначениеИспользования", str),
        full_name=get_element_from(xml_element, "НаименованиеПолное", str),
        nomenclature_group=get_element_from(xml_element, "НоменклатурнаяГруппа", str),
        nomenclature_group_of_costs=get_element_from(xml_element, "НоменклатурнаяГруппаЗатрат", str),
        number_GTD=get_element_from(xml_element, "НомерГТД", str),
        main_image=get_element_from(xml_element, "ОсновноеИзображение", str),
        main_supplier=get_element_from(xml_element, "ОсновнойПоставщик", str),
        responsible_manager=get_element_from(xml_element, "ОтветственныйМенеджерЗаПокупки", str),
        bet_NDS=get_element_from(xml_element, "СтавкаНДС", str),

        cost_item=get_element_from(xml_element, "СтатьяЗатрат", str),
        country=get_element_from(xml_element, "СтранаПроисхождения", str),
        external_certification=get_element_from(xml_element, "ТребуетсяВнешняяСертификация", str),
        internal_certification=get_element_from(xml_element, "ТребуетсяВнутренняяСертификация", str),
        service=get_element_from(xml_element, "Услуга", str),
        serial_numbers=get_element_from(xml_element, "ВестиСерийныеНомера", str),
        complect=get_element_from(xml_element, "Комплект", str),

        direction_Of_WriteOff_Of_Manufactured_Products=get_element_from(xml_element,
                                                                   "НаправлениеСписанияВыпущеннойПродукции",
                                                                   str),
        assigning_a_serial_number=get_element_from(xml_element, "ПорядокПрисвоенияСерийногоНомера", str),
        price_group=get_element_from(xml_element, "ЦеноваяГруппа", str),
        OKP=get_element_from(xml_element, "ОКП", str),
        budget_item=get_element_from(xml_element, "СтатьяБюджета", str),
        service_material_classifier=get_element_from(xml_element, "КлассификаторМатериаловУслуг", str),
        unit_of_measurement=get_element_from(xml_element, "ЕдиницаИзмеренияМест", str),
        emergency_Stock_Nomenclature=get_element_from(xml_element, "НоменклатураАварийногоЗапаса", str),
        correct_Nom=get_element_from(xml_element, "ПравильнаяНоменклатура", str),
        delete=get_element_from(xml_element, "НаУдаление", str),
        Code_OKPD=get_element_from(xml_element, "КодОКПД", str),
        Lom149NK=get_element_from(xml_element, "Лом149НК", str),
        Code_TNVED=get_element_from(xml_element, "КодТНВЭД", str),
    )


def product_type_parser(file: Path) -> [ProductType]:
    tag_name = "CatalogObject.Номенклатура"
    xml_doc = xml.dom.minidom.parse(str(file))
    product_types = []
    for e in tqdm(xml_doc.getElementsByTagName(tag_name)):
        product_types.append(parse_product_type(e))
    return product_types
