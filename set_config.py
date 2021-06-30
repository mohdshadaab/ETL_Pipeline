import datetime
import configparser

def set_time(time: datetime.datetime):
    edit = configparser.ConfigParser()
    edit.read("/home/shadaab/airflow/tribesai/config.ini")
    #Get the time section
    timeparam = edit["time"]
    #Update the time
    timeparam["year"]=str(time.year)
    timeparam["month"]=str(time.month)
    timeparam["day"]=str(time.day)
    

    #Write changes back to file
    with open("/home/shadaab/airflow/tribesai/config.ini", 'w') as configfile:
        edit.write(configfile)

#set_time(datetime.datetime.now())
