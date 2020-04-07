'''ask for sentence; add it to a variable that capitalises the first letter
and adds a full stop. Add to variable the more sentences are added.

If it is a question, add a question mark
question references added to a tuple - Is, How, What, Where, How'''


def punctuate(sentence):  # Function to add punctuation to a sentence
    for loop in Questions:  # Loop to verify if Question word is found in str
        if sentence.find(loop.casefold()) > -1:  # If Question word found, result > 0
            return "%s?" % (sentence)  # If found, add Question mark.
        elif loop == Questions[(len(Questions) - 1)]:  # Checking if loop is at end
            return "%s." % (sentence)  # If loop at end, sentence is not a question.


Punctuation = (".", "!", ":", "?", " ")  # Tupple for punctuation marks and Questions (Used to check if already exists)
Questions = ("When", "Where", "What", "How", "Why", "Who", "Is", "Does", "Howcome", "Should")
Sentence = ""  ##TOTAL output (added from correct)
Response = ""  ##Received from user input
Correct = ""  ##Processed word, after determining it's nature.
while Response.lower() != "/end":  # Runs continuously as long as input != /end
    Response = (input("Enter a word: ")).casefold()  # casefold() puts all into lower
    if Response.lower() == "/end":  # Checks if user enters '/end'
        break  ##Ends loop if user enters '/end'
    else:  # Will always run if user doesnt end program
        '''if (Response[-1] != ".") and (Response[-1] != "?"):'''  # Second option for specific values
        if Response[-1] in Punctuation:  # Checking sentence has existing punc.
            Correct = Response  # If it does, sentence does not need correcting.
        else:
            Correct = punctuate(Response)  # If no punc, sentence needs correcting - function called.
    Sentence = "%s %s" % (Sentence, Correct.capitalize())  # processed sentence added to TOTAL output.
print(Sentence)  # End result.
