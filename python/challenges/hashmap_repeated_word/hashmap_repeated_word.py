import string

def repeated_word(str):
    str = str.translate(str.maketrans('', '', string.punctuation))
    count = {}
    words = str.split()
    for word in words:
        if word.lower() in count:
            return word
        else:
            count[word.lower()] = 1

    return None

if __name__ == '__main__':
    str = "Once upon a time, there was a brave princess who..."
    print(repeated_word(str))
