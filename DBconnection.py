import sqlite3 as sql
import os
mypath=os.path.dirname(__file__)
class DBconnection:
    __dbconnect=mypath+"/project.db"   
    def Connect(self):
        try:            
            conn=sql.connect(self.__dbconnect)
            return conn
        except ConnectionError as e:
            print(e.strerror)
            return 0
    
    def ExecuteNoReturn(self, query):
        try:
            conn = self.Connect()
            cur = conn.cursor()# type: ignore 
            cur.execute(query)
            conn.commit() # type: ignore 
        except Exception as ex:
            print(ex)
    
    def Execute(self, query):
        try:
            conn = self.Connect()
            cur = conn.cursor()# type: ignore 
            cur.execute(query)
            conn.commit() # type: ignore 
            return True
        except Exception as ex:
            return False
        
    def Return(self, query):
        conn = self.Connect()
        cur = conn.cursor()# type: ignore 
        cur.execute(query)
        result = cur.fetchone()
        return result