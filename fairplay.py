class Fairplay:
    def __init__(self, k, t):
        self.key = k
        self.text = t
    
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

# fairplay = Fairplay("JALANGANESHASEPULUH", "TEMUIIBUNANTIMALAM")
# fairplay.key.replace(" ", "").upper()
# fairplay.text.replace(" ", "").upper()
# print(fairplay.encrypt(fairplay.key, fairplay.text))
# print(fairplay.decrypt("JALANGANESHASEPULUH", "ZBRSFYKUPGLGRKVSNLQV"))