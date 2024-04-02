print("Welcome to Area Calculator")

while True:
    print("Options:")
    print("1.Circle")
    print("2.Triangle")
    print("3.Square")
    print("4.Rectangle")

    option = int(input("Enter your choice:"))

    if option == 1:
        r = float(input("Enter a Radius: "))
        area = 3.1416 * r * r #pi * r *r
        print(f"Circal area is {area}")
    elif option == 2:
        a = float(input("Enter a : "))
        b = float(input("Enter b : "))
        c = float(input("Enter c : "))
        s = (a+b+c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f"Triangle area is {area}")
    elif option == 3:
        
        a = float(input("Enter a : "))
        area = a * a
        print(f'Square area is {area}')
    elif option == 4:
        a = float(input("Enter a : "))
        b = float(input("Enter b : "))
        area = a * b
        print(f'Rectangle area is {area}')
        
    d = input("do you want to continue? if yes enter y else enter n: ")
    if  d =='y' or d =='Y':
        continue
    else:
        break
        
