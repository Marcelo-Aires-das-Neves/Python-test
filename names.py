names = ""
for _ in range(3):
     names = (input("What's your name? "))
    with open("names.txt", "a") as file:
        file.write(f"{names} \n")