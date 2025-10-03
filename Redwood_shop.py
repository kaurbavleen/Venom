item_code = input("Enter item code(A) Apparel, (F) Footwear : ")
SP = float(input("Enter selling price (per unit) of time: "))

if item_code == 'a' or item_code == 'A':
    item = "Apparel"
    if SP <= 1000:
        gst = 5
    else:
        gst = 12

elif item_code == "f" or item_code == "F":
    item = "Footwear"
    if SP <= 500:
        gst = 5
    else:
        gst = 18

cgst = SP * (gst/2)/100   
sgst = cgst
amount = SP + cgst + sgst # Consumer willl purchase at this price
print('-' * 65)
print("\t\t\t Invoice")
print('-' * 65)
print()
print("Item:  {0:>51s}".format(item))
print("Price: \t\t{0:40.2f}".format(SP))
print("\t CGST(@, (gst/2),%) : \t\t{0:15.2f}".format(cgst))
print("\t SGST(@, (gst/2),%) : \t\t{0:15.2f}".format(sgst))
print('-' * 65)
print("Amount payable: \t\t {0:23.2f}".format(amount))
print('-' * 65)
