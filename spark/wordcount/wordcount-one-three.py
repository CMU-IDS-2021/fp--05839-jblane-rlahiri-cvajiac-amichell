import pyspark
import sys
import re
import os


def open_book_names_list(base_path, book_paths):
    """
    Opens the file names for the books to be processed

    :param base_path: the path to the file directory
    :param book_paths: the file name containing the book file names
    :return: a set containing all of the file names
    """
    with open(book_paths, "r") as f:
        file_names = f.read().split("\n")
    output_file_names = set()
    for file_name in file_names:
        if file_name != "":
            full_path = os.path.join(base_path, file_name)
            output_file_names.add(full_path)
    return output_file_names


def open_stopwords(stop_words_file_path):
    """
    opens the stop words file and provides a set which can be used to filter tokens/words later

    :param stop_words_file_path: the path to find the stop words file in the local directory
    :return: a set of stop words to filter out
    """
    # create a list of the stop_words
    with open(stop_words_file_path, "r") as f:
        stop_words = f.read().split("\n")
    return set(stop_words)


def get_book(book_file_path):
    """
    Opens the book and returns it as a single string

    :param book_file_path: the local path to the book
    :return: a list of all of the words in the book
    """
    try:
        with open(book_file_path, "r") as book_file:
            book = book_file.read()
    except UnicodeDecodeError:
        try:
            with open(book_file_path, "r", encoding="8859") as book_file:
                book = book_file.read()
        except:
            print(f"file: {book_file_path}, not encoded as Unicode or iso-8859")
            return []
    return [book]


def get_words(book, word_re, stop_words):
    """
    Gets all of the words from the provided book

    :param book: The book, in text, provided as a string from the rdd
    :param word_re: The word matching regex, (validate each word is valid)
    :param stop_words: A set containing words we don't care about
    :return: list of words in the book
    """
    lines = book.split("\n")
    words_in_book = {}
    for line in lines:
        tokens = line.split(" ")
        for token in tokens:
            if not token.isascii():
                continue  # we aren't interested in non-ascii
            if token.isalpha():  # token is only made up of A-Z or a-z characters
                word = token.lower()
                if word in stop_words:
                    continue  # still not interested if it is a stop_word
                if word in words_in_book:
                    words_in_book[word] += 1
                else:
                    words_in_book[word] = 1
            elif re.match(word_re, token) is None:
                continue  # fails to match the regex
            else:
                cleaned_token = token.strip('\'').strip('-').strip('"').lower()
                word = cleaned_token.strip('\'').strip('-').strip('"')
                if len(word) > 0:  # make sure the word is still valid
                    if word in stop_words:  # make sure the word should be counted
                        continue
                    if word in words_in_book:
                        words_in_book[word] += 1
                    else:
                        words_in_book[word] = 1
    return list(words_in_book.items())


if __name__ == "__main__":
    # Input validation
    if len(sys.argv) != 5:
        print("usage: wordcount-naive.py <input_books_list>.txt <books_base_path> <output_path> <stop_words_file>")
    # Get the arguments
    input_books_list = sys.argv[1]
    input_books_base_path = sys.argv[2]
    output_path = sys.argv[3]
    stop_words_file = sys.argv[4]

    conf = pyspark.SparkConf().setAppName("WordCount-Optimizations-One-Three")
    sc = pyspark.SparkContext(conf=conf)

    book_file_paths = open_book_names_list(input_books_base_path, input_books_list)
    book_file_names = sc.parallelize(book_file_paths)

    books = book_file_names.flatMap(get_book)

    # compile a regex to identify valid word tokens
    word_regex = re.compile(r"^[\'-]?[\"]?[A-Za-z\'-]+[\"]?[\'-]?$")

    # Get all of words we should not include as a set
    stop_words = open_stopwords(stop_words_file)

    words = books.flatMap(lambda x: get_words(x, word_regex, stop_words))
    word_counts = words.map(lambda x: (x, 1))\
                       .reduceByKey(lambda x, y: x + y)

    word_counts.saveAsTextFile(output_path)
    sc.stop()
