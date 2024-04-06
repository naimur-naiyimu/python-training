import random
scret_number = random.randint(1,100)
point = 0
while True:
    guess=int(input("please guess the number : "))
    point -= 1

    if scret_number == guess:
        print(f"You are winner!  your point is {point}")
        d=input("Do you want to continue?if yes enter Y else N:")
        if d=='Y' or d=='y':
            scret_number=random.randint(1,100)
            point = 0
            continue
        else:
            break
    
    elif scret_number> guess:
        print("Try to higer")
    elif scret_number< guess:
        print("Try to Lower")
      

       
       
