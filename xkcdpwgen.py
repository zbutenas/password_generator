#!/usr/bin/env python3
import argparse, random

words = 4
caps = 0
numbers = 0
symbols = 0
string = ""
i = 0
sym = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--words", help= "include WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps", help= "capitalize the first letter of the CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", help= "insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", help= "insert SYMBOLS random symbols in the password (default=0)")
args = parser.parse_args()
       
if args.words:
    words = int(args.words)
if args.caps:
    caps += int(args.caps)
if args.numbers:
    numbers += int(args.numbers)
if args.symbols:
    symbols += int(args.symbols)

while i in range(0, words):
    if caps > 0:
        if numbers > 0:
            if symbols > 0:
                string += (random.choice(sym)) + (random.choice(num)) + (random.choice(open("wordList.txt").read().split())).capitalize()
                caps -= 1
                numbers -= 1
                symbols -= 1
                i += 1
            else:
                string += (random.choice(num)) + (random.choice(open("wordList.txt").read().split())).capitalize()
                caps -= 1
                numbers -= 1
                i += 1
        elif symbols > 0:
            string += (random.choice(sym)) + (random.choice(open("wordList.txt").read().split())).capitalize()
            caps -= 1
            symbols -= 1
            i += 1
        else:
            string += (random.choice(open("wordList.txt").read().split())).capitalize()
            caps -= 1
            i += 1
    elif numbers > 0:
        if symbols > 0:
            string += (random.choice(sym)) + (random.choice(num)) + (random.choice(open("wordList.txt").read().split()))
            numbers -= 1
            symbols -= 1
            i += 1
        else:
            string += (random.choice(num)) + (random.choice(open("wordList.txt").read().split()))
            numbers -= 1
            i += 1
    elif symbols > 0:
        string += (random.choice(sym)) + (random.choice(open("wordList.txt").read().split())).capitalize()
        symbols -= 1
        i += 1
    else:
        string += (random.choice(open("wordList.txt").read().split()))
        i += 1

if caps > words or numbers > words or symbols > words:
    print("You have requested too many CAPS, NUMBERS, or SYMBOLS.")
    print("We have adjusted your arguments to generate a new password.")
    print(string)
else:
    print(string)


    
