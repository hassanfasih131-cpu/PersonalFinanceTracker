from file_handler import readtransaction,writetransaction
import json
def addtransaction():
    data=readtransaction()
    type=input("Enter the transaction type (income/expense): ").lower()
    category=input("Enter the category (travel,medicine,food,ect)").lower()
    Bool=True
    while Bool:
        try:
            amount=float(input("Enter the amount you want to add: "))
            break
        except ValueError:
            print("Please enter a numeric value")
    date=input("Enter the date you want to add (DD/MM/YYYY) ")
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

def filtertransactions():
    data=readtransaction()
    if len(data)==0:
        print("No transactions found.")
        return
    else:
        category=input("Enter what category you want to filter transactions for: ").lower()
        for i in data:
            if i["category"]==category:
                print("Type: ",i[type],
                      "Category: ",i[category],
                      "Amount: ",i["amount"],
                      "Date: ",i["date"])

def spendinglimit():
    total=0
    data=readtransaction()
    category=input("Enter what category you want to set a limit to: ").lower()
    limit=float(input("Enter the limit: "))
    for i in data:
        if i["type"].lower()=="expense":
            if i["category"].lower()==category:
                total+=i["amount"]
    if total>=limit:
        print("The limit has been reached")
    else:
        print("You are within the limit\n"
              "The total is: ",total,
              "\nThe limit is: ",limit)