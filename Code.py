import json
from difflib import get_close_matches

data = json.load(open("076 data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead of ? \n Press y for Yes, n for No :" %get_close_matches(w, data.keys())[0])
        yn=yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="n":
            return "Please Enter a valid selection"
        else:
            return "Please Enter y for Yes , n for No"
    else:
        return "Please Enter a valid selection"

word = input("Enter your word to find meaning for :")
print(translate(word))

output = translate(word)

if type(output) == list:
    for x in output:
        print(x)
else:
    print(output)
