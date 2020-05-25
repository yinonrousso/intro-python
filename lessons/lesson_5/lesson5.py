# l3 = [[[1,2,3.0],[9,6.5,5],[4,5,-2]],[[-1.2,-2,4],[-9,-6,7],[2,3,0]]]

# # challenge1: print every element using for loops
# # challenge2: print only integer numbers for every element using list

# for x in l3:
#     for y in x:
#         for z in y:
#             print (z)


# print ("end challenge one")

# for x in l3:
#      for y in x:
#             for z in y:
#                 if type(z)==int:
#                     print (z)

# print ("end challenge two")

# def function_name(parameter1, parameter2...):
    #function scope 
    # return value
def add(x, y):
    z = x + y
    return z
    
def mult(x, y):
    return x * y
    
def sub(x, y):
    return x - y
    
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("you cant divide by zero")
        exit(0)    

def expo(x,y):
    return x ** y
print (expo(2,4))
    
    
print(mult(5, 5))

x = 27
y = 0

print(sub(x,y))

print(div(x,y))

#challenge: make expo function without using ** 

    
# ans = add(2, 3)
# x = add(5, 7)
# print(ans)
# print(x)
    
# l1 = [1,2,3,4]    
# l2 = [5,6,7,8]   
# l3 = []
# for i in range(4):
#     # lisadd = add(l1[i], l2[i])  
#     lisadd = l1[i] + l2[i]
#     print(lisadd)
#     l3.append(lisadd)

# l3.append(7)
# print(l3)  
   
   
    
    
