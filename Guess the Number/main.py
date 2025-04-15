import random 
computer = random.randint(1,100)
times = 1

while True:
    try:
        number = int(input("Guess the Number(1-100): "))
        if(number == computer):
            print(f"Congrates! You Win in {times} times")
            break
        elif(number < computer):
            if(times == 7):
             print("You reached maximum limit!")
             break
            print("Guess greater number!")
            times += 1
        else:
            if(times == 7):
             print("You reached maximum limit!")
             break
            print("Guess smaller number!")
            times += 1
            


    except ValueError:
        print("Enter Integer Value!") 

         