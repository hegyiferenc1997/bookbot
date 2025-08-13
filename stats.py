# Functions for the main.py project
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_char(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def report(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list