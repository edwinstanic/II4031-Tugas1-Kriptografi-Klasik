class Enigma:
    def __init__(self, k, t):
        self.key = k
        self.text = t
        
if __name__ == "__main__":
    choice = int(input("Mau encrypt(0) / decrypt(1)?"))
    if(choice == 0):
        rf = open("plainteks.txt", "r")
        plain_text = rf.read().replace(" ", "").lower()
        plain_text = ''.join(filter(str.isalpha, plain_text))   
        print(plain_text)
        key = input("Kunci: ").lower()
    else:
        f = open("cipherteks.txt", "r")
        cipher_text = f.read().replace(" ", "").lower()
        key = input("Kunci: ").lower()