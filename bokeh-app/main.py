
import yaml
import os
from functools import partial

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt 
import matplotlib.cm as cm

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.io import show, output_notebook, curdoc
from bokeh.models.widgets import Slider, TextInput, CheckboxGroup, Panel, Tabs
from bokeh.themes import Theme

import Plasmodesma_Utilities_mpl as PU
import BucketUtilities_mpl as BU

# CHOOSE PARAMETERS: DATASETS & NETMODE
folder = "bokeh-app/SMARTE_v3/Results" #Folder containing the results of one calculation serie.
mode = "TOCSY" #4 modes available: HSQC, TOCSY, COSY, DOSY: determines which experiments are loaded
data_name = "SMARTE2_161123" #name of the csv of the first data to display, here SMARTE2
data_name2 = "SMARTE1_161123" #name of the csv of the second data to display, here SMARTE5
dataref = ["ARTEref_161123"] #name of the reference dataset in the results folder.
Sym = True #Symetrize or not.
Net = True #Cleaning or not.
NETMODE = "mieux" #Cleaning mode.
Y = np.array([0,0.11, 0.98, 0,0,0.4]) #Activities of the different fractions from SMARTE1 to SMARTE3
(tab1,tab2)=PU.mpl_create_app(curdoc, folder=folder, data_name=data_name, data_name2=data_name2, activities=Y, 
    manip_mode=mode, dataref=dataref, normalize=False,netmode=NETMODE, sym=Sym, net=Net, display=["std"], nfeatures=100, debug=1)

curdoc().add_root(Tabs(tabs=[ tab1,tab2]))
curdoc().title = "Plasmo_Analysis_SMARTE"
curdoc().theme = Theme(json=yaml.load("""
        attrs:
            Figure:
                background_fill_color: "#DDDDDD"
                outline_line_color: white
                toolbar_location: right
            Grid:
                grid_line_dash: [6, 4]
                grid_line_color: white
    """))
