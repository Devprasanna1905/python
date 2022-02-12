class Pizza:
    def __init__(self,name,price,collection,veg=False):
        
        self.name=name
        self.price=price
        self.collection=collection
        self.veg=veg
    
    '''def get_input(self):
        self.name=input("enter the pizza name: ")
        self.price=int(input("enter price: "))'''
    
    def ti(self):
        print("----Pizza menu----")
        print()
        
    def display(self):
        
        if self.veg:
            print("{} Pizza : {}$ -Veg ".format(self.name,self.price))
            
        else:    
            print("{} Pizza : {}$ ".format(self.name,self.price))
        print(", ".join(self.collection))
        print()

class custompizza(Pizza):
    baseprice=7
    perprice=1.2
    i=0
    
    def __init__(self):
        custompizza.i+=1
        self.no=custompizza.i
        
        super().__init__("Custom {}".format(self.no),0, [])
        self.ask_user()
        self.compute()
        
    def ask_user(self):
        
        print()
        print("ingredient for custom pizza",self.no)
        while True:
            ingredient = input("Add an ingredient (or press ENTER to finish) : ")
            if ingredient=="":
                return
            self.collection.append(ingredient)
               
    def compute(self):
        self.price=(len(self.collection)*self.perprice)+self.baseprice
        return self.price
pizzas=[Pizza("calzone",8.99,("cheese","berry","paneer"),True),Pizza("hawai",8,("cheese","ham","paneer")),Pizza("4 seasons", 11, ("eggs", "tomato", "emmental", "ham")),
Pizza("vegetarian", 8, ("mushrooms", "tomato", "oignons", "bell pepper"), True),custompizza(),custompizza()]

#pizza1.get_input()
for j in range(0,1):
    pizzas[j].ti()
#def pizzasort(e):
    #return e.name
#pizzas.sort(key=pizzasort)    
for i in pizzas:
    i.display()
