test_list = [5, 6, 7]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing tuple
test_tup = (9, 10)
 
# Adding Tuple to List and vice - versa
# Using tuple(), data type conversion [tuple + list]
res = tuple(list(test_tup) + test_list)
 
# printing result
print("The container after addition : " + str(res))
