def anagram(string1, string2):
    """
    :param string1: String -- the first python string.
    :param string2: String -- the second python string.

    :return: True if string1 is anagram of string2
             False otherwise.
    """
    string1, string2 = string1.replace(" ", ""), string2.replace(" ", "")
    #same # of each letter = anagram

    letters = {}

    for c in string1:
        if letters.get(c, None) is None:
            letters[c] = 1
            continue
        letters[c] += 1

    for c in string2:
        if letters.get(c, None) is None:
            return False
        letters[c] -= 1

    return all(c == 0 for c in letters.values())


'''
note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
#
# def main():
#     string1 = "william shakespeare"
#     string2 = "i am a weakish speller"
#     print(anagram(string1, string2))
#
#     string1 = "software"
#     string2 = "swear oft"
#     print(anagram(string1, string2))
#
# if __name__ == '__main__':
#     main()
