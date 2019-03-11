# XOR Encrypt Exercise

xor_encrypt(text, key)
xor_decrypt(secret text, key)

text="this is a sentence"
key="amsterdam"
encrypted = text ^ key

print(xor_encrypt)

plaintext = 92
key = 31

print(plaintext)

encrypted = plaintext ^ key
print(encrypted)

decrypted = encrypted ^ key

print(decrypted)

###

def func_one():
    print('running func_one')
    x = ord('a')

y= func_one
print(y) # look it just says that y is a function, that's not what we want

y = func_one() # now it runs func_one
print(y) # ok, now None, hmm what did we forget?

def func_two():
    print('running func_two')
    x = ord('a')
    return x # return the ord of a

y = func_two()
print(y) # success!