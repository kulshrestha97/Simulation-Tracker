# SQLDataset for SIMULATION TRACKER.

__author__="Rajat Kulshreshtha"
import MySQLdb
from MySQLdb.cursors import DictCursor

class database:
    """
     Database class will have the behavior of connecting MySQL database
     with Python, using the MySQLdb API.\n It also exhibits the behaviour of inserting and creating tables. 
     """

    def __init__(self, server, user, password, db):
        self.server = server
        self.user = user
        self.password = password
        self.db = db
     
        self.conn = MySQLdb.connect(self.server,self.user,self.password,self.db)
        self.cur = self.conn.cursor()
        
    def masterinsert(self, masterinsert):
        # Here we have to parse the report in order to get the value of dutname, and all the other variables.
        """
        inserts the data in the Master Table.
        """        
        try:
        
            self.conn.ping(True)
            self.cur.execute(masterinsert)
            
            self.conn.commit()
            print('Master Data Inserted Correctly')
        except:
            self.conn.rollback()
       

        # TODO : Make modifications in select function later.
    def branchcreate(self,query):
        """
        Creates the branch table for storing test cases result.
        """
        try:
            self.conn.ping(True)
            self.cur.execute(query)

            self.conn.commit()
            print('Table Created Successfully')
        except:
            self.conn.rollback()
        
    def branchinsert(self,query, valueslist):
        """
        Inserts the data derived from the execution of commands.
        """
        try:
            self.conn.ping(True)
            self.cur.executemany(query, valueslist)
            self.conn.commit()
            print("Data Added Successfully")
        except:
            self.conn.rollback()
        self.conn.close()


    

class displaydata:
    """
    Display class has the behaviour to extract data from SQL Table, and display for the template.
    """

    def __init__(self, server, user, password, db):
       self.server = server
       self.user = user
       self.password = password
       self.db = db
       self.conn = MySQLdb.connect(self.server,self.user,self.password,self.db, cursorclass=DictCursor, use_unicode=True)
       self.cur = self.conn.cursor()
    
    def select(self):
        tableoftable_list = dict() 
        self.cur.execute("SELECT * FROM TOTALREPORT ORDER BY TIME DESC;")
        display = self.cur.fetchall()
        
        for i in range(len(display)):
            tablequery = "SELECT * FROM "+display[i]['design_name']+display[i]['time']+";"
            dictkey = display[i]['design_name']+display[i]['time']
            dictkey = str(dictkey)

            self.cur.execute(tablequery)
            tabledisplay = self.cur.fetchall()
            tabledisplay = list(tabledisplay)
            tableoftable_list.update({dictkey:tabledisplay})
        # print(tableoftable_list)
        
        self.cur.close()
        self.conn.close()
        return display, tableoftable_list