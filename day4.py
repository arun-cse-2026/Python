#datastructures

#list
my_list = [10, 20, 30, 40]
print(my_list[0])  # 10 (first element)
print(my_list[3]) # 40 (last element)
print(my_list)
my_list.append(50)       # add at end
my_list.insert(1, 15)    # add 15 at index 1
print(my_list)
my_list.remove(30)    # remove value 30
my_list.pop()         # remove last element
print(my_list)

#Tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple[2])  

#set
my_set={1,2,3,}
my_set.add(5)
print(my_set)
my_set.remove(2)  
print(my_set)

#Dictionary
my_dict = {"name": "Ram", "age": 20}
print(my_dict["name"])  
my_dict["age"] = 21        # update age
print(my_dict["age"])
my_dict["city"] = "Chennai" # add new key-value
print(my_dict["city"])
del my_dict["city"]        # remove key "city"
my_dict.pop("age")         # remove key "age"
print(my_dict)


