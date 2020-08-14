import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Multiple_Plots_Figure1'],extensions=['png'])
def test_generate_figure1():

    t = np.arange(0.0,5.0,0.01)
    s1 = np.sin(2*np.pi*t)
    s2 = np.sin(4*np.pi*t)
    fig = plt.figure(figsize=(8,6))
    axes1 = fig.add_subplot(2,1,1,title='Sin(2*pi*x)')
    axes1.plot(t,s1)
    axes2 = fig.add_subplot(2,1,2,title='Sin(4*pi*x)')
    axes2.plot(t,s2)

@image_comparison(baseline_images=['Multiple_Plots_Figure2'],extensions=['png'])
def test_generate_figure2():

    np.random.seed(1000)
    x = np.random.rand(10)
    y = np.random.rand(10)
    z = np.sqrt(x**2+y**2)
    fig = plt.figure(figsize=(8,6))
    axes1 = fig.add_subplot(2,2,1,title='Scatter plot with Upper Traingle Markers')
    axes1.scatter(x,y,s=80,c=z,marker='^')
    axes1.set(xticks=[0.0,0.4,0.8,1.2],
              yticks=[-0.2,0.2,0.6,1.0])
    axes2 = fig.add_subplot(2,2,2,title='Scatter plot with Plus Markers')
    axes2.scatter(x,y,s=80,c=z,marker='+')
    axes2.set(xticks=[0.0,0.4,0.8,1.2],
              yticks=[-0.2,0.2,0.6,1.0])
    axes3 = fig.add_subplot(2,2,3,title='Scatter plot with Circle Markers')
    axes3.scatter(x,y,s=80,c=z,marker='o')
    axes3.set(xticks=[0.0,0.4,0.8,1.2],
              yticks=[-0.2,0.2,0.6,1.0])
    axes4 = fig.add_subplot(2,2,4,title='Scatter plot with Diamond Markers')
    axes4.scatter(x,y,s=80,c=z,marker='d')
    axes4.set(xticks=[0.0,0.4,0.8,1.2],
              yticks=[-0.2,0.2,0.6,1.0])
    fig.tight_layout()

@image_comparison(baseline_images=['Multiple_Plots_Figure3'],extensions=['png'])
def test_generate_figure3():

    fig = plt.figure(figsize=(8,6))
    x = np.arange(1,101)
    y1=x
    y2=x**2
    y3=x**3
    import matplotlib.gridspec as gd
    g = gd.GridSpec(2,2)
    axes1 = plt.subplot(g[0,0],title='y = x')
    axes1.plot(x,y1)
    axes2 = plt.subplot(g[1,0],title='y = x**2')
    axes2.plot(x,y2)
    axes3 = plt.subplot(g[0:,1],title='y = x**3')
    axes3.plot(x,y3)
    fig.tight_layout()