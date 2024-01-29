# input of capacity of jars

j1= int (input("enter capacity of jar 1 : "))
j2= int (input("enter capacity of jar 2 : "))
g = int (input("enter your goal : "))

# switchcase
def display():
    # print("enter your choice : ")
    print("Rule 1: fill jar 1")
    print("Rule 2: fill jar 2")
    print("Rule 3: empty jar 1")
    print("Rule 4: empty jar 2")
    print("Rule 5: transfer water from j1 to j2")
    print("Rule 6: transfer water from j2 to j1")
    print("Rule 7: transfer water from j1 to j2 untill j2 is filled")
    print("Rule 8: transfer water from j2 to j1 untill j1 is filled")

# inisilize the value
    x , y = 0


display()
choice =int (input("enter your choice"))
