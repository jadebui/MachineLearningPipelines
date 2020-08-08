import pandas as pd #Libraries for processing data in python
import numpy as np #Libraries for processing numeric in python
def preprocessing_data (data):
    data['accept_lat'] = data['accept_lat'].astype('float64') 
    data['accept_lng'] = data['accept_lng'].astype('float64')
    data['pickup_lat'] = data['pickup_lat'].astype('float64')
    data['pickup_lng'] = data['pickup_lng'].astype('float64') 
    ###convert type date_time for board_time,accept_time (before type string)
    data['board_time'] =  pd.to_datetime(data['board_time'])
    data['accept_time'] =  pd.to_datetime(data['accept_time'])
    ### If experience=Nan =>experience=0 
    data['experience']=data['experience'].fillna(0)
    ### Calculator ETA
    #ETA = board_time - accept_time
    data['ETA1'] =  data['board_time'].subtract(data['accept_time'])
    #get hour of ETA
    data['ETA_hours'] =data['ETA1'].dt.components['hours']
    #get days of ETA
    data['ETA_days'] =data['ETA1'].dt.components['days']
    #get munutes of ETA
    data['ETA_minutes'] =data['ETA1'].dt.components['minutes']
    #sum minutes of ETA
    data['ETA']=data['ETA_hours']*60+data['ETA_minutes']
    # remove days of ETA >0 (because it's noise data)
    is_ETA = data['ETA_days']==0
    data= data[is_ETA]
    # clean data:drop unused columns
    data=data.drop(['ETA1','ETA_hours','ETA_days','ETA_minutes'],1)
    ###Feature Engineering
    #get day in month of accept day
    data.loc[:, 'accept_day'] = data['accept_time'].dt.day
    #get hour in day of accept day
    data.loc[:, 'accept_hour'] = data['accept_time'].dt.hour
    #get minute in day of accept day
    data.loc[:, 'accept_minute'] = data['accept_time'].dt.minute
    #get minute in day of accept day
    data['accept_minute_of_the_day'] = data.accept_time.dt.hour*60 + data.accept_time.dt.minute
    #get weekday in week of accept day
    data['accept_weekday'] = data.accept_time.dt.weekday
    #Calculator week_delta
    data['week_delta'] = (data.accept_weekday + ((data.accept_time.dt.hour + (data.accept_time.dt.minute / 60.0)) / 24.0))
    #clean data: drop unused columns
    data=data.drop(['accept_time','board_time'],1)
    return data