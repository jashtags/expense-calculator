from save import fetchdata
import sampledbc
import mysql.connector
from mysql.connector import Error
#import turtle

print("__________________________________________________________________________")
print(" Welcome to my expence calulator ")
print(" Select your option from given felow ")
print(" 1. Enter Your Expenses \n 2. Credits \n 3. Debits \n 4. Exit")
flag=1
print("Your choice has been recorded, Please wait while we connect with our Database")
print("......")
print()
conlink={
'user':'root','password':'JaShhash256#','host':'127.0.0.1','database':'expensecalc',
'autocommit':True,'auth_plugin':'','database':'expensecalc',
}
conn=mysql.connector.connect(**conlink)
cursor=conn.cursor()
while flag:
    print(" Select your option from given Below ")
    print(" 1. Enter Your Expenses \n 2. Credits \n 3. Debits \n 4. Exit")
    choice=int(input())
    if choice==4:
        print("              Thank you :)                     ")
        flag=0
    elif choice==1:
        print(" Select where you have spent your money from the options below below ")
        print(" 1. Travelling and Expenses \n 2. EMI for car \n 3. EMI for bike \n 4. Stationary \n 5. Groceries \n 6. Clothes and Accessories \n 7. Other Expenses")
        enter=int(input())
        if enter=="":
            print("Please Enter your choice")
        if enter==1:
            selectionmade="travelling"
        elif enter==2:
            selectionmade="emi for car"
        elif enter==3:
            selectionmade="emi for bike"
        elif enter==4:
            selectionmade="stationary"
        elif enter==5:
            selectionmade="Groceries"
        elif enter==6:
            selectionmade="Clothes"
        else:
            selectionmade="others"
        try:
            if conn.is_connected():
                print("Succesfully Established your connection to the database")
                print("Please Enter the money you have spent in your selection of index", enter)
                print("__")
                money=int(input())
                print("__")
                #print(money)
                query="INSERT into store (savings) VALUES(%s)"
                lin=(money)
                cursor.execute(query,lin)
        except Error as e:
            print("We are sorry, your query could not be processed")
            print("Error was ",e)
    elif choice==2:
        print("You have selected to view your credits ")
        try:
            query="SELECT sum(income) FROM expensecalc.store"
            #print(query[0])
            cursor.execute(query)
            res=cursor.fetchall()
            print(res[0][0])
        except Error as e:
            print("We have encountered an error")
            print("error is ",e)
    elif choice==3:
        print("You have choosen to see your debits")
        try:
            query="SELECT sum(debits) FROM expensecalc.store"
            cursor.execute(query)
        except Error as e:
            print("Sorry we could not fetch your debits")
