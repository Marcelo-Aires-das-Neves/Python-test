def main():
    name = input("What is your name? ")
    print(hello2(name))
    
def hello2(to="World"):
    return f"Hello, {to}"


if __name__ == "__main__":
    main()