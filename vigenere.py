from pydoc import plain

class Vigenere:
    def __init__(self, k, t):
        self.key = k
        self.text = t
    
    def full_key(self):
        full_key = self.key
        subtract = len(self.text)-len(full_key)
        
        if(subtract > 0):
            loop = len(self.text)//len(full_key)-1
            remainder = len(self.text)%len(full_key)
            for i in range(loop):
                for i in self.key:
                    full_key += i
            for i in range(remainder):
                full_key += self.key[i]
        return full_key

    def alphabet_to_num(self, a):
        return ord(a)-97

    def num_to_alphabet(self, a):
        return chr(a+97)

    def encrypt(self, k, p):
        cipher_text = ""
        for i in range(len(p)):
            if(ord(p[i]) >= 97 and ord(p[i]) <= 122):
                c = (self.alphabet_to_num(str(p[i]))+self.alphabet_to_num(str(k[i])))%26
                cipher_text+=self.num_to_alphabet(c).upper()
        return cipher_text
    
    def decrypt(self, k, c):
        plain_text = ""
        for i in range(len(c)):
            p = (self.alphabet_to_num(str(c[i].lower()))-self.alphabet_to_num(str(k[i])))%26
            plain_text+=self.num_to_alphabet(p).lower()
        return plain_text
        
if __name__ == "__main__":
    choice = int(input("Mau encrypt(0) / decrypt(1)?"))
    if(choice == 0):
        rf = open("plainteks.txt", "r")
        plain_text = rf.read().replace(" ", "").lower()
        plain_text = ''.join(filter(str.isalpha, plain_text))   
        print(plain_text)
        key = input("Kunci: ").lower()
        
        v = Vigenere(key, plain_text)
        print(v.encrypt(v.full_key(), plain_text))
        wf = open("cipherteks.txt", "w")
        wf.write(v.encrypt(v.full_key(), plain_text))
    else:
        f = open("cipherteks.txt", "r")
        cipher_text = f.read().replace(" ", "").lower()
        key = input("Kunci: ").lower()
        
        v = Vigenere(key, cipher_text)
        print(v.decrypt(v.full_key(), cipher_text))
        