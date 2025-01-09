with open("exemplo5.csv") as file:
    for line in file:
        row = line.strip().split(",")
        print(f"{row[0]}: {row[1]}")
        