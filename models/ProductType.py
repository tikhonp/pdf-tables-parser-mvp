from dataclasses import dataclass


@dataclass
class ProductType:
    identifier: str
    is_deleted: bool
    code: int
    description: str
    full_name: str
    weight: bool
    keep_operational_records_of_balances: bool
    keep_records_by_series_VNZP: bool
    is_set: bool
    external_certification: bool
    internal_certification: bool
    service: bool
    serial_numbers: bool
    complect: bool
    Lom149NK: bool
    delete: bool
    responsible_manager: str
    bet_NDS: str
    is_folder: bool
    emergency_Stock_Nomenclature: bool
    parent: str
    article: str
    basic_unit: str
    weight_factor_of_occurrence: int
    keep_batch_records_by_series: bool
    keep_records_by_series: bool
    keep_records_by_characteristics: bool
    type_of_reproduction: str
    type_of_nomenclature: str
    units_for_reports: str
    unit_of_storage_of_leftovers: str
    purpose_of_use: int
    nomenclature_group: int
    nomenclature_group_of_costs: int
    number_GTD: int
    main_image: int
    main_supplier: int
    cost_item: int
    country: int
    direction_Of_WriteOff_Of_Manufactured_Products: int
    assigning_a_serial_number: int
    price_group: int
    OKP: int
    budget_item: int
    service_material_classifier: int
    unit_of_measurement: int
    correct_Nom: int
    Code_OKPD: int
    Code_TNVED: int

    def __str__(self):
        return self.full_name
