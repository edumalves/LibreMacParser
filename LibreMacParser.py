import pandas as pd
import dateparser as dp

rawdata = pd.read_csv("EduardoAlves_glucose.csv", header=1, parse_dates=True, index_col='Device Timestamp', infer_datetime_format=True)
datekeeper = open("LibreMacParser.ini", "r")
dateonfile = datekeeper.read()

last_export_date = dp.parse(dateonfile)

new_logs = rawdata[rawdata.index >= last_export_date]

new_export_date = new_logs.index[-1]

new_logs.to_csv('GlucoseExport.csv')

datekeeper.close
datekeeper = open("LibreMacParser.ini", "w")
datekeeper.write(str(new_export_date))
datekeeper.close

print("Export file successfully generated.")
print("Export data from", str(dateonfile))
print("Last data exported is as of", str(new_export_date))