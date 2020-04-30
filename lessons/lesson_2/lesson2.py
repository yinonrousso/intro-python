
# #Lesson 2
# 
# #Slight Recap
# # int -> num
# # string -> word/phrase
# # boolean -> true/false
# # conditions equate to boolean value
# 
# # If/Else excersise
# 
# \n -> new line
# # Pizza Example

# Ask for pizza or calzone
# What toppings do you want: 1) Olives, 2) peppers, 3)onions
# Name for order

# age = str(input("Enter your age: "))



# print ("Please select numbers for order")

# mainOrder = int(input("1. Pizza\n2. Calzone \n"))
 
# if mainOrder == 1: 
#     mainOrder = "Pizza"
    
# elif mainOrder == 2: 
#     print("Calzone")
#     mainOrder  = "Calzone"
    
# else:
#     print("invalid order")
    
# toppings  = int(input("1. Olives\n2. Onions\n3. Bacon\n"))
 
# if toppings == 1: 
#     toppings = "Olives"
    
# elif toppings == 2: 
#     toppings = "Onions"
    
# elif toppings == 3: 
#     toppings = "Bacon"    
    
# else:
#     print("invalid order")    
    
# orderName = str(input("Name for Order: "))    

# print()
# print("This is your order: ")
# print(orderName)
# print(mainOrder)
# print(toppings)



# Intro to array
# Note in python we use lists
# list of size 6
#        0  1 2  3  4  5
ages = [13,15,2,99,104,16]
#            0        1     2        3      4
names = ["yinon","yehuda","maor","mikee","kwon"]

# list slicing
# list[inclusive:exclusive]
print(names[1:4])

# fill list named nums with numbers 1-100
nums = [num for num in range(1,101)]

# print last element in list
print(nums[-1]) 
  
