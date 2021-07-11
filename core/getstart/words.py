"""
Module doc string
"""
import sys
from urllib.request import urlopen

sample_URL='http://sixty-north.com/c/t.txt'

def fetch_words(url):
    """ Fetch a list of words from and url - html document """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_word(story_words):
    print(story_words)

def main(url):
    #url = sys.argv[1]  -- not work when import
    words = fetch_words(url)
    print_word(words)

if __name__ == '__main__':
    main(sys.argv[1])

