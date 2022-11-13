from string import ascii_lowercase as alpha

def encrypt(text:str ) -> str:
    ls = []
    for letter in text:
        ls.append(alpha[alpha.index(letter) + 3])
    encrypted_text = ''.join(ls)
    return encrypted_text

def decrypt(text:str ) -> str:
    ls = []
    for letter in text:
        ls.append(alpha[alpha.index(letter) - 3])
    encrypted_text = ''.join(ls)
    return encrypted_text


print(encrypt('abc'))
print(decrypt('def'))