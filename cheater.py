class Cheater:
    def __init__(self, wordlist: list, num_chars: int):
        self.wordlist = wordlist
        self.guesses = {}
        self.num_chars = num_chars

    def get_result(self):
        colors = []
        for _ in range(5):
            while True:
                word = input("Enter letter color: ")
                if word not in ["g", "b", "y"]:
                    print("Not a valid option try again")
                    continue
                else:
                    colors.append(word)
                    break
        return colors

    def generate_guess(self):
        # Do freq analysis
        frequencies = {num: {} for num in range(self.num_chars)}
        for word in self.wordlist:
            for char in frequencies:
                if word[char] in frequencies[char]:
                    frequencies[char][word[char]] += 1
                else:
                    frequencies[char][word[char]] = 1
        # Generate per-character regex's
        if self.guesses != {}:
            char_re = {0: ""}
            must_contain = []
            impossible = []
            for guess in self.guesses:
                for char in range(self.num_chars):
                    if guess[char] == 'g':
                        char_re[char] = guess[char]
                    elif guess[char] == 'y':
                        must_contain.append(guess[char])
                    elif guess[char] == 'b':
                        impossible.append(guess[char])
        # sort guesses by frequency and pick first guess that matches regex
        guess = ""
        return guess

    def run(self):
        self.guesses = {}
        for _ in range(5):
            guess = self.generate_guess()
            print(f"Guess {guess}")
            self.guesses[guess] = self.get_result()
            print(self.guesses)
