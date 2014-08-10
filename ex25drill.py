def break_words(stuff):
# The below line is a documentation comment, it shows up in PowerShell
## when you use help to understand ex25 and/or a specific function
    """This function will break up words for us."""
# The below line uses the python split function on the argument
## (in this case a string sentence with text). It splits the string
## using the separator defined within the (), I tested with letter 'o'
    words = stuff.split('o')
    return words
    
def sort_words(words):
    """Sorts the words."""
# The below line uses sort function on the argument & returns result
    return sorted(words)
    
def print_first_word(words):
    """Prints the first words after popping it off."""
# The below line uses pop function on argument. words variable is a
## list, so pop() returns last item in the list, in this example we are
## telling pop to start at position zero in the list, so it returns 
## first word
    word = words.pop(0)
    print word
    
def print_last_word(words):
    """Prints the last word after popping it off."""
# The below line uses pop function on argument. words variable is a
## list, so pop() returns last item in the list, in this example we are
## telling pop to start at position -1 which is one spot from the end
## in the list, so it returns last word
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
# The below line 
    words = break_words(sentence)
    return sort_words(words)
    

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)