from spellchecker import SpellChecker

import re
import json

class TextCorrect:

    def __init__(self):
        
        my_data = self.get_json_data("polish_word_frequency_dict.json")

        self.spell = SpellChecker(language=None)
        self.spell.word_frequency.load_json(my_data)

    def get_json_data(self, json_file):
        """
        Imports the json data into a python dictionary

        Parameters
        ----------
        json_file : str
            The name of json file in the format of a python dictionary

        Returns
        -------
        data : dict
            The json data in a Python dictionary
        """
        f = open(json_file)
        data = json.load(f)
        f.close()
        return data

    def get_text_data(self, text):
        word_regex = re.compile(r'[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+')

        # string of the text as it appear in the original text with all capitilization, formatting, and punctuation
        self.original_text = text
        
        # list of words with case preserved
        word_list = word_regex.findall(text)
        self.case_preserved_words = word_list

        # list of words all lowervase # this will be used for text correction
        word_list_lower = [word.lower() for word in word_list]
        self.words_lower = word_list_lower 

    def correct_words(self):
        self.corrected_words = []
        for word in self.words_lower:
            self.corrected_words.append(self.spell.correction(word))

    def restore_case(self):
        for i, preserved_word in enumerate(self.case_preserved_words):
            for char in range(len(preserved_word)):
                if preserved_word[char].isupper():
                    result = self.corrected_words[i]
                    chars = list(result)
                    chars[char] = chars[char].upper()
                    result = ''.join(chars)
                    self.corrected_words[i] = result
        print(self.corrected_words)

    def replace_words(self):
        converted_text = self.original_text
        for i, original_word in enumerate(self.case_preserved_words):
            if original_word != self.corrected_words[i]:
                converted_text = converted_text.replace(original_word, self.corrected_words[i])
        return converted_text

    def run_correct(self, text):
        self.get_text_data(text)
        self.correct_words()
        self.restore_case()
        return self.replace_words()
