from matplotlib import pyplot as plt
#from matplotlib import style
import numpy as np

#style.use('ggplot')

N = 6

cassandra = np.genfromtxt('rollup_cassandra.csv',dtype = None, delimiter = ',', names = True)
cloud9 = np.genfromtxt('rollup-cloud9.csv',dtype = None, delimiter = ',', names = True)
nutch = np.genfromtxt('rollup-nutch.csv',dtype = None, delimiter = ',', names = True)
classification = np.genfromtxt('rollup-classification.csv',dtype = None, delimiter = ',', names = True)
streaming = np.genfromtxt('rollup-streaming.csv',dtype = None, delimiter = ',', names = True)

unique_Exp = np.unique(cassandra['Exp'])
cassandra_sum = {category: cassandra['Core_0_IPC'][cassandra['Exp'] == category].sum() for category in unique_Exp}
cloud_sum = {category: cloud9['Core_0_IPC'][cloud9['Exp'] == category].sum() for category in unique_Exp}
nutch_sum = {category: nutch['Core_0_IPC'][nutch['Exp'] == category].sum() for category in unique_Exp}
classification_sum = {category: classification['Core_0_IPC'][classification['Exp'] == category].sum() for category in unique_Exp}
streaming_sum = {category: streaming['Core_0_IPC'][streaming['Exp'] == category].sum() for category in unique_Exp}

#print(grouped_means['bingo_MTPS2400'])
#print(np.average(cassandra['Core_0_IPC']))
#print(np.average(cassandra['Core_0_LLC_total_miss']))
#print(np.average(cassandra['Core_0_LLC_load_miss']))
#print(np.average(cassandra['Core_0_LLC_RFO_miss']))
#print(np.average(cassandra['Core_0_LLC_writeback_miss']))
#print(np.average(cassandra['Filter']))
cassandra_x = []
cloud_x = []
nutch_x = []
classification_x = []
streaming_x = []

for category in unique_Exp:
	cassandra_x.append(cassandra_sum[category])
	cloud_x.append(cloud_sum[category])
	nutch_x.append(nutch_sum[category])
	classification_x.append(classification_sum[category])
	streaming_x.append(streaming_sum[category])
ind = np.arange(N)
width = 0.25
fig = plt.subplots(figsize = (10, 8))
p1 = plt.bar(ind, cassandra_x, width)
p2 = plt.bar(ind+2*width/3, cloud_x, width)
p3 = plt.bar(ind+4*width/3, nutch_x, width)
p4 = plt.bar(ind+2*width, classification_x, width)
p5 = plt.bar(ind+8*width/3, streaming_x, width)
plt.title('Cloud Suite (MTPS2400)')
plt.xticks(ind+0.3, unique_Exp)
plt.ylim(0, 3.0)
plt.xlim(-0.2, 6.7)
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('cassandra','cloud9','nutch','classification','streaming'))
plt.show()