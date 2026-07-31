from file_handler import readtransaction,writetransaction
import json
def addtransaction():
    data=readtransaction()
    type=input("Enter the transaction type (income/expense): ")
    category=input("Enter the category (travel,medicine,food,ect)")
    date=input("Enter the date you want to add (DD/MM/YYYY) ")
    Bool=True
    while Bool:
        try:
            amount=float(input("Enter the amount you want to add: "))
            break
        except ValueError:
            print("Please enter a numeric value")
    transaction={"type":type
          ,"category":category
          ,"date":date
          ,"amount":amount}
    print("The data has been added successfully")
    data.append(transaction)
    writetransaction(data)
