########################################################################
 ##
 ## CS 101 Lab
 ## Program 10
 ## Name: Huynh Gia Huy-Jim Huynh
 ## Email: hghydv@umsystem.edu
 ##
 ## PROBLEM : Create write a program to ask the user for a text file to read.
 ## You’ll want to read all the words and output a count of the words that are 
 ## used the most. 
 ## ALGORITHM :
 ##      Step 1:  Start
 ##      Step 2:  Use from string import punctuation
 ##      Step 3:  Define function get_file()
 ##      Step 4:  Make if __name__ == "__main__" function
 ##      Step 5:  Declare word dictionary
 ##      Step 6:  Declare file by calling get_file() function
 ##      Step 7:  Read the file by using for loops
 ##      Step 10: Use if function to check  key is greater or equal to 3.
 ##      Step 11: Check both the lower and upper case, word that only appear once
 ##      Step 12: End
 ##ERROR HANDLING
 ##      N/A
 ##
 ## OTHER COMMENTS:
 ##      Any special comments
 ##
 ########################################################################
from string import punctuation
def get_file():
    user_file = input('Enter of the name of the file to open: ')
    while True:
        try:
            with open(user_file, 'r') as file:
                lines = file.readlines()
            return lines
        except:
            print('Could not open file {}'.format(user_file))
            print('Please try again')
            user_file = input('Enter of the name of the file to open: ')
if __name__ == "__main__" :
    word_dict = dict()
    file = get_file()
    for line in file:
        for n in line:
            if n in punctuation:
                line = line.replace(n, "")
    for line in file:
        for text in line.lower().strip().split(" "):
            text = text.strip(punctuation)
            if len(text) <= 3:
                continue
            else:
                if text in word_dict.keys():
                    word_dict[text] = word_dict[text] + 1
                else:
                    word_dict[text] = 1
    word_freq_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
    only_once = 0
    for key in word_freq_dict:
        if word_freq_dict[key] == 1:
            only_once += 1
    print('\nMost frequently used words')
    print('{:<3}{:>20}{:>12}'.format('#', 'Word', 'Freq.'))
    print('=' * 35)
    for i, key in enumerate(word_freq_dict):
        print('{:<3}{:>20}{:>12}'.format(i + 1, key, word_freq_dict[key]))
    print('\nThere are {} words that occur only once'.format(only_once))
    print('There are {} unique words in the document'.format(len(word_freq_dict)))
