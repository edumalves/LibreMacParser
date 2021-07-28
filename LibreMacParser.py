import pandas as pd
import matplotlib.pyplot as plt
import datetime

rawdata = pd.read_csv("EduardoAlves_glucose.csv", header=1, parse_dates=True, index_col='Device Timestamp', infer_datetime_format=True)

last_import_date = datetime.datetime(2021,6,24,9,14,0)

new_logs = rawdata[rawdata.index >= last_import_date]

new_logs.to_csv('GlucoseExport.csv')
