# from caesar_config import alphabet
# from caesar_config import logo

answer = True


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
while answer is True:

    direction = input('Type "Encode" to encrypt, type "Decode" to decrypt:\n').lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text_index, shift_index):

        cypher = ""
        if direction == "encode":
            for i in text:
                if i in alphabet:
                    index_number = alphabet.index(i)
                    position = (index_number + shift)
                    cypher += str(alphabet[position % len(alphabet)])  # cycle the alphabet from the start
                else:
                    cypher += i  # to add spaces, numbers and symbols

            print(f'The encoded text is:\n"{cypher}"\n')

        elif direction == "decode":
            for i in text:
                if i not in alphabet:
                    cypher += i  # to add spaces, numbers and symbols
                else:
                    index_number = alphabet.index(i)
                    position = (index_number - shift)
                    cypher += str(alphabet[position % len(alphabet)])  # cycle the alphabet from the start

            print(f'The encoded text is:\n"{cypher}"\n')
        else:
            print("Not valid.")

    caesar(text_index=text, shift_index=shift)
    reply = input("Restart the cypher? Type Y or N:\n ")

    if reply == "y":
        print("_\n")  # to separate one instance from another
    else:
        answer = False  # start again the while loop

print("_\n")
print("Cypher ended.")
