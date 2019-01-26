def LFSR(data, iv):
    fback = 0x12345678
    temp = iv & 0xFF
    for i in data:
        lsb = 1 & temp
        if (lsb == 1):
            iv = ((iv >> 1) ^ fback)
        if lsb:
            iv >>= 1
        yield i ^ temp


def Crypt(data, iv):
    return bytes(LFSR(data, iv))


print(Crypt(b'apple', 0x12345678))
temp = Crypt(b'apple', 0x12345678)
print(Crypt(temp, 0x12345678))
print(Crypt(b'cheese', 0x12345678))
temp = Crypt(b'cheese', 0x12345678)
print(Crypt(temp, 0x12345678))
print(Crypt(b'almond', 0x12345678))
temp = Crypt(b'almond', 0x12345678)
print(Crypt(temp, 0x12345678))
print(Crypt(b'grapes', 0x12345678))
temp = Crypt(b'grapes', 0x12345678)
print(Crypt(temp, 0x12345678))
