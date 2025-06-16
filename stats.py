def count_words(text):
    return len(text.split())


def count_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        characters[char] = characters.get(char, 0) + 1

    return characters


def sort_on(dict):
    return dict["num"]


def sort_dictionary(char_count):
    res = []
    for char in char_count:
        res.append({"char": char, "num": char_count[char]})
    res.sort(reverse=True, key=sort_on)
    return res

