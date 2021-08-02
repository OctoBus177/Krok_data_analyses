import pandas as pd

def export_df_in_excel(name_file,name_list , df):
    df.to_excel(name_file, sheet_name=name_list)
