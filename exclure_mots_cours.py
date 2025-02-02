def exclude_short_words(words_list: list[str] = ["Hello", "World", "I'm", "Nathan"]):
    return [word for word in words_list if len(word) > 3]


if __name__ == "__main__":
    print(exclude_short_words())