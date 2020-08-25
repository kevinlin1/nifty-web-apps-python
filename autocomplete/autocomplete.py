from data import city_weights


def all_matches(prefix):
    return [term for term in city_weights if term.startswith(prefix)]


if __name__ == "__main__":
    while True:
        prefix = input("Query: ")
        if not prefix:
            exit()
        # Step 1: Return the top 5 matches
        for term in all_matches(prefix)[:5]:
            print(city_weights[term], term)
        print()
