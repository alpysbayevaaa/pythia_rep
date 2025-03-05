#from matplotlib import pyplot as plt
#from matplotlib import style
from IPython.display import display
#from PyQt5.QtWidgets import QWidget,QScrollArea, QTableWidget, QVBoxLayout,QTableWidgetItem,QApplication
import numpy as np
import pandas as pd
#import seaborn as sns
#from sklearn import preprocessing

N = 6
cassandra = pd.read_csv('rollup_cassandra.csv', sep = ',', header=None)
cloud9 = pd.read_csv('rollup-cloud9.csv', sep = ',', header=None)
nutch = pd.read_csv('rollup-nutch.csv', sep = ',', header=None)
classification = pd.read_csv('rollup-classification.csv', sep = ',', header=None)
streaming = pd.read_csv('rollup-streaming.csv',sep = ',', header=None)
workloads=[cassandra,cloud9,nutch,classification,streaming]
unique_Exp = np.unique(cassandra[1][1:])

cassandra_mod = cassandra[2][1:].values
sum = 0
lenght = len(cassandra_mod)
print(lenght)
print(cassandra_mod)
for i in range(lenght):
	sum = sum + float(cassandra_mod[i-1])
ave = sum/lenght
print(sum)
print(ave)

df =  pd.DataFrame(cassandra_mod)

print(df)
print(unique_Exp)
display(cassandra_mod)



'''
sns.heatmap(cassandra_mod)
#sns.heatmap(cassandra_mod, annot=False)

plt.show()
win = QWidget()
scroll = QScrollArea()
layout = QVBoxLayout()
table = QTableWidget()
scroll.setWidget(table)
layout.addWidget(table)
win.setLayout(layout)

table.setColumnCount(len(df.columns))
table.setRowCount(len(df.index))
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        table.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))

win.show()


#stats_df = pd.DataFrame({
#"Mean": df.mean()

#cassandra_avg = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'bingo_MTPS2400'].sum() for workload in workloads}
bingo_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'bingo_MTPS2400'].sum() for workload in workloads}
dspatch_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'dspatch_MTPS2400'].sum() for workload in workloads}
mlop_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'mlop_MTPS2400'].sum() for workload in workloads}
ppf_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'ppf_MTPS2400'].sum() for workload in workloads}
pythia_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'pythia_MTPS2400'].sum() for workload in workloads}
spp_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'spp_MTPS2400'].sum() for workload in workloads}


#print(grouped_means['bingo_MTPS2400'])
#print(np.average(cassandra['Core_0_IPC']))
#print(np.average(cassandra['Core_0_LLC_total_miss']))
#print(np.average(cassandra['Core_0_LLC_load_miss']))
#print(np.average(cassandra['Core_0_LLC_RFO_miss']))
#print(np.average(cassandra['Core_0_LLC_writeback_miss']))
#print(np.average(cassandra['Filter']))
bingo_x = []
dspatch_x = []
mlop_x = []
ppf_x = []
pythia_x = []
spp_x = []
for workload in workloads:
	bingo_x.append(bingo_sum[f"{workload=}"])
	dspatch_x.append(dspatch_sum[f"{workload=}"])
	mlop_x.append(mlop_sum[f"{workload=}"])
	ppf_x.append(ppf_sum[f"{workload=}"])
	pythia_x.append(pythia_sum[f"{workload=}"])
	spp_x.append(spp_sum[f"{workload=}"])
ind = np.arange(0,N,1.35)
width = 0.25
#bar_labels = ['red', 'blue', 'green', 'orange', 'pink']
bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:grey', 'tab:olive', 'tab:purple']

#fig = plt.subplots(figsize = (15, 8))
#p1 = plt.bar(ind, bingo_x, color=bar_colors[0], align='edge', width=width)
#p2 = plt.bar(ind+3*width/4, dspatch_x, color=bar_colors[1], align='edge', width=width)
#p3 = plt.bar(ind+6*width/4, mlop_x, color=bar_colors[2], align='edge', width=width)
#p4 = plt.bar(ind+9*width/4, ppf_x, color=bar_colors[3], align='edge', width=width)
#p5 = plt.bar(ind+12*width/4, pythia_x, color=bar_colors[4], align='edge', width=width)
#p6 = plt.bar(ind+15*width/4, spp_x, color=bar_colors[5], align='edge', width=width)
#plt.title('Cloud Suite (MTPS2400)')
#plt.xticks(ind+0.55, ("cassandra","cloud9","nutch","classification","streaming"))
#plt.ylim(0, 3.0)
#plt.xlim(-0.2, 6.7)
#plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]),unique_Exp)
#plt.show()

#app = QApplication([])
cassandra = np.genfromtxt('rollup_cassandra.csv',dtype = None, delimiter = ',', names = True)

cloud9 = np.genfromtxt('rollup-cloud9.csv',dtype = None, delimiter = ',', names = True)
nutch = np.genfromtxt('rollup-nutch.csv',dtype = None, delimiter = ',', names = True)
classification = np.genfromtxt('rollup-classification.csv',dtype = None, delimiter = ',', names = True)
streaming = np.genfromtxt('rollup-streaming.csv',dtype = None, delimiter = ',', names = True)
'''