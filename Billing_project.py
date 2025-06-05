import datetime
user_name=input("enter the User name :")
Qty=int(input("How many iphone you want : "))
cost=100000
amount=cost*Qty
cgst=2.5/100
sgst=2.5/100
amount_cgst=amount*cgst
amount_sgst=amount*sgst
if Qty==2:
    discount=amount*10/100
elif Qty<=5:
    discount=amount*15/100
elif Qty<=10:
    discount=amount*17/100
elif Qty<=15:
    discount=amount*23/100
elif Qty>15:
    discount=amount*25/100
discount_amount=amount-discount
total_amount=discount_amount+amount_cgst+amount_sgst

print("\n\n")
print("\t       Chethan Co. LTD.")
print("\t  Electric city, Bangalore-560100")
print("\t\t    ph : 9380623134")
print("\t\t GST IN:xxxxxxxxxxxxxx")
print("\t\t      BILL")
print("------------------------------------------------------")
print("   Memo# 17/41840\t ",datetime.datetime.now())
print("   User : {}\t\t\tPax# 1".format(user_name))
print("\t\t  Order# 1")
print("------------------------------------------------------")
print("Product\t\t\tQty\t Rate\tAmount")
print("------------------------------------------------------")
print(" Iphone\t\t\t{}\t {}\t{}".format(Qty,cost,amount))
print("------------------------------------------------------")
print("Sub Total \t\t\t\t{}".format(amount))
print("Distcount \t\t\t\t",discount)
print("C Gst @ 2.5%\t\t\t\t",amount_cgst)
print("S Gst @ 2.5%\t\t\t\t",amount_sgst)
print("------------------------------------------------------")
print("Total\t Qty : {}\t\tAmt\t{} \n".format(Qty,total_amount))
print("Thank You , Please Visit again")