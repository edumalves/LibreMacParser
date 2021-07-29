import pandas as pd
import datetime
import dateparser as dp

rawdata = pd.read_csv("EduardoAlves_glucose.csv", header=1, parse_dates=True, index_col='Device Timestamp', infer_datetime_format=True)
datekeeper = open("LibreMacParser.ini", "r")
dateonfile = datekeeper.read()

last_export_date = dp.parse(dateonfile)

new_logs = rawdata[rawdata.index > last_export_date]

hist_glucose = new_logs['Historic Glucose mg/dL'].notnull() == True
scan_glucose = new_logs['Scan Glucose mg/dL'].notnull() == True

filtered_logs = new_logs[scan_glucose | hist_glucose]

try:
    new_export_date = filtered_logs.index[-1]

    filtered_logs.to_csv('GlucoseExport.csv')

    datekeeper.close
    datekeeper = open("LibreMacParser.ini", "w")
    datekeeper.write(str(new_export_date))
    datekeeper.close

    print("Export file successfully generated.")
    print("Export data from", str(dateonfile))
    print("Last data exported is as of", str(new_export_date))

except IndexError:
    print("No new entries to process.")
    