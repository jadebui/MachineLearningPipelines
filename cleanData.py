import pandas as pd #Libraries for processing data in python
import numpy as np #Libraries for processing numeric in python
def clean_data(data):
    data=data.loc[data.accept_lat <21.2]
    data=data.loc[data.accept_lat >20.85]
    data=data.loc[data.accept_lng >105.6]
    data=data.loc[data.accept_lng <106.0]
    data=data.loc[data.pickup_lat <21.2]
    data=data.loc[data.pickup_lat >20.85]
    data=data.loc[data.pickup_lng >105.6]
    data=data.loc[data.pickup_lng <106.0]
    data=data.loc[data.ETA <25]
    data=data.loc[data.distance <9]
    return data