import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import time
def render_graph(data, name_img):
    plt.xkcd()

    graph_type = data['gtype']

    #upto six elements
    val_fields = ['val1', 'val2', 'val3', 'val4', 'val5', 'val6']
    tick_fields = ['tick1', 'tick2', 'tick3', 'tick4', 'tick5', 'tick6']

    values = []
    tick_text = []
    for tick_field, val_field in zip(tick_fields, val_fields):
        if data[tick_field]!='' and data[val_field]!='':
            values.append(data[val_field])
            tick_text.append(data[tick_field])

    values = [float(x) for x in values]
    max_val = max(values)
    values = [(x * 100)/max_val for x in values]
    number_of_bars = len(values)
    quanta = 60.0/(2*number_of_bars)
    left_values = [quanta + i*2*quanta for i in range(0, number_of_bars)]
    tick_values = [quanta + i*2*quanta for i in range(0, number_of_bars)]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    if graph_type == 'bar':
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xlim([0, 60])
        ax.set_ylim([0, 110])

        ax.bar(left_values, values, quanta)
        ax.set_xticks(tick_values)
        ax.set_xticklabels(tick_text)
        plt.yticks([])
        plt.ylabel(data['xlabel'])
        plt.ylabel(data['ylabel'])

    if graph_type == 'pie':
        ax.pie(values, labels= tick_text,
                autopct='%1.1f%%', shadow=True, startangle=90)


    plt.title(data['title'])

    plt.savefig('static/{}'.format(name_img))
