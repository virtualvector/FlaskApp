import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3 #used to render matplotlib output in webpages


def get_data_from_mlscript():
    fig, ax = plt.subplots(1, 1)
    ax.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    fig.savefig('static/images/matplot_img.png')

    """
    #save fig to a html file
    fig, ax = plt.subplots(1, 1)
    ax.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    with open('templates/plot_fig.html','w') as fl:
        mpld3.save_html(fig,fl)

    """
        