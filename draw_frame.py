
import matplotlib.pyplot as plt
import import_data as id


def make_region_draw():
    df_to_diagram = id.get_df_from_excel('/home/octobus/work/Krok_it_school/Krok_data_analyses/Analysis.xlsx', 'region')
    fig, graphic = plt.subplots()
    graphic.barh(df_to_diagram['Город'], df_to_diagram['Продажи, руб'])
    fig.set_figwidth(16)
    fig.set_figheight(6)
    plt.show()