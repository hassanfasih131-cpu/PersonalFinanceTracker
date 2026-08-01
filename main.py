from file_handler import readtransaction, writetransaction
from finance import addtransaction, viewsummary, filtertransactions, spendinglimit

while True:
    print("\nWelcome to the Personal Finance Tracker app")
    print("You can: \n"
          "1- Add a transaction\n"
          "2- View all transactions\n"
          "3- Filter transactions\n"
          "4- Set Spending Limit\n"
          "5- Exit")

    choice=int(input("Enter your choice(choose the number):\n"))
    if choice==1:
        addtransaction()
    elif choice==2:
        viewsummary()
    elif choice==3:
        filtertransactions()
    elif choice==4:
        spendinglimit()
    elif choice==5:
        break
    else:
        print("\nPlease enter a valid choice")