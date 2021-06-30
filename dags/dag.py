try:
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from datetime import datetime
    import os
    import sys

    print("Dag is working")
except Exception as e:
    print("Error  {} ".format(e))





def data_collect():
    #import tribesai.data_gen
    
    sys.path.insert(0,'/home/shadaab/airflow/tribesai')
    from set_config import set_time
    
    set_time(datetime.now())
    os.system('python /home/shadaab/airflow/tribesai/data_gen.py')
    return "Data Collection Successful!!"

def database_load():
    #import tribesai.data_trans
    os.system('python /home/shadaab/airflow/tribesai/data_trans.py')
    return "Loaded to database!"

default_args={
            'owner': 'shadaab',
            'retries': 1,
            'retry_daily': timedelta(minutes=5),
            'start_date' : datetime(2021, 5, 29),   #the start date is set to a month before so that it executes for the past 30 days when run
        } 

with DAG(
        "main_dag",
        schedule_interval="@daily",     #cron expression 
        default_args=default_args,
        #start_date= days_ago(30),
        catchup=False) as dag:

    data_collect = PythonOperator(
        task_id="data_collect",
        python_callable=data_collect

    )

    database_load = PythonOperator(
        task_id="database_load",
        python_callable=database_load,
       
    )

data_collect >> database_load       #flow of tasks
