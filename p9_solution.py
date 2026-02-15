List  = [1,2,2,1]
unique_item = set()
for item in List:
    if item in unique_item:
        print("duplicate item is: \n", item)
        break
    else:
        unique_item.add(item)
