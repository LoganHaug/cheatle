import cheater as c
import re

with open("v5char.txt") as f:
    words = f.read()
    words = words.split("\n")

cheat = c.Cheater(words, 5)
cheat.run()