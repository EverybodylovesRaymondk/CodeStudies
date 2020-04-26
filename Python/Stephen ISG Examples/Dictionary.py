import json
from difflib import get_close_matches
import time

dictionary = json.load(open("data.json"))


def find(a):
    if a in dictionary:
        return {a.title(): dictionary[a]}
    elif a.title() in dictionary:
        return {a.title(): dictionary[a.title()]}
    elif a.upper() in dictionary:
        return {a.upper(): dictionary[a.upper()]}
    elif len(get_close_matches(a, dictionary.keys())) > 0:
        CloseMatches = (get_close_matches(a, dictionary.keys(), n=4))
        for matches in CloseMatches:
            choice = (input('Did you mean %s ? Y/N: ' % matches)).lower()
            while type(check(choice)) == str:
                choice = input('That input was invalid. Please enter Y/N: ').lower()
            if check(choice.lower()):
                return {matches.title(): dictionary[matches]}
                break
            elif (matches == CloseMatches[-1]) and (choice.lower() == 'n'):
                return "No more suggestions could be made for that word, please retry."
    else:
        return "That word was not found in the dictionary"


def check(b):
    if (b.lower()).startswith("y"):
        return True
    elif (b.lower()).startswith("n"):
        return False
    else:
        return "Invalid"


repeat = True
while repeat:
    response = (input("Would you like to look a word up in the dictionary? Yes/No): ")).lower()
    print("\n")
    while type(check(response)) == str:
        response = (input("That input was invalid. Would you like to look a word up in the dictionary? Yes/No: ")).lower()
    repeat = check(response)
    if repeat:
        word = (input("What word would you like to search? - ")).casefold()
        output = find(word)
        print("\n")
        if type(output) == str:
            print(output)
            print("\n")
        else:
            for out in output:
                print("%s:" % out)
                if type(output[out]) == list:
                    for result in output[out]:
                        print("- %s" % result)
                else:
                    print("- %s" % output[out])
                print("\n")
    else:
        print("\n")
        print("Ok! Cheers.")
        time.sleep(1)
        exit
