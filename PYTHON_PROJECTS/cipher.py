#alphabet to use for encryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

#a bolean value for while loop
is_true = True

#a while for continous process of encryption and decrytion
while is_true:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt  and 'end' to end process:\n")

  #an if statement to create a breakage from loop when a certain command is taken as input
  if direction == "end":
    is_true = False
    break

  #receiving inputs for user that needs to be encrypted or decrypted
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  encrypted_message = []
  position = 0
  new_position = 0

  #function for encryption
  def encrypt(text, shift):
    for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position <= 25:
          letter_1 = alphabet[new_position]
          encrypted_message.append(letter_1)
        else:
          new_position = new_position % 26
          letter_1 = alphabet[new_position]
          encrypted_message.append(letter_1)
      else:
        letter_1 = letter
        encrypted_message.append(letter_1)
    print(''.join(encrypted_message))



  #function for decryption
  decrypted_message = []
  def decrypt(text, shift):
    for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position > -1:
          letter_1 = alphabet[new_position]
          decrypted_message.append(letter_1)
        else:
          new_position = (((new_position * -1) % 26) * -1) + 26
          letter_1 = alphabet[new_position]
          decrypted_message.append(letter_1)
      else:
        letter_1 = letter
        decrypted_message.append(letter_1)
    print(''.join(decrypted_message))


  #if statement to call on function when a certain input is taken from user
  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)
  