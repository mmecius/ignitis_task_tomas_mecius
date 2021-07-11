import pandas as pd  # type: ignore

ignore_missing_imports = True
file_path = "files/excel_files/grupės.xlsx"


class ExcelFileManager:
    def read_excel_file_to_list(self: str) -> str:
        """Reads excel file to DataFrame"""
        df = pd.read_excel(file_path)
        list_groups = df["Pavadinimas"].tolist()
        return list_groups
