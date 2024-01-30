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




# # input of capacity of jars

# j1= int (input("enter capacity of jar 1 : "))
# j2= int (input("enter capacity of jar 2 : "))
# g1 = int (input("enter your goal in jar 1: "))
# g2 = int (input("enter your goal in jar 2: "))


# # inisilize the value
# x , y = 0

# # switchcase
# def display():
#     # print("enter your choice : ")
#     print("\nx =" , x)
#     print("y =" , y)

#     print("\nRule 1: fill jar 1")
#     print("Rule 2: fill jar 2")
#     print("Rule 3: empty jar 1")
#     print("Rule 4: empty jar 2")
#     print("Rule 5: transfer water from j1 to j2")
#     print("Rule 6: transfer water from j2 to j1")
#     print("Rule 7: transfer some water from j1 to j2 untill j2 is filled")
#     print("Rule 8: transfer some water from j2 to j1 untill j1 is filled")
    



# # display()
# # choice =int (input("enter your choice"))

# while (x!= g1 or y!=g2):
#     display()
#     choice =int (input("enter your choice"))
    
#     # case 1
#     if (choice==1):
#         x= j1
#         display()

#     # case 2
#     if (choice==2):
#         y= j2
#         display()

#     # case 3
#     if (choice ==3):
#         x= 0
#         display()

#     # case 4
#     if (choice ==4):
#         y= 0
#         display()

#     # case 5
#     if (choice ==5):
#         if (x>0 and x+y <= j2):
#             x=0,y=y+x
#             display()
#         else:
#             print ("invalid")

#     # case 6
#     if (choice ==6):
#         if (y>0 and x+y<=j1):
#             y=0, y=y+x
#             display()
#         else:
#             print("invalid input")

#     # caose 7
#     if (choice== 7):
#         if (x> 0 and x+y >=j2):
#             x=x-(j2-y), y=j2



    

