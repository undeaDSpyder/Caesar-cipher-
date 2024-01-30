import ascii
sometext = input("Please type your text to encrypt: ")
key = input("Please type your key: ")
key = int(key)


def rot_x(realtext, step):
    result = ""
    letters_array = [chr(i) for i in range(256)]

    for eachLetter in realtext:
        index = letters_array.index(eachLetter)
        newIndex = index + step
        if (newIndex > len(letters_array)):
            newIndex = newIndex - (len(letters_array-1))
            newLetter = letters_array[newIndex]
        else:
            newLetter = letters_array[newIndex]
        result += newLetter
    print(result)

rot_x(sometext, key)
