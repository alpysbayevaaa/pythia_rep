from matplotlib import pyplot as plt
#from matplotlib import style
import numpy as np
import statistics

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

# Configuration matrices
nopref_x = []
bingo_x = []
dspatch_x = []
mlop_x = []
ppf_x = []
pythia_x = []
spp_x = []

# confs matrix
confs=[bingo_x, dspatch_x, mlop_x, ppf_x, pythia_x, spp_x]

# Workload matrices
cassandra_y = []
cloud9_y = []
nutch_y = []
classification_y = []
streaming_y = []

# Workloads_y maxtrix
workloads_y = [cassandra_y, cloud9_y, nutch_y, classification_y, streaming_y]

# average matrix
average = [0] * 5

# stdev matrix
stdev = []

# COV matrix
cov = []

# header matrix
header = ['configurations','Cassandra','Cloud9','Nutch','Classification','Streaming']

conf0 = ['NOPREF']
conf1 = ['BINGO']
conf2 = ['DSPATCH']
conf3 = ['MLOP']
conf4 = ['PPF']
conf5 = ['PYTHIA']
conf6 = ['SPP']
avg_y = ['AVG']
stdev_y = ['STDEV']
cov_y = ['COV']

outs = [header, conf0, conf1, conf2, conf3, conf4, conf5, conf6, avg_y, stdev_y, cov_y]	

for workload in workloads:
	nopref_x.append(nopref_sum[f"{workload=}"])
	bingo_x.append(bingo_sum[f"{workload=}"])
	dspatch_x.append(dspatch_sum[f"{workload=}"])
	mlop_x.append(mlop_sum[f"{workload=}"])
	ppf_x.append(ppf_sum[f"{workload=}"])
	pythia_x.append(pythia_sum[f"{workload=}"])
	spp_x.append(spp_sum[f"{workload=}"])

for conf in confs:
	cassandra_y.append(float(conf[0]))
	cloud9_y.append(float(conf[1]))
	nutch_y.append(float(conf[2]))
	classification_y.append(float(conf[3]))
	streaming_y.append(float(conf[4]))

for workload_y in workloads_y:
	stdev.append(statistics.stdev(workload_y))

for conf in confs:
	for i in range(5):
		average[i] = average[i] + conf[i]

for i in range(5):
	average[i] = average[i] / 6

for i in range(5):
	cov.append(stdev[i]/average[i])

for i in range(5):
	conf0.append(str(round(nopref_x[i],5)))
	conf1.append(str(round(bingo_x[i],5)))
	conf2.append(str(round(dspatch_x[i],5)))
	conf3.append(str(round(mlop_x[i],5)))
	conf4.append(str(round(ppf_x[i],5)))
	conf5.append(str(round(pythia_x[i],5)))
	conf6.append(str(round(spp_x[i],5)))
	avg_y.append(str(round(average[i],5)))
	stdev_y.append(str(round(stdev[i],5)))
	cov_y.append(str(round(cov[i],5)))

output = []

for out in outs:
	out[-1] = out[-1]+'\n'

for out in outs:
	output.append(out)

a = np.asarray(output)

a.tofile("statistics.csv", sep=',', format='%s')

print(output)

ind = np.arange(0,N,1.25)
width = 0.25
bar_colors = ['w', 'black']
fig = plt.subplots(figsize = (15, 8))
p1 = plt.bar(ind, nopref_x, color=bar_colors[0], align='edge', edgecolor='black', width=width, hatch='//')
p2 = plt.bar(ind+3*width/2, average, color=bar_colors[1], align='edge', edgecolor='black', width=width)
plt.title('Cloud Suite (MTPS2400)')
plt.xticks(ind+0.2, ('Cassandra','Cloud9','Nutch','Classification','Streaming'))
plt.ylim(0, 3.0)
plt.xlim(-0.2, 6.7)
plt.legend((p1[0], p2[0]),("w/o prefetch","prefetch"))
plt.show()