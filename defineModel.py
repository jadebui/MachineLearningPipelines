from tensorflow.keras import backend
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
def baseline_model():
    #===create model===#
    model = Sequential()
    model.add(Dense(1024, input_dim=12, activation='relu'))
    model.add(Dense(512, input_dim=12, activation='relu'))
    model.add(Dense(256, input_dim=12, activation='relu'))
    model.add(Dense(128, input_dim=12, activation='relu'))
    model.add(Dense(64, input_dim=12, activation='relu'))
    model.add(Dense(32, input_dim=12, activation='relu'))
    model.add(Dense(16, input_dim=12, activation='relu'))
    model.add(Dense(8, input_dim=12, activation='relu'))
    model.add(Dense(4, input_dim=12, activation='relu'))
    model.add(Dense(1))
    #===Compile model===#
    model.compile(loss='mean_absolute_error', optimizer='adam',metrics=['msle'])
    return model