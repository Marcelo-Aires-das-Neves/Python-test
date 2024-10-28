while True:
    
    try:
        x = int(input("Enter a number: "))

    except ValueError: 
        print("Invalid input")
    else:
        break   
    
print(f"x = {x}")