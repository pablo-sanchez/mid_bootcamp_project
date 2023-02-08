import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def num_cat_splitter(df):
    df1 = df.copy()
    numerical_df = df1.select_dtypes(np.number)
    categorical_df = df1.select_dtypes(object)
    return numerical_df, categorical_df

def numericals_classifier(df):
    df1 = df.copy()
    continuous = []
    discrete = []
    for col in df1.columns:
        if df1[col].nunique() > 36:
             continuous.append(df1[col])
        else:
            discrete.append(df1[col])
    continuous_df = pd.DataFrame(continuous).T
    discrete_df = pd.DataFrame(discrete).T 
    return continuous_df, discrete_df

def hist_generator(df, save="Yes", name ='../Slides/distib_num_cont.png'):
    plt_size = len(df.columns)
    fig, ax = plt.subplots(plt_size, figsize=(12,20))
    n = 0
    for col in df.columns:
        sns.histplot(data = df, x = col, ax = ax[n])
        n +=1
    plt.tight_layout()
    if save =="Yes":
        plt.savefig(name, dpi=300, transparent=True)
    plt.show()
    
def box_generator(df, save="Yes", name ='../Slides/with_outliers_plot.png'):
    plt_size = len(df.columns)
    fig, ax = plt.subplots(plt_size, figsize=(16,16))
    n = 0
    for col in df.columns:
        sns.boxplot(data = df, x = col, ax = ax[n])
        n +=1
    plt.tight_layout()      
    if save =="Yes":
        plt.savefig(name, dpi=300, transparent=True)
    plt.show()
    
    
def countplot_generator(df, save="Yes", name ='../Slides/countplot_cat.png'):
    plt_size = len(df.columns)
    fig, ax = plt.subplots(plt_size, figsize=(8,50))
    n = 0
    for col in df.columns:
        if (len(df[col].value_counts().index)) >= 6:
            sns.countplot(data = df, y = col, order = df[col].value_counts().index, ax = ax[n])
        else:
            sns.countplot(data = df, x = col, order = df[col].value_counts().index, ax = ax[n])
        n +=1
    plt.tight_layout()
    if save =="Yes":
        plt.savefig(name, dpi=300, transparent=True)
    plt.show()
    
def percentage_generator(df):
    for col in df.columns:
        print('These are the percentages for the column:', col)
        print((df[col].value_counts(normalize=True)*100).round(2))
        print()
def outlier_remover(df):
    df1 = df.copy()
    thr=3
    to_remove = []
    for col in df1.columns:
        sd_dw = np.mean(df1[col]) - (thr*(df1[col].std()))
        sd_up = np.mean(df1[col]) + (thr*(df1[col].std()))
        out = df1[(df1[col] < sd_dw)|(df1[col] > sd_up)]
        to_remove += list(out.index)
    df1 = df1.drop(to_remove)
    df1 = df1.reset_index(drop=True)
    return df1
