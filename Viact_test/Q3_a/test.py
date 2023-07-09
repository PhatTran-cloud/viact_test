import csv
from class_hierachy import ClassHierarchy
import pickle

file_path = r"E:\SelfLearning\Neo4J\technical_test_2023_07\question3\id_to_name.txt" 

data_list = []  

# print("[INFO] Reading file...")
# with open(file_path, 'r') as file:
#     for line in file:
#         datas = (line.split('\t'))
#         data = datas[0]
#         if data not in data_list:             
#             data_list.append(data.strip("\n"))

# print("[INFO] Read Done!")
# # print(len(data_list))
# set_data = list(set(data_list))
# print(len(set_data))
with open("./set_data.txt", 'rb') as f:
    set_data = pickle.load(f)


file_path = r"E:\SelfLearning\Neo4J\technical_test_2023_07\question3\hierarchy.txt" 
dictionary_data ={} 

with open(file_path, 'r') as file:
    for line in file:
        datas = (line.split(' '))
        
        key = datas[0]
        value = datas[1].rstrip('\n')
        
        
        if dictionary_data.get(key) is not None:           
            dictionary_data[key].append(value)
        else:
            dictionary_data[key] = []
            dictionary_data[key].append(value)
            
            
hierarchy_class = ClassHierarchy()
for _key in set_data:
    
    list_parent_id = [_key] # Define stack structure
    
     
    while list_parent_id:
       
        key = list_parent_id.pop()
        hierarchy_class.add_class(key)

        if dictionary_data.get(key) is None:
            continue    
        
        list_children_id = dictionary_data[key]

        [list_parent_id.append(x) for x in list_children_id]
        
        for id_children in list_children_id:
            if id_children == 'n00020090':
                print('aasdw')
            hierarchy_class.add_class(id_children,key)

print("aaaa")