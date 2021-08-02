import pandas as pd


def get_df_from_excel(name_file, name_list):
    excel = pd.ExcelFile(name_file)
    return excel.parse(name_list)
