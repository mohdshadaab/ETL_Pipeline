# Step 1
The given file can be run after initializing airflow to the directory, running web server and airflow scheduler

`airflow db init`

`airflow users create \
 --username admin \
 --firstname YOUR_FIRSTNAME \
 --lastname YOUR_LASTNAME \
 --role Admin \
 --email name@example.org`

`airflow webserver --port 8080`

Run this command in a different terminal
`airflow scheduler`

The data_gen.py handles the creation and storage of jsondata in ./data folder in the format of data/year/month/day/ , the data_trans.py writes the json data to the database and the dag.py handles the scheduling/running at specified intervals.

# Step 2

Install neo4j desktop from https://neo4j.com/download/

Setup the DB and new user as given in neo4j documentation

To use APOC procedure for loading JSON file:\
	1. Select DB, go to plugins and install APOC\
	2. From neo4j desktop select the db, and go to menu(three dots)-> open folder-> DBMS\
	3. In the DBMS folder go to conf and create 'apoc.conf' file.\
	4. Write the following lines in 'apoc.conf' :\
		apoc.import.file.enabled=true\
		apoc.import.file.use_neo4j_config=false\
	5. Restart the DB.
