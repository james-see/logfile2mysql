# logfile2mysql
parse your log file and store it into mysql

## Log file format

The line format in this case is from Aria2web like this:
`2016-06-08 10:54:10.233636 [INFO] [rpc_helper.cc:103] Executing RPC method system.multicall`

You will need to reformat your parser as necessary and adjust the table fields as necessary for your logs.

## Install

1. Clone into a handy location.
2. Update your dbconfig.py file as necessary with the right userpass and username and path and log file name. 
3. Run the logs_db_and_table_creator.sql script in MySQL to create empty table.

## Run

Run python or python3 log2mysql.py


