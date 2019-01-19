import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3 #used to render matplotlib output in webpages
import os


def get_data_from_mlscript():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    plt.plot(t,s)
    plt.savefig('static/images/new_plot.png')
    return 'static/images/new_plot.png'
    
    """
    fig, ax = plt.subplots(1, 1)
    ax.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    #os.remove('static/images/matplot_img.png')
    #fig.savefig('static/images/matplot_img.png')
    
    """
    """
    #save fig to a html file
    fig, ax = plt.subplots(1, 1)
    ax.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    with open('templates/plot_fig.html','w') as fl:
        mpld3.save_html(fig,fl)

    """
        