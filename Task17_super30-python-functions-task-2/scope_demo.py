x = 10   # global variable

def show_scope():
    x = 5   # local variable
    print("Inside function:", x)

show_scope()
print("Outside function:", x)
