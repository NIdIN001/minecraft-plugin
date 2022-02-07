import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import inspect, os.path

    

try: 
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path     = os.path.dirname(os.path.abspath(filename))


    df=pd.read_csv(path+"\\observers.csv", index_col=3, names=['x','y','z'], delimiter=';')
    df.index=np.arange(len(df['x']))
    figure = plt.figure(frameon=True) 
    plt.scatter(df['x'].values,df['z'].values,s=1,c='g')
    #plt.savefig('C:\\Users\\alex\\Desktop\\test.png')

    figure.set_size_inches(1, 1)
    plt.savefig(path+"\\imgs\\test.png", dpi=128)


    print("Done!")
except Exception as e:
    print(e)
