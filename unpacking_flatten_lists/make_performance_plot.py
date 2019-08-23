import matplotlib
from matplotlib import pyplot as plt
import json
from typing import List

from unpacking_flatten_lists import BASEDIR
from unpacking_flatten_lists.data import get_data_name_order
from unpacking_flatten_lists.performance import INCREMENT_MODE_NAME, DECREMENT_MODE_NAME


AVERAGE = 'average'
matplotlib.use('tkagg')  # for use plt.show().


def main(exclude_funcs: List[str] = None) -> None:
    with open(BASEDIR / 'performance.json', 'r') as json_data_file:
        data = json.load(json_data_file)

    if exclude_funcs is None:
        func_names = sorted(data.keys())
    else:
        func_names = sorted(set(data.keys()) - set(exclude_funcs))

    modes = sorted(data[func_names[0]].keys()) + [AVERAGE]
    data_names_with_order = get_data_name_order()

    plot_numbers = len(modes)
    fig, axs = plt.subplots(1, plot_numbers, figsize=(9, 3), sharey=True)

    for plot_number, mode in enumerate(modes):
        curr_axs = axs[plot_number]
        for func_name in func_names:
            try:
                plt_data = sorted(data[func_name][mode].items(), key=lambda x: data_names_with_order.index(x[0]))
            except KeyError as err:  # for 'average'
                if mode != AVERAGE:
                    raise KeyError from err
                inc_data, dec_data = data[func_name].get(INCREMENT_MODE_NAME), data[func_name].get(DECREMENT_MODE_NAME)
                raw_plt_data = {k: (inc_data.get(k) + dec_data.get(k)) / 2 for k in set(inc_data) & set(dec_data)}
                plt_data = sorted(raw_plt_data.items(), key=lambda x: data_names_with_order.index(x[0]))

            x_data_items, y_data_items = zip(*plt_data)
            curr_axs.plot(x_data_items, y_data_items, label=func_name)

            curr_axs.set_title(mode)
            curr_axs.legend()
            plt.setp(curr_axs.xaxis.get_majorticklabels(), rotation=90)

    plt.show()


if __name__ == '__main__':
    main()
    main(exclude_funcs=['tishka_flatten', 'outer_flatten_2', 'recursion_flatten'])
