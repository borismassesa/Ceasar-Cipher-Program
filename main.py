alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in plain_text:
        if letter == " ":
            cipher_text += " "
        else:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_text = alphabet[new_position]
            cipher_text += new_text

    print(f"Here is the {direction}d result: {cipher_text}")


ceasar(plain_text=text, shift_amount=shift, cipher_direction=direction)
