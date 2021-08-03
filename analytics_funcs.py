import pandas as pd
import export_data as ed

id_contr = 'Факты.Контрагент ID'
name_spend ='Продажи, руб'
name_marj = 'Маржинальная прибыль'
name_city = 'Город'

def analysis_partners_by_region(df_part, df_sales):
    df_result = df_part.merge(df_sales,how = 'inner', left_on= 'Контрагент ID', right_on = 'Факты.Контрагент ID')
    unique_df_reg = df_result['Регион'].unique()
    df_total = pd.DataFrame(columns=[name_city, name_spend])
    for row in unique_df_reg:
        help = [str(row)]
        res_sum_sale = df_result.loc[df_result['Регион'].isin(help)][name_spend].sum()
        new_row = {
            name_city: row,
            name_spend: res_sum_sale
        }

        df_total = df_total.append(new_row, ignore_index= True)

    df_total =  df_total.sort_values(by = name_spend, ascending=False)
    ed.export_df_in_excel('/home/octobus/work/Krok_it_school/Krok_data_analyses/Analysis.xlsx', 'region', df_total)
