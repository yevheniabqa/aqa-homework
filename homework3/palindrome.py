
def isPalindrome(word):

    rev = ''.join(reversed(word))

    if (word == rev):
        return True
    return False

word = input('Enter your word: ')
pali_word = isPalindrome(word)
 
if (pali_word):
    print("+")
else:
    print("-")
