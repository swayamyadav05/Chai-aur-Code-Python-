# List Uniquness Checker

items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate: ", item)
        # break
        continue
    unique_items.add(item)
    
# for fruit in items:
#     # print(fruit)
#     if items.count(fruit) == 1:
#         break
#     else:
#         print("Duplicate: ",fruit)
        
print(unique_items)