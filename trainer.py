import pandas as pd #Libraries for processing data in python
import numpy as np #Libraries for processing numeric in python
import pickle as pkl #save model and sclaer
import json #read file json
from tf_notification_callback import TelegramCallback
import datetime, time #processing data datetime type
from sklearn.model_selection import train_test_split #split training data/ testing data
from sklearn.preprocessing import MinMaxScaler #scaler data
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error#Metric for evaluation
#===Libraries for build model by Keras===#
from tensorflow.keras import backend
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from defineModel import baseline_model
from uploadModel import upload_to_bucket
"""  The following block is all you need in order 
  to use the Keras Telegram bot callback. Just 
  add telegram_callback to the list of        
  callbacks passed to model.fit       """
telegram_callback = TelegramCallback('1128967661:AAEacoWxFmLsoPYC7HTm8A9l8Mey5ZwzMuc',
                                     '-427725964',
                                     'ETA Model',
                                      ['loss', 'val_loss'],
                                      ['mean_squared_logarithmic_error','val_mean_squared_logarithmic_error'],
                                      True)
def train(data):
    X=np.asarray(data.drop(['ETA'],axis=1))
    y=np.asarray(data["ETA"])
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    with open("han_bike_scalers.pkl", "wb") as outfile:
        pkl.dump(scaler, outfile)
        upload_to_bucket('model/han_bike_scalers.pkl', 'han_bike_scalers.pkl', 'aha-ds-ml-pipeline')
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
    model = KerasRegressor(build_fn=baseline_model,epochs=2, batch_size=3, verbose=1)
    history=model.fit(X_train,y_train,validation_data=(X_test, y_test),callbacks=[telegram_callback])
    #==============================================================================
    # Predict & Evaluation
    #==============================================================================
    prediction = model.predict(X_test)
    score = mean_absolute_error(y_test, prediction)
    if score <5:
        model.model.save('han_bike_models.h5')
        upload_to_bucket('model/han_bike_models.h5', 'han_bike_models.h5', 'aha-ds-ml-pipeline')
    return model