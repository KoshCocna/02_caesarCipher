from caesarCipherArt import logo

print(logo)
endGame = False

def encrypt(shift, message):
    encText = []
    for letter in message:
        letter = chr((ord(letter)-97+shift)%26+97)
        encText.append(letter)
    encText = ''.join(encText)
    print(encText)

def decrypt(shift, message):
    decText = []
    for letter in message:
        letter = chr((ord(letter) - 97 + 26 - shift) % 26 + 97)
        decText.append(letter)
    decText = ''.join(decText)
    print(decText)
while not endGame:
    cipher = input("type 'encode' to encrypt, type 'decode' to decrypt: ")
    shift = int(input("type the shift number: "))
    msg = input("type your message: ")
    if cipher == 'encode':
        encrypt(shift, msg)
    elif cipher == 'decode':
        decrypt(shift, msg)
    else:
        print("ops... I guess it's typo.")
        continue
    status = input("type 'yes' if you want to go again. Otherwise type 'no': ")
    if status == 'no':
        endGame = True
