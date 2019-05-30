import matplotlib.pyplot as plt
import json
from collections import OrderedDict, defaultdict


def main():
    with open('performance.json', 'r') as json_data_file:
        data = json.load(json_data_file)

    # or increase, it's the same
    names = sorted(data['decrease'].keys(), reverse=True)

    done_data = {
        'decrease': defaultdict(list),
        'increase': defaultdict(list),
        'average': {}
    }

    decrease_data = OrderedDict(
        sorted(data['decrease'].items(), key=lambda t: t[0], reverse=True))

    for d in decrease_data.values():
        for k, v in d.items():
            done_data['decrease'][k].append(v / 10000)

    increase_data = OrderedDict(
        sorted(data['increase'].items(), key=lambda t: t[0], reverse=True))

    for d in increase_data.values():
        for k, v in d.items():
            done_data['increase'][k].append(v / 10000)

    for k in done_data['decrease'].keys():
        done_data['average'][k] = [
            (x + y) / 2
            for x, y in zip(done_data['decrease'][k], done_data['increase'][k])
        ]

    fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

    # increase plot
    for label, values in done_data['increase'].items():
        axs[0].plot(names, values, label=label)
    axs[0].legend()

    # decrease plot
    for label, values in done_data['decrease'].items():
        axs[1].plot(names, values, label=label)
    axs[1].legend()

    # both average plot
    for label, values in done_data['average'].items():
        axs[2].plot(names, values, label=label)
    axs[2].legend()

    # rotation X ticks
    plt.setp(axs[0].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(axs[2].xaxis.get_majorticklabels(), rotation=90)

    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.2)
    plt.show()


if __name__ == '__main__':
    main()
