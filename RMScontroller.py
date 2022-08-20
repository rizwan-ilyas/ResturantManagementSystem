from RMSmodel import *
from RMSview import *

class RMScontroller:
    def __init__(self):
        self.model=RMSmodel("localhost","root","","we")

    def AddDish(self):
        id=input("Enter dish Id : ")
        name=input("Enter your name : ")
        ingredients=input("Enter Ingredients (separated by ',') :  ")
        price=input("Enter Price : ")
        catagory=input("Enter its Catagory : ")
        adddish=inventory(id,name,ingredients,price,catagory)
        self.model.addDish(adddish.tDetail)

    def verifyAdmin(self):
        user=input("Enter userName : ")
        psw=input("Enter password : ")
        if(user=="admin" and psw=="admin"):
            return True
        return False

    def showDishes(self):
        dishes=self.model.allDishes()
        print("Please Select From the Given Table by Dish-ID and Press 0 for End")
        print("%-4s %-8s %-15s %-30s %-8s %s" %("Sr#","Dish-ID","Name","Ingredients","Price","Catagory"))
        for x in dishes:
            print("%-4s %-8s %-15s %-30s %-8s %s" %(x[0],x[1],x[2],x[3],x[4],x[5]))


    def placeOrder(self):
        inp=input("Press q for End/Quit and 1 for Adding More Dishes\nEnter Your Choice : ")
        order=[]
        while(inp!="q"):
            repeats = False
            id=input("Enter Dish-ID of Specific Dish to order : ")
            for x in order:
                if (x["id"] == id):
                    repeats=True
                    print("Dish Reapeats.....")
                    break

            if(self.model.isValidDish(id) and (not repeats)):
                num=int(input("Enter Number of Dishes : "))
                if(num>0):
                    ord={"id":id,"numOfDishes":num}
                    order.append(ord)
            else:
                if(not repeats):
                    print("Does Not Valid Dish ID!!")
            inp = input("Press 1 for Adding More Dishes or Q for quit\nEnter Your Choice : ")
        dine=input("Do You Want to Dine(y/n) : ")
        isDine=True if (dine=='y' or dine=='Y') else False
        print("Select Payment Methode (Press 1 for Cash and 2 for through Credit card)")
        payment=input("Enter Your Payement Method : ")
        throughCash=True if(payment=='1') else False
        return self.calculation(order,isDine,throughCash)

    def calculation(self,order,isdine,cashPay):
        total=0
        dineTax=0
        GST = 0

        prices=self.model.getPrice(order)
        for index, x in enumerate(prices):
            total=total+(x*int(order[index]["numOfDishes"]))
        if(isdine):
            dineTax=total/100
        GST=((total*16)/100) if(cashPay) else ((total*8)/100)
        total=round(total+dineTax+GST,2)
        #os.system("cls")
        print("\t\t\t*******************Your BILL*******************")
        alldetail=self.model.getall(order)
        print("%-3s %-10s %-10s %-12s %-10s %s" %("Sr#","Dish-ID","Name","Price/Dish","# of Dish","TotalPrice"))
        for index,x in enumerate(alldetail):
            print("%-3s %-10s %-10s %-12s %-10s %s" % (index+1, x[1], x[2], x[4],order[index]["numOfDishes"],round(float(x[4])*float(order[index]["numOfDishes"]),3)))
        print("")
        print("%-38s"%(""),"Dine Tax = ",dineTax)
        print("%-38s"%(""),"GST      = ",GST)
        print("%-38s"%(""),"Total    = ",total)

        print("\t*******************Thanks For Your Visit*******************")

def Menu():
    rms = RMScontroller()
    check=input("Are you Customer(y/n) : ")
    if(check=='y' or check=='Y'):
        isAdmin=False
    elif(check=='n' or check=='N'):
        isAdmin=True

    if(isAdmin):
        if(rms.verifyAdmin()):  #default user name and password for Admin is admin,admin
            rms.AddDish()
        else:
            print("Incorrect username or password!!")
    else:
        rms.showDishes()
        rms.placeOrder()





