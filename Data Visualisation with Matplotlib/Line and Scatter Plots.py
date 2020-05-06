import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Sine_Wave_Plot'],extensions=['png'])
def test_sine_wave_plot():
    fig = plt.figure(figsize=(12,3))
    ax= fig.add_subplot(111)
    t = np.linspace(0,2,200)
    v = np.sin(2.5*np.pi*t)
    plt.plot(t,v,label='sin(t)',color='red')
    xticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]
    yticks=[-1,0,1]
    plt.xlabel('Time (seconds)')
    plt.ylabel('Voltage (mV)')
    plt.title('Sine Wave')
    plt.xlim((0,2))
    plt.ylim((-1,1))
    plt.xticks(xticks)
    plt.yticks(yticks)
    plt.grid(ls='--')
    ax.legend()
   
   

@image_comparison(baseline_images=['Multi_Curve_Plot'],extensions=['png'])
def test_multi_curve_plot():
    fig = plt.figure(figsize=(12,3))
    ax= fig.add_subplot(111)
    x = np.linspace(0,5,20)
    y1=x
    y2=x**2
    y3=x**3
    plt.plot(x,y1,color='red',marker='o',label='y = x')
    plt.plot(x,y2,color='green',marker='s',label='y = x**2')
    plt.plot(x,y3,color='blue',marker='^',label='y = x**3')
    plt.xlabel('X')
    plt.ylabel('f(X)')
    plt.title('Linear, Quadratic, & Cubic Equations')
    ax.legend()


@image_comparison(baseline_images=['Scatter_Plot'],extensions=['png'])
def test_scatter_plot():
    fig = plt.figure(figsize=(12,3))
    ax= fig.add_subplot(111)
    s = [50, 60, 55, 50, 70, 65, 75, 65, 80, 90, 93, 95]
    months=range(1,13)
    plt.scatter(months,s,color='red',edgecolor='black')
    plt.xlabel('Months')
    plt.ylabel('No. of Cars Sold')
    plt.title("Cars Sold by Company 'X' in 2017")
    plt.xlim((0,13))
    plt.ylim((20,100))
    plt.xticks([1,3,5,7,9,11])
    ax.set_xticklabels(['Jan','Mar','May','Jul','Sep','Nov'])