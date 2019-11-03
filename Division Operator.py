num1 = int(input('"Enter First Number": '))
num2 = int(input('"Enter Second Number": '))
division = num1 / num2
if division == int(num1 / num2):
    print("Completely Divisible")
elif division == float(num1 / num2):
    print("Not Completely Divisible")    
else:
    print("Ivalid Input")    