from googletrans import Translator
import bs4
import json

print("Hello World")

while Translating==True:
    translator = Translator()
    translation = translator.translate(text, dest='en')
    text=input(("Values to translate:"))
    print(translation.text)