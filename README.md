# log-parser
Python tool to parse and analyze Linux journald data

Purpose: A tool that takes in log data and figures out if there is anything suspicious.

How it works: It looks at the severity of each log entry. Syslog packs facility and severity into one number called PRI. journald is different. It stores severity on its own as PRIORITY, a number from 0 to 7. This tool reads that number and turns it into a name like Warning or Error.

It prints anything Warning or worse. It also prints Notice, because I found that failed logins show up as Notice.
