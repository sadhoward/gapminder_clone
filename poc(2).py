import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation



##從 plotting 檢視表選取所有的資料
connection=sqlite3.connect("data/gapminder.db")
plotting_df=pd.read_sql("""select*from plotting;""",con=connection)
connection.close
#透過matploting繪製動畫
fig, ax = plt.subplots() #建畫布
#定義一個函數
def updare_plot(year_to_plot):
    ax.clear()
    subset_df = plotting_df[plotting_df["dt_year"] == year_to_plot]
    lex = subset_df["life_expectancy"].values #y軸變數
    gdp_pcap = subset_df["gdp_per_capita"].values#X軸變數
    cont = subset_df["continent"].values#顏色
    ##print(subset_df["continent"].unique()) #要幾個顏色
    color_map = {
        "asia": "r",
        "africa": "g",
        "europe": "b",
        "americas": "c"
        }
    for xi, yi, ci in zip(gdp_pcap, lex, cont):
        ax.scatter(xi, yi, color=color_map[ci])
    #走回圈
    ax.set_title(f"The world in {year_to_plot}")
    ax.set_xlabel("GDP Per Capita(in USD)")
    ax.set_ylabel("Life Expectancy")
    ax.set_ylim(20, 100)
    ax.set_xlim(0, 100000)
    plt.show()
ani=animation.FuncAnimation(fig,func=updare_plot, frames=range(2000,2024), interval=10)
ani.save("animation.gif",fps=10)