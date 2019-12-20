
import pandas as pd
from pandas import DataFrame


def Exercise_1():
    k = int(input("input an integer："))
    assert isinstance(k, int)
    left = sum(range(1, k + 2))
    right = int(((k + 1) * ((k + 1) + 1)) / 2)
    print("left:{}, right:{}".format(left, right))
    assert left == right


def decimals(x):
    return "{:0.2f}".format(x)


def Exercise_2():
    data = pd.read_csv("wiki_data.csv")
    data_new = pd.DataFrame()

    data_new['people-per-km'] = data['Population'] / data['Totalarea(km)']
    data_new['people-per-miles'] = data['Population'] / (data['Totalarea(km)'] * 0.62137 ** 2)
    data_new['Country'] = data['Country']
    data_new['City'] = data['City']
    df1 = data_new.sort_values(by='people-per-km')
    df1.to_csv("results.csv", index=None)


def Exercise_3():
    import numpy as np
    import statsmodels.api as sm
    x = np.arange(-10, 10)
    y = 2 * x + np.random.normal(size=len(x))
    X = sm.add_constant(x)
    model = sm.OLS(y, X)
    fit = model.fit()
    print("y={}".format(fit.params[0]), "+", "{}x".format(fit.params[1]))


Exercise_1()
print("===========================================")
Exercise_2()
print("===========================================")
Exercise_3()
