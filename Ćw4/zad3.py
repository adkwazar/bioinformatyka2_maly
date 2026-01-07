import matplotlib.pyplot as plt
from scipy import stats

x = [] #tutaj po przecinku wpisz ekspresje genuA w kolejnych chwilach czasowych
y = [] #tutaj po przecinku wpisz ekspresje genuB w kolejnych chwilach czasowych

#rysuje wykres y(x)
plt.scatter(x, y)
plt.show()

#wyznacza wsp. korelacji oraz wartosc pvalue
res = stats.spearmanr(x, y)
print(res.statistic)
print(res.pvalue)
