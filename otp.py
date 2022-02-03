from pydoc import plain
import string    
import random

class OTP:
    def __init__(self, k, t):
        self.key = k
        self.text = t

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
        
        keyf = open("key.txt", "w")
        randomKey =  ''.join((random.choice(string.ascii_lowercase) for x in range(10000)))
        keyf.write(randomKey)
        keyf.close()
        
        o = OTP(randomKey, plain_text)
        
        wf = open("cipherteks.txt", "w")
        wf.write(o.encrypt(randomKey, plain_text))
        wf.close()
    else:
        f = open("cipherteks.txt", "r")
        cipher_text = f.read().replace(" ", "").lower()
        
        keyf = open("key.txt", "r")
        randomKey = keyf.read()
        
        o = OTP(randomKey, cipher_text)
        
        print(o.decrypt(randomKey, cipher_text))