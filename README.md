# TerminalRoastDB
Basic minimal scripting to run a roast recipe from MySQL DB on Fresh Roast SR700 coffee roaster

# Setting Up A Development Environment

Requirements are Python3, MySQL Database server.

Ubuntu Linux

    sudo apt-get install git python3 python3-pip python3-mysql.connector mysql-server 
    
    
# Setup MySQLDB

- Create a database terminalroastDB
- Create user terminalroaster
- with password terminalroasterpasswd

Make sure user terminalroaster has access to database terminalroastDB and run SQL in TerminalRoastDB/sql/TerminalRoastDB_create_DB_tables.sql for this database.

