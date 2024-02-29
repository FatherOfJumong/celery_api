# General DE_LOCAL_DEV_ENV

## Supported components:
- Airflow cluster
    - Airflow webserver
        - UI: http://localhost:8080/  (login and password: airflow)
    - Airflow schedular (edgenode)
- Hadoop cluster
    - HDFS
        - HDFS WEB UI: http://localhost:9870/
    - YARN
        - YARN UI: http://localhost:8088/
- Jupyter (edgenode)
    - http://localhost:8888/

## Profiles:
Available profiles for docker-compose:
    "jupyter"
    "airflow"
    "hive"

Example of profiles usage:
    run jupyter: docker-compose --profile jupyter up --build
    run jupyter and hive: docker-compose --profile jupyter --profile hive up --build
    run all: docker compose --profile "*" up --build

## Setup steps
1. Setup proxy from 'Command Prompt' 
> :warning: **If you are on windows OS**: Use specifically 'Command Prompt' as another shells may not apply set command!
- set HTTP_PROXY=http://thegate.bog.ge:8080
- set HTTPS_PROXY=http://thegate.bog.ge:8080

2. generate ssh keys using ssh-keygen
> :warning: **If you are using DE_LOCAL_DEV_ENV repo as development folder**: generate ssh keys in gitignored folder (ssh-keys)!
- create doler ~/DE_LOCAL_DEV_ENV/ssh-keys
- run ssh-keygen Generate ssh keys: 
    ssh-keygen -b 2048 -t rsa -f <path to folder>/de_local_dev_env/ssh-keys/id_rsa -q -N ""
- check ~/DE_LOCAL_DEV_ENV/ssh-keys folder you should see 2 files there: id_rsa, id_rsa.pub

3. Change directory to ~/de_local_dev_env

4. If you need to install requirements for airflow edgenode (airflow providers, additional libs and etc.) update requirements.txt file at path: 
~/de_local_dev_env/images/conf/ubuntu_x_airflow

5. From directory ~/de_local_dev_env run command to start containers:
docker compose --profile "*" up --build 

6. To use spark in Airflow:
    - open airflow (http://localhost:8080/)
    - go to Admin.Connections
    - create connection:
        Connection Id: spark_default
        Connection Type: Spark
        Host: yarn
        Extra: { "deploy-mode": "client" }

7. You can  adjust connection to HIVE server.
Copy jdbc driver from container:
    HOW to do that:
        OPTION A:
            Go to docker-desktop and go to "hive-server" container,
            Go to link "Files"
            Go to "/usr/local/hive/jdbc". Here you can find file "hive-jdbc-3.1.3-standalone.jar". Click right button on mouse and choose "SAVE" button.
        OPTION B:
            command below will copy jar file from hive-server container to root of disk D
            run command in command prompt: docker cp hive-server:/usr/local/hive/jdbc/hive-jdbc-3.1.3-standalone.jar D:\

    
    Then you can adjust connection to HIVE via jdbc ui client. In my case it's DBeaver:
        JDBC URL: jdbc:hive2://localhost:10000/default
        and
        set path to JDBC driver

## Mounted folders:
- hdfs
- postgres_airflow_metastore_data
- postgres_hive_metastore_data

## Pitfals
1. check that all files that are copied to image have LF end of line
2. if you rebuild docker-compose make sure to first delete temp folders containing mounted folders

## Working on project
1. You need to volume you project folder to container in either service based on your project nature:
- airflow-edgenode
- jupyter-edgenode

2. If you want to work on your airflow dags then you need to change './dags:/opt/airflow/dags' volume in airflow-edgenode accordingly