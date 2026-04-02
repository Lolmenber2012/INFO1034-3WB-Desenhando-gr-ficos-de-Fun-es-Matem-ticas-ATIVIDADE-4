from turtle import *
from math import *
def soma_2(x):
    return x + 2


#- y = √x
def equa1(x):
    return isqrt(x) *2

#- y = 1/x
def equa2(x):
    return 1/x 

#- y = 2^x 
def equa3(x):
    return 2**x
    

#- y = 5 - x^2
def equa4(x):
    return 5 - x**2


# - y = x^2 - 5x + 6
def equa5(x):
    return x**2 - 5*x + 6

#- y = x^3 - x^2 - x + 1
def equa6(x):
    return x**3 - x*82 - x + 1




t= Turtle()

t.speed(0)





#BP


#plano Cartesiano
def Plano_Cartesiano():
        t.color('black')
        # Eixo dos X
        t.pu()
        t.goto(-300, 0)
        t.pd()
        t.goto(300, 0)
        t.stamp()

        # Eixo dos Y
        t.pu()
        t.goto(0, -300)
        t.pd()
        t.goto(0, 300)
        t.lt(90)
        t.stamp()
#---------------------------------

#t.color('red')
#t.pu()
#t.goto(-400,soma_2(-100))
#t.pd()
#t.goto(400, soma_2(100))

#print(list(range(-100,100)))

#for x in range(-100, 100):
    #print(x)

#def
#t.color('green')
#t.pu()
#t.goto(-200,soma_2(-200))
#t.pd()
#for x in range(-99, 101):
    #t.goto(x*2, soma_2(x*2))


def equação1 ():
    t.color('gold')
    t.pu()
    t.goto(0,equa1(500))
    t.pd()
    for x in range(0, 101):
        t.goto(x*2, equa1(x*2))
    
    
#Parte de cima
def equação2 ():
    t.color('red')
    t.pu()
    t.goto(10,equa2(100))
    t.pd()
    for x in range(1, 101):
        t.goto(x, equa2(x/50)*10)

#parte de Baixo
    t.color('red')
    t.pu()
    t.goto(-299,equa2(100))
    t.pd()
    for x in range(-299, 0):
        t.goto(x, equa2(x/50)*10)   
    



def equação3():
    t.color('blue')
    t.pu()
    t.goto(0,equa3(100))
    t.pd()
    for x in range(-99, 101):
        t.goto(x, equa3(x))
    

def equação4():
    t.color('green')
    t.pu()
    t.goto(-100,equa4(100))
    t.pd()
    for x in range(-99, 101):
        t.goto(x, equa4(x))
    
    

def equação5():
    t.color('orange')
    t.pu()
    t.goto(-100,equa5(100))
    t.pd()
    for x in range(-99, 101):
        t.goto(x, equa5(x))
    

def equação6():
    t.color('pink')
    t.pu()
    t.goto(-100,equa6(100))
    t.pd()
    for x in range(-99, 101):
        t.goto(x, equa6(x))
    
    











Plano_Cartesiano()
equação1()
t.clear()
Plano_Cartesiano()
equação2()
t.clear()
Plano_Cartesiano()
equação3()
t.clear()
Plano_Cartesiano()
equação4()
t.clear()
Plano_Cartesiano()
equação5()
t.clear()
Plano_Cartesiano()
equação6()
t.clear()















mainloop()
