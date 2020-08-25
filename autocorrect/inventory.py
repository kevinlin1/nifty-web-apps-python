from collections import Counter, defaultdict
from heapq import nlargest
from math import sqrt
from random import sample
from string import ascii_letters, ascii_lowercase

from data import english_words


class LetterInventory:
    """The LetterInventory class keeps track of a character count vector."""

    def __init__(self, s):
        """Constructs a letter inventory with the counts of the letters from
        the given string ignoring the case of the letters.
        """
        self.counts = Counter(ch for ch in s if ch in ascii_letters)

    def __getitem__(self, letter):
        """Returns the count for the given letter ignoring case."""
        if letter not in ascii_letters:
            raise ValueError("invalid letter: " + letter)
        return self.counts[letter.lower()]

    def similarity(self, o):
        """Returns the cosine similarity between this inventory and the other
        inventory.
        """
        product = selfNorm = oNorm = 0
        for letter in ascii_lowercase:
            product += self[letter] * o[letter]
            selfNorm += self[letter] ** 2
            oNorm += o[letter] ** 2
        if selfNorm <= 0 or oNorm <= 0:
            return 0
        return product / (sqrt(selfNorm) * sqrt(oNorm))

    def __str__(self):
        """Returns a string representation of this letter inventory as a
        bracketed sequence of letters in alphabetical order with n occurrences
        of a letter that has a count of n in the inventory.
        """
        items = sorted(self.counts.items(), key=lambda pair: pair[0])
        return "[" + "".join(ch * n for ch, n in items) + "]"

    def __eq__(self, o):
        """Returns true if and only if the other inventory stores the same
        character counts as this inventory.
        """
        return self.counts == o.counts

    def __hash__(self):
        """Returns a hash code value for this letter inventory."""
        return hash(str(self))


# Step 0: Initialize data for the algorithm
anagrams = defaultdict(set)
for word in english_words:
    anagrams[LetterInventory(word)].add(word)

if __name__ == "__main__":
    while True:
        s = input("Query: ")
        if not s:
            exit()
        # Step 1: Return the top 10 most similar options
        target = LetterInventory(s)
        for li in nlargest(10, anagrams, key=target.similarity):
            options = anagrams.get(li)
            if s in options:
                print(s)
            else:
                print(sample(options, 1)[0])
        print()
