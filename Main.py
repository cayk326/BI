import pandas as pd
import os
import natsort
import numpy as np
import glob
import csv
from time import time
from bokeh.plotting import figure, output_file, show, reset_output
from bokeh.layouts import gridplot, column, row
from bokeh.models.widgets import Tabs, Panel



class Util():
    def __init__(self):
        print('create contractor')
    def AllFileList(self,file_path):
        all_files = natsort.natsorted((glob.glob(os.path.join(file_path, "*.csv"))))
        return all_files

    def ConstractDataFrame(self,all_files):
        data_length_list = np.arange(all_files.__len__())  # To store length of each data frame
        for i in range(all_files.__len__()):
            data_length_list[i] = pd.read_csv(all_files[i],header=header_pos).__len__()
        each_file = (pd.read_csv(f, header=header_pos) for f in all_files)  # read all csv as data frame
        dataframe = pd.concat(each_file, ignore_index=True)  # connect all data frame
        return dataframe,data_length_list

    def calctime(self,func):
        start = time()
        r = func()
        return {'value': r, 'time': time()-start}

class Plotting():

    def __init__(self):
        self.mode = ['']
        self.basedata = ['time','distance']

    def plot(self):
        reset_output()
        output_file("result.html")
        TOOLTIPS = [
            ("index", "$index"),
            ("(x,y)"
             , "($x, $y)"),
        ]

        p1 = figure(
            title="Time - SWA",
            width=600,
            height=200,
            x_axis_label='Time',
            y_axis_label='SWA',
            tooltips=TOOLTIPS
        )

        p2 = figure(
            title="Time - Throttle",
            width=600,
            height=200,
            x_range=p1.x_range,
            x_axis_label='Time',
            y_axis_label='Throttle',
            tooltips=TOOLTIPS
        )

        p3 = figure(
            title="Time - Brake",
            width=600,
            height=200,
            x_range=p2.x_range,
            x_axis_label='Time',
            y_axis_label='Brake',
            tooltips=TOOLTIPS
        )

        p1.line(df.iloc[:, 0], df.iloc[:, 1], legend="SWA")
        p2.line(df.iloc[:, 0], df.iloc[:, 2], legend="Throttle")
        p3.line(df.iloc[:, 0], df.iloc[:, 3], legend="Brake")
        # p = gridplot([[p1,p2,p3]])
        # show(p)
        first = Panel(child=gridplot([[p1, p2],[p3,None]]), title='first')
        second = Panel(child=gridplot([[p1, p2],[p3,None]]), title='second')
        tabs = Tabs(tabs=[first, second])
#       layout = gridplot([[p1,p2],[p3,None]])
        #layout = row(column(p1, p2), p3)
        show(tabs)

    def plotDf(self,df,lengthlist):
        reset_output()
        output_file("result.html")
        TOOLTIPS = [
            ("index", "$index"),
            ("(x,y)"
            , "($x, $y)"),
        ]

        p1 = figure(
            title="Time - SWA",
            width=600,
            height=200,
            x_axis_label='Time',
            y_axis_label='SWA',
            tooltips=TOOLTIPS
        )

        p2 = figure(
            title="Time - Throttle",
            width=600,
            height=200,
            x_range=p1.x_range,
            x_axis_label='Time',
            y_axis_label='Throttle',
            tooltips=TOOLTIPS
        )

        p3 = figure(
            title="Time - Brake",
            width=600,
            height=200,
            x_range=p2.x_range,
            x_axis_label='Time',
            y_axis_label='Brake',
            tooltips=TOOLTIPS
        )

        p4 = figure(
            title="Time - Speed",
            width=600,
            height=200,
            x_range=p3.x_range,
            x_axis_label='Time',
            y_axis_label='Speed',
            tooltips=TOOLTIPS
        )


        currntloc = 0
        for i in range(lengthlist.__len__()):
            if i == 0:
                p1.line(df.iloc[0:lengthlist[i], 0], df.iloc[0:lengthlist[i], 1], legend="data No"+str(i),color=color[i])
                p2.line(df.iloc[0:lengthlist[i], 0], df.iloc[0:lengthlist[i], 2], legend="data No"+str(i),color=color[i])
                p3.line(df.iloc[0:lengthlist[i], 0], df.iloc[0:lengthlist[i], 3], legend="data No"+str(i),color=color[i])
                p4.line(df.iloc[0:lengthlist[i], 0], df.iloc[0:lengthlist[i], 4], legend="data No" + str(i),color=color[i])
                currentloc = lengthlist[i]
            else:
                p1.line(df.iloc[currentloc:sum(list(lengthlist)[0:i+1]), 0], df.iloc[currentloc:sum(list(lengthlist)[0:i+1]), 1], legend="data No"+str(i),color=color[i])
                p2.line(df.iloc[currentloc:sum(list(lengthlist)[0:i + 1]), 0],df.iloc[currentloc:sum(list(lengthlist)[0:i + 1]), 2], legend="data No" + str(i),color=color[i])
                p3.line(df.iloc[currentloc:sum(list(lengthlist)[0:i + 1]), 0],df.iloc[currentloc:sum(list(lengthlist)[0:i + 1]), 3], legend="data No" + str(i),color=color[i])
                p4.line(df.iloc[currentloc:sum(list(lengthlist)[0:i + 1]), 0],df.iloc[currentloc:sum(list(lengthlist)[0:i + 1]), 4], legend="data No" + str(i),color=color[i])
                currentloc = currentloc+lengthlist[i]


        #first = Panel(child=gridplot([[p1, p2, p3,p4], [p3, None]]), title='first')
        #second = Panel(child=gridplot([[p1, p2, p3], [p3, None]]), title='second')
        #tabs = Tabs(tabs=[first, second])
        layout = gridplot([[p1,p2],[p3,p4]])
        #layout = row(column(p1, p2), p3)
        show(layout)


        return




class Dictionary():
    from collections import defaultdict
    def __init__(self):
        print('')

    def MakeDictionary(self):
        dict = Dictionary.defaultdict(list)
        # Make Dictionary
        dict['SWA'].append(['SWA','SteeringWheelAngle','steer_wheel_angle'])
        dict['Time'].append(['Time', 'time'])
        dict['Distance'].append(['Distance', 'distance'])
        return dict

if __name__ == '__main__':
    print('start')
    'Settings information'
    data_directory_path = r'C:\Users\yuta0\PycharmProjects\AI\BITool\data'  # Directory which is stored data
    header_pos = 2
    color = ['red','yellow', 'green', 'blue', 'black']

    util_ins = Util()
    all_files_path = util_ins.AllFileList(data_directory_path)
    dict_ins = Dictionary()
    plot_ins = Plotting()
    header_dict = dict_ins.MakeDictionary()



    for i in range(all_files_path.__len__()):
        df = pd.read_csv(all_files_path[i], header=header_pos)
        df_shape = df.shape
        cols = list(df.columns.values)
        #plot_ins.plot()


    df2,data_length_list = util_ins.ConstractDataFrame(all_files_path)
    plot_ins.plotDf(df2,data_length_list)
    print('')