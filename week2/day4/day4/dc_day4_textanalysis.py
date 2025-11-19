import os
import string 
#DAily Challenge: Text Analysis
#Create a Text class to analyze text data, either from a string or a file. 
# Then, create a TextModification class to perform text cleaning.

#Part I: Analyzing a Simple String

class Text():
    def __init__(self, input_str: str):
        #A class for analyzing text data
        if not isinstance(input_str, str):
            raise TypeError("Text must be a string.")
        self.txt = input_str
        

    def word_frequency(self, word: str):
        #Return how many times 'word' appears in the text. Case-insensitive
        if not word or not isinstance(word, str):
            raise ValueError("word must be a non-empty string.")
        
        words = self.txt.lower().split()
        target = word.lower()
        count = words.count(target)
        return count if count > 0 else None

    def most_common_word(self):
        #Return the most frequent word in the text
        words = self.txt.lower().split()
        if not words:
            return None

        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        return max(word_counts, key=word_counts.get)
    
    def unique_words(self):
        #Return a list of unique words, case-insensitive
        words = self.txt.lower().split()
        return list(set(words))
    
#Part II: Analyzing Text from a File

    @classmethod
    def from_file(cls, file_path: str):
        #Load text from a file safely.
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return cls(content)
        except Exception as e:
            raise IOError(f"Error reading file: {e}")
        

class TextModification:

    @staticmethod
    def remove_punctuation(text: str):
        #Remove punctuation characters from text
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)
    
    @staticmethod
    def clean_text(text: str):
        #Full pipeline: lowercase → remove punctuation → remove double spaces
        text = TextModification.to_lowercase(text)
        text = TextModification.remove_punctuation(text)
        text = TextModification.remove_extra_spaces(text)
        return text



    # Test loading from file
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_text = Text.from_file(dir_path + "/dc_text.txt")
        print("\nSuccessfully loaded text from file.")
    except Exception as e:
        print("File loading failed:", e)

    print("\nAll tests complete.")
    
dir_path = os.path.dirname(os.path.realpath(__file__))


text_obj = Text.from_file(dir_path + '/dc_text.txt')

print("Frequency of 'cotton':", text_obj.word_frequency("cotton"))
print("Most common word:", text_obj.most_common_word())
print("Unique words:", text_obj.unique_words())
print(text_obj.most_common_word())


