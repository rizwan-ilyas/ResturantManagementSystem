class inventory:
    def __init__(self,id,name,ingredients,price,catagory):
        self.id=id
        self.name=name
        self.ingredients=ingredients
        self.price=price
        self.catagory=catagory
        self.tDetail=[self.id,self.name,self.ingredients,self.price,self.catagory]
    def getDetails(self):
        return self.tDetail
