sum_num  = int(input("Till what number you want to calculate the sum: \n"))
sum = 0
for num in range(sum_num + 1):
    if num % 2 == 0:
     sum = sum + num

print(sum)