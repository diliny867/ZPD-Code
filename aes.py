#lookup table
sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

#inverse lookup table
invsbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

#process state, using sbox lookup table
def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = sbox[state[i][j]]

#reverse process state, using invsbox lookup table
def inv_sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = invsbox[state[i][j]]

#shift state rows
def shift_rows(row):
    row[0][1], row[1][1], row[2][1], row[3][1] = row[1][1], row[2][1], row[3][1], row[0][1]
    row[0][2], row[1][2], row[2][2], row[3][2] = row[2][2], row[3][2], row[0][2], row[1][2]
    row[0][3], row[1][3], row[2][3], row[3][3] = row[3][3], row[0][3], row[1][3], row[2][3]

#inverse shift state rows
def inv_shift_rows(row):
    row[0][1], row[1][1], row[2][1], row[3][1] = row[3][1], row[0][1], row[1][1], row[2][1]
    row[0][2], row[1][2], row[2][2], row[3][2] = row[2][2], row[3][2], row[0][2], row[1][2]
    row[0][3], row[1][3], row[2][3], row[3][3] = row[1][3], row[2][3], row[3][3], row[0][3]

#get state round key
def add_round_key(state, k):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= k[i][j]

#permutes column byte
xtime = lambda x: (((x << 1) ^ 27) & 255) if (x & 128) else (x << 1)

#mix single state column
def mix_single_column(col):
    t = col[0] ^ col[1] ^ col[2] ^ col[3]
    u = col[0]
    col[0] ^= t ^ xtime(col[0] ^ col[1])
    col[1] ^= t ^ xtime(col[1] ^ col[2])
    col[2] ^= t ^ xtime(col[2] ^ col[3])
    col[3] ^= t ^ xtime(col[3] ^ u)

#mix states column bytes
def mix_columns(col):
    for i in range(4):
        mix_single_column(col[i])

#reverse mix states column bytes
def inv_mix_columns(col):
    for i in range(4):
        u = xtime(xtime(col[i][0] ^ col[i][2]))
        v = xtime(xtime(col[i][1] ^ col[i][3]))
        col[i][0] ^= u
        col[i][1] ^= v
        col[i][2] ^= u
        col[i][3] ^= v
    mix_columns(col)

#lookup table
rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

#convert bytes array to matrix
def bytes2matrix(text):
    out =[]
    for i in range(0, len(text), 4):
        out.append(list(text[i:i + 4]))
    return out

#convert matrix to bytes array
def matrix2bytes(matrix):
    out = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            out.append(matrix[i][j])
    return bytes(out)

#xor bytes of a with b
def xor_bytes(a, b):
    out = []
    for i in range(len(a)):
        out.append(a[i]^b[i])
    return bytes(out)

#increase all bytes in byte array
def inc_bytes(a):
    out = list(a)
    for i in reversed(range(len(out))):
        if out[i] == 255:
            out[i] = 0
        else:
            out[i] += 1
            break
    return bytes(out)

#split text to blocks (with length 16)
def split_blocks(text, block_size=16):
    out = []
    for i in range(0, len(text), block_size):
        out.append(text[i:i + 16])
    return out
from memory_profiler import profile
#AES class
class AES:
    #initialize AES class
    def __init__(self, key):
        self.rounds = 10 #10 rounds if key = 128 bit
        self.key_matrices = self.expand_key(key)

    #calculate a list of key matrices for given key
    def expand_key(self, key):
        key_columns = bytes2matrix(key) #transform key to matrix
        iteration_size = len(key) // 4 #get iteration size
        i = 1
        while len(key_columns) < (self.rounds + 1) * 4: #generate key for each round
            word = list(key_columns[-1]) #copy previous word
            if len(key_columns) % iteration_size == 0: #perform operation for each row
                word.append(word.pop(0)) #circular shift of word[]
                word = [sbox[b] for b in word] #calculate word from sbox
                word[0] ^= rcon[i]
                i += 1
            word = xor_bytes(word, key_columns[-iteration_size]) #xor with word from previous iteration
            key_columns.append(word)
        out = []
        for i in range(len(key_columns) // 4): #fill out list with generated keys
            out.append(key_columns[4*i : 4*(i+1)])
        return out

    #calculates plaintexts blocks bytes to xor it to
    def encrypt_block(self, plaintext):
        plain_state = bytes2matrix(plaintext)
        add_round_key(plain_state, self.key_matrices[0])
        for i in range(1, self.rounds):#state transformation procedure
            sub_bytes(plain_state)
            shift_rows(plain_state)
            mix_columns(plain_state)
            add_round_key(plain_state, self.key_matrices[i])
        sub_bytes(plain_state)#last round of transformation is a bit different
        shift_rows(plain_state)
        add_round_key(plain_state, self.key_matrices[-1])
        return matrix2bytes(plain_state)

    #encrypt text
    @profile
    def encrypt_ctr(self, plaintext, iv):
        blocks = []
        salt = iv
        for plaintext_block in split_blocks(plaintext):#splits text to blocks
            block = xor_bytes(plaintext_block, self.encrypt_block(salt))#permutes block by currently calculated salt
            blocks.append(block)
            salt = inc_bytes(salt)
        return b''.join(blocks)

    #decrypt text
    @profile
    def decrypt_ctr(self, ciphertext, iv):
        blocks = []
        salt = iv
        for ciphertext_block in split_blocks(ciphertext):#splits encrypted text to blocks
            block = xor_bytes(ciphertext_block, self.encrypt_block(salt))#permutes block by currently calculated salt
            blocks.append(block)
            salt = inc_bytes(salt)
        return b''.join(blocks)
