#Anagram Checker:
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker():
    
    def __init__(self):
        path = os.path.join(dir_path, "sowpods.txt")
        with open(path, "r", encoding="utf-8") as f:
            words = f.read().lower().split()
            self.words = set(words)

    def is_valid_word(self, word):#this will check if the word is in the file list
        word = word.lower()
        return word in self.words

    
    def is_anagram(self, word1, word2): #this will compare if 2words contain the same letters (but not in the same order)
        return sorted(word1) == sorted(word2) and word1 != word2

    def get_anagrams(self, word):#this will return a list of anagrams
        word = word.lower()
        anagrams = []
        for item in self.words:
            if self.is_anagram(word, item):
                anagrams.append(item)
        return sorted(anagrams)
    


        
