alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



'''
#using different functions
def encrypt(user_text, shift_amount):
    cipher = ""
    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_text = alphabet[new_position]
        cipher += new_text
    print(f"The Encoded text is {cipher}")

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def decrypt(user_text, shift_amount):
    cipher = ""
    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_text = alphabet[new_position]
        cipher += new_text
    print(f"The decoded text is {cipher}")

if task == "encode":
    encrypt(user_text = text, shift_amount = shift)
elif task == "decode":
    decrypt(user_text=text, shift_amount=shift)
else:
    print("Invalid Input! please enter encode/decode")'''

### Merging the encode and the decode function

def crypt(user_text, shift_amount, user_task):
    cipher = ""
    for character in user_text:
        if character in alphabet:
            position = alphabet.index(character)
            if user_task == "encode":
                new_position = position + shift
            elif user_task == "decode":
                new_position = position - shift
            else:
                print("Invalid Input! please enter encode/decode")
            new_text = alphabet[new_position]
            cipher += new_text
        else:
            cipher += character
    print(f"The {task}d text is {cipher}")

to_be_continued = True
while to_be_continued:
    task = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    crypt(user_task=task, user_text=text, shift_amount=shift)
    choice = input("\nDo you want to continue?(Yes or No):\n").lower()
    if choice == "no":
        to_be_continued = False
        print("Good Bye!")



 
