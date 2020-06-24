import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = 'Times New Roman'
# plt.rcParams['figure.figsize'] = (5.6, 3.5)

label_list = ['50', '100', '150', '200', '250']  # 横坐标刻度显示值

fedavg_list = np.array([184, 384, 600, 810, 994])  # 纵坐标值1
fedcs_list = np.array([116, 236, 372, 500, 616])  # 纵坐标值2
ddqn_list = np.array([183, 383, 599, 808, 995])  # 纵坐标值3
pred_list = np.array([184, 384, 600, 810, 994])  # 纵坐标值4
offline_list = np.array([184, 384, 600, 810, 994])  # 纵坐标值4

fedavg_choose_list = np.array([500, 1000, 1500, 2000, 2500])
fedcs_choose_list = np.array([158, 308, 494, 660, 818])
ddqn_choose_list = np.array([198, 413, 649, 871, 1072])
pred_choose_list = np.array([200, 414, 650, 870, 1070])
offline_choose_list = np.array([184, 384, 600, 810, 994])

err_fa_list = [8, 11, 19, 26, 31]
err_fc_list = [2, 4, 6, 8, 10]
err_dq_list = [2, 6, 10, 14, 16]
err_pr_list = [2, 4, 6, 8, 10]

x = range(len(label_list))

error_params = dict(elinewidth=2, ecolor='black', capsize=3)  # 设置误差标记参数

fig, ax = plt.subplots()

rects1 = plt.bar(x, height=fedavg_list, width=0.15, color='#2ca02c', label="FedAvg [Google Team]",
                 hatch='.')  # , yerr=err_fa_list, error_kw=error_params)
rects11 = plt.bar(x, height=fedavg_choose_list - fedavg_list, width=0.15, color='#2ca02c',
                  alpha=0.5, bottom=fedavg_list)

rects2 = plt.bar([i + 0.15 for i in x], height=fedcs_list, color='#1f77b4', width=0.15, label="FedCS [Nishio, 2019]",
                 hatch='xx')  # , yerr=err_fc_list, error_kw=error_params)
rects21 = plt.bar([i + 0.15 for i in x], height=fedcs_choose_list - fedcs_list, width=0.15, color='#1f77b4',
                  alpha=0.5, bottom=fedcs_list)

rects3 = plt.bar([i + 0.3 for i in x], height=ddqn_list, color='#ff7f0e', width=0.15, label="DDQN-based (Proposed)",
                 hatch='')  # , yerr=err_dq_list, error_kw=error_params)
rects31 = plt.bar([i + 0.3 for i in x], height=pred_choose_list - ddqn_list, width=0.15, color='#ff7f0e',
                  alpha=0.5, bottom=ddqn_list)

rects4 = plt.bar([i + 0.45 for i in x], height=offline_list, color='#d62728', width=0.15,
                 label="Offline", hatch='\\')  # , yerr=err_pr_list, error_kw=error_params)
rects41 = plt.bar([i + 0.45 for i in x], height=offline_choose_list - offline_list, width=0.15, color='#d62728',
                  alpha=0.5, bottom=offline_list)
#
# rects4 = plt.bar([i + 0.45 for i in x], height=pred_list, color='#d62728', width=0.15,
#                  label="Proactive FedCS", hatch='\\', yerr=err_pr_list, error_kw=error_params)
# rects41 = plt.bar([i + 0.45 for i in x], height=pred_choose_list-pred_list, width=0.15, color='#d62728',
#                   alpha=0.5, bottom=pred_list)

# rects1 = plt.bar(x, height=fedavg_list/fedavg_choose_list, width=0.15, color='#2ca02c', label="FedAvg [Google Team]",
# hatch='.')
# rects2 = plt.bar([i + 0.15 for i in x], height=fedcs_list/fedcs_choose_list, color='#1f77b4', width=0.15, label="FedCS [Nishio, 2019]",
# hatch='xx')
# rects3 = plt.bar([i + 0.3 for i in x], height=ddqn_list/pred_choose_list, color='#ff7f0e', width=0.15, label="DDQN-based (Proposed)",
# hatch='')
# rects4 = plt.bar([i + 0.45 for i in x], height=offline_list/offline_choose_list, color='#d62728', width=0.15,
# label="Offline", hatch='\\')

# rects4 = plt.bar([i + 0.45 for i in x], height=pred_list/pred_choose_list, color='#d62728', width=0.15,
# label="Proactive FedCS", hatch='\\')

# plt.rcParams['figure.figsize'] = (5.6, 3.5)


plt.ylabel("# of Valid / Invalid Participants", fontsize=18)
ax = plt.gca()  # 获取当前图像的坐标轴信息
ax.yaxis.get_major_formatter().set_powerlimits((0, 1))

# plt.ylabel("Ratio of Valid Participants", fontsize=18)
# plt.ylim(0, 1.5)
# plt.yticks([0, 0.5, 1])


plt.xticks([index + 0.22 for index in x], label_list)

plt.tick_params(labelsize=14)

plt.xlabel("FL Rounds", fontsize=18)
leg = ax.legend(fontsize=14, loc=1)  # , frameon=False)
leg.set_draggable(True)
plt.tight_layout()
# plt.savefig('./imgs/Accumulated numbers.pdf', bbox_inches='tight')

# plt.annotate(color='r', s="# of\n invalid\n Patis",
#              xy=(0.1, 350), xycoords='data',
#              xytext=(0.25,250), textcoords='data',
#              size=14,
#              arrowprops=dict(arrowstyle="-[", color='r', connectionstyle='angle3'))


left, bottom, width, height = 0.13, 0.46, 0.3, 0.3
ax2 = fig.add_axes([left, bottom, width, height])

men_means = (20, 10, 10, 10, 10)
women_means = (25, 10, 10, 10, 10)
ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

rects1 = ax2.bar(ind - width / 2, men_means, width, color='white')
rects2 = ax2.bar(0.15, 15, width, color='#49b9c2', hatch='')
rects3 = ax2.bar(0.15, 25, width, color='#49b9c2', alpha=0.5, hatch='')

ax2.annotate(color='#000000', s="# of invalid\n Participants",
             xy=(0.45, 20), xycoords='data',
             xytext=(0.8, 15), textcoords='data',
             size=14,
             arrowprops=dict(arrowstyle="-[", color='#000000', connectionstyle='angle3'))

ax2.annotate(color='#000000', s="# of valid\n Participants",
             xy=(0.45, 7), xycoords='data',
             xytext=(0.8, 3), textcoords='data',
             size=14,
             arrowprops=dict(arrowstyle="-[", color='#000000', connectionstyle='angle3'))

# ax2.bar(0.01, bottom=0.02, height=0.02, width=0.0005, color='#d62728',
#                   alpha=1)
plt.ylim(0, 40)
ax2.axis('off')

plt.show()

