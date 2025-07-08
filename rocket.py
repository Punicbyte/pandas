import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
fd001_train=pd.read_csv("nasa.csv",sep=" ",header=None)
fd001_train.drop(fd001_train.columns[[26,27]], axis=1,inplace=True)
fd001_train.columns=['unit_number','time_in_cycles','setting_1','setting_2','TRA','T2','T24','T30','T50','P2','P15','P30','Nf',
           'Nc','epr','Ps30','phi','NRf','NRc','BPR','farB','htBleed','Nf_dmd','PCNfR_dmd','W31','W32' ]
fd001_train.drop(['Nf_dmd','PCNfR_dmd','P2','T2','TRA','farB','epr'],axis=1,inplace=True)
fd001_train["max"]=fd001_train.groupby("unit_number").time_in_cycles.transform("max")
fd001_train["RUL"]=fd001_train["max"]-fd001_train["time_in_cycles"]
fd001_train.drop("max",axis=1,inplace=True)


sns.heatmap(fd001_train.corr(),annot=True,cmap="RdYlGn",linewidths=0.2,linecolor="black")
fig=plt.gcf()
fig.set_size_inches(20,20)
plt.show()


