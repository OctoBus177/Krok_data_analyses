
import matplotlib.pyplot as plt
import import_data as id


def make_region_draw():
    df_to_diagram = id.get_df_from_excel('./Analysis.xlsx', 'region')
    print(df_to_diagram)
    plt.bar( df_to_diagram['Продажи, руб'],df_to_diagram['Город'])
    plt.show()