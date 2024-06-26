#Functions

q = input("Bet: ")
while q != "2":
    print("You Lose")
    q = input("Bet: ")
else:
    print("You Win!")

num1 = int(input("Bet: "))
num2 = int(input("Bet: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

def t():
    print("Hello")
t()

def add():
    print(1 + 1)                #result = 2 
    return 1 + 1                #result wont be display in console
add()

def add():
    return 1 + 1 
print(add())                    #result = 2

def add():
    return 1 + 1 

def sub():
    print(1 - 1)   
num = add()
num2 = sub()

print(num)
print(num2)

def add(x):
    print(x + y)
y = 12
add(1)


def triangle(b1, b2, g1):                               #ordered parameters
    print(f"{b1} likes {g1}")
    print(f"{b2} likes {g1}")
triangle("bertox", "jayvier", "marjore")

def triangle(b1, b2, g1):              
    print(f"{b1} likes {g1}")
    print(f"{b2} likes {g1}")
triangle(b2="bertox", b1="jayvier", g1="marjore")       #assigning parameters 

def names(*args):
    for arg in args:
        print(arg)
names("bertox", "jayvier", "jerson", "marjore")

def names(**bargs):
    for key, value in bargs.items():
        print(f"{key} -> {value}")
names(pablo="Airon", bubbles="Daniel")









