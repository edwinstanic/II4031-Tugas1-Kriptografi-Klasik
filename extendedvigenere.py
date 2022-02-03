class ExtendedVigenere:
    def __init__(self, k, t):
        self.key = k
        self.text = t
    
    def encrypt(self, k, p):
        ciphertext = []
        keyIdx = 0
        for char in p:
            charIdx= ord(char)
            if charIdx != -1:
                charIdx = charIdx + ord(k[keyIdx % len(k)])
                keyIdx += 1

            # Kondisi apabila charIdx > 256
            charIdx = charIdx % 256
            ciphertext.append(chr(charIdx))

        return ''.join(ciphertext)

    def decrypt(self, k, c):
        plaintext = []
        keyIdx = 0
        for char in c:
            charIdx= ord(char)
            if charIdx != -1:
                charIdx = charIdx - ord(k[keyIdx % len(k)])
                keyIdx += 1

            # Kondisi apabila charIdx > 256
            charIdx = charIdx % 256
            plaintext.append(chr(charIdx))
        
        return ''.join(plaintext)

if __name__ == "__main__":
    choice = int(input("Mau encrypt(0) / decrypt(1)?"))
    if(choice == 0):
        rf = open("plainteks.txt", "r")
        plain_text = rf.read()  
        print(plain_text)
        key = input("Kunci: ")
        
        v = ExtendedVigenere(key, plain_text)
        print(v.encrypt(key, plain_text))
        wf = open("cipherteks.txt", "w")
        wf.write(v.encrypt(key, plain_text))
    else:
        f = open("cipherteks.txt", "r")
        cipher_text = f.read()
        key = input("Kunci: ")
        
        v = ExtendedVigenere(key, cipher_text)
        print(v.decrypt(key, cipher_text))