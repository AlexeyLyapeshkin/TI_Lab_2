import time


# 10000000000000000000000000010 = [29,2] = 268435458
# 11010111111010111101011101110 = 452819694
# 11111111111111111111111111111 = 536870911

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

def Cipher(filename, int, poly):

    register = 452819694
    # register = 536870911
    mask = 268435458
    mask_obr = 536870911
    print(bin(mask), bin(register))
    b_arr = bytearray()
    file_out = open(filename+'.cph', 'wb')
    start_time = time.time()

    for b in bytes_from_file(filename):
        key_byte = 0
        i = 7
        while i >= 0:
            check = register & mask

            if register & 268435456 == 268435456:
                key_byte = key_byte ^ 2 ** i

            register = register << 1

            if check == 268435456 or check == 2:
                register = register ^ 1

            register = register & mask_obr

            i -= 1
        b_arr.append(b ^ key_byte)

    print("--- %s seconds ---" % (time.time() - start_time))
    file_out.write(b_arr)
    file_out.close()

def DeCipher(filename, int, poly):

    register = 452819694
    # register = 536870911
    mask = 268435458
    mask_obr = 536870911
    print(bin(mask), bin(register))
    b_arr = bytearray()
    file_out = open(filename, 'wb')
    start_time = time.time()

    for b in bytes_from_file(filename+'.cph'):
        key_byte = 0
        i = 7
        while i >= 0:
            check = register & mask

            if register & 268435456 == 268435456:
                key_byte = key_byte ^ 2 ** i

            register = register << 1

            if check == 268435456 or check == 2:
                register = register ^ 1

            register = register & mask_obr

            i -= 1
        b_arr.append(b ^ key_byte)

    print("--- %s seconds ---" % (time.time() - start_time))
    file_out.write(b_arr)
    file_out.close()
Cipher('1.mp4',1,1)
DeCipher('1.mp4',1,1)
#print(check,' ',key_byte)