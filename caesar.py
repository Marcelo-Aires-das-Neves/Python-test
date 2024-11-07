def get_user_input():
    """Get user input for direction, text, and shift amount."""
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    return direction, text, shift

def caesar_cipher(text, shift, direction):
    """Encrypt or decrypt the text using the Caesar cipher."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output_text = ""

    if direction == "decode":
        shift = -shift

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter  # Keep non-alphabet characters unchanged

    return output_text

def main():
    """Main function to run the Caesar cipher."""
    should_continue = True

    while should_continue:
        direction, text, shift = get_user_input()
        result = caesar_cipher(text, shift, direction)
        print(f"Here is the {direction}d result: {result}")

        restart = input("Type 'yes' to continue or 'no' to exit:\n").lower()
        if restart == 'no':
            should_continue = False
            print("Goodbye")

if __name__ == "__main__":
    main()