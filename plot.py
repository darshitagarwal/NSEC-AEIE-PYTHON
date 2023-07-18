import numpy as np
import matplotlib.pyplot as plt
import random
class DataPlot:
    def PlotCoordinates():
        global x_axis,y_axis
        x_axis=np.random.randint(10,90,10)
        y_axis=np.random.randint(20,100,10)
        print("\t\t-----Coordinates-----")
        print("X-axis => ", x_axis)
        print("Y-axis => ", y_axis)
    def PlotGraph():
        plt.plot(x_axis,color="blue",marker="o",mfc="yellow",linestyle="dashed")
        plt.plot(y_axis,color="red",marker="o",mfc="black")
        plt.grid(color="green")
        plt.show()
DataPlot.PlotCoordinates()
DataPlot.PlotGraph()
        