import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

def render_graph(data, name_img):
    plt.xkcd()
    graph_type = data['gtype']

    if graph_type == 'bar' or graph_type == 'pie':
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

    if graph_type == 'stackbar':
        vert_categories = data['xcategories'].split(',')

        val_fields = ['val1', 'val2', 'val3', 'val4', 'val5', 'val6']
        tick_fields = ['tick1', 'tick2', 'tick3', 'tick4', 'tick5', 'tick6']

        stacks = []
        categories = []
        for tick_field, val_field in zip(tick_fields, val_fields):
            if data[tick_field]!='' and data[val_field]!='':
                stacks.append([int(x) for x in data[val_field].split(',')])
                print(stacks[-1])
                categories.append(data[tick_field])

        stacks = np.array(stacks).transpose()

        N = len(stacks[0])
        ind = np.arange(N)
        width = 0.6

        pstacks = []
        for stack in stacks:
            if len(pstacks) == 0:
                pstacks.append(plt.bar(ind, stack, width))
                prev_stack = stack
            else:
                pstacks.append(plt.bar(ind, stack, width, bottom=prev_stack))
                prev_stack = [x + y for x, y in zip(stack, prev_stack)]

        plt.ylabel(data['ylabel'])
        plt.xticks(ind, categories)
        plt.yticks(np.arange(0, max(prev_stack), 10))
        n_stacks = [x[0] for x in pstacks]
        plt.legend(n_stacks, vert_categories)

    plt.title(data['title'])

    plt.savefig('static/{}'.format(name_img), bbox_inches='tight')
    plt.close()
