import mysql.connector
from mysql.connector import errorcode
import csv
from passlib.hash import sha256_crypt

# SET SQL_SAFE_UPDATES = 0;
# delete from ticket_Sales_event
# SET SQL_SAFE_UPDATES = 1;

def getDBConnection(host, dbs, usr, pwd):
    cnx = None
    try:
        cnx = mysql.connector.connect(user=usr, password= pwd,
                                      host=host ,
                                      database=dbs)
        print('connected to db')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("OOPS check id and pw")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return cnx


def processCSV(cnx):
    cur = cnx.cursor()
    with open('../data/third_party_sales.csv') as csvfile:
        reader = csv.reader(csvfile)
        sql_statement = """
                            INSERT INTO TICKET_SALES_EVENT
                            (ticket_id, trans_date, event_id, event_name, event_date, event_type, 
            event_city, customer_id, price, num_tickets)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                            """
        try:
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

def query_popular_tickets(cnx):
    sql_stmt = """
            SELECT event_id, event_name, sum(num_tickets)
            FROM TICKET_SYS.TICKET_SALES_EVENT
            GROUP BY event_id, event_name
            ORDER BY sum(num_tickets) desc limit 3;
            """
    cur = cnx.cursor()
    cur.execute(sql_stmt)
    records = cur.fetchall()
    cur.close()
    print('Here are the most popular tickets in the past month:')
    for row in records:
       print(' -    ', row[1])


if __name__ == "__main__":
    host = input("Enter mySQL host:")
    dbs = input("Enter mySQL db schema:")
    usr = input("Enter mySQL user:")
    pwd = input("Enter mySQL pw:")
    hash =sha256_crypt.hash(pwd)
    if sha256_crypt.verify(pwd, hash):
        conn = getDBConnection(host,dbs,usr,pwd)
        processCSV(conn)
    # # Get the most popular ticket in the past month
        query_popular_tickets(conn)
