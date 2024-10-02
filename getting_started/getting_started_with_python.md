# Getting Started with Python for Data Scientists

## Introduction
Python is a general purpose programming language with a simple syntax that has gain popularity among data scientists due to a rich ecosystem of statistics, machine learning, and visualization packages.  The purpose of this tutorial is to get an analyst up and running with Python.  There are a miriad of excellent resources for getting started with Python for datascience.  This is not meant to be a replacement for self-study but rather a concise launching-off point.  

## Installing Python
There are multiple ways to install Python; this tutorial uses Anaconda because it is a popular way to manage scientific libraries.  

1. Visit [Anaconda's website](https://www.anaconda.com/download) and download the installer for your operating system.
2. Follow the installation instructions on the website to set up Anaconda on your system.

## Setting Up Your Environment
Python is an open-source project that is being continuously improved.  Moreover, scientific libraries are developed by separate entities for different purposes and are also being continuously improved.  Since a change to one package can potentially break another package, we need a way to manage all the versions of the different packages to keep things working.  

A virtual environment is basically a named folder with all the packages and version numbers you want to run.  The Anaconda prompt is a tool for making the virtual environment that helps to hide some of the complexity.  Here is how to set up an environment with key scientific packages.    

From Windows, find and open up an Anaconda prompt.  The prompt will default to the "base" environment, but it is better to make a new environment to play with.  Type these commands in the Anaconda prompt:
```
conda create --name myenv
```
now go into the environment:
```
activate myenv
```
now that you are in the environment, install the packages you might want:  
```
conda install pip
pip install numpy scipy matplotlib pandas statsmodels jupyterlab
```
## Running Python for the First Time
To get started with Python, JupyterLab is a good place to start.  Jupyter notebooks are a powerful technology that combines code, visuals and text in a format that can be run and rendered in the browser.  To launch jupyter lab, open up an Anaconda prompt and run the following:  
```
activate myenv
jupyter lab
```
This should launch a Jupyter Lab session in the web browser.  Your Anaconda prompt window needs to stay running the background.  

Now that you are in Jupyter, you can start running Python.  This is a big topic. . .  but let's at least get you to load data into a Pandas DataFrame from Excel.  From inside of Jupyter, import pandas:  
```{python}
import pandas as pd
```
Then upload data from Excel:  
```{python}
path = r"\path\to\folder"
file = "my_excel_file.xlsx"
df = pd.read_excel(path+"\\"+file)
df
```
The contents of the dataframe should render in the notebook.  

## Topics of Further Study
Your Python journey has started and it is now time to get learning.  
* **Python** many data science projects will require only a basic knowledge of Python.  However, it can be useful to go deeper and understand the ins and outs of functions and classes (and many other topics) in Python. 
* **Data Wrangling** how to wrangle data in Pandas or other tools, how to hit databases and call SQL from Python.  How to manage data pipelines.  How to summarize data.
* **Visualization** how to make visualizations with packages such as pandas-plot, matplotlib, seaborn, pandas-bokeh
* **Statistics and Machine Learning** this gets fun scikit-learn, statsmodels, and many other statistical packages for helping to learn features of your data.  
* **Developer Environments** You will want to upgrade from Jupyter Lab to an integrated developer environment such as VSCode at some point in your journey. 
* **Version Control** Using Git/ GitHub to organize, store, share and collaborate.  

There are countless books, blogs, videos, courses, and meetups, on these (and more) topics. 


