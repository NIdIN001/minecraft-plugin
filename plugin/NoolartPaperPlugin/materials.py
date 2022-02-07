import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import inspect, os.path



    
def graphic(name):

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path     = os.path.dirname(os.path.abspath(filename))

    text_file=open(path+ "\\res\\" + name+'.csv')
    lines = text_file.read().split(';')
    data=np.array(lines[:-1],dtype=int)


    fig = plt.figure(frameon=False) 
    fig.set_size_inches(5, 5)

    depth=np.flip(np.arange(len(data)))

    plt.rcParams['font.size'] = 10

    ax=fig.add_subplot()


    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.set_xlabel('value')
    ax.set_ylabel('h, m')
    ax.minorticks_on()

    ax.grid(which='major',
            color = 'k',
           alpha=0.5)

    ax.grid(which='minor',
            color = 'gray',
            linestyle = ':')

    ax.plot(data,depth,label=name,linewidth=3)
    plt.legend()
    plt.gca().invert_yaxis()
    plt.savefig(path+ "\\imgs\\" + name+'.jpg', dpi=76.8)

    print(name + " graphic is done")
            


graphic("Density")
graphic("Magnetic")
graphic("Res")
graphic("Vs")
graphic("Vp")
graphic("Rad")
