# TerminalRoastDB v0.1.5
Command line controller for Fresh Roast SR700 coffee roaster. Used to run a roast recipes stored in MySQL DB.

TerminalRoastDB contains a server daemon that connects to the roaster and waits for commands.  Once the server is running commands can be issued from command line. 

# Usage
To make sure you are able to connect to the Fresh Roast SR700 coffee roaster

    sudo python3 com_test.py

To start the TerminalRoastDB server daemon

    ./TerminalRoastDB.sh

You will need to enter your sudo password.

To run your roast or send commands to the roaster login with a second terminal session and go into the cmds directory.

    cd TerminalRoastDB/cmds
    
To run a roast recipe use the following command where X is the roast recipe ID number.

    python3 Roaster_Run_Recipe.py X
    
To override the roaster fan speed use the following command where X is the fan speed(1-9).

    python3 Roaster_Set_Fan.py X
    
To override the roaster temperature use the following command where X is the temperature in degrees fahrenheit.

    python3 Roaster_Set_Temp.py X
    
To override the roaster timer use the following command where X is the time in seconds.

    python3 Roaster_Set_Time.py X
    
Overrides to the fan speed, temperature, and timer only last for the duration of the current step.  When the next step of the recipe engages the step settings will be honored.

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

(If you change database, user and password be sure to change the appropriate lines of code near the beginning of recipe.py)

Make sure user terminalroaster has access to database terminalroastDB and run SQL in TerminalRoastDB/sql/TerminalRoastDB_create_DB_tables.sql for this database.

For detailed information on database structure, please refer to wiki page: [MySQL terminalroastDB tables and fields](https://github.com/infinigrove/TerminalRoastDB/wiki)

#ToDo

- Web LAMP front end to maintain recipies
- Web LAMP front end to control roaster
- Log roast data to MySQL during roast
- Import JSON recipes
