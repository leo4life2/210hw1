def vigenere_encrypt(plain, key):
    """
    :param plain: String -- a python input string. The plain text.
    :param key: String -- a python input string. The key.

    :return: String -- the cipher python string text.
    """
    # To do
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabets_to_index = {}
    index_to_alphabets = {}

    for i, alphabet in enumerate(alphabets):
        alphabets_to_index[alphabet] = i
        index_to_alphabets[i] = alphabet

    #pad key
    if len(key) < len(plain):
        key *= len(plain)//len(key) + 1
        diff = len(plain) - len(key)
        key = key[:diff]

    result = []
    for c_p, c_k in zip(plain, key):
        shift = alphabets_to_index[c_p] # index of plaintext is shift
        key_index = alphabets_to_index[c_k]

        target_index = (key_index + shift) % 26
        ciphered_letter = index_to_alphabets[target_index]
        result.append(ciphered_letter)

    return ''.join(result)

def vigenere_decrypt(cipher, key):
    '''
    :param cipher: String -- a python input string. The cipher text.
    :param key: String -- a python input string. The key.

    :return: String -- the plain python string text.
    '''
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabets_to_index = {}
    index_to_alphabets = {}

    for i, alphabet in enumerate(alphabets):
        alphabets_to_index[alphabet] = i
        index_to_alphabets[i] = alphabet

    #pad key
    if len(key) < len(cipher):
        key *= len(cipher)//len(key) + 1
        diff = len(cipher) - len(key)
        key = key[:diff]

    result = []

    for c_c, c_k in zip(cipher, key):
        shift = alphabets_to_index[c_k] # index of key is shift
        cipher_index = alphabets_to_index[c_c]

        target_index = (cipher_index - shift) % 26
        deciphered_letter = index_to_alphabets[target_index]
        result.append(deciphered_letter)

    return ''.join(result)



'''
note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

# def main():
#     print(vigenere_encrypt("ATTACKATDAWN", "NYUSH"))   # NRNSJXYNVHJL
#
#     print(vigenere_encrypt("DATASTRUCTURE", "NYUSH"))   # QYNSZGPOUAHPY
#
#     print(vigenere_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLSEBAQXJGFVCOLKAHTQPFM
#
#     print(vigenere_encrypt("CUTE", "NYUSH"))  # PSNW
#
#     print(vigenere_decrypt("NRNSJXYNVHJL", "NYUSH"))   # ATTACKATDAWN
#     print(vigenere_decrypt("QYNSZGPOUAHPY", "NYUSH"))   # DATASTRUCTURE
#     print(vigenere_decrypt("NZWVLSEBAQXJGFVCOLKAHTQPFM", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
#     print(vigenere_decrypt("PSNW", "NYUSH"))  # CUTE
#
# if __name__ == '__main__':
#     main()
