from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# The below function helps to encode or decode messages based on user input
def caesar(input_text, no_shift, dir):
  crypt=[]
  for alp in input_text:
    # Checking if the alp is an alphabet, if not then it will directly get appended at line 30; no need of encode or decode.
    if alp in alphabet:
      # Find the current index position
      current_index = alphabet.index(alp)

      if dir == "encode":
        # For encode operation we move the index in forward direction by the shift amount
        current_index += no_shift
        # Handling the case of index out of bound
        if current_index >= 26:
          current_index -= 26

      elif dir == "decode":
        # For decode operation we move the index in backward direction by the shift amount
        current_index -= no_shift
        # Handling the case of index out of bound
        if current_index < 0:
          current_index += 26
      alp=alphabet[current_index]
    # Appending the list with updated alp
    crypt.append(alp)
  # Converting the list to string
  final_output = ''.join(crypt)
  print(f"The {dir} text of {input_text} is {final_output}")

start = True
while start:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # Incase the shift input is not within the range of alphabet size
  shift %= 26
  caesar(input_text=text, no_shift=shift, dir=direction)
  restart=input("You want to continue? Type 'yes' or 'no': ").lower()
  if restart=="no":
    start=False
  elif restart=="yes":
    start=True


  