# generate 3 figures: 
# both-a0: testing time of hw and sw of 2 datasets with A0
# a1-vary-k: testing time with A1
# a1-vary-x: testing time with A1 

import numpy as np
import matplotlib.pyplot as plt




x = np.array([0, 1, 2])

fig, ax1 = plt.subplots()

y_D32 = np.array([0.514277784, 0.263244848, 0.138112728])
y_D64 = np.array([2.75939916, 1.422673848, 0.756544608])

y_sw_D32 = np.array([795.5, 795.5, 795.5])
y_sw_D64 = np.array([4066.8, 4066.8, 4066.8])

y_speedup_D32 = np.array([1546.82940766502, 3021.90149605511, 5759.78775830132])
y_speedup_D64 = np.array([1473.79910052593, 2858.56101573605, 5375.49267683103])


color = 'tab:red'
ax1.set_ylabel("Exec Time(sec, Log)", color=color)

ax1.scatter(x, y_D32, color='red', marker='s', linestyle='-', label='hw-DSmall')
ax1.scatter(x, y_sw_D32, color='red', marker='*', linestyle='-', label="sw-DSmall")
ax1.scatter(x, y_D64, color='green', marker='s', linestyle='-', label='hw-DLarge')
ax1.scatter(x, y_sw_D64, color='green', marker='*', linestyle='-', label="sw-DLarge")

ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels([r'P4', r'P8', r'P16'])

ax1.set_yscale('log')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([0.1, 50000])
ax1.set_title("Execution time (HW vs SW) & Speed Up", pad= 30)
ax1.legend(bbox_to_anchor=(0., 1, 1., .102), loc='lower left',
           ncol=2, borderaxespad=0., prop={'size':9}, frameon=False)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Speed Up', color=color)  # we already handled the x-label with ax1
ax2.plot(x, y_speedup_D32, color="cyan", marker='o', label='hw-DSmall')
ax2.plot(x, y_speedup_D64, color=color, marker='x', label='hw-DLarge')

ax2.tick_params(axis='y', labelcolor=color)
ax1.grid(True, color="pink", ls='-.', axis='y')

ax2.legend(bbox_to_anchor=(1.0, 1.0), loc='lower right',
           ncol=1,  borderaxespad=0., prop={'size': 9}, frameon=False)
fig.tight_layout()  # otherwise the right y-label is slightly clipped


fig.savefig("../both-a0.pdf", dpi=300)



x1 = 1024*np.array([4, 8, 16, 32, 64, 128, 256])
y_hw_x4_variedk = np.array([
0.00450472,
0.00651464,
0.01010828,
0.02154848,
0.0348834,
0.06800028,
0.13315324
])
y_sw_x4_variedk = np.array([
0.88557544,
1.75513508,
3.49712892,
7.04553892,
14.08259284,
28.13921712,
56.25201172,
])

y_speedup_variedk = np.array([
196.588342893676,
269.41397836258,
345.9667638807,
326.962222857482,
403.704708829988,
413.810312545772,
422.46070557502
])

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_ylabel("Exec Time(sec, Log)", color=color)
ax1.set_xlabel("numK (with numX = 4)", color='black')
ax1.scatter(x1, y_hw_x4_variedk, color='orange', marker='<', linestyle='-', label='hw')
ax1.scatter(x1, y_sw_x4_variedk, color='purple', marker='s', linestyle='-', label="sw")

ax1.set_xticks(x1)
ax1.set_xticklabels([r'4K', r'8K', r'16K', r'32K', r'64K', r'128K', r'256K'])
#ax1.legend(loc='center left', prop={'size': 12}, frameon=True)
ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=3, borderaxespad=0., prop={'size': 10}, frameon=True)

ax1.set_yscale('log')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([0.001, 100])
ax1.set_title("Execution time (HW vs SW) & Speed Up [A1]-varied numK", pad= 30)



ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Speed Up', color=color)  # we already handled the x-label with ax1
ax2.plot(x1, y_speedup_variedk, color=color, marker='o', label='speed-up')


ax2.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower right',
           ncol=2,  borderaxespad=0., prop={'size': 10}, frameon=True)
ax2.tick_params(axis='y', labelcolor=color)


fig.tight_layout()  # otherwise the right y-label is slightly clipped
ax1.grid(True, color="pink", ls='-.', axis='y')


fig.savefig("../a1-vary-k.pdf", dpi=300)



x1 = np.array([4, 8, 16, 32, 64, 128, 256])
y_hw_k4K_variedx = np.array([
0.00450472,
0.00609904,
0.01004748,
0.01882384,
0.03505624,
0.06701456,
0.1344052
])
y_sw_k4K_variedx = np.array([
0.88557544,
1.7580992,
3.49511844,
5.96618252,
13.77638112,
26.84441392,
54.65120976
])

y_speedup_variedx = np.array([
196.588342893676,
288.258348854902,
347.860203752583,
316.948216729424,
392.979427343035,
400.575843816627,
406.615292860693
])

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_ylabel("Exec Time(sec, Log)", color=color)
ax1.set_xlabel("numX (with numK = 4K)", color='black')
ax1.scatter(x1, y_hw_k4K_variedx, color='orange', marker='<', linestyle='-', label='hw')
ax1.scatter(x1, y_sw_k4K_variedx, color='purple', marker='s', linestyle='-', label="sw")
#ax1.set_xticks([0, 1, 2,3,4,5,6])
#ax1.set_xticklabels([r'4', r'8', r'16', r'32', r'64', r'128', r'256'])

ax1.set_yscale('log')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([0.001, 100])
ax1.set_title("Execution time (HW vs SW) & Speed Up [A1]-varied numX", pad=30)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Speed Up', color=color)  # we already handled the x-label with ax1
ax2.plot(x1, y_speedup_variedx, color=color, marker='o', label="speed-up")
ax2.tick_params(axis='y', labelcolor=color)
ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=3, borderaxespad=0., prop={'size': 10}, frameon=True)
ax2.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower right',
           ncol=2,  borderaxespad=0., prop={'size': 10}, frameon=True)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
ax1.grid(True, color="pink", ls='-.', axis='y')

fig.savefig("../a1-vary-x.pdf", dpi=300)
