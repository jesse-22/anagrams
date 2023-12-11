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
            else:
                print("No anagram can be made")

    @staticmethod
    def get_list_anagrams(wordlist, phrase):
        word_list = []
        phrase_len = len_phrase = len(phrase)
        chosen_words = []
        counter = 0
        for word in wordlist:
            for word_in_phrase in phrase:
                if sorted(word_in_phrase) == sorted(word):
                    word_list.append(word)
        print(','.join(word_list))

        while counter in range(phrase_len):
            chosen_word = input("Which word would you like to select?")
            chosen_words.append(chosen_word)
            word_list.remove(chosen_word)
            counter += 1
            if counter < phrase_len:
                print(' '.join(word_list))
        print(' '.join(chosen_words))


def main():
    word_list = readfile(WORDSLIST)

    word = input("Enter a phrase separated by a space")
    phrase_input = word.split()
    a = Anagram([phrase_input])
    a.get_list_anagrams(word_list, phrase_input)


if __name__ == "__main__":
    main()
