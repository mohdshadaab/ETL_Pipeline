import neo4j
import datetime
import configparser
from config import config_stuff
from neo4j import GraphDatabase
from os import listdir
from os.path import isfile, join
from set_config import set_time

graphdb=GraphDatabase.driver(uri="bolt://localhost:7687/",auth=("shad","2772"))# use auth credentials for your db
print(graphdb)
session=graphdb.session()

config_obj = configparser.ConfigParser()
config_obj.read("/home/shadaab/airflow/tribesai/config.ini")
timeparam=config_obj["time"]
pathparam=config_obj["paths"]
   
#Current year,month and day
date = datetime.datetime.now() 
year = timeparam["year"]
month = timeparam["month"]
day = timeparam["day"]

#Save the file day wise, Example:- ../2021/6/27/shadaab@tribes.ai.json
DATE_DIR = "/".join([str(pathparam["data_dir"]),year,month,day])

#Get the usage file names from data_dir
onlyfiles = [f for f in listdir(DATE_DIR) if isfile(join(DATE_DIR, f))]

#run query for all users
for i in onlyfiles:
    subq = f"""
    CALL apoc.load.json("file://{DATE_DIR}/{i}") yield value""" 
    q=subq+""" 
    unwind value.usages as u
    unwind value.device as d
    MERGE (usr:User {user_id:value.user_id})
    MERGE (ap:App {app_name:u.app_name, app_category:u.app_category})
    MERGE (dev:Device {os:d.os})
    MERGE (br:Brand {brand:d.brand})
    MERGE (usr)-[r1:USED {time_created:time(), time_event: value.usages_date, usage_minutes: u.minutes_used}]->(ap)-[r2:ON {time_created:time()}]->(dev)-[r3:OFF {time_created:time()}]->(br)
    """
    print(q)
    session.run(q)

   

print(onlyfiles)

