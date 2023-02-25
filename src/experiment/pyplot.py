import pyqtgraph

def plot_sample():
    xVals=[0,1,2,3,4,5,6]
    yVals=[-2,1,0,1,2,4,8]
    pw = pyqtgraph.plot(xVals, yVals, pen='r')  # plot x vs y in red
    # pw.plot(xVals, yVals2, pen='b')
    #
    # win = pg.GraphicsLayoutWidget()  # Automatically generates grids with multiple items
    # win.addPlot(data1, row=0, col=0)
    # win.addPlot(data2, row=0, col=1)
    # win.addPlot(data3, row=1, col=0, colspan=2)
    #
    # pg.show(imageData)  # imageData must be a numpy array with 2 to 4 dimensions



if __name__ == "__main__":
    plot_sample()
