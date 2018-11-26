import json

from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower().strip()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        user_input =  input("Did you mean %s instead? Enter Y for Yes or N for No: " % get_close_matches(word, data.keys())[0])
        if user_input == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif user_input == "N":
            return "The word doesn't exist"
        else:
            return "We don't understand you"
    else:
        return "The word doesn't exist"


word = input("Enter word: ")

results = (translate(word))

if type(results) == list:
    for item in results:
        print(item)
else:
    print(results)
