import json
import random

import matplotlib.pyplot as plt
import numpy as np


def plot_raw_result():
    result_path = 'stats/niid_50round_pro07.txt'

    with open(result_path, 'r') as outfile:
        data = json.load(outfile)

    train_accuracy = data['train_accuracy']
    train_loss = data['train_loss']
    valid_accuracy = data['valid_accuracy']
    valid_loss = data['valid_loss']

    print(len(train_accuracy))
    print(len(valid_accuracy))

    x = []
    y = []
    t_acc = []
    v_acc = []
    num = []

    for r in train_accuracy:
        x.append(r[0])
        t_acc.append(r[2])

    for v in valid_accuracy:
        y.append(v[0])
        v_acc.append(v[2])
        num.append(v[3])

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()  # 共享x轴
    ax1.plot(x, t_acc, color='r', label='train_acc')
    ax1.plot(y, v_acc, color='b', label='valid_acc')
    ax1.set(xlabel='round', ylabel='accuracy', title='ddqn4 niid choose')
    ax1.legend(loc=2)
    ax2.plot(y, num, color='g', label='client_num')
    ax2.set_ylim(0, 10)
    ax2.set(ylabel='update_num')
    ax2.legend(loc=7)
    plt.show()


def plot_raw_acc():

    c0_nniid_50round_drop3_result = './testbed_result/mnist/nniid/50round_drop3/client_0_global_model_local_data_acc.txt'
    c1_nniid_50round_drop3_result = './testbed_result/mnist/nniid/50round_drop3/client_1_global_model_local_data_acc.txt'
    c2_nniid_50round_drop3_result = './testbed_result/mnist/nniid/50round_drop3/client_2_global_model_local_data_acc.txt'

    c0_nniid_50round_pro08_result = './testbed_result/mnist/nniid/50round_pro08/client_0_global_model_local_data_acc.txt'
    c1_nniid_50round_pro08_result = './testbed_result/mnist/nniid/50round_pro08/client_1_global_model_local_data_acc.txt'
    c2_nniid_50round_pro08_result = './testbed_result/mnist/nniid/50round_pro08/client_2_global_model_local_data_acc.txt'

    c0_nniid_50round_pro09_result = './testbed_result/mnist/nniid/50round_pro09/client_0_global_model_local_data_acc.txt'
    c1_nniid_50round_pro09_result = './testbed_result/mnist/nniid/50round_pro09/client_1_global_model_local_data_acc.txt'
    c2_nniid_50round_pro09_result = './testbed_result/mnist/nniid/50round_pro09/client_2_global_model_local_data_acc.txt'

    final_c0_iid_50round_all_result = './testbed_result/mnist/iid/50round_all/client_0_global_model_local_data_acc.txt'
    final_c0_nniid_50round_all_result = './testbed_result/mnist/nniid/50round_all/client_0_global_model_local_data_acc.txt'
    final_c0_nniid_50round_pro09_result = './testbed_result/mnist/nniid/final_pro09/client_0_global_model_local_data_acc.txt'
    final_c0_nniid_50round_pro07_result = './testbed_result/mnist/nniid/final_pro07/client_0_global_model_local_data_acc.txt'


    nniid_50round_all_result = './testbed_result/mnist/nniid/50round_all/global_model_global_data_acc.txt'
    nniid_50round_drop3_result = './testbed_result/mnist/nniid/50round_drop3/global_model_global_data_acc.txt'
    nniid_50round_drop5_result = './testbed_result/mnist/nniid/50round_drop5/global_model_global_data_acc.txt'

    nniid_50round_pro08_result = './testbed_result/mnist/nniid/50round_pro08/global_model_global_data_acc.txt'
    nniid_50round_pro09_result = './testbed_result/mnist/nniid/50round_pro09/global_model_global_data_acc.txt'
    nniid_50round_pro07_result = './testbed_result/mnist/nniid/50round_pro07/global_model_global_data_acc.txt'
    final_nniid_50round_pro07_result = './testbed_result/mnist/nniid/final_pro07/global_model_global_data_acc.txt'
    final_nniid_50round_pro09_result = './testbed_result/mnist/nniid/final_pro09/global_model_global_data_acc.txt'

    iid_50round_all_result = './testbed_result/mnist/iid/50round_all/global_model_global_data_acc.txt'
    iid_50round_drop3_result = './testbed_result/mnist/iid/50round_drop3/global_model_global_data_acc.txt'

    niid_50round_all_result = './testbed_result/mnist/niid/50round_all/global_model_global_data_acc.txt'
    niid_50round_drop3_result = './testbed_result/mnist/niid/50round_drop3/global_model_global_data_acc.txt'

    niid_50round_pro07_result = './testbed_result/mnist/niid/50round_pro07/global_model_global_data_acc.txt'

    # c0_nniid_50round_pro08_acc = np.loadtxt(c0_nniid_50round_pro08_result)
    # c1_nniid_50round_pro08_acc = np.loadtxt(c1_nniid_50round_pro08_result)
    # c2_nniid_50round_pro08_acc = np.loadtxt(c2_nniid_50round_pro08_result)
    #
    # c0_nniid_50round_pro09_acc = np.loadtxt(c0_nniid_50round_pro09_result)
    # c1_nniid_50round_pro09_acc = np.loadtxt(c1_nniid_50round_pro09_result)
    # c2_nniid_50round_pro09_acc = np.loadtxt(c2_nniid_50round_pro09_result)
    #
    # c0_nniid_50round_drop3_acc = np.loadtxt(c0_nniid_50round_drop3_result)
    # c1_nniid_50round_drop3_acc = np.loadtxt(c1_nniid_50round_drop3_result)
    # c2_nniid_50round_drop3_acc = np.loadtxt(c2_nniid_50round_drop3_result)
    #
    # final_c0_nniid_50round_all_acc = np.loadtxt(final_c0_nniid_50round_all_result)
    # final_c0_nniid_50round_pro07_acc = np.loadtxt(final_c0_nniid_50round_pro07_result)
    # final_c0_nniid_50round_pro09_acc = np.loadtxt(final_c0_nniid_50round_pro09_result)
    # final_c0_iid_50round_pro09_acc = np.loadtxt(final_c0_iid_50round_all_result)

    nniid_50round_all_acc = np.loadtxt(nniid_50round_all_result)
    nniid_50round_drop3_acc = np.loadtxt(nniid_50round_drop3_result)
    nniid_50round_drop5_acc = np.loadtxt(nniid_50round_drop5_result)

    nniid_50round_pro08_acc = np.loadtxt(nniid_50round_pro08_result)
    nniid_50round_pro09_acc = np.loadtxt(nniid_50round_pro09_result)
    nniid_50round_pro07_acc = np.loadtxt(nniid_50round_pro07_result)
    final_nniid_50round_pro07_acc = np.loadtxt(final_nniid_50round_pro07_result)
    final_nniid_50round_pro09_acc = np.loadtxt(final_nniid_50round_pro09_result)

    iid_50round_all_acc = np.loadtxt(iid_50round_all_result)
    iid_50round_drop3_acc = np.loadtxt(iid_50round_drop3_result)

    niid_50round_all_acc = np.loadtxt(niid_50round_all_result)
    niid_50round_drop3_acc = np.loadtxt(niid_50round_drop3_result)
    niid_50round_pro07_acc = np.loadtxt(niid_50round_pro07_result)

    x = np.arange(len(nniid_50round_all_acc))


    # plt.plot(x, iid_50round_all_acc, label='tpu_iid_all_acc')
    # plt.plot(x, iid_50round_drop3_acc, label='iid_drop3_acc')
    # plt.plot(x, niid_50round_all_acc, label='niid_all_acc')
    # plt.plot(x, niid_50round_drop3_acc, label='niid_drop3_acc')
    # plt.plot(x, niid_50round_pro07_acc, label='niid_pro07_acc')
    # plt.plot(x, nniid_50round_drop3_acc, label='nniid_drop3_acc')
    # plt.plot(x, nniid_50round_pro08_acc, label='nniid_pro08_acc')
    # plt.plot(x, nniid_50round_pro09_acc, label='nniid_pro_09_acc')
    # plt.plot(x, nniid_50round_pro07_acc, label='nniid_pro07_acc')

    plt.plot(x, iid_50round_all_acc, '-', linewidth='1.5', label='All alive (i.i.d)')
    plt.plot(x, nniid_50round_all_acc, '-', linewidth='1.5', label='All alive (non-i.i.d)')
    plt.plot(x, final_nniid_50round_pro09_acc, '-', linewidth='1.5', label='Device fail probability=10% (non-i.i.d)')
    plt.plot(x, final_nniid_50round_pro07_acc, '-', linewidth='1.5', label='Device fail probability=30% (non-i.i.d)')

    # plt.plot(x, nniid_50round_drop5_acc, label='nniid_drop5_acc')
    # plt.plot(x, c0_nniid_50round_pro08_acc, label='c0_nniid_pro08_acc')
    # plt.plot(x, c1_nniid_50round_pro08_acc, label='c1_nniid_pro08_acc')
    # plt.plot(x, c2_nniid_50round_pro08_acc, label='c2_nniid_pro08_acc')
    # plt.plot(x, c0_nniid_50round_pro09_acc, label='c0_nniid_pro09_acc')
    # plt.plot(x, c1_nniid_50round_pro09_acc, label='c1_nniid_pro09_acc')
    # plt.plot(x, c2_nniid_50round_pro09_acc, label='c2_nniid_pro09_acc')
    # plt.plot(x, c0_nniid_50round_drop3_acc, label='c0_nniid_drop3_acc')
    # plt.plot(x, c1_nniid_50round_drop3_acc, label='c1_nniid_drop3_acc')
    # plt.plot(x, c2_nniid_50round_drop3_acc, label='c2_nniid_drop3_acc')
    # plt.plot(x, final_c0_iid_50round_pro09_acc, '-', linewidth='1.5', label='client_iid_alive_acc')
    # plt.plot(x, final_c0_nniid_50round_all_acc, '-', linewidth='1.5', label='client_nniid_alive_acc')
    # plt.plot(x, final_c0_nniid_50round_pro09_acc, '-', linewidth='1.5', label='client_nniid_probability_09_acc')
    # plt.plot(x, final_c0_nniid_50round_pro07_acc, '-', linewidth='1.5', label='client_nniid_probability_07_acc')

    plt.ylim(0.4, 1)
    # plt.ylim(0, 1)
    # plt.ylabel('Accuracy', fontdict={'size': 16})
    plt.ylabel('Accuracy')
    # plt.xlabel('Round', fontdict={'size': 16})
    plt.xlabel('Round of global model training')
    # leg = plt.legend(fontsize=15)
    plt.legend()
    # plt.tick_params(labelsize=12)

    plt.show()

