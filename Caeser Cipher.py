def cipher_code(input_text, input_shift, input_code_type):
    word = ''
    input_shift %= 26
    if input_code_type == "decode":
        input_shift *= -1
    for char in input_text:
        if char == " ":
            word += " "
        else:
            position = alphabet.index(char)
            new_position = position + input_shift
            word += alphabet[new_position]
    print(f"Your message is : {word.capitalize()}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   

                          88                                 
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

while True:
    correct_input = True
    while correct_input is True:
        code_type = input("\nEnter 'encode' to encrypt or 'decode' to decrypt:\n").lower()
        if code_type == "encode":
            correct_input = False
        elif code_type == "decode":
            correct_input = False
    text = input("Type your message:\t").lower()
    shift = int(input("Type the shift number:\t"))
    cipher_code(text, shift, code_type)
    continue0 = input("\nIf you want to continue press 'y' if not press 'n':\t")
    if continue0 == 'n':
        break
