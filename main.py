import pandas as pd

import import_data as id
import export_data as ed
import analytics_funcs as af
import draw_frame

NAME = "/home/octobus/work/Krok_it_school/Krok_data_analyses/DataSet_практика.xlsx"
SALES = "Подажи"
PRODUCTS = "Товары"
PARTNERS = "Контрагенты"

ANALYSIS = "ANALYSIS"

ANALYSIS_PARTNERS_BY_REGION = "./ANALYSIS_PARTNERS_BY_REGION"

if __name__=="__main__":
    df_sales = id.get_df_from_excel(NAME, SALES)
    df_products = id.get_df_from_excel(NAME, PRODUCTS)
    df_partners = id.get_df_from_excel(NAME, PARTNERS)
    af.analysis_partners_by_region(df_partners, df_sales)
    draw_frame.make_region_draw()