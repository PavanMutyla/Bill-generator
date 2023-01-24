class Pizza:
    cost=0
    def gst(self):
        return (Pizza.cost*(3))/100
        
    
class veg(Pizza):
    def Price(self):
        vp = 220
        Pizza.cost+=vp
        
        return Pizza.cost
    def cheeze(self):
        extra_cheeze = 25
        
        return extra_cheeze
    def origano(self):
        extra_ori = 30
        return extra_ori
    def combo(self):
        french = 100
        veg_burger = 130
        combo_price = french+veg_burger
        
        return combo_price
    
class nonveg(Pizza):
    def Price(self):
        np = 250
        Pizza.cost+=np
        
        return  Pizza.cost
    def cheeze(self):
        extra_cheeze = 25
        
        
        return extra_cheeze
    def origano(self):
        extra_ori = 30
       
        
        return extra_ori
    def combo(self):
        french = 100
        nonveg_burger = 150
        combo_price = french+nonveg_burger
        
        
        return combo_price
    
a =int( input('enter your choice \n1.veg\n2.non-veg\n'))
if(a == 1):
    order = veg()
elif(a == 2):
    order = nonveg()
else:
    print('please select correct option')

print('your addons')
b = input('1.cheese\n2.origano\n3.combo\n4.no')

if(b=='1'):
       
         
         print(f'your addon price is {order.cheeze()}') 
         print(f'your total  cost  including gst is { order.cheeze() + order.Price()+order.gst()}')
        
elif(b=='2'):
        x = order.origano()
        print(f'your addon price is {order.origano()}')
       
        print(f'your total cost including gst is {order.origano()+ order.Price()+order.gst()}')
        
    
elif(b=='3'):
         print(f'your addon price is {order.combo()}')
         x = order.combo()
      #  print(f'your addon cost is {order.comdo()}')
         print(f'your total cost including gst is {x+ order.Price()+order.gst()}')
elif(b=='4'):
    print(f'tou total cost is {order.Price()}')
else:
        print('wrong option')
