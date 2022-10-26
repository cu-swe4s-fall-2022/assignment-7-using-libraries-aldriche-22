import sys
import argparse
import os
import matplotlib.pyplot as plt
import pandas as pd

def get_command_line_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file_name",
                        type = str,
                        help = "file name of the csv to read")

    return parser.parse_args()

def make_iris_boxplot(iris_csv):
    '''
    Description: 
    Creates a boxplot to visualize sepal and petal width and length 
    Input:
    iris_csv: str
        file path to the iris csv data
    '''
    try:
        iris = pd.read_csv(iris_csv)
    except: 
        FileNotFoundError
        sys.exit(1)
        
    iris.columns = ['sepal_width', 
                    'sepal_length', 
                    'petal_width', 
                    'petal_length', 
                    'species']
    measurement_names = ['sepal_length', 
                         'sepal_width', 
                         'petal_width', 
                         'petal_length']
    plt.boxplot(iris[measurement_names], labels = measurement_names)
    plt.ylabel('cm')
    plt.show()
    plt.savefig('iris.png')

def make_iris_scatterplot(iris_csv):
    '''
    Description: 
        Creates a scatterplot to visualize petal width v length 
    Input: 
        iris_csv: str
    '''
    try:
        iris = pd.read_csv(iris_csv)
    except: 
        FileNotFoundError
        sys.exit(1)
    
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

def multi_panel(iris_csv):
    '''
    Combines a histogram and a scatter plot into a multi panel figure
    Input: 
        iris_csv: str
    '''
    try:
        iris = pd.read_csv(iris_csv)
    except: 
        FileNotFoundError
        sys.exit(1)
    
    fig, axes = plt.subplots(1,2)
    fig.set_size_inches(10,10)
    fig.delaxes(axes[0,1])
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    print(axes.shape)
    
    # left: historgram 
    axes[0,0].hist(iris['petal_length'])
    axes[0,0].set_ylabel('count')
    
    # right: scatter 
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]        
        axes[0,1].scatter(iris_subset['petal_length'], 
                          iris_subset['petal_width'], 
                          label=species_name, 
                          s=5, 
                          alpha=0.5)
    axes[0,1].legend()
    axes[0,1].set_ylabel('petal_length')
    axes[0,1].set_xlabel('petal_width')
    plt.show()
    plt.savefig('multi_panel_figure.png')
    
def main():
    args = get_command_line_args()
    
    make_iris_boxplot(args.file_name)
    make_iris_scatterplot(args.file_name)
    multi_panel(args.file_name)
    
    
if __name__ == '__main__':
    main()