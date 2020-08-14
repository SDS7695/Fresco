import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Plot_with_Style1'],extensions=['png'])
def test_generate_plot_with_style1():
    with plt.style.context('ggplot'):
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        sepal_len = [5.01, 5.94, 6.59]
        sepal_wd = [3.42, 2.77, 2.97]
        petal_len = [1.46, 4.26, 5.55]
        petal_wd = [0.24, 1.33, 2.03]
        species = ['setosa', 'versicolor', 'viriginica']
        species_index1 = [0.7, 1.7, 2.7]
        species_index2 = [0.9, 1.9, 2.9]
        species_index3 = [1.1, 2.1, 3.1]
        species_index4 = [1.3, 2.3, 3.3]
        plt.bar(species_index1,sepal_len,width=0.2,label='Sepal Length')
        plt.bar(species_index2,sepal_wd,width=0.2,label='Sepal Width')
        plt.bar(species_index3,petal_len,width=0.2,label='Petal Length')
        plt.bar(species_index4,petal_wd,width=0.2,label='Petal Width')
        ax.set(xlabel='Species',ylabel='Iris Measurements (cm)',
               title = 'Mean Measurements of Iris Species',
               xlim=(0.5,3.7),ylim=(0,10),
               xticks=[1.1,2.1,3.1],
               xticklabels=['setosa','versicolor','viriginica'])
        ax.legend()
       
@image_comparison(baseline_images=['Plot_with_Style2'],extensions=['png'])
def test_generate_plot_with_style2():
    with plt.style.context('seaborn-colorblind'):
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        sepal_len = [5.01, 5.94, 6.59]
        sepal_wd = [3.42, 2.77, 2.97]
        petal_len = [1.46, 4.26, 5.55]
        petal_wd = [0.24, 1.33, 2.03]
        species = ['setosa', 'versicolor', 'viriginica']
        species_index1 = [0.7, 1.7, 2.7]
        species_index2 = [0.9, 1.9, 2.9]
        species_index3 = [1.1, 2.1, 3.1]
        species_index4 = [1.3, 2.3, 3.3]
        plt.bar(species_index1,sepal_len,width=0.2,label='Sepal Length')
        plt.bar(species_index2,sepal_wd,width=0.2,label='Sepal Width')
        plt.bar(species_index3,petal_len,width=0.2,label='Petal Length')
        plt.bar(species_index4,petal_wd,width=0.2,label='Petal Width')
        ax.set(xlabel='Species',ylabel='Iris Measurements (cm)',
               title = 'Mean Measurements of Iris Species',
               xlim=(0.5,3.7),ylim=(0,10),
               xticks=[1.1,2.1,3.1],
               xticklabels=['setosa','versicolor','viriginica'])
        ax.legend()
   


@image_comparison(baseline_images=['Plot_with_Style3'],extensions=['png'])
def test_generate_plot_with_style3():

    with plt.style.context('grayscale'):
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        sepal_len = [5.01, 5.94, 6.59]
        sepal_wd = [3.42, 2.77, 2.97]
        petal_len = [1.46, 4.26, 5.55]
        petal_wd = [0.24, 1.33, 2.03]
        species = ['setosa', 'versicolor', 'viriginica']
        species_index1 = [0.7, 1.7, 2.7]
        species_index2 = [0.9, 1.9, 2.9]
        species_index3 = [1.1, 2.1, 3.1]
        species_index4 = [1.3, 2.3, 3.3]
        plt.bar(species_index1,sepal_len,width=0.2,label='Sepal Length')
        plt.bar(species_index2,sepal_wd,width=0.2,label='Sepal Width')
        plt.bar(species_index3,petal_len,width=0.2,label='Petal Length')
        plt.bar(species_index4,petal_wd,width=0.2,label='Petal Width')
        ax.set(xlabel='Species',ylabel='Iris Measurements (cm)',
               title = 'Mean Measurements of Iris Species',
               xlim=(0.5,3.7),ylim=(0,10),
               xticks=[1.1,2.1,3.1],
               xticklabels=['setosa','versicolor','viriginica'])
        ax.legend()