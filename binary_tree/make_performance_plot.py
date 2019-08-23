import matplotlib
from matplotlib import pyplot as plt
import json
import operator
from typing import List

from binary_tree import BASEDIR

matplotlib.use('tkagg')  # for use plt.show().


def main(exclude_datalist_names: List[str] = None) -> None:
    with open(BASEDIR / 'performance.json', 'r') as json_data_file:
        data = json.load(json_data_file)

    class_names = sorted(data.keys())
    tests_names = sorted(data[class_names[0]], key=operator.itemgetter(1))

    plot_numbers = len(tests_names)

    fig, axs = plt.subplots(1, plot_numbers, figsize=(9, 3), sharey=True)

    for plot_number, tests_name in enumerate(tests_names):
        curr_axs = axs[plot_number]
        for class_name in class_names:
            plt_data = sorted(data[class_name][tests_name].items())
            if exclude_datalist_names:
                plt_data = [i for i in plt_data if not any(i[0] == exc for exc in exclude_datalist_names)]

            x_data_items, y_data_items = zip(*plt_data)
            curr_axs.plot(x_data_items, y_data_items, label=class_name)

            curr_axs.set_title(tests_name)
            curr_axs.legend()
            plt.setp(curr_axs.xaxis.get_majorticklabels(), rotation=90)

    plt.show()


if __name__ == '__main__':
    # main(exclude_datalist_names=['datalist_1000000'])
    main()
