# Project2
# Analyze olympics data
## project description
Project2,we are worked as a group to analyze large olympics dataset in Spark by creating RDD's ,DataDrames and we have started quering using SparkSql
## Technologies Used
* Hadoop
* Spark
* Github
## Features
* Fault tolerance
* List of features ready and TODOs for future development using this project some query are solved using pyspark,dataframe,following questions are listed below.
1) Write a Query to Count Female participants in year 2004 from India?
2) Write a query to Count the no of Females Participants from each country in every year
3) Write a query to Count the no of males Participants from each country in every year
## Getting Started
* To start this project user need to install sandbox-Hortonworks in virtual machine.After installing the VM start the VM then put the following  commmand in git bash then connect to VM sing "ssh maria_dev@sandbox-hdp.hortonworks.com -p 2222" after this you need to put the password the default password for USER maria_dev is "maria_dev"
* Create a folder in local VM using command "mkdir folder_name"
* In this folder clone the git repository from where we pull the dataset using command "git clone 'git repository link' "
* All dataet are in a zip file we have to unzip it using command "unzip file_name" (N.B: if you are unzip in the current file ) .
* After unzip all the file create a folder in hdfs using command which is little bit difference before we tried while creating folder is "hdfs dfs -mkdir folder_name" (By default this folder created in the path user/maria_dev/ ) and copy all file to the hdfs folder by ""hdfs dfs -put file-name /user/maria_dev/folder_name".
* Before performing all the above action try to check whether your Ambari which is management platform for hadoop started all services or not. 
* After performing all the action try to create a .py file where write all the program using "vi" editor and save the file using esc + : + wq .
* After saving the file give command "spark-submit file_name" it will execute the file using SPARK 2 version.
## Usage
* Using this project any one can perform analysis with the olympics dataset.
## Contributors
* CH.Nishank
* Chekurtha Sravani
* Shetu Das
* Ankith Sharma
