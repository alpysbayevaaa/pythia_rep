from matplotlib import pyplot as plt
#from matplotlib import style
import numpy as np

#style.use('ggplot')

N = 6

cassandra = np.genfromtxt('rollup-cassandra_with_nopref.csv',dtype = None, delimiter = ',', names = True)
cloud9 = np.genfromtxt('rollup-cloud9_with_nopref.csv',dtype = None, delimiter = ',', names = True)
nutch = np.genfromtxt('rollup-nutch_with_nopref.csv',dtype = None, delimiter = ',', names = True)
classification = np.genfromtxt('rollup-classification_with_nopref.csv',dtype = None, delimiter = ',', names = True)
streaming = np.genfromtxt('rollup-streaming_with_nopref.csv',dtype = None, delimiter = ',', names = True)

workloads=[cassandra,cloud9,nutch,classification,streaming]
unique_Exp = np.unique(cassandra['Exp'])
nopref_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'nopref_MTPS2400'].sum() for workload in workloads}
bingo_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'bingo_MTPS2400'].sum() for workload in workloads}
dspatch_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'dspatch_MTPS2400'].sum() for workload in workloads}
mlop_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'mlop_MTPS2400'].sum() for workload in workloads}
ppf_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'ppf_MTPS2400'].sum() for workload in workloads}
pythia_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'pythia_MTPS2400'].sum() for workload in workloads}
spp_sum = {f"{workload=}": workload['Core_0_IPC'][workload['Exp'] == 'spp_MTPS2400'].sum() for workload in workloads}

nopref_x = []
bingo_x = []
dspatch_x = []
mlop_x = []
ppf_x = []
pythia_x = []
spp_x = []
for workload in workloads:
	nopref_x.append(nopref_sum[f"{workload=}"])
	bingo_x.append(bingo_sum[f"{workload=}"])
	dspatch_x.append(dspatch_sum[f"{workload=}"])
	mlop_x.append(mlop_sum[f"{workload=}"])
	ppf_x.append(ppf_sum[f"{workload=}"])
	pythia_x.append(pythia_sum[f"{workload=}"])
	spp_x.append(spp_sum[f"{workload=}"])
ind = np.arange(0,N,1.25)
width = 0.25
#bar_labels = ['red', 'blue', 'green', 'orange', 'pink']
bar_colors = ['w', 'tab:green', 'tab:blue', 'tab:red', 'tab:grey', 'tab:olive', 'tab:purple']

fig = plt.subplots(figsize = (15, 8))

p1 = plt.bar(ind, nopref_x, color=bar_colors[0], align='edge', edgecolor='black', width=width, hatch='//')
p2 = plt.bar(ind+3*width/5, dspatch_x, color=bar_colors[1], align='edge', edgecolor='black', width=width)
p3 = plt.bar(ind+6*width/5, mlop_x, color=bar_colors[2], align='edge', edgecolor='black', width=width)
p4 = plt.bar(ind+9*width/5, bingo_x, color=bar_colors[3], align='edge', edgecolor='black', width=width)
p5 = plt.bar(ind+12*width/5, ppf_x, color=bar_colors[4], align='edge', edgecolor='black', width=width)
p6 = plt.bar(ind+15*width/5, pythia_x, color=bar_colors[5], align='edge', edgecolor='black', width=width)
p7 = plt.bar(ind+18*width/5, spp_x, color=bar_colors[6], align='edge', edgecolor='black', width=width)
plt.title('Cloud Suite (MTPS2400)')
plt.xticks(ind+0.55, ("cassandra","cloud9","nutch","classification","streaming"))
plt.ylim(0, 3.0)
plt.xlim(-0.2, 6.7)
plt.legend((p4[0], p2[0], p3[0], p1[0], p5[0], p6[0], p7[0]),unique_Exp)
plt.show()