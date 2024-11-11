#Define the number of score about your true love.
def conbined_names():
    conbined = ""
    name1 = "Marcelo" #input("What's your true love's name: ").lower()
    name2 = "Maria Silvana" #input("What's your true love's name: ").lower()
    conbined = name1 + name2
    return conbined

def score(conbined):
    score = 0
    first_name = sum(conbined.count(letter) for letter in "true")
    second_name = sum(conbined.count(letter) for letter in "love")
    score = str(first_name) + str(second_name)
    return score

def main():
    print("Welcome to the Love Calculator!")
    print("Your score is: " + score(conbined_names()))




if __name__ == "__main__":
    main()