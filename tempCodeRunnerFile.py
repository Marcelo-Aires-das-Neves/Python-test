def display_word(word, correct_letters):
    """Display the current state of the word to guess."""
    display = ""
    for letter in word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    return display
