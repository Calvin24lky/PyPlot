import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def to_percent(temp, position):
    return '%1.0f'%(temp) + '%'

def plot_consumption():
    # df = pd.read_csv('./resource_usage/simple_test/fl_usage.csv', usecols=['time', 'system/cpu', 'system/memory']).values
    df = pd.read_csv('./resource_usage/on_board_test/system.csv', usecols=['time', 'system/cpu', 'system/memory']).values

    x = [0, ]
    cpu_usage = [0, ]
    mem_usage = [0, ]

    for i in range(0, df.shape[0]):
        if df[i][1] != 'undefined':
            x.append(int(df[i][0]))
            cpu_usage.append(float(df[i][1]))
            mem_usage.append(float(df[i][2]))
            print(df[i])

    plt.ylim(0, 100)
    # plt.yticks([0, 20, 40, 60, 80, 100])
    plt.xticks([0, 500, 1000, 1500, 2000])

    # use plt.step() to plot step line
    # plt.step(x, cpu_usage, '-', linewidth='2', label='CPU Consumption')
    plt.plot(x, cpu_usage, '-', linewidth='2', label='CPU Consumption')
    plt.plot(x, mem_usage, '--', linewidth='2', label='Memory Consumption')
    plt.ylabel('Real-time Consumption', fontdict={'size': 21})
    plt.xlabel('Running Time (Second)', fontdict={'size': 22})
    plt.tick_params(labelsize=19)
    leg = plt.legend(fontsize=18)
    leg.set_draggable(True)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_consumption()
