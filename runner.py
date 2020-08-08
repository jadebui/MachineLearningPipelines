from data import get_gbq_dataframe
import data
from preprocessingData import preprocessing_data
from cleanData import clean_data
from trainer import train
sql=data.sql
if __name__ == '__main__':
  data = get_gbq_dataframe(sql)
  data = preprocessing_data(data)
  data = clean_data(data)
  data = train(data)



