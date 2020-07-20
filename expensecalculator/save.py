import mysql.connector
from mysql.connector import Error
def fetchdata():

    try:
    #conn=mysql.connector.connect(host="localhost",password="JaShhash256",database="expensecalc",user="root")
        conlink={
        'user':'root','password':'JaShhash256#','host':'127.0.0.1','database':'expensecalc',
        'autocommit':True,'auth_plugin':'','database':'expensecalc',
        }
        conn=mysql.connector.connect(**conlink)
        cursor=conn.cursor()
        if conn.is_connected():
            print("You are Connected to the database ")
            selectquery="SELECT * FROM expensecalc.store;"
            cursor.execute(selectquery)
            records=cursor.fetchall()
        #print("Number of data points available are",cursor.rawcount)
            for i in records:
                print("Income=",i[0])
                print("savings=",i[1])
                print("purchases ",i[2])
    except Error as e:
            print("Error occurred was : ",e )
