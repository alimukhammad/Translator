# Detect a language then translate it to English
from googletrans import Translator

text = input("Enter a text in any language to see it translate in English:\n")
# text = """Pour souvent, quand sur mon canapé je mens D'humeur vacante ou songeuse, Ils clignotent sur cet œil intérieur Quel est le bonheur de la solitude; Et puis mon cœur se remplit de plaisir, Et danse avec les jonquilles."""

translator = Translator()

lang = translator.detect(text)
print(lang)

translated = translator.translate(text, dest='en')
print("Here is the translated text in English:\n ", translated.text)

res = translator.translate(text, dest = 'en')

