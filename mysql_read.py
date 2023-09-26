# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:57:00 2023

@author: jules
"""

print('mysql_read application')

pip install mysql-connector-python

import mysql.connector

dbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wt"
    )

myCursor=dbconnection.cursor()
myCursor.execute("SELECT * FROM agents")

allAgents = myCursor.fetchall()

print(allAgents)

for a in allAgents:
    print(a[1])

