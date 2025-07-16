from datetime import datetime

print("WELCOME TO U MART")
User_Name=input("Enter Your Name :")

Lists='''
Rice         Rs 60
Wheat Flour  Rs 45 kg
Wheat Flour  Rs 45 kg
Sugar        Rs 40 kg
Salt         Rs 20 kg
Toor Dal     Rs 95 
Moong Dal    Rs 100
Chana Dal    Rs 80
Cooking Oil  Rs 120 liter
Milk         Rs 55 liter
Tea Powder   Rs 80 kg
Coffee       Rs 110 kg
Eggs         Rs 6 per egg
Bread        Rs 35
Butter       Rs 150 
Paneer       Rs 75
Maggi        Rs 15
Biscuits     Rs 25
Tomato       Rs 30 kg
Onion        Rs 25
Potato       Rs 20 kg
Carrot       Rs 40
Cabbage      Rs 35 kg
Apple        Rs 120
Banana       Rs 50
Orange       Rs 90  
''' 
print(Lists)

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]


items={"Rice": 60,
    "Wheat Flour": 45,"Sugar": 40,"Salt": 20,"Toor Dal": 95, "Moong Dal": 100,"Chana Dal": 80,
    "Cooking Oil": 120,"Milk": 55,"Tea Powder": 80, "Coffee": 110, "Eggs": 72, "Bread": 35,
    "Butter": 150, "Paneer": 75, "Maggi": 15,"Biscuits": 25,"Tomato": 30, "Onion": 25,
    "Potato": 20,"Carrot": 40,"Cabbage": 35,"Apple": 120,"Banana": 50,"Orange": 90}
option=int(input("For items list Type 1:"))
if option==1:
    print(Lists)
for i in range(len(items)):
    inp1=int(input("If you want buy Enter 1 or 2 for exist:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item, quantity, price))

            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry You entered item is not available")
    else:
        print("You entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Peoples Mart",25*"=")
            print(28*" ","Tirupati")
            print("Name:"" ","Date:",datetime.now())
            print(75*"-")
            print("sno", 8*" ",'items',5*" ",'Quantity',8*" ",'price')

            for i in range(len(pricelist)):
               print(i,8*' ',5*' ',ilist[i],10*'',qlist[i],18*"" ,plist[i])

            

            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst + TotalAmount", 40*" ",'Rs',finalamount)
            print(75*"-")
            print(25*" ","Thanks for visiting",User_Name)
            print(75*"-")