def Crypt(data, iv):
    for i in data:
        fback = 0x87654321
        lsb = 1 & iv
        if (lsb == 1):
            iv = ((iv >> 1) ^ fback)
        if lsb:
            iv >>= 1
        yield i ^ iv


print(bytes(Crypt(b'apple', 0x78)))
temp = bytes(Crypt(b'apple', 0x78))
print(bytes(Crypt(temp, 0x78)))
