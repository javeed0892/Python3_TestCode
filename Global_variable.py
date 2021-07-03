x = "I hate "#this a global variable
def myfun():
    x = 5#this a local variable used inside the function.
    global y
    y = 7
    print(x,y )
myfun()
print(x, y)

carname = "Volvo"
print(type)
is_try = True