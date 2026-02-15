name = input("what is your input: \n")
for char in name:
  print(char)
  if  name.count(char) ==1:
    print("first non repeated character is: \n", char)
    break