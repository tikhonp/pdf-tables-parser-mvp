from pathlib import Path

from pandas import DataFrame

from img2table.document import PDF


from img2table.ocr import TesseractOCR


def get_tables(file: Path) -> [DataFrame]:
    pdf = PDF(file,
              pages=None,
              detect_rotation=True,
              pdf_text_extraction=True)

    ocr = TesseractOCR(lang="rus")

    # Table identification and extraction
    pdf_tables = pdf.extract_tables(ocr=ocr)

    output_tables = []
    for _, tables in pdf_tables.items():
        output_tables += [t.df for t in tables]
    return output_tables
