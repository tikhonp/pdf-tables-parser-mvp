import os
import sys
from pathlib import Path

from get_final_rows import get_final_rows
from get_tables import get_tables


def parse_input_file() -> Path:
    try:
        return Path(sys.argv[1])
    except IndexError:
        print("Usage: " + os.path.basename(__file__) + " <file path>")
        sys.exit(1)


if __name__ == "__main__":
    file_path = parse_input_file()
    dataframes = get_tables(file_path)
    final_data = [get_final_rows(d) for d in dataframes]
    print(final_data)
