import os
import json
import datetime
import random
import configparser

#List of user
users=["vinit@tribes.ai","guilermo@tribes.ai","christian@tribes.ai","elly@tribes.ai","shadaab@tribes.ai"]
#current date and time
date=datetime.datetime.now()
usage_date=date.strftime("%Y-%m-%d")
#App usage template
apps=[{
    "name":"slack",
    "mins_used": 0,
    "category":"communication"
},
{
    "name":"gmail",
    "mins_used": 0,
    "category":"communication"
},
{
    "name":"jira",
    "mins_used": 0,
    "category":"task_management"
},
{
    "name":"google drive",
    "mins_used": 0,
    "category":"file_management"
},
{
    "name":"chrome",
    "mins_used": 0,
    "category":"web_browser"
},
{
    "name":"spotify",
    "mins_used": 0,
    "category":"entertainment_music"
}]

random.seed(1)
#Function to create the json file for all users
def create_json():
    config_obj = configparser.ConfigParser()
    config_obj.read("/home/shadaab/airflow/tribesai/config.ini")
    timeparam=config_obj["time"]
    pathparam=config_obj["paths"]
   
    #Current year,month and day
    date = datetime.datetime.now() 
    year = timeparam["year"]
    month = timeparam["month"]
    day = timeparam["day"]
    for i in range(len(users)):

        app_usage = apps

        total_mins = 480   # given total time is 480 mins = 8 hours

        #Randomize the users so that there's no pattern in minutes_used values
        user_sequence = [i for i in range(6)]
        random.shuffle(user_sequence)

        #Assign a random value between 1 and total_mins
        for j in user_sequence:
            app_usage[j]["mins_used"] = random.randrange(1,total_mins)

            #Subtract the assigned random value of the app from 480
            #coz sum of minutes_used for all should not be greater than 480
            total_mins = total_mins - app_usage[j]["mins_used"]   
        #Assign the values in dictionary,
        #Kept few things constant(device and apps list)
        json_dict={
            "user_id": users[i],
            "usages_date": usage_date,
            "device":{
                "os": "ios",
                "brand": "apple"
            },
            "usages":[
                
                {
                    "app_name": app_usage[0]["name"],
                    "minutes_used": app_usage[0]["mins_used"],
                    "app_category": app_usage[0]["category"]
                },
                {
                    "app_name": app_usage[1]["name"],
                    "minutes_used": app_usage[1]["mins_used"],
                    "app_category": app_usage[1]["category"]
                },
                {
                    "app_name": app_usage[2]["name"],
                    "minutes_used": app_usage[2]["mins_used"],
                    "app_category": app_usage[2]["category"]
                },
                 {
                    "app_name": app_usage[3]["name"],
                    "minutes_used": app_usage[3]["mins_used"],
                    "app_category": app_usage[3]["category"]
                },
                {
                    "app_name": app_usage[4]["name"],
                    "minutes_used": app_usage[4]["mins_used"],
                    "app_category": app_usage[4]["category"]
                },
                {
                    "app_name": app_usage[5]["name"],
                    "minutes_used": app_usage[5]["mins_used"],
                    "app_category": app_usage[5]["category"]
                }]
        }
        #Save each user's data as json file
        save_json(json_dict, timeparam)

#Function to create json file     
def save_json(data : dict, time: dict):

    DATA_DIR = "/home/shadaab/airflow/tribesai/data"
   
    #Current year,month and day
    date = datetime.datetime.now() 
    year = time["year"]
    month = time["month"]
    day = time["day"]

    #Save the file day wise, Example:- ../2021/6/27/shadaab@tribes.ai.json
    DATE_DIR = "/".join([DATA_DIR,year,month,day])
    MKDIR_CMD = "mkdir -p "+ DATE_DIR
    JSON_PATH = DATE_DIR+"/"+data["user_id"]+".json"

    if(os.path.exists(DATE_DIR)!=True):
        os.system(MKDIR_CMD)
    
    with open(JSON_PATH, 'w') as f:
        json.dump(data,f)




if __name__=="__main__":
    create_json()
    