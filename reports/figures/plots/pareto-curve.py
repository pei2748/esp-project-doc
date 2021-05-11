# generate 2 figures: Pareto-curve-A0.pdf and Pareto-curve-A1.pdf

import numpy as np
import matplotlib.pyplot as plt


area = [0.0637597333333333,0.115788446666667,0.220295786666667,0.0616230066666667,0.11420724000000000000,0.21982562000000000000,0.0717121346666667,0.12439184800000000000,0.230369001333333,0.06855116800000000000,0.121786401333333,0.228874594666667]

latency = [2077060,1096580,607620,2157060,1176580,687620,19754540,19753260,19752640,39421740,39420460,39419840]


plt.scatter(latency[0], area[0], color='red', linestyle='-', label="P4- -A0-DMA64", marker='<') 
plt.scatter(latency[1], area[1], color='blue', linestyle='-', label="P8- -A0-DMA64", marker='<')
plt.scatter(latency[2], area[2], color='green', linestyle='-', label="P16-A0-DMA64", marker='<')

plt.scatter(latency[3], area[3], color='red', linestyle='-', label="P4- -A0-DMA32", marker='*')
plt.scatter(latency[4], area[4], color='blue', linestyle='-', label="P8- -A0-DMA32", marker='*')
plt.scatter(latency[5], area[5], color='green', linestyle='-', label="P16-A0-DMA32", marker='*')

lgd = plt.legend(bbox_to_anchor=(1.45, 1.03),loc='upper right', prop={'size': 12}, frameon=True)
plt.grid(True, color="grey", ls='-.', axis='y', which='minor')
#plt.ylim([0.1, 10])
plt.title("Pareto Curve of 6 Designs with Architecture A0")
plt.xlabel("Latency (ns)")
plt.ylabel("Area")
plt.grid(True, color="grey", ls='-.', axis='y')
plt.savefig("../Pareto-curve-A0.pdf", bbox_extra_artists=(lgd,),bbox_inches='tight',dpi=300)

plt.clf()

plt.scatter(latency[6], area[6], color='red', linestyle='-', label="P4- -A1-DMA64", marker='x')
plt.scatter(latency[7], area[7], color='blue', linestyle='-', label="P8- -A1-DMA64", marker='x')
plt.scatter(latency[8], area[8], color='green', linestyle='-', label="P16-A1-DMA64", marker='x')

plt.scatter(latency[9], area[9], color='red', linestyle='-', label="P4- -A1-DMA32", marker='o')
plt.scatter(latency[10], area[10], color='blue', linestyle='-', label="P8- -A1-DMA32", marker='o')
plt.scatter(latency[11], area[11], color='green', linestyle='-', label="P16-A1-DMA32", marker='o')

lgd=plt.legend(bbox_to_anchor=(1.45, 1.03),loc='upper right', prop={'size': 12}, frameon=True)
plt.grid(True, color="grey", ls='-.', axis='y', which='minor')
#plt.ylim([0.1, 10])
plt.title("Pareto Curve of 6 Designs with Architecture A1")
plt.xlabel("Latency (ns)")
plt.ylabel("Area")
plt.grid(True, color="grey", ls='-.', axis='y')

plt.savefig("../Pareto-curve-A1.pdf", bbox_extra_artists=(lgd,),bbox_inches='tight',dpi=300)
