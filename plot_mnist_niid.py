import json
import matplotlib.pyplot as plt
import numpy as np


def subplot_fedcs(length, interval):
    f1_path = './MNIST/niid/fedcs0.txt'
    f2_path = './MNIST/niid/fedcs2.txt'
    f3_path = './MNIST/niid/fedcs4.txt'
    f4_path = './MNIST/niid/fedcs6.txt'
    f5_path = './MNIST/niid/fedcs8.txt'

    f1_acc = []
    f2_acc = []
    f3_acc = []
    f4_acc = []
    f5_acc = []

    # f1
    with open(f1_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f1_acc.append(f1_acc[j - 1])
            j += 1
        f1_acc.append(i[2])
        j += 1
    f1_acc = np.array(f1_acc)

    # f2append
    with open(f2_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f2_acc.append(f2_acc[j - 1])
            j += 1
        f2_acc.append(i[2])
        j += 1
    f2_acc = np.array(f2_acc)

    # f3
    with open(f3_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f3_acc.append(f3_acc[j - 1])
            j += 1
        f3_acc.append(i[2])
        j += 1
    f3_acc = np.array(f3_acc)

    # f4
    with open(f4_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f4_acc.append(f4_acc[j - 1])
            j += 1
        f4_acc.append(i[2])
        j += 1
    f4_acc = np.array(f4_acc)

    # f5
    with open(f5_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f5_acc.append(f5_acc[j - 1])
            j += 1
        f5_acc.append(i[2])
        j += 1
    f5_acc = np.array(f5_acc)

    acc_max = []
    acc_min = []
    acc_mean = []

    for i in range(length):
        if i % interval == 0:
            tmp = np.array([f1_acc[i], f2_acc[i], f3_acc[i], f4_acc[i], f5_acc[i]])
            acc_max.append(np.max(tmp))
            acc_min.append(np.min(tmp))
            acc_mean.append(np.mean(tmp))

    return acc_min, acc_max, acc_mean


def subplot_ddqn(length, interval):
    f1_path = './MNIST/niid/ddqn0.txt'
    f2_path = './MNIST/niid/ddqn2.txt'
    f3_path = './MNIST/niid/ddqn4.txt'
    f4_path = './MNIST/niid/ddqn6.txt'
    f5_path = './MNIST/niid/ddqn8.txt'

    f1_acc = []
    f2_acc = []
    f3_acc = []
    f4_acc = []
    f5_acc = []

    # f1
    with open(f1_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f1_acc.append(f1_acc[j - 1])
            j += 1
        f1_acc.append(i[2])
        j += 1
    f1_acc = np.array(f1_acc)

    # f2
    with open(f2_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f2_acc.append(f2_acc[j - 1])
            j += 1
        f2_acc.append(i[2])
        j += 1
    f2_acc = np.array(f2_acc)

    # f3
    with open(f3_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f3_acc.append(f3_acc[j - 1])
            j += 1
        f3_acc.append(i[2])
        j += 1
    f3_acc = np.array(f3_acc)

    # f4
    with open(f4_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f4_acc.append(f4_acc[j - 1])
            j += 1
        f4_acc.append(i[2])
        j += 1
    f4_acc = np.array(f4_acc)

    # f5
    with open(f5_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f5_acc.append(f5_acc[j - 1])
            j += 1
        f5_acc.append(i[2])
        j += 1
    f5_acc = np.array(f5_acc)

    acc_max = []
    acc_min = []
    acc_mean = []

    for i in range(length):
        if i % interval == 0:
            tmp = np.array([f1_acc[i], f2_acc[i], f3_acc[i], f4_acc[i], f5_acc[i]])
            acc_max.append(np.max(tmp))
            acc_min.append(np.min(tmp))
            acc_mean.append(np.mean(tmp))

    return acc_min, acc_max, acc_mean


def subplot_fedavg(length, interval):
    f1_path = './MNIST/niid/rand0.txt'
    f2_path = './MNIST/niid/rand2.txt'
    f3_path = './MNIST/niid/rand4.txt'
    f4_path = './MNIST/niid/rand6.txt'
    f5_path = './MNIST/niid/rand8.txt'

    f1_acc = []
    f2_acc = []
    f3_acc = []
    f4_acc = []
    f5_acc = []

    # f1
    with open(f1_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f1_acc.append(f1_acc[j - 1])
            j += 1
        f1_acc.append(i[2])
        j += 1
    f1_acc = np.array(f1_acc)

    # f2
    with open(f2_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f2_acc.append(f2_acc[j - 1])
            j += 1
        f2_acc.append(i[2])
        j += 1
    f2_acc = np.array(f2_acc)

    # f3
    with open(f3_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f3_acc.append(f3_acc[j - 1])
            j += 1
        f3_acc.append(i[2])
        j += 1
    f3_acc = np.array(f3_acc)

    # f4
    with open(f4_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f4_acc.append(f4_acc[j - 1])
            j += 1
        f4_acc.append(i[2])
        j += 1
    f4_acc = np.array(f4_acc)

    # f5
    with open(f5_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f5_acc.append(f5_acc[j - 1])
            j += 1
        f5_acc.append(i[2])
        j += 1
    f5_acc = np.array(f5_acc)

    acc_max = []
    acc_min = []
    acc_mean = []

    for i in range(length):
        if i % interval == 0:
            tmp = np.array([f1_acc[i], f2_acc[i], f3_acc[i], f4_acc[i], f5_acc[i]])
            acc_max.append(np.max(tmp))
            acc_min.append(np.min(tmp))
            acc_mean.append(np.mean(tmp))

    return acc_min, acc_max, acc_mean


def subplot_pred(length, interval):
    f1_path = './MNIST/niid/pred0.txt'
    f2_path = './MNIST/niid/pred2.txt'
    f3_path = './MNIST/niid/pred4.txt'
    f4_path = './MNIST/niid/pred6.txt'
    f5_path = './MNIST/niid/pred8.txt'

    # f1_path = './results/mnist/iid/pred/pred0.txt'
    # f2_path = './results/mnist/iid/pred/pred1.txt'
    # f3_path = './results/mnist/iid/pred/pred2.txt'
    # f4_path = './results/mnist/iid/pred/pred3.txt'
    # f5_path = './results/mnist/iid/pred/pred4.txt'

    f1_acc = []
    f2_acc = []
    f3_acc = []
    f4_acc = []
    f5_acc = []

    # f1
    with open(f1_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f1_acc.append(f1_acc[j - 1])
            j += 1
        f1_acc.append(i[2])
        j += 1
    f1_acc = np.array(f1_acc)

    # f2
    with open(f2_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f2_acc.append(f2_acc[j - 1])
            j += 1
        f2_acc.append(i[2])
        j += 1
    f2_acc = np.array(f2_acc)

    # f3
    with open(f3_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f3_acc.append(f3_acc[j - 1])
            j += 1
        f3_acc.append(i[2])
        j += 1
    f3_acc = np.array(f3_acc)

    # f4
    with open(f4_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f4_acc.append(f4_acc[j - 1])
            j += 1
        f4_acc.append(i[2])
        j += 1
    f4_acc = np.array(f4_acc)

    # f5
    with open(f5_path, 'r') as fb:
        data = json.load(fb)
    valid_acc = data['valid_accuracy']
    j = 0
    for i in valid_acc:
        while j < i[0]:
            f5_acc.append(f5_acc[j - 1])
            j += 1
        f5_acc.append(i[2])
        j += 1
    f5_acc = np.array(f5_acc)

    acc_max = []
    acc_min = []
    acc_mean = []

    for i in range(length):
        if i % interval == 0:
            tmp = np.array([f1_acc[i], f2_acc[i], f3_acc[i], f4_acc[i], f5_acc[i]])
            acc_max.append(np.max(tmp))
            acc_min.append(np.min(tmp))
            acc_mean.append(np.mean(tmp))

    return acc_min, acc_max, acc_mean


def plot_mnist_result(interval=3):
    length = 200
    x = np.arange(0, length, interval)
    fedcs_min, fedcs_max, fedcs_mean = subplot_fedcs(length, interval)
    ddqn_min, ddqn_max, ddqn_mean = subplot_ddqn(length, interval)
    avg_min, avg_max, avg_mean = subplot_fedavg(length, interval)

    fig, ax = plt.subplots()

    plt.plot(x, avg_mean, 'v-', linewidth=1.5, color='#d62728', label='Offline')
    plt.fill_between(x, avg_min, avg_max, color='#d62728', alpha=0.25)
    plt.plot(x, ddqn_mean, '*-', linewidth=1.5, color='#ff7f0e', label='DDQN-based (Proposed)')
    plt.fill_between(x, ddqn_min, ddqn_max, color='#ff7f0e', alpha=0.25)
    plt.plot(x, fedcs_mean, '+--', linewidth=1.5, color='#1f77b4', label='FedCS [Nishio, 2019]')
    plt.fill_between(x, fedcs_min, fedcs_max, color='#1f77b4', alpha=0.25)


    # niid
    plt.ylim(0.4, 1.0)

    # plt.rcParams['figure.figsize'] = (6, 4)

    plt.xticks([0, 50, 100, 150, 200])
    plt.tick_params(labelsize=18)
    plt.xlabel('FL Rounds', fontdict={'size': 21})
    plt.ylabel('Test Accuracy', fontdict={'size': 20})
    leg = ax.legend(fontsize=15)  # , frameon=False)
    leg.set_draggable(True)
    plt.title('MNIST (non-i.i.d.)', fontdict={'size': 20})
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_mnist_result(interval=7)   # 7



