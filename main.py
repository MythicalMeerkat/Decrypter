# This program will take two headers, XOR them, and convert the result to little endian
# Group 16 (Jeff, Tyler, Mason, Dustin)


def little(str_x):
    t = bytearray.fromhex(str_x)
    t.reverse()
    return ''.join(format(x,'02x') for x in t).upper()


unencrypted_header = input("Enter the unencrypted Header (HEX): ")
encrypted_header = input("Enter the encrypted Header (HEX): ")

xored = hex(int(unencrypted_header, 16) ^ int(encrypted_header, 16))[2:]
xored_filled = xored.zfill(16)

xored_little = little(xored_filled)
print("Key: ")
print(xored_little)