def plot_global_model_traiining():
    nniid_50round_all_result = './testbed_result/mnist/nniid/50round_all/global_model_global_data_acc.txt'
    iid_50round_all_result = './testbed_result/mnist/iid/50round_all/global_model_global_data_acc.txt'
    final_nniid_50round_pro07_result = './testbed_result/mnist/nniid/final_pro07/global_model_global_data_acc.txt'
    final_nniid_50round_pro09_result = './testbed_result/mnist/nniid/final_pro09/global_model_global_data_acc.txt'

    nniid_50round_all_acc = np.loadtxt(nniid_50round_all_result)
    final_nniid_50round_pro07_acc = np.loadtxt(final_nniid_50round_pro07_result)
    final_nniid_50round_pro09_acc = np.loadtxt(final_nniid_50round_pro09_result)
    iid_50round_all_acc = np.loadtxt(iid_50round_all_result)
    x = np.arange(len(nniid_50round_all_acc))

    plt.plot(x, iid_50round_all_acc, ':', linewidth=3, label='Device always available (i.i.d)')
    plt.plot(x, nniid_50round_all_acc, '-', linewidth=3, label='Device always available (non-i.i.d)')
    plt.plot(x, final_nniid_50round_pro09_acc, '--', linewidth=3, label='Fail probability=10% (non-i.i.d)')
    plt.plot(x, final_nniid_50round_pro07_acc, '-.', linewidth=3, label='Fail probability=30% (non-i.i.d)')

    plt.ylim(0.01, 1.05)
    # plt.ylabel('Accuracy', fontdict={'size': 16})
    plt.ylabel('Test Accuracy of Model', fontdict={'size': 21})
    plt.xlabel('Rounds of global-model training', fontdict={'size': 22})
    plt.tick_params(labelsize=20)
    plt.tight_layout()
    leg = plt.legend(fontsize=16)  # , frameon=False)
    leg.set_draggable(True)
    plt.show()

def plot_local_model_training():
    final_c0_iid_50round_all_result = './testbed_result/mnist/iid/50round_all/client_0_global_model_local_data_acc.txt'
    final_c0_nniid_50round_all_result = './testbed_result/mnist/nniid/50round_all/client_0_global_model_local_data_acc.txt'
    final_c0_nniid_50round_pro09_result = './testbed_result/mnist/nniid/final_pro09/client_0_global_model_local_data_acc.txt'
    final_c0_nniid_50round_pro07_result = './testbed_result/mnist/nniid/final_pro07/client_0_global_model_local_data_acc.txt'

    final_c0_nniid_50round_all_acc = np.loadtxt(final_c0_nniid_50round_all_result)
    final_c0_nniid_50round_pro07_acc = np.loadtxt(final_c0_nniid_50round_pro07_result)
    final_c0_nniid_50round_pro09_acc = np.loadtxt(final_c0_nniid_50round_pro09_result)
    final_c0_iid_50round_pro09_acc = np.loadtxt(final_c0_iid_50round_all_result)

    x = np.arange(len(final_c0_nniid_50round_all_acc))

    plt.plot(x, final_c0_iid_50round_pro09_acc, ':', linewidth=3, label='Device always available (i.i.d)')
    plt.plot(x, final_c0_nniid_50round_all_acc, '-', linewidth=3, label='Device always available (non-i.i.d)')
    plt.plot(x, final_c0_nniid_50round_pro09_acc, '--', linewidth=3, label='Fail probability=10% (non-i.i.d)')
    plt.plot(x, final_c0_nniid_50round_pro07_acc, '-.', linewidth=3, label='Fail probability=30% (non-i.i.d)')

    plt.ylim(-0.09, 1.05)
    # plt.ylabel('Accuracy', fontdict={'size': 16})
    plt.ylabel('Test Accuracy of Model', fontdict={'size': 21})
    plt.xlabel('Rounds of local-model training', fontdict={'size': 22})
    plt.tick_params(labelsize=20)
    plt.tight_layout()
    leg = plt.legend(fontsize=16)  # , frameon=False)
    leg.set_draggable(True)
    plt.show()

if __name__ == '__main__':
    # plot_raw_result()
    # plot_raw_acc()
    # plot_global_model_traiining()
    plot_local_model_training()



