names = []

with open("exemplo5.txt") as file: 
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello, {name}!")