from pydoc import plain
import random

class Enigma:
    def __init__(self, k, t):
        self.key = k
        self.text = t
        self.rotor_1_1 = []
        self.rotor_1_2 = [22, 11, 24, 3, 5, 12, 26, 8, 4, 13, 20, 25, 9, 18, 21, 10, 1, 6, 15, 14, 7, 2, 23, 16, 19, 17]
        self.rotor_2_1 = []
        self.rotor_2_2 = [11, 15, 23, 21, 13, 9, 25, 2, 1, 19, 8, 24, 10, 12, 20, 16, 4, 18, 3, 5, 14, 6, 26, 17, 22, 7]
        self.rotor_3_1 = []
        self.rotor_3_2 = [21, 2, 23, 19, 8, 24, 7, 12, 20, 9, 3, 14, 18, 1, 15, 10, 16, 13, 11, 25, 22, 4, 26, 5, 17, 6]
        
        self.convertKey()
        self.setRotor()
        
    def setRotor(self):
        k1 = self.key_in_num[0]
        temp = k1
        for i in range(26):
            if(temp<=26):
                self.rotor_1_1.append(temp)
            else:
                temp-=26
                self.rotor_1_1.append(temp)
            temp+=1
            
        k2 = self.key_in_num[1]
        temp = k2
        for i in range(26):
            if(temp<=26):
                self.rotor_2_1.append(temp)
            else:
                temp-=26
                self.rotor_2_1.append(temp)
            temp+=1
            
        k3 = self.key_in_num[2]
        temp = k3
        for i in range(26):
            if(temp<=26):
                self.rotor_3_1.append(temp)
            else:
                temp-=26
                self.rotor_3_1.append(temp)
            temp+=1
    
    def alphabet_to_num(self, a):
        return ord(a)-96

    def num_to_alphabet(self, a):
        return chr(a+96)

    def convertKey(self):
        self.key_in_num = []
        for i in range(3):
            self.key_in_num.append((self.alphabet_to_num(self.key[i])))
            
    def encrypt(self):
        cipher_text = ""
        
        for i in range(len(self.text)):
            l = self.text[i]
            p0 = self.alphabet_to_num(l)
            nr1 = self.rotor_1_1[p0-1]
            for i in range(len(self.rotor_1_2)):
                if(self.rotor_1_2[i] == nr1):
                    p1 = i+1
            nr2 = self.rotor_2_1[p1-1]
            for i in range(len(self.rotor_2_2)):
                if(self.rotor_2_2[i] == nr2):
                    p2 = i+1
            nr3 = self.rotor_3_1[p2-1]
            for i in range(len(self.rotor_3_2)):
                if(self.rotor_3_2[i] == nr3):
                    p3 = i+1
            
            cipher_text = cipher_text + self.num_to_alphabet(p3)
            
            self.rotor_3_1 = self.rotor_3_1[-1:] + self.rotor_3_1[:-1]
            self.rotor_3_2 = self.rotor_3_2[-1:] + self.rotor_3_2[:-1]
            
            if(i%26 == 0):
                self.rotor_2_1 = self.rotor_2_1[-1:] + self.rotor_2_1[:-1]
                self.rotor_2_2 = self.rotor_2_2[-1:] + self.rotor_2_2[:-1]
            
            if(i%676 == 0):
                self.rotor_1_1 = self.rotor_1_1[-1:] + self.rotor_1_1[:-1]
                self.rotor_1_2 = self.rotor_1_2[-1:] + self.rotor_1_2[:-1]
        
        print(cipher_text)
        return cipher_text
    
    def decrypt(self):
        plain_text = ""
    
        for i in range(len(self.text)):
            self.rotor_3_1 = self.rotor_3_1[-1:] + self.rotor_3_1[:-1]
            self.rotor_3_2 = self.rotor_3_2[-1:] + self.rotor_3_2[:-1]
            
            if(i%26 == 0):
                self.rotor_2_1 = self.rotor_2_1[-1:] + self.rotor_2_1[:-1]
                self.rotor_2_2 = self.rotor_2_2[-1:] + self.rotor_2_2[:-1]
            
            if(i%676 == 0):
                self.rotor_1_1 = self.rotor_1_1[-1:] + self.rotor_1_1[:-1]
                self.rotor_1_2 = self.rotor_1_2[-1:] + self.rotor_1_2[:-1]
        
        for i in range(len(self.text)-1, -1, -1):
            self.rotor_3_1 = self.rotor_3_1[1:] + self.rotor_3_1[:1]
            self.rotor_3_2 = self.rotor_3_2[1:] + self.rotor_3_2[:1]
            
            if(i%26 == 0):
                self.rotor_2_1 = self.rotor_2_1[1:] + self.rotor_2_1[:1]
                self.rotor_2_2 = self.rotor_2_2[1:] + self.rotor_2_2[:1]
            
            if(i%676 == 0):
                self.rotor_1_1 = self.rotor_1_1[1:] + self.rotor_1_1[:1]
                self.rotor_1_2 = self.rotor_1_2[1:] + self.rotor_1_2[:1]
            
            l = self.text[i]
            p0 = self.alphabet_to_num(l)
            nr1 = self.rotor_3_1[p0-1]
            for i in range(len(self.rotor_1_2)):
                if(self.rotor_3_2[i] == nr1):
                    p1 = i+1
            nr2 = self.rotor_2_1[p1-1]
            for i in range(len(self.rotor_2_2)):
                if(self.rotor_2_2[i] == nr2):
                    p2 = i+1
            nr3 = self.rotor_1_1[p2-1]
            for i in range(len(self.rotor_3_2)):
                if(self.rotor_1_2[i] == nr3):
                    p3 = i+1
                    
            plain_text = plain_text + self.num_to_alphabet(p3)
            
        print(plain_text)
        return plain_text
                
if __name__ == "__main__":
    choice = int(input("Mau encrypt(0) / decrypt(1)?"))
    if(choice == 0):
        rf = open("plainteks.txt", "r")
        plain_text = rf.read().replace(" ", "").lower()
        plain_text = ''.join(filter(str.isalpha, plain_text))   
        key = input("Kunci: ").replace(" ", "").lower()
        key = ''.join(filter(str.isalpha, key))
        
        e = Enigma(key, plain_text)
        e.encrypt()
    else:
        f = open("cipherteks.txt", "r")
        cipher_text = f.read().replace(" ", "").lower()
        key = input("Kunci: ").lower()
        
        e = Enigma(key, cipher_text)
        e.decrypt()
        