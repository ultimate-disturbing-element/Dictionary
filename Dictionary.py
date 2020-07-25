import json
from difflib import get_close_matches

data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide=input("Press y  for Yes and n for No: ")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            return  ("Wrong Keys")
        else:
            return("you have Enter wrong input please Enter JUst y or n")
    else:
        return print("Meaning doesn't Exist")

word=input("Enter THE word you want to search: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
