# TerminalRoastDB v.0.0.1
Basic minimal scripting to run a roast recipe from MySQL DB on Fresh Roast SR700 coffee roaster

# Usage
First make sure you are properly connected to the Fresh Roast SR700 coffee roaster

    sudo python3 com_test.py

Second test your recipe where 'X' is the recipe ID number.

    sudo python3 TerminalRoastDB-test.py X

Now run your roast where 'X' is the recipe ID number.

    sudo python3 TerminalRoastDB.py X

# Setting Up A Development Environment

Requirements are Python3, MySQL Database server.

Ubuntu Linux

    sudo apt-get install git python3 python3-pip python3-mysql.connector mysql-server 
    git clone https://github.com/infinigrove/TerminalRoastDB.git
    cd TerminalRoastDB
    pip3 install -r requirements.txt
    
    
# Setup MySQLDB

- Create a database terminalroastDB
- Create user terminalroaster
- with password terminalroasterpasswd

Make sure user terminalroaster has access to database terminalroastDB and run SQL in TerminalRoastDB/sql/TerminalRoastDB_create_DB_tables.sql for this database.

For detailed information on database structure, please refer to wiki page: [MySQL terminalroastDB tables and fields](https://github.com/infinigrove/TerminalRoastDB/wiki)

#ToDo

- Web LAMP front end to maintain recipies
- Web LAMP front end to control roaster
- Log roast data to MySQL during roast
- Import JSON recipes
