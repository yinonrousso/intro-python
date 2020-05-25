# Lesson 4: For loops and lists

# Recap on lists
# 
# list slicing
# print(cars[1:])

# print(cars)
# for item in list:
    # print(item)


# Get a new list of only the whole intger numbers
# if statement syntax
# if 'condition':
#     'statement'

# x = 2.2
# if type(x) == int:
#     print(x)


# nums =  [45.2, 3, 7, 95.2, 54, -3]

# for whole in nums:
#     if type(whole) == float:
#         print(whole) 

# 2D lists and nested for loops

# list_of_lists = [[1,2,3],[9,6,5],[4,5,-2]]

# for mylist in list_of_lists:
#     print(mylist)
#     for num in mylist:
#         print (num)


l3 = [[[1,2,3.0],[9,6.5,5],[4,5,-2]],[[-1.2,-2,4],[-9,-6,7],[2,3,0]]]

# challenge1: print every element using for loops
# challenge2: print only integer numbers for every element using list

for x in l3:
    for y in x:
        for z in y:
            print (z)


print ("end challenge one")

for x in l3:
     for y in x:
            for z in y:
                if type(z)==int:
                    print (z)

print ("end challenge two")