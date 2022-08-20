import pymysql

class RMSmodel:
    def __init__(self,host,user,psw,database):
        self.host=host
        self.user=user
        self.psw=psw
        self.database=database
        self.connection=None
        try:
            self.connection=pymysql.connect(host=self.host,user=self.user,password=self.psw,database=self.database)
            print("Connected Successfully")
        except Exception as e:
            print("Connection error")

    def addDish(self,details):
        query="insert into inventory (id, `name`, `ingredients`, `price`, `catagory`) values(%s,%s,%s,%s,%s)"
        argu=(details)
        cursor=self.connection.cursor()
        try:
            cursor.execute(query,argu)
            self.connection.commit()
        except Exception as e:
            print("Something Went wrong While adding dish")
        finally:
            cursor.close()

    def allDishes(self):
        query="select * from inventory;"
        cursor=self.connection.cursor()
        try:
            cursor.execute(query)
            dishes=cursor.fetchall()
        except Exception as e:
            print("Something Went Wrong while Displaying Dishes")
        finally:
            cursor.close()
        return dishes

    def isValidDish(self,id):
        query="select * from inventory where id=%s"
        cursor=self.connection.cursor()
        cursor.execute(query,id)
        if(cursor.fetchone()!=None):
            cursor.close()
            return True
        cursor.close()
        return False

    def getPrice(self,order):
        query = "select price from inventory where id=%s"
        cursor = self.connection.cursor()
        prices=[]
        for x in order:
            cursor.execute(query, x["id"])
            prices.append(int(cursor.fetchone()[0]))
        cursor.close()
        return prices

    def getall(self,order):
        query = "select * from inventory where id=%s"
        cursor = self.connection.cursor()
        detail=[]
        for x in order:
            cursor.execute(query, x["id"])
            detail.append(cursor.fetchone())
        cursor.close()
        return detail


# b=["1234","bread","weat",20,"Gold"]
# a=RMSmodel("localhost","root","","we")
# a.addDish(b)





