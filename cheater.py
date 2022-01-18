import re

class Cheater:
    def __init__(self, wordlist: list, num_chars: int):
        self.wordlist = wordlist
        self.curr_wordlist = wordlist
        self.guesses = {}
        self.num_chars = num_chars

    def get_result(self):
        while True:
            word = input("Enter every letter color: ")
            for char in word:
                if char not in ["g", "b", "y"]:
                    print("Not a valid option try again")
                    break
            else:
                return word

    def generate_guess(self):
        # Do freq analysis
        frequencies = {num: {} for num in range(self.num_chars)}
        for word in self.wordlist:
            for char in frequencies:
                if word[char] in frequencies[char]:
                    frequencies[char][word[char]] += 1
                else:
                    frequencies[char][word[char]] = 1
        word_freqs = []
        # Sort words by per character freq
        for word in self.wordlist:
            num = 0
            for char in range(self.num_chars):
                num += frequencies[char][word[char]]
            word_freqs.append((num, word))
        word_freqs.sort(key=lambda val: val[0])
        # Generate per-character regex's
        if self.guesses != {}:
            char_re = {}
            must_contain = []
            impossible = []
            for guess in self.guesses:
                print(f"GUESS DICT: {self.guesses[guess]}")
                for char in range(self.num_chars):
                    if self.guesses[guess][char] == 'g':
                        char_re[char] = guess[char]
                    elif self.guesses[guess][char] == 'y':
                        must_contain.append(guess[char])
                    elif self.guesses[guess][char] == 'b':
                        impossible.append(guess[char])
            impossible_pat = "[^" + ''.join(impossible) + "]{1}"
            pat_str = ""
            for char in range(self.num_chars):
                if char in char_re:
                    pat_str += char_re[char]
                else:
                    pat_str += impossible_pat
            print(pat_str)
            first_pat = re.compile(pat_str)
            new_word_freqs = []
            for word in word_freqs:
                if re.search(first_pat, word[1]):
                    print(word[1])
                    new_word_freqs.append(word)
            for word in new_word_freqs.copy():
                valid = True
                for char in must_contain:
                    if char not in word[1]:
                        valid = False
                if not valid:
                    new_word_freqs.remove(word)
            return new_word_freqs[-1][1]

        else:
            for word in reversed(word_freqs):
                if len(set(word[1])) == self.num_chars:
                    return word[1]

    def run(self):
        self.guesses = {}
        for _ in range(6):
            guess = self.generate_guess()
            print(f"Guess {guess}")
            g = input("What did you guess: ")
            self.guesses[g] = self.get_result()
