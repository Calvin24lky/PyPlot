import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.interpolate import make_interp_spline
import random

def to_percent(temp, position):
    return '%1.0f'%(temp) + '%'

def printPredTaskUsage():
    df = pd.read_csv('./resource_usage/simple_test/pred_usage.csv', usecols=['time', 'system/cpu', 'system/memory']).values
    # df = pd.read_csv('./resource_usage/on_board_test/system.csv', usecols=['time', 'system/cpu', 'system/memory']).values

    x = [0, ]
    cpu_usage = [0, ]
    mem_usage = [0, ]

    for i in range(0, df.shape[0]):
        if df[i][1] != 'undefined':
            x.append(int(df[i][0]))
            cpu_usage.append(float(df[i][1]))
            mem_usage.append(float(df[i][2]))
            print(df[i])

    plt.ylim(0, 60)
    plt.yticks([10, 20, 30, 40, 50, 60, 70])
    plt.xticks([0, 60, 120, 180, 240, 300])
    plt.plot(x, cpu_usage, '-', linewidth='2.5', label='CPU Consumption')
    plt.plot(x, mem_usage, '-.', linewidth='2.5', label='Memory Consumption')
    plt.tick_params(labelsize=20)
    plt.ylabel('Real-time Consumption', fontdict={'size': 23})
    plt.xlabel('Running Time (Second)', fontdict={'size': 25})
    leg = plt.legend(fontsize=18)
    leg.set_draggable(True)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.tight_layout()
    plt.show()

def printFLTaskUsage():
    df = pd.read_csv('./resource_usage/simple_test/fl_usage.csv', usecols=['time', 'system/cpu', 'system/memory']).values
    # df = pd.read_csv('./resource_usage/on_board_test/system.csv', usecols=['time', 'system/cpu', 'system/memory']).values

    x = [0, ]
    cpu_usage = [0, ]
    mem_usage = [0, ]

    for i in range(0, df.shape[0]):
        if df[i][1] != 'undefined':
            x.append(int(df[i][0]))
            cpu_usage.append(float(df[i][1]))
            mem_usage.append(float(df[i][2]))
            print(df[i])

    plt.tick_params(labelsize=15)
    plt.ylim(0, 100)
    plt.yticks([0, 20, 40, 60, 80, 100])
    plt.xticks([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300])

    # use plt.step() to plot step line
    plt.step(x, cpu_usage, '-', linewidth='2', label='CPU Consumption')
    plt.plot(x, mem_usage, '--', linewidth='2', label='Memory Consumption')
    plt.ylabel('Real-time Consumption', fontdict={'size': 18})
    plt.xlabel('Running Time (Second)', fontdict={'size': 18})
    leg = plt.legend(fontsize=18)
    leg.set_draggable(True)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.tight_layout()
    plt.show()

def printFLTaskNetwork():
    df = pd.read_csv('resource_usage/simple_test/fl_net.csv', usecols=['time', 'recv', 'sent']).values
    x = [0,]
    recv_tmp = [0,]
    sent_tmp = [0,]
    recv = [0,]
    sent = [0,]

    for i in range(0, df.shape[0]):
        if df[i][1] != 'undefined':
            x.append(int(df[i][0]))
            recv_tmp.append(float(df[i][1]))
            sent_tmp.append(float(df[i][2]))
            recv.append(float(df[i][1]) - recv_tmp[-2])
            sent.append(float(df[i][2]) - sent_tmp[-2])
            print(df[i])

    x_smooth = np.linspace(min(x), max(x), 132)
    recv_smooth = make_interp_spline(x, recv)(x_smooth)
    sent_smooth = make_interp_spline(x, sent)(x_smooth)

    plt.tick_params(labelsize=14)
    plt.ylim(-1000000, 17000000)
    # plt.yticks([0, 20, 40, 60, 80, 100])
    plt.xticks([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300])
    plt.plot(x_smooth, recv_smooth, '-', linewidth='2', label='Received from FL parameter server')
    plt.plot(x_smooth, sent_smooth, '--', linewidth='2', label='Sent to FL parameter server')
    # plt.plot(x, recv)
    # plt.plot(x, sent)
    plt.ylabel('Data Transmitted (Byte)', fontdict={'size': 18})
    plt.xlabel('Running Time (Second)', fontdict={'size': 18})
    leg = plt.legend(fontsize=14)
    leg.set_draggable(True)
    # plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    printPredTaskUsage()
    # printFLTaskUsage()
    # printFLTaskNetwork()
