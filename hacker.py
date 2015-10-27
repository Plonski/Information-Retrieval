__author__ = 'Thomas Plonski'

#
#   Changes each letter of the entered string into its "hacker" equivalent
#   Example: "bait" -> "8@17"
#

import re

s = input("What would you like to change to hacker speak?")

rep = {"a": "&", "b": "8", "s": "5", "p": "9", "i": "1", "e": "3", "t": "7", "l": "!"} # Define desired replacements here
s = s.lower()                                            # To lowercase
for l in s:                                              # Goes through each letter of entered string
    if l in rep:                                         # Checks if letter is defined to have a value associated to it
        s = re.sub(l,rep[l], s)                          # If above is True: substitutes the letter with its associated value

print(s)