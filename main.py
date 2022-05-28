# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from fileinput import filename
from itertools import count

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("/Users/ednaliban/Desktop/I4GxZuri/Reading Text Files /story.txt", "r") as filename:
        read_file = filename.read()
        return read_file 


def countwords(text):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = dict()
    split_text = text.split(" ")
    print(split_text)

    for i in split_text:
        if i in count:
            count[i] += 1
        else: 
            count[i] = 1

    return count

print(countwords('./story.txt'))

