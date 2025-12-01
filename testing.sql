userName = "admin"
password = "admin"

query = "SELECT userID \"
	FROM users \
	WHERE userName = "'+ userName +'" \
	AND password = "'+ password +'"


userName = "admin"
password = "x' OR 1=1 --"

query = "SELECT userID " \
        "FROM users " \
        "WHERE userName = '" + userName + "' " \
        "AND password = '" + password + "'"


import subprocess

serverIpAddress = "127.0.0.1"

pingCmd = "ping -c 1 " + serverIpAddress
subprocess.Popen(pingCmd, shell=True)

ping -c 1 127.0.0.1