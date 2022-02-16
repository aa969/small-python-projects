def count_words(filename):
    """Count the approximate number of words in file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        number_words = len(words)
        print(f"The file {filename} has about {number_words} words")


filenames = ['/Users/aa742/Desktop/Alice in Wonderland.txt', '/Users/aa742/Desktop/Siddhartha.txt']

for filename in filenames:
    count_words(filename)
