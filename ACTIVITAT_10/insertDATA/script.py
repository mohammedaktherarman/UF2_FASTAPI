import pandas as pd

readedDocument = pd.read_csv("paraules_temàtica_penjat.csv")
processedDocument = readedDocument.to_dict(orient="list")
print(processedDocument)

words = processedDocument['WORD']
themes = processedDocument['THEME']

for word,theme in zip(words, themes):
    



