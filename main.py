# ! /usr/bin/python3
from sys import exit as sysExit
import sys
import random
import string

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget

class Vigenere(QtWidgets.QMainWindow):
    def __init__(self):
        super(Vigenere, self).__init__()
        loadUi("vigenere.ui", self)
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.clicked.connect(self.setEncrypt)
        self.decryptButton.clicked.connect(self.setDecrypt)
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.backToMain)
        
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
    
    def generate(self):
        self.key = self.key_input.toPlainText().replace(" ", "").lower()
        self.key = ''.join(filter(str.isalpha, self.key))
        self.text = self.text_input.toPlainText().replace(" ", "").lower()
        self.text = ''.join(filter(str.isalpha, self.text))

        if(self.isEncrypt):
            self.results.setText(self.encrypt(self.key, self.text))
        else:
            self.results.setText(self.decrypt(self.key, self.text))
    
    def setEncrypt(self):
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Plainteks")
        self.resultText.setText("Cipherteks :")
        self.generateButton.setText("Enkripsi Pesan")
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.decryptButton.setStyleSheet("background-color: none")
    
    def setDecrypt(self):
        rf = open("cipherteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Cipherteks")
        self.resultText.setText("Plainteks :")
        self.generateButton.setText("Dekripsi Pesan")
        self.isEncrypt = False
        self.decryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.setStyleSheet("background-color: none")
    
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
        k = self.full_key()
        for i in range(len(p)):
            if(ord(p[i]) >= 97 and ord(p[i]) <= 122):
                c = (self.alphabet_to_num(str(p)[i])+self.alphabet_to_num(str(k)[i]))%26
                cipher_text+=self.num_to_alphabet(c).upper()
        
        wf = open("cipherteks.txt", "w")
        wf.write(cipher_text)
        
        return cipher_text
    
    def decrypt(self, k, c):
        plain_text = ""
        k = self.full_key()
        for i in range(len(c)):
            p = (self.alphabet_to_num(str(c)[i].lower())-self.alphabet_to_num(str(k)[i]))%26
            plain_text+=self.num_to_alphabet(p).lower()
        return plain_text
    
    def backToMain(self):
        main = Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ExtendedVigenere(QtWidgets.QMainWindow):
    def __init__(self):
        super(ExtendedVigenere, self).__init__()
        loadUi("extendedvigenere.ui", self)
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.clicked.connect(self.setEncrypt)
        self.decryptButton.clicked.connect(self.setDecrypt)
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.backToMain)
        
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
    
    def generate(self):
        self.key = self.key_input.toPlainText()
        self.text = self.text_input.toPlainText()

        if(self.isEncrypt):
            self.results.setText(self.encrypt(self.key, self.text))
        else:
            self.results.setText(self.decrypt(self.key, self.text))
    
    def setEncrypt(self):
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Plainteks")
        self.resultText.setText("Cipherteks :")
        self.generateButton.setText("Enkripsi Pesan")
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.decryptButton.setStyleSheet("background-color: none")
    
    def setDecrypt(self):
        rf = open("cipherteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Cipherteks")
        self.resultText.setText("Plainteks :")
        self.generateButton.setText("Dekripsi Pesan")
        self.isEncrypt = False
        self.decryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.setStyleSheet("background-color: none")
    
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

    def backToMain(self):
        main = Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Fairplay(QtWidgets.QMainWindow):
    def __init__(self):
        super(Fairplay, self).__init__()
        loadUi("fairplay.ui", self)
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.clicked.connect(self.setEncrypt)
        self.decryptButton.clicked.connect(self.setDecrypt)
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.backToMain)
        
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
    
    def generate(self):
        self.key = self.key_input.toPlainText().replace(" ", "").upper()
        self.key = ''.join(filter(str.isalpha, self.key))
        self.text = self.text_input.toPlainText().replace(" ", "").upper()
        self.text = ''.join(filter(str.isalpha, self.text))

        if(self.isEncrypt):
            self.results.setText(self.encrypt(self.key, self.text))
        else:
            self.results.setText(self.decrypt(self.key, self.text))
    
    def setEncrypt(self):
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Plainteks")
        self.resultText.setText("Cipherteks :")
        self.generateButton.setText("Enkripsi Pesan")
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.decryptButton.setStyleSheet("background-color: none")
    
    def setDecrypt(self):
        rf = open("cipherteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Cipherteks")
        self.resultText.setText("Plainteks :")
        self.generateButton.setText("Dekripsi Pesan")
        self.isEncrypt = False
        self.decryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.setStyleSheet("background-color: none")
    
    def generateKey(self, k, arr):
        finalKey = []
        # Menghilangkan huruf berulang dan huruf 'J'
        for char in k:
            if char not in finalKey:
                if char != "J":
                    # Asumsi menghilangkan huruf 'J' pada key
                    finalKey.append(char)
        
        # Menambahkan huruf yang belum ada
        for i in range (65,91):
            if chr(i) not in finalKey:
                if i != 74:
                    finalKey.append(chr(i))

        # Memasukkan key ke bujursangkar 5x5
        k = 0
        for i in range (5):
            for j in range(5):
                arr[i][j] = finalKey[k]
                k += 1

        return ''.join(finalKey)

    def replaceJ(self, p):
        p.replace("J", "I")

    def keyIdx(self, c, arr):
        loc = []
        for i in range(5):
            for j in range(5):
                if arr[i][j] == c:
                    loc.append(i)
                    loc.append(j)
        return loc
        
    def encrypt(self, k, p):
        ciphertext = []
        keyArr = [[" " for i in range(5)] for j in range(5)]
        modifiedKey = self.generateKey(k, keyArr)

        # Menyisipkan huruf "X" untuk pasangan huruf yang sama
        for i in range(0,len(p)+1,2):
            if i < len(p)-1:
                if p[i] == p [i+1]:
                    p = p[:i+1] + "X" + p[i+1:]
        
        if len(p) % 2 != 0:
            p = p + "X"
        
        for i in range(0,len(p)+1,2):
            if i < len(p)-1:
                loc1 = self.keyIdx(p[i], keyArr)
                loc2 = self.keyIdx(p[i+1], keyArr)

                # Kondisi 1 - Kunci berada pada baris yang sama
                if loc1[0] == loc2[0]:
                    ciphertext.append(keyArr[loc1[0]][(loc1[1]+1) % 5])
                    ciphertext.append(keyArr[loc2[0]][(loc2[1]+1) % 5])

                # Kondisi 2 - Kunci berada pada kolom yang sama
                elif loc1[1] == loc2[1]:
                    ciphertext.append(keyArr[(loc1[0]+1) % 5][loc1[1]])
                    ciphertext.append(keyArr[(loc2[0]+1) % 5][loc2[1]])

                # Kondisi 3 - Kunci tidak berada pada baris dan kolom yang sama
                else:
                    ciphertext.append(keyArr[loc1[0]][loc2[1]])
                    ciphertext.append(keyArr[loc2[0]][loc1[1]])
        
        return ''.join(ciphertext)
    
    def decrypt(self, k, c):
        plaintext = []
        keyArr = [[" " for i in range(5)] for j in range(5)]
        modifiedKey = self.generateKey(k, keyArr)

        for i in range(0,len(c)+1,2):
            if i < len(c)-1:
                loc1 = self.keyIdx(c[i], keyArr)
                loc2 = self.keyIdx(c[i+1], keyArr)

                # Kondisi 1 - Kunci berada pada baris yang sama
                if loc1[0] == loc2[0]:
                    plaintext.append(keyArr[loc1[0]][(loc1[1]-1) % 5])
                    plaintext.append(keyArr[loc2[0]][(loc2[1]-1) % 5])

                # Kondisi 2 - Kunci berada pada kolom yang sama
                elif loc1[1] == loc2[1]:
                    plaintext.append(keyArr[(loc1[0]-1) % 5][loc1[1]])
                    plaintext.append(keyArr[(loc2[0]-1) % 5][loc2[1]])

                # Kondisi 3 - Kunci tidak berada pada baris dan kolom yang sama
                else:
                    plaintext.append(keyArr[loc1[0]][loc2[1]])
                    plaintext.append(keyArr[loc2[0]][loc1[1]])
        
        return ''.join(plaintext)
    
    def backToMain(self):
        main = Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class OTP(QtWidgets.QMainWindow):
    def __init__(self):
        super(OTP, self).__init__()
        loadUi("otp.ui", self)
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.clicked.connect(self.setEncrypt)
        self.decryptButton.clicked.connect(self.setDecrypt)
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.backToMain)
        
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        
        keyf = open("key.txt", "w")
        self.randomKey =  ''.join((random.choice(string.ascii_lowercase) for x in range(10000)))
        keyf.write(self.randomKey)
        keyf.close()
        
        self.key_input.setText(self.randomKey)
    
    def generate(self):
        self.key = self.key_input.toPlainText()
        self.text = self.text_input.toPlainText().replace(" ", "").lower()
        self.text = ''.join(filter(str.isalpha, self.text))

        if(self.isEncrypt):
            self.results.setText(self.encrypt(self.key, self.text))
        else:
            self.results.setText(self.decrypt(self.key, self.text))
    
    def setEncrypt(self):
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        
        self.text_label.setText("Plainteks")
        self.resultText.setText("Cipherteks :")
        self.generateButton.setText("Enkripsi Pesan")
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.decryptButton.setStyleSheet("background-color: none")
    
    def setDecrypt(self):
        rf = open("cipherteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        
        self.text_label.setText("Cipherteks")
        self.resultText.setText("Plainteks :")
        self.generateButton.setText("Dekripsi Pesan")
        self.isEncrypt = False
        self.decryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.setStyleSheet("background-color: none")

    def alphabet_to_num(self, a):
        return ord(a)-97

    def num_to_alphabet(self, a):
        return chr(a+97)

    def encrypt(self, k, p):
        cipher_text = ""
        for i in range(len(p)):
            if(ord(p[i]) >= 97 and ord(p[i]) <= 122):
                c = (self.alphabet_to_num(str(p)[i])+self.alphabet_to_num(str(k)[i]))%26
                cipher_text+=self.num_to_alphabet(c).upper()
        
        wf = open("cipherteks.txt", "w")
        wf.write(cipher_text)
        
        return cipher_text
    
    def decrypt(self, k, c):
        plain_text = ""
        for i in range(len(c)):
            p = (self.alphabet_to_num(str(c)[i].lower())-self.alphabet_to_num(str(k)[i]))%26
            plain_text+=self.num_to_alphabet(p).lower()
        return plain_text
    
    def backToMain(self):
        main = Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Enigma(QtWidgets.QMainWindow):
    def __init__(self):
        super(Enigma, self).__init__()
        loadUi("enigma.ui", self)
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.clicked.connect(self.setEncrypt)
        self.decryptButton.clicked.connect(self.setDecrypt)
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.backToMain)
        
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
    
    def convertKey(self):
        self.key_in_num = []
        for i in range(3):
            self.key_in_num.append((self.alphabet_to_num(self.key[i])))
    
    def setRotor(self):
        self.rotor_1_1 = []
        self.rotor_1_2 = [22, 11, 24, 3, 5, 12, 26, 8, 4, 13, 20, 25, 9, 18, 21, 10, 1, 6, 15, 14, 7, 2, 23, 16, 19, 17]
        self.rotor_2_1 = []
        self.rotor_2_2 = [11, 15, 23, 21, 13, 9, 25, 2, 1, 19, 8, 24, 10, 12, 20, 16, 4, 18, 3, 5, 14, 6, 26, 17, 22, 7]
        self.rotor_3_1 = []
        self.rotor_3_2 = [21, 2, 23, 19, 8, 24, 7, 12, 20, 9, 3, 14, 18, 1, 15, 10, 16, 13, 11, 25, 22, 4, 26, 5, 17, 6]
        
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
    
    def generate(self):
        self.key = self.key_input.toPlainText()
        self.text = self.text_input.toPlainText().replace(" ", "").lower()
        self.text = ''.join(filter(str.isalpha, self.text))
        self.convertKey()
        self.setRotor()

        if(self.isEncrypt):
            self.results.setText(self.encrypt())
        else:
            self.results.setText(self.decrypt())
        
        self.setRotor()
    
    def setEncrypt(self):
        rf = open("plainteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Plainteks")
        self.resultText.setText("Cipherteks :")
        self.generateButton.setText("Enkripsi Pesan")
        self.isEncrypt = True
        self.encryptButton.setStyleSheet("background-color: yellow")
        self.decryptButton.setStyleSheet("background-color: none")
    
    def setDecrypt(self):
        rf = open("cipherteks.txt", "r")
        self.text = rf.read()
        self.text_input.setText(self.text)
        self.results.setText("")
        self.key_input.setText("")
        
        self.text_label.setText("Cipherteks")
        self.resultText.setText("Plainteks :")
        self.generateButton.setText("Dekripsi Pesan")
        self.isEncrypt = False
        self.decryptButton.setStyleSheet("background-color: yellow")
        self.encryptButton.setStyleSheet("background-color: none")

    def alphabet_to_num(self, a):
        return ord(a)-96

    def num_to_alphabet(self, a):
        return chr(a+96)

    def encrypt(self):
        cipher_text = ""
        
        for i in range(len(self.text)):
            
            l = self.text[i]
            p0 = self.alphabet_to_num(l)
            nr1 = self.rotor_1_1[p0-1]
            for j in range(len(self.rotor_1_2)):
                if(self.rotor_1_2[j] == nr1):
                    p1 = j+1
            nr2 = self.rotor_2_1[p1-1]
            for j in range(len(self.rotor_2_2)):
                if(self.rotor_2_2[j] == nr2):
                    p2 = j+1
            nr3 = self.rotor_3_1[p2-1]
            for k in range(len(self.rotor_3_2)):
                if(self.rotor_3_2[k] == nr3):
                    p3 = k+1
            
            cipher_text = cipher_text + self.num_to_alphabet(p3)
            
            self.rotor_3_1 = self.rotor_3_1[-1:] + self.rotor_3_1[:-1]
            self.rotor_3_2 = self.rotor_3_2[-1:] + self.rotor_3_2[:-1]
            
            if(i!=0 and i%25 == 0):
                self.rotor_2_1 = self.rotor_2_1[-1:] + self.rotor_2_1[:-1]
                self.rotor_2_2 = self.rotor_2_2[-1:] + self.rotor_2_2[:-1]
            
            if( i!=0 and i%675 == 0):
                self.rotor_1_1 = self.rotor_1_1[-1:] + self.rotor_1_1[:-1]
                self.rotor_1_2 = self.rotor_1_2[-1:] + self.rotor_1_2[:-1]
        
        wf = open("cipherteks.txt", "w")
        wf.write(cipher_text)
        
        return cipher_text
    
    def decrypt(self):
        plain_text = ""
    
        for i in range(len(self.text)):
            self.rotor_3_1 = self.rotor_3_1[-1:] + self.rotor_3_1[:-1]
            self.rotor_3_2 = self.rotor_3_2[-1:] + self.rotor_3_2[:-1]
            
            if(i!=0 and i%25 == 0):
                self.rotor_2_1 = self.rotor_2_1[-1:] + self.rotor_2_1[:-1]
                self.rotor_2_2 = self.rotor_2_2[-1:] + self.rotor_2_2[:-1]
            
            if(i!=0 and i%675 == 0):
                self.rotor_1_1 = self.rotor_1_1[-1:] + self.rotor_1_1[:-1]
                self.rotor_1_2 = self.rotor_1_2[-1:] + self.rotor_1_2[:-1]
        
        for i in range(len(self.text)-1, -1, -1):
            self.rotor_3_1 = self.rotor_3_1[1:] + self.rotor_3_1[:1]
            self.rotor_3_2 = self.rotor_3_2[1:] + self.rotor_3_2[:1]
            
            if(i!=0 and i%25 == 0):
                self.rotor_2_1 = self.rotor_2_1[1:] + self.rotor_2_1[:1]
                self.rotor_2_2 = self.rotor_2_2[1:] + self.rotor_2_2[:1]
            
            if(i!=0 and i%675 == 0):
                self.rotor_1_1 = self.rotor_1_1[1:] + self.rotor_1_1[:1]
                self.rotor_1_2 = self.rotor_1_2[1:] + self.rotor_1_2[:1]
            
            l = self.text[i]
            p0 = self.alphabet_to_num(l)
            nr1 = self.rotor_3_2[p0-1]
            for i in range(len(self.rotor_3_1)):
                if(self.rotor_3_1[i] == nr1):
                    p1 = i+1
            nr2 = self.rotor_2_2[p1-1]
            for i in range(len(self.rotor_2_1)):
                if(self.rotor_2_1[i] == nr2):
                    p2 = i+1
            nr3 = self.rotor_1_2[p2-1]
            for i in range(len(self.rotor_1_1)):
                if(self.rotor_1_1[i] == nr3):
                    p3 = i+1
                    
            plain_text = self.num_to_alphabet(p3) + plain_text
            
        return plain_text
    
    def backToMain(self):
        main = Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)
        self.vigenereButton.clicked.connect(self.moveToVigenere)
        self.vigenereExtendedButton.clicked.connect(self.moveToExtendedVigenere)
        self.playfairButton.clicked.connect(self.moveToFairplay)
        self.enigmaButton.clicked.connect(self.moveToEnigma)
        self.otpButton.clicked.connect(self.moveToOTP)
        
    def moveToVigenere(self):
        vigenere = Vigenere()
        widget.addWidget(vigenere)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def moveToExtendedVigenere(self):
        extendedVigenere = ExtendedVigenere()
        widget.addWidget(extendedVigenere)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def moveToFairplay(self):
        fairplay = Fairplay()
        widget.addWidget(fairplay)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def moveToEnigma(self):
        enigma = Enigma()
        widget.addWidget(enigma)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def moveToOTP(self):
        otp = OTP()
        widget.addWidget(otp)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    
    widget = QStackedWidget()
    widget.addWidget(main)
    widget.setMinimumHeight(1080)
    widget.setMinimumWidth(1920)

    widget.show()
    
    sys.exit(app.exec_())