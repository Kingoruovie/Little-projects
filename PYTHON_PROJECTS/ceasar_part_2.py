alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def ceasar(plain_text, shift_amount, needed_direction):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if needed_direction == "encode":
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    elif needed_direction == "decode":
      new_position = position - shift_amount
      cipher_text += alphabet[new_position]
  print(cipher_text)

ceasar(plain_text = text, shift_amount = shift, needed_direction = direction)