#/usr/local/bin/python
'''
Author: James Campbell
Date Created: June 8th 2016
Date Updated:
What: Converts a log file (formated as date [space] log-type [space] log-code [space] log-description) and then imports into a mysql table called logs (see logs.sql to setup db & table)
Requirements: MySQL and Python. pip3 install mysqlclient or pip install MySQL-Python if 2.x
'''
import from dbconfig * # your user and password credentials in separate file
import sys
from datetime import datetime
try: import pymysql.cursors
except ImportError as e:
    print(e)
    exit('need to install pymysql via pip install pymysql first...')

# globals - set all your info here
pathtolog = pathconfig
logfilename = logfileconfig
dbuser = userconfig  # from dbconfig.py
dbpassword = passconfig  # from dbconfig.py
charsetdefault = 'utf8mb4'
databasedefault = 'logs'
hostdefault = '127.0.0.1'

# connect to db
try:
    connection = pymysql.connect(host=hostdefault,
                             user=dbuser,
                             password=dbpassword,
                             db=databasedefault,
                             charset=charsetdefault,
                             cursorclass=pymysql.cursors.DictCursor)
except:
    exit ('check database connnection and make sure you setup logs table and database via logs_db_and_table_creator.sql')
loglines = [line.strip() for line in open(pathtolog+logfilename)]
for entry in loglines:
    if entry.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))== False:  # handle for when log is wrong
        continue
    # parse out each line string based on formatting quirks from log file itself
    # in this case the format is:
    # 2016-06-08 10:54:10.233636 [INFO] [rpc_helper.cc:103] Executing RPC method system.multicall
    logdate_str = ' '.join([entry.split(' ')[0],entry.split(' ')[1]])  # get time string first
    logdate = datetime.strptime(logdate_str, '%Y-%m-%d %H:%M:%S.%f')  # convert to date object
    logtype = entry.split(' ')[2]  # nice and bracketed output for the logtype [INFO]
    logcode = entry.split(' ')[3]  # nice and bracketed output for the logcode [rpc_helper..]
    logdescription = entry.rsplit(']')[-1].strip()  # get everything after last bracket
    with connection.cursor() as cursor:
        sql = "insert into logs(logdate,logtype,logcode,logdescription) values(%s,%s,%s,%s);"
        cursor.execute(sql,(logdate,logtype,logcode,logdescription))
connection.commit()
connection.close()
exit('successfully finished')
