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

def viewsummary():
    data=readtransaction()
    if len(data)==0:
        print("No transactions found.")
        return
    total_income=0
    total_expense=0
    for transaction in data:
        if transaction["type"].lower()=="income":
            total_income+=transaction["amount"]
        elif transaction["type"].lower()=="expense":
            total_expense+=transaction["amount"]
    balance = total_income-total_expense
    print("Total Income : ",total_income)
    print("Total Expense: ",total_expense)
    print("Balance: ",balance)