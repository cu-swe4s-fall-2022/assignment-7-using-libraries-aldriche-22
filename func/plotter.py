import argparse
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd

def get_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name",
                        type = str, 
                        help = "The file name of the dataset")

    return parser.parse_args()


def main(): 
    args = get_data()
    
    # read the data
    iris = pd.read_csv(args.file_name, sep=',')

    iris.columns = ['sepal_width', 
                    'sepal_length', 
                    'petal_width', 
                    'petal_length', 
                    'species']
    measurement_names = ['sepal_length', 
                         'sepal_width', 
                         'petal_width', 
                         'petal_length']

    # make the boxplot
    plt.boxplot(iris[measurement_names], labels = measurement_names)
    plt.ylabel('cm')
    plt.show()
    plt.savefig('iris.png')

    # make the scatterplot
    plt.subplots()
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]        
        plt.scatter(iris_subset['petal_length'], 
                    iris_subset['petal_width'], 
                    label=species_name)
    plt.legend()
    plt.ylabel('petal_length')
    plt.xlabel('petal_width')
    plt.title('Petal width v length by species')

    plt.show()
    plt.savefig('petal_width_v_length_scatter.png')


    # make the multi panel plot
    fig, axs = plt.subplots(1,2)
    fig.set_size_inches(10,10)
    #fig.delaxes(axs[1,2])
    #axs.spines.right.set_visible(False)
    #axs.spines.top.set_visible(False)


    # left: historgram 
    axs[0].boxplot(iris[measurement_names], labels = measurement_names)
    axs[0].set_ylabel('cm')

    # right: scatter 
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]        
        axs[1].scatter(iris_subset['petal_length'], 
                          iris_subset['petal_width'], 
                          label=species_name, 
                          s=5, 
                          alpha=0.5)

    axs[1].legend()
    axs[1].set_ylabel('petal_length')
    axs[1].set_xlabel('petal_width')
    plt.show()
    plt.savefig('multi_panel_figure.png')


    
if __name__ == '__main__':
    main()