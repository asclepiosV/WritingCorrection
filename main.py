
print("Enter the text to correct")

text = input().split()

with open('word.txt') as f:
    wordlist = f.read().splitlines()

i = 0





def exist(word):
    with open('word.txt') as f:
        wordlist = f.read().splitlines()
    if word in wordlist:
        check = 1
    else:
        check = 0
    return check


def correction(word):
    alphab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    prop = []
    check = 0
    count = 0
    j = 0
    k = 0
    wordsave = word
    lst = list(word)
    while j < len(lst):
        while k < len(alphab):
            lst[j] = alphab[k]
            word = ''.join(lst)
            check = exist(word)
            lst = list(wordsave)
            if check == 1:
                prop.append(word)
                count = 1
            k += 1
        j += 1
        k = 0

    if check == 0 and count == 0:
        word = 'undefined'
        prop.append(word)
    return prop



while i < len(text):
    check = exist(text[i])
    if check == 1 :
        print("\"" + text[i] + "\"" + " is correct")
    else:
        print("\"" + text[i] + "\"" + " is incorrect\n")
        prop = correction(text[i])

        print("You can use ")
        print(prop)
        print("instead of \"" + text[i] + "\"\n")
    i+=1

