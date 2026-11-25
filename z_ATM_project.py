""" ATM Projects """
# # method 1: single user after login
# balance = 0
# while True:
#     print("\n ATM Menu:")
#     print("1. Credit")
#     print("2. Debit")
#     print("3. Balance")
#     print("4. Exit")
#     choice = input("Enter your choice (1-4): ")
#     if choice == '1':
#         amount = float(input("Enter amount to credit: "))
#         if amount <= 0:
#             print("Please enter a positive amount.")
#         else:
#             balance += amount
#             print(f"${amount} credited to your account.")
#     elif choice == '2':
#         amount = float(input("Enter amount to debit: "))
#         if amount <= 0:
#             print("Please enter a positive amount.")
#         elif amount > balance:
#             print("Insufficient balance.")
#         else:
#             balance -= amount
#             print(f"${amount} debited from your account.")
#     elif choice == '3':
#         print(f"Your current balance is: ${balance}")
#     elif choice == '4':
#         print("Thank you for using the ATM. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


# # method 2: Multi user
# login_data = {"vamsi":"123"}
# balance = 0
# while True:
#     num = "Main Menu"
#     num_1 = "1. Credit"
#     num_2 = "2. Debit"
#     num_3 = "3. Balance"
#     num_4 = "4. New login"
#     num_5 = "5. Exit"
#     print("-"*10)
#     print(num)
#     print(num_1)
#     print(num_2)
#     print(num_3)
#     print(num_4)
#     print(num_5)
#     menu_choice = int(input("Enter your choice: "))
#     if menu_choice == 5:            # 5. Exit
#         print("Thank you for Visit. Goodbye!")
#         break

#     if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
#         user_name = str(input("Enter your user name: "))
#         password = str(input("Enter your password: "))
#         for i,j in login_data.items():
#             if user_name == i and password == j:
#                 print("login successfull")

#                 if menu_choice == 1:        # 1. Credit
#                     amount = float(input("Enter amount to credit: "))
#                     if amount <= 0:
#                         print("Please enter positive amount: ")
#                     else:
#                         balance += amount
#                         print(f"${amount} credited to your account.")
#                         press_button = int(input('''Press "1" to see your Account Balance: '''))
#                         if press_button == 1:
#                             print(f"Total Balance: {balance}")
#                         else:
#                             break

#                 if menu_choice == 2:        # 2. Debit
#                     debit_amount = float(input("Enter withdraw amount: "))
#                     if debit_amount <= balance:
#                         balance -= debit_amount
#                         print(f"{debit_amount} Withdraw in your account")
#                         press_button = int(input('''Press "1" to see your Account Balance: '''))
#                         if press_button == 1:
#                             print(f"Total Balance: {balance}")
#                         else:
#                             break
#                     else:
#                         print("Insufficient Funds")
#                         press_button = int(input('''Press "1" to see your Account Balance: '''))
#                         if press_button == 1:
#                             print(f"Total Balance: {balance}")
#                         else:
#                             break

#                 if menu_choice == 3:        # 3. Balance
                    
#                         print(f"Hi,{user_name} your Account Balance is: {balance} ")

#     if menu_choice == 4:                # 4. new login
#         new_user_name = input("Enter user name: ").lower()
#         new_password = input("Enter password: ")
#         login_data[new_user_name] = [new_password]
#         print(f"Welcome to {new_user_name}")
#         print("Account has been created successfully")
#         print("Thank you for choosing")

#     if menu_choice != 1 and   menu_choice != 2 and menu_choice != 3 and menu_choice !=4 and menu_choice !=5 :
#         print(" Invalid choice. Please try again. ")
        
# # End



# method 3      def function 

# main data
login_data = [["vamsi","123",500]]

def cridit():
     user_name = input("Enter User name: ").strip().lower()
     password = input("Enter Password: ").strip()
     for i in login_data:
         if user_name == i[0] and password == i[1]:
          print("\t\tLogin in sucessfull...")
          enter_cridit = int(input("Enter your Cridit Amount: "))
          if enter_cridit <=0:
              print("Amount must be greater than 0.")
              return
          i[2] += enter_cridit
          print(f"Your Account Balance is: {i[2]}")
          break
     else:
        print("Login in failed, Please enter proper user name and password...!")
     pass

def withdraw():
    user_name = input("Enter User name: ").strip().lower()
    password = input("Enter Password: ").strip()
    for i in login_data:
        if user_name == i[0] and password == i[1]:
            withdraw_amount = int(input("Enter Withdraw amount: "))
            if withdraw_amount <= i[2]:
                i[2] -= withdraw_amount
                print(f"Withdrawal sucessfull, Remaining Balance: {i[2]}")
                break
            else:
                print("Insufficient founds")
                break
        else:
            print("Invalid username or password. Please try again.\n")
            break
    pass

def balance():
    while True:
        print('''\t\t\t\t\tFor EXIT enter "stop" ''')
        user_name = input("Enter User name: ").strip().lower()
        if user_name != "stop":
            password = input("Enter Password: ").strip()
        else:
            user_name == "stop"
            break
        found = False
        for i in login_data:
            if user_name == i[0] and password == i[1]:
                print(f"Hi {i[0]}, Your Acount Balance is {i[2]}\n")
                found = True
                break
        if found:
            break
        else:
            print("Invalid username or password. Please try again.\n")
    pass

def New_login():
        while True:
            user_name = input("Enter User name: ").strip().lower()
            password = input("Enter Password: ").strip()
            user_name_exists = any(user_name == entry[0] and password == entry[1] for entry in login_data)
            if user_name_exists:
                 print(f"{user_name} is already Exist's, Change your user name and password...!")
            else:
                 break
        while True:
          print("\t\t\t\t\tminimum Required balance is: 500/-")
          minimun_balance = int(input("Please cridit minimum Balance:"))
          if minimun_balance < 0:
               print(f"Your enter {minimun_balance}, Enter properly...!")
          else:
                break
        login_data.append([user_name,password,minimun_balance])
        print(f'''login sucessfull
    Your user name is: {user_name} 
        Password is: {password}
            Your Account Balance is: {minimun_balance}''')    
        pass

def exit():
    print(f"\tThank you for using the ATM. Goodbye :) ")
    pass



# main program loop
while True:
    print("\n---ATM Ment---")
    print("1. Cridit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. New login")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print(f"{choice} not in Main list, Enter proper Choice...!")
        pass


    elif choice == 1:     # Done
        cridit()


    elif choice == 2:     # Done
        withdraw()


    elif choice == 3:     # Done
        balance()


    elif choice == 4:     # Done
        New_login()


    elif choice == 5:     # Done
        exit()
        break

# End




# # method 4      oops

# # method 5      



