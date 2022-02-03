# ! /usr/bin/python3
from sys import exit as sysExit
import sys
import random
import string

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QGridLayout, QDialog, QScrollArea, QScrollBar, QWidget, QPushButton, QLabel

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

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)
        self.vigenereButton.clicked.connect(self.moveToVigenere)
        self.vigenereExtendedButton.clicked.connect(self.moveToExtendedVigenere)
        self.otpButton.clicked.connect(self.moveToOTP)
        
    def moveToVigenere(self):
        vigenere = Vigenere()
        widget.addWidget(vigenere)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def moveToExtendedVigenere(self):
        extendedVigenere = ExtendedVigenere()
        widget.addWidget(extendedVigenere)
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