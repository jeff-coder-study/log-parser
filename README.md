# log-parser
Python tool to parse and analyze Linux syslog data

Purpose: A tool that takes in syslog data and figures out if there is anything suspicious. 

How it works: It looks at two things form the logs, facility and severity. 

The log contains both as a number known as PRI and to untangle them 