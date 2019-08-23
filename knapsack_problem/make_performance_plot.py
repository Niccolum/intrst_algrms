import matplotlib
from matplotlib import pyplot as plt
import json

from knapsack_problem import BASEDIR
from knapsack_problem.performance import SMALL_STAT_NAME, BIG_STAT_NAME

matplotlib.use('tkagg')  # for use plt.show().


def main(*, stat_type) -> None:
    with open(BASEDIR / 'performance.json', 'r') as json_data_file:
        data = json.load(json_data_file)[stat_type]

    func_names = sorted(data.keys())

    fig, axs = plt.subplots()

    for func_name in func_names:
        # sorted by int in datalist name for correct sort by ascending items count in a knapsack
        plt_data = sorted(data[func_name].items(), key=lambda x: int(x[0].split('_')[1]))
        x_data_items, y_data_items = zip(*plt_data)
        axs.plot(x_data_items, y_data_items, label=func_name)

        axs.set_title(stat_type)
        axs.legend()
        plt.setp(axs.xaxis.get_majorticklabels(), rotation=90)

    plt.show()


if __name__ == '__main__':
    # main(stat_type=SMALL_STAT_NAME)
    main(stat_type=BIG_STAT_NAME)

