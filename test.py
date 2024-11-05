distances = {
    "Voyager 1": 163,
    "Voyager 2": 1,
    "Voyager 3": 2, 
    "Voyager 4": 3,
    "Voyager 5": "4 kk"
}

def main():
    spacecraft = input("Enter the spacecraft name: ")
    try:
        m = float(distances[spacecraft])
    except KeyError:
        print("Spacecraft not found")
    except ValueError:
        print("Invalid input")
    else:
        print(f"{spacecraft} is {convert_to_miles(m)} miles away")  
    """    
    finally:
        print("Thanks for using this program")   """ 
def convert_to_miles(km):   
    return km * 149597870700



if __name__ == "__main__":
    main()  
