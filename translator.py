import os
from tabulate import tabulate
from googletrans import Translator

class Main_Translator(object):
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.translator = Translator()

    def translation(self):
        translator = self.translator.translate(self.word, dest=self.language)
        data = [["Original Sentence:", "Translated Sentance:"],
                [self.word, str(translator.text)]]
        return tabulate(data, headers="firstrow", tablefmt="fancy_grid")

    def __str__(self):
        return self.translation()

if __name__ == '__main__':
    sentence = input("Enter text to translate: ")
    os.system("cls")
    print(Main_Translator(sentence, "en"))