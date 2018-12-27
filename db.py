import configparser
import psycopg2
from psycopg2 import sql

class DBInterface():
    def __init__(self,configfile):
        config=configparser.ConfigParser()
        config.read(configfile)
        cfg=config['postgresql']
        try:
            self.conn = psycopg2.connect("dbname="+cfg['db']+" user="+cfg["user"]+" host="+cfg["host"]+" password="+cfg["password"])
    
        except:
            print("Error connecting to db")

    def storeData(self,temperature, humidity):
        try:
            cur=self.conn.cursor()
            query="INSERT INTO pomiary(moment,temperatura_zewn,wilgotnosc) VALUES(NOW(),{0},{1})"
            cur.execute(sql.SQL(query.format(temperature,humidity)))
            self.conn.commit()
        except Exception as e:
            print("I am unable to write to the database")
            print(e)

