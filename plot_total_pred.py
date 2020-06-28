import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def to_percent(temp, positon):
    return '%1.0f'%(100*temp) + '%'

x = np.arange(200)

tmp = np.loadtxt('./Pred_Acc_Loss/rnn/rnn_acc_loss1.txt')
rnn_poi_acc1 = tmp[5]
rnn_sl_acc1 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/rnn/rnn_acc_loss2.txt')
rnn_poi_acc2 = tmp[5]
rnn_sl_acc2 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/rnn/rnn_acc_loss3.txt')
rnn_poi_acc3 = tmp[5]
rnn_sl_acc3 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/rnn/rnn_acc_loss4.txt')
rnn_poi_acc4 = tmp[5]
rnn_sl_acc4 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/rnn/rnn_acc_loss5.txt')
rnn_poi_acc5 = tmp[5]
rnn_sl_acc5 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/rnn/rnn_acc_loss6.txt')
rnn_poi_acc6 = tmp[5]
rnn_sl_acc6 = tmp[7]

poi_max = []
poi_min = []
poi_mean = []
sl_max = []
sl_min = []
sl_mean = []

for i in range(200):
    poi_tmp = np.array([rnn_poi_acc1[i], rnn_poi_acc2[i], rnn_poi_acc3[i], rnn_poi_acc4[i], rnn_poi_acc5[i], rnn_poi_acc6[i]])
    sl_tmp = np.array([rnn_sl_acc1[i], rnn_sl_acc2[i], rnn_sl_acc3[i], rnn_sl_acc4[i], rnn_sl_acc5[i], rnn_sl_acc6[i]])
    poi_max.append(np.max(poi_tmp))
    poi_min.append(np.min(poi_tmp))
    poi_mean.append(np.mean(poi_tmp))

    sl_max.append(np.max(sl_tmp))
    sl_min.append(np.min(sl_tmp))
    sl_mean.append(np.mean(sl_tmp))

# plt.rcParams['figure.figsize'] = [5.6, 4]

plt.tick_params(labelsize=14)
plt.ylim(0.15, 0.99)
# plt.yticks([0.3, 0.5, 0.7, 0.9])
plt.plot(x, poi_mean, '-', linewidth='2', label='POI (RNN)')
plt.fill_between(x, poi_min, poi_max, alpha=0.25)
plt.plot(x, sl_mean, ':', linewidth='2', label='Sojourn duration (RNN)')
plt.fill_between(x, sl_min, sl_max, alpha=0.25)


tmp = np.loadtxt('./Pred_Acc_Loss/gru/gru_acc_loss1.txt')
gru_poi_acc1 = tmp[5]
gru_sl_acc1 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/gru/gru_acc_loss2.txt')
gru_poi_acc2 = tmp[5]
gru_sl_acc2 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/gru/gru_acc_loss3.txt')
gru_poi_acc3 = tmp[5]
gru_sl_acc3 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/gru/gru_acc_loss4.txt')
gru_poi_acc4 = tmp[5]
gru_sl_acc4 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/gru/gru_acc_loss5.txt')
gru_poi_acc5 = tmp[5]
gru_sl_acc5 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/gru/gru_acc_loss6.txt')
gru_poi_acc6 = tmp[5]
gru_sl_acc6 = tmp[7]

poi_max = []
poi_min = []
poi_mean = []
sl_max = []
sl_min = []
sl_mean = []

for i in range(200):
    poi_tmp = np.array([gru_poi_acc1[i], gru_poi_acc2[i], gru_poi_acc3[i], gru_poi_acc4[i], gru_poi_acc5[i], gru_poi_acc6[i]])
    sl_tmp = np.array([gru_sl_acc1[i], gru_sl_acc2[i], gru_sl_acc3[i], gru_sl_acc4[i], gru_sl_acc5[i], gru_sl_acc6[i]])
    poi_max.append(np.max(poi_tmp))
    poi_min.append(np.min(poi_tmp))
    poi_mean.append(np.mean(poi_tmp))

    sl_max.append(np.max(sl_tmp))
    sl_min.append(np.min(sl_tmp))
    sl_mean.append(np.mean(sl_tmp))

# plt.rcParams['figure.figsize'] = [5.6, 4]

plt.tick_params(labelsize=14)
plt.ylim(0.15, 0.99)
# plt.yticks([0.3, 0.5, 0.7, 0.9])
plt.plot(x, poi_mean, '-', linewidth='2', label='POI (GRU)')
plt.fill_between(x, poi_min, poi_max, alpha=0.25)
plt.plot(x, sl_mean, '--', color='#aa5500', linewidth='2', label='Sojourn duration (GRU)')
plt.fill_between(x, sl_min, sl_max, alpha=0.25)


# tmp = np.loadtxt('./Pred_Acc_Loss/lstm/lstm_acc_loss1.txt')
# lstm_poi_acc1 = tmp[5]
# lstm_sl_acc1 = tmp[7]
# tmp = np.loadtxt('./Pred_Acc_Loss/lstm/lstm_acc_loss2.txt')
# lstm_poi_acc2 = tmp[5]
# lstm_sl_acc2 = tmp[7]
# tmp = np.loadtxt('./Pred_Acc_Loss/lstm/lstm_acc_loss3.txt')
# lstm_poi_acc3 = tmp[5]
# lstm_sl_acc3 = tmp[7]
# tmp = np.loadtxt('./Pred_Acc_Loss/lstm/lstm_acc_loss4.txt')
# lstm_poi_acc4 = tmp[5]
# lstm_sl_acc4 = tmp[7]
# tmp = np.loadtxt('./Pred_Acc_Loss/lstm/lstm_acc_loss5.txt')
# lstm_poi_acc5 = tmp[5]
# lstm_sl_acc5 = tmp[7]
# tmp = np.loadtxt('./Pred_Acc_Loss/lstm/lstm_acc_loss6.txt')
# lstm_poi_acc6 = tmp[5]
# lstm_sl_acc6 = tmp[7]

tmp = np.loadtxt('./Pred_Acc_Loss/lstm/loss_and_acc1.txt')
lstm_poi_acc1 = tmp[5]
lstm_sl_acc1 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/lstm/loss_and_acc2.txt')
lstm_poi_acc2 = tmp[5]
lstm_sl_acc2 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/lstm/loss_and_acc3.txt')
lstm_poi_acc3 = tmp[5]
lstm_sl_acc3 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/lstm/loss_and_acc4.txt')
lstm_poi_acc4 = tmp[5]
lstm_sl_acc4 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/lstm/loss_and_acc5.txt')
lstm_poi_acc5 = tmp[5]
lstm_sl_acc5 = tmp[7]
tmp = np.loadtxt('./Pred_Acc_Loss/lstm/loss_and_acc6.txt')
lstm_poi_acc6 = tmp[5]
lstm_sl_acc6 = tmp[7]

poi_max = []
poi_min = []
poi_mean = []
sl_max = []
sl_min = []
sl_mean = []

for i in range(200):
    poi_tmp = np.array([lstm_poi_acc1[i], lstm_poi_acc2[i], lstm_poi_acc3[i], lstm_poi_acc4[i], lstm_poi_acc5[i], lstm_poi_acc6[i]])
    sl_tmp = np.array([lstm_sl_acc1[i], lstm_sl_acc2[i], lstm_sl_acc3[i], lstm_sl_acc4[i], lstm_sl_acc5[i], lstm_sl_acc6[i]])
    poi_max.append(np.max(poi_tmp))
    poi_min.append(np.min(poi_tmp))
    poi_mean.append(np.mean(poi_tmp))

    sl_max.append(np.max(sl_tmp))
    sl_min.append(np.min(sl_tmp))
    sl_mean.append(np.mean(sl_tmp))

# plt.rcParams['figure.figsize'] = [5.6, 4]

plt.ylim(-0.04, 1)
# plt.yticks([0.3, 0.5, 0.7, 0.9])
plt.plot(x, poi_mean, '-', color='#df0000', linewidth='2', label='POI (LSTM)')
plt.fill_between(x, poi_min, poi_max, alpha=0.25)
plt.plot(x, sl_mean, '-.', color='#aa55fe', linewidth='2', label='Sojourn duration (LSTM)')
plt.fill_between(x, sl_min, sl_max, alpha=0.25)

plt.tick_params(labelsize=16)
plt.ylabel('Prediction Accuracy', fontdict={'size': 20})
plt.xlabel('Epoch', fontdict={'size': 20})
leg = plt.legend(fontsize=17)
leg.set_draggable(True)

# plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

plt.tight_layout()
plt.show()

print(poi_max[-1], poi_min[-1])
print(sl_max[-1], sl_min[-1])



