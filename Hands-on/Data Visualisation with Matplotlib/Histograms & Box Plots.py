import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

def test_hist_of_a_sample_normal_distribution():
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    np.random.seed(100)
    x1 = np.random.normal(25,3,1000)
    plt.hist(x1,bins=30)
    plt.xlabel('X1')
    plt.ylabel('Bin Count')
    plt.title('Histogram of a Single Dataset')
    fig.savefig('histogram_normal.png')

def test_boxplot_of_four_normal_distribution():
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    np.random.seed(100)
    x1 = np.random.normal(25,3,1000)
    x2 = np.random.normal(35,5,1000)
    x3 = np.random.normal(55,10,1000)
    x4 = np.random.normal(45,3,1000)
    labels = ['X1', 'X2', 'X3', 'X4']
    plt.boxplot([x1,x2,x3,x4],notch=True,sym='+',patch_artist=True)
    plt.xlabel('Dataset')
    plt.ylabel('Value')
    plt.title('Box plot of Multiple Datasets')
    ax.set_xticklabels(labels)
    fig.savefig('box_distribution.png')
    
test_hist_of_a_sample_normal_distribution()
test_boxplot_of_four_normal_distribution()
