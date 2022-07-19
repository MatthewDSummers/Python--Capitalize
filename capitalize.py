# A function to capitalize the first letter of each word in a string

def say(word):

    #capitalize the first word
    if ord(word[0]) < 123 and ord(word[0]) > 96:
        lower_case_value = ord(word[0])
        upper_case_value = lower_case_value - 32
        capitalized_word = word.replace(word[0], chr(upper_case_value), 1)
        word = capitalized_word

    #capitalize each new word
    for i in range(len(word)):
        if word[i] == chr(32):
            if ord(word[i+1]) < 123 and ord(word[i+1]) > 96:
                lower_case_value = ord(word[i+1])
                upper_case_value = lower_case_value - 32
                remainder = word[i+2:]
                word = word[:i] + " " + chr(upper_case_value) + remainder
    return("Hi " + word)

print(say("mark richard hamill"))   #returns Mark Richard Hamill
print(say("mark richard"))   #returns Mark Richard
print(say('mark'))   #returns Mark
print(say('Mark Richard hamill'))   #also returns Mark Richard Hamill
                            # and so on