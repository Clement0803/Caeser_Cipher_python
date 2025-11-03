alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(plain_text,shift_amount):
    cipher_text=""
    
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shift_amount
            new_position %= len(alphabet) # Wrap around the alphabet, for example index 25 + 3 = index 28 should wrap to index 2 
            cipher_text +=alphabet[new_position]
        else:
            cipher_text+=letter
    print(f"The encoded text is {cipher_text}")
    
def decrypt(cipher_text,shift_amount):
    plain_text=""
    
    for letter in cipher_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position-shift_amount
            new_position %= len(alphabet) # Wrap around the alphabet, for example index 2 - 3 = index -1 should wrap to index 25
            plain_text+=alphabet[new_position]
        else:
            plain_text+=letter
    print(f"The decoded text is {plain_text}")
    
def caeser(start_text,shift_amount,cipher_direction):
    if cipher_direction=="encode":
        encrypt(plain_text=start_text,shift_amount=shift_amount)
    elif cipher_direction=="decode":
        decrypt(cipher_text=start_text,shift_amount=shift_amount)
        
        
if __name__ == "__main__":
    while True:
        restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart=="yes":
            direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text=input("Type your message:\n").lower()
            shift=int(input("Type the shift number:\n"))
            caeser(start_text=text,shift_amount=shift,cipher_direction=direction)
        else:
            print("Goodbye!")
            break