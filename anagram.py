WORDSLIST = "words.txt"


def readfile(wordlist):
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDSLIST, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


class Anagram:
    def __init__(self, phrase):
        self.phrase = phrase

    def check_phrase(self):
        wordslist = readfile(WORDSLIST)
        word_list = []
        word_reverse = self.phrase[::-1]
        print(word_reverse)
        for word in wordslist:
            if sorted(self.phrase) == sorted(word):
                word_list.append(word)
                for w in wordslist:
                    if w == word_reverse:
                        print(w)
                    return w


def main():
    readfile(WORDSLIST)
    word = input("Enter word")
    a = Anagram(word)
    a.check_phrase()


if __name__ == "__main__":
    main()
