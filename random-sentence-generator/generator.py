from random import choice

grammar = {
    "SENTENCE": [
        ["NOUNP", "VERBP"]
    ],
    "NOUNP": [
        ["DET", "ADJS", "NOUN"],
        ["PROPNOUN"],
    ],
    "PROPNOUN": [
        ["John"],
        ["Jane"],
        ["Sally"],
        ["Spot"],
        ["Fred"],
        ["Elmo"],
    ],
    "ADJS": [
        ["ADJ"],
        ["ADJ", "ADJS"],
    ],
    "ADJ": [
        ["big"],
        ["green"],
        ["wonderful"],
        ["faulty"],
        ["subliminal"],
        ["pretentious"],
    ],
    "DET": [
        ["the"],
        ["a"],
    ],
    "NOUN": [
        ["dog"],
        ["cat"],
        ["man"],
        ["university"],
        ["father"],
        ["mother"],
        ["child"],
        ["television"],
    ],
    "VERBP": [
        ["TRANSVERB", "NOUNP"],
        ["INTRANSVERB"],
    ],
    "TRANSVERB": [
        ["hit"],
        ["honored"],
        ["kissed"],
        ["helped"],
    ],
    "INTRANSVERB": [
        ["died"],
        ["collapsed"],
        ["laughed"],
        ["wept"],
    ],
}


def generate(target, n=1):
    """Randomly generate n grammatical sentences for the target."""
    if target not in grammar or n <= 0:
        return []
    return [_generate(target).strip() for _ in range(n)]


def _generate(target):
    """Returns either the given target if it is a terminal symbol or a
    randomly generated string, possibly with a trailing space.
    """
    if target not in grammar:
        return target + " "
    return "".join(_generate(part) for part in choice(grammar[target]))


if __name__ == "__main__":
    print("Valid symbols: " + " ".join(grammar.keys()))
    while True:
        target = input("Target: ")
        if not target:
            exit()
        # Step 1: Return 10 randomly-generated strings
        for result in generate(target, 10):
            print(result)
        print()
