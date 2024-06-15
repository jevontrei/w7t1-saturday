def count_words(text):
    words = text.split()
    return len(words)


def unique_words(text):
    words = text.lower().split()
    return set(words)

# sentence = "Hi, I'm a coder and I AM cool and I am a coder."


print(unique_words("Good morning everyone, welcome to life. This life is good"))
