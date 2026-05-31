x = "awesome" #Global variable
def myfunc(): #Create a func
    global x #Creating global variable inside the function
    x = "fantastic" #Local variable
    print("Python is " + x)
myfunc()
print("Python is " + x)