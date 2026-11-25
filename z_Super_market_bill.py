# """Super market Bill Generator"""

name = input("Enter your name: ")

# list of items
list_items = '''
Rice        Rs  120/kg
Sugar       Rs  20/kg
Oil         Rs  250/liter
Salt        Rs  25/kg
Paneer      Rs  200/kg
Maggie      Rs  12/packet
Boost       Rs  280/bottle
'''

# Decleration _Data storage
total_price = 0
finel_price = 0
i_list = []
q_list = []
p_list = []

# Each item price
list_items_1 = {"rice":120, "sugar":20, "oil":250, "salt":25, "panner":200, "maggie":12, "boost":280,}

# main code 
while True:
    choose_option = int (input("Press 1 for List or 2 to Exit: "))
    if choose_option == 2:
            print("*...Thank you for shopping...*")
            break

    elif choose_option == 1:
        while True:
            print(list_items)
            if choose_option == 1:
                     print('''\t\t\t\tEnter "stop" to exit''')
                     product_selected_list =input("Which product you want: ").lower()
                     if product_selected_list in list_items_1:
                          i_list.append(product_selected_list)
                          p_list_1 = product_selected_list in list_items_1
                          p_list.append(list_items_1[product_selected_list])

                     else:
                          print(f"{product_selected_list} is not in list... check it once!")
                          break
                     quantity_selected = int(input(f"Enter how many {product_selected_list} items you Want: "))
                     q_list.append(quantity_selected)


    elif choose_option != 1 and choose_option != 2:
        print(f"Please select 1 or 2 only!")
        break
    elif choose_option == "stop":
            print(f"Collect your Finel bill...")
            break

#final bill layout
    print(f"{"="*23} Vamsi Krishna {"="*22}")
    print("\t\t\tCherukupalli")
    print(f"Name: {name}")
    print(f"{"-"*60}")
    print(f" S.No\t\titems\t\tquantity\tprice ")


    range_number = i_list.copy()
    for i in range(range_number.__len__()):
        print(f"  {i+1}\t\t{i_list[i]}\t\t  {q_list[i]}\t\t{p_list[i]}")
        total_price += (q_list[i]*p_list[i])

    tax_amount = (total_price*12)/100
    finel_price = total_price + tax_amount
    print(f"{"-"*60}")
    print(f"\t\t\t\tTotal amount: Rs {total_price}")
    print(f"  Tax amount\t\t\t\t Rs {tax_amount}")

    Discount = 0
    percentage = 0
    if finel_price >= 2000 and finel_price <= 2999 :
          Discount = (finel_price*5)/100
          percentage = 5
          print(f"    Discount: {percentage}%\t\tRs {Discount}")
    if finel_price >= 3000 and finel_price <= 4999 :
          Discount = (finel_price*10)/100
          percentage = 10
          print(f"    Discount: {percentage}%\t\tRs {Discount}")
    if finel_price >= 5000 :
          Discount = (finel_price*20)/100
          percentage = 20
          print(f"    Discount: {percentage}%\t\tRs {Discount}")

    print(f"{"-"*60}")
    print(f"\t\t\t\tFinal amount: Rs {finel_price-Discount}")

    print(f"{"-"*60}")
    print(f"\t\t Thank you & Visit again")
    print(f"{"-"*60}")

# End
