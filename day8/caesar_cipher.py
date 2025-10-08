from caesar_logo import logo

def encrypt(word, shift):
    encrypted_word = ""
    
    for c in word:
        c_num = ord(c)

        encrypted_word += chr(c_num + shift)

    return encrypted_word

def decrypt(word, shift):
    decripted_word = ""
    
    for c in word:
        c_num = ord(c)

        decripted_word += chr(c_num - shift)

    return decripted_word


print(logo)
while True:
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    option = input()

    print("Type your message:")
    message = input()

    print("Type the shift number:")
    shift = int(input())

    if option == 'encode':
        encripted_message = encrypt(message, shift)

        print(f"Here's the encode result: {encripted_message}")

    elif option == 'decode':
        encripted_message = decrypt(message, shift)

        print(f"Here's the decode result: {encripted_message}")
    
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    choose = input()

    if choose == 'no':
        print("Goodbye!")
        break


