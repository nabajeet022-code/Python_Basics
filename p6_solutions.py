number = int(input("what is your factorial number? : \n"))
factorial = 1
while number > 0 :
    factorial  = factorial * number
    number -= 1

print(factorial)