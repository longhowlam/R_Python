import spacy
# Load the installed model "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")

doc = nlp("This is a text")
# Token texts
[token.text for token in doc]
# ['This', 'is', 'a', 'text']