# this funciton creates a list with the information of the item

def add_item_info(name, price, amount_sold, **total_amount_sold):
    total_amount_sold['Item Name'] = name
    total_amount_sold['Item Price'] = price
    total_amount_sold['Amount sold']= amount_sold
    sold = (float(price) + int(amount_sold))
    total_amount_sold['Total made'] = sold

    return total_amount_sold

active = True

#this loop will ask the user for the item information until the user inputs 'no'

while active:
    
    user_response = input("Do you wanna add items? (yes/no) ")

    if user_response == "no":
        break

    item_name = input("What is the name of the item? ")
    item_price = input("what is the price of the item? (add decimals too)")
    total_amount = input(f"How many {item_name} did you sell? ")

#then we add all this information into the list

    item_added = add_item_info(item_name, item_price, total_amount)

#and finally we show the information of the item inside the list

    print(item_added)