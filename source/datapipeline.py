import mysql.connector
from mysql.connector import errorcode
import csv
from passlib.hash import sha256_crypt

global pwd

def datapipeline(host, dbs, usr, pwd):
    try:
        cnx = mysql.connector.connect(user=usr, password= pwd,
                                      host=host ,
                                      database=dbs)
        print('connected to db')
        cur = cnx.cursor()
        with open('../data/third_party_sales.csv') as csvfile:
            reader = csv.reader(csvfile)
            sql_statement = """
                            INSERT INTO TICKET_SALES_EVENT
                            (ticket_id, trans_date, event_id, event_name, event_date, event_type, 
            event_city,event_addr, customer_id, price)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                            """
            for row in reader:
                cur.execute(sql_statement,row)
    # commit in chunks if large file. this should do for current rows
        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("OOPS check id and pw")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cur.close()
        cnx.close()


if __name__ == "__main__":
    host = input("Enter mySQL host:")
    dbs = input("Enter mySQL db schema:")
    usr = input("Enter mySQL user:")
    pwd = input("Enter mySQL pw:")
    hash =sha256_crypt.hash(pwd)
    if(sha256_crypt.verify(pwd, hash)):
        datapipeline(host,dbs,usr,pwd)
