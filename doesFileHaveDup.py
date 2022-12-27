def doesFileHaveDup(filename):
    file = open(filename)
    content = str(file.read())
    wordlist = content.split()

    dict = {}

    for word in wordlist:
        value = dict.get(word, -1)
        if (value != -1):
            return True
        else:
            dict[word] = 1

    return False

if __name__ == "__main__":
    print(doesFileHaveDup("test_dup.txt"))
    print(doesFileHaveDup("test_nodup.txt"))