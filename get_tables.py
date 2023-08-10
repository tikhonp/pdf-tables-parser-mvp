from pathlib import Path

from img2table.document import PDF
from img2table.ocr import TesseractOCR
from pandas import DataFrame


def get_tables(file: Path) -> [DataFrame]:
    pdf = PDF(str(file), detect_rotation=False, pdf_text_extraction=True)

    ocr = TesseractOCR(lang="rus")

    # Table identification and extraction
    pdf_tables = pdf.extract_tables(ocr=ocr)
    print(pdf_tables)
    output_tables = []
    for _, tables in pdf_tables.items():
        output_tables += [t.df for t in tables]
    return output_tables
