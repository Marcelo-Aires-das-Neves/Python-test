try:
    x = int(input("Enter a number: "))

except ValueError: 
    print("Invalid input")
else:
    print(f"x = {x}")