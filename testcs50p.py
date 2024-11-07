def calculate_love_score(name1, name2):
    """Calculate the love score based on the names provided."""
    combined_name = (name1 + name2).lower()
    
    first_digit = sum(combined_name.count(char) for char in "true")
    second_digit = sum(combined_name.count(char) for char in "love")
    
    love_score = int(f"{first_digit}{second_digit}")
    return love_score

def main():
    """Main function to run the love score calculation."""
    name1 = "Marcelo"
    name2 = "Maria Silvana"
    love_score = calculate_love_score(name1, name2)
    print(f"The love score for {name1} and {name2} is: {love_score}")

if __name__ == "__main__":
    main()
