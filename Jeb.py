def occurrences(text):
    count = 0
    words = text.split()

    for word in words:
        if word.startswith("C") and word.endswith("jeb"):
            count += 1

    return count