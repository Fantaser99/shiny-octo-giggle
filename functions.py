import itertools
import time


def prime_factors(n):
    res = []
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            res.append(i)
    return res

# prime_factors(1234567890123456789012345678901234567890)
# [2, 3, 3, 5, 73, 101, 137, 3541, 3607, 3803, 27961, 1676321, 5964848081]

def queens():
    res = []
    
    
    def add_new(positions=[]):
        """
        positions[i] = x of the queen in row number i
        """
        if len(positions) == 8:
            res.append(positions[:])
            return
        for x in range(8):
            y = len(positions)
            flag = True
            for y1 in range(len(positions)):
                if x == positions[y1]:
                    flag = False
                if abs(x - positions[y1]) == y - y1:
                    flag = False
            if flag:
                positions.append(x)
                add_new(positions=positions)
                positions.pop()
    
    
    add_new()
    for position in res:
        for y in range(8):
            x = position[y]
            s = ["."] * 8
            s[x] = "Q"
            print(*s)
        print()


def analyze(filename):
    alphabet = set([chr(i) for i in range(ord('а'), ord('я') + 1)])
    f = open(filename)
    freq = {}
    s = 0
    for c in alphabet:
        freq[c] = 0
    for line in f:
        for c in line.strip().lower():
            if c in alphabet:
                freq[c] += 1
                s += 1
    f.close()
    return freq, s

def frequencies(filename):
    alphabet, s = analyze(filename)
    for c in sorted(alphabet.keys()):
        print("{}: {}%".format(c, int(alphabet[c] / s * 10000) / 100))


def decipher(txtfile, encfile):
    data_txt = analyze(txtfile)
    data_enc = analyze(encfile)
    
    stats_txt = list(data_txt[0].keys())
    stats_txt.sort(key=lambda x: data_txt[0][x])
    
    stats_enc = list(data_enc[0].keys())
    stats_enc.sort(key=lambda x: data_enc[0][x])
    
    enc_file_descriptor = open(encfile)
    enc_text = enc_file_descriptor.read()
    enc_file_descriptor.close()
    
    decrypted_text = ""
    
    for char in enc_text:
        if char in stats_enc:
            decrypted_text += stats_txt[stats_enc.index(char)]
        else:
            decrypted_text += char
    
    print(decrypted_text)


