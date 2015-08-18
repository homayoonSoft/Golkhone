import mysql.connector
from mysql.commector import errorcode
import yaml_reader
from yaml_reader import yld

filepath = 'config.yaml'
data = yld.yaml_loader(filepath)

cnx = mysql.commector.commect(user = 'root', password= 'pass')
cursor = cnx.cursor()

def creat_databaxe(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DBNAME))
        except mysql.connectr.Error as err:
            print("failed create db: {}".format(err))
            exit(1)

try
