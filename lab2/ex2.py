from caesar import *

# this is the list of bigrams, from most frequent to less frequent
bigrams = ["TH", "HE", 'IN', 'OR', 'HA', 'ET', 'AN', 'EA', 'IS', 'OU', 'HI', 'ER', 'ST', 'RE', 'ND']

# this is the list of monograms, from most frequent to less frequent
monograms = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

# this is the dictionary containing the substitution table (e.g. subst_table['A'] = 'B')
# TODO fill it in the create_subst_table function
subst_table = {}

# these are the dictionaries containing the frequency of the mono/bigrams in the text
# TODO fill them in the analize function
freq_table_bi = {}
freq_table_mono = {}

# sorts a dictionary d by the value
def sort_dictionary(d):
    sorted_dict = list(reversed(sorted(d.items(), key=operator.itemgetter(1))))
    return sorted_dict

# computes the frequencies of the monograms and bigrams in the text
def analize(text):
    global freq_table_bi

    # TODO 1.1 fill in the freq_table_mono dictionary

    # TODO 1.2 fill in the freq_table_bi dictionary

# creates a substitution table using the frequencies of the bigrams
def create_subst_table():
    global subst_table

    # TODO 2.1 sort the bigrams frequence table by the frequency

    # TODO 2.2 fill in the substitution table by associating the sorted frequence
    # dictionary with the given bigrams

# fills in the letters missing from the substitution table using the frequencies
# of the monograms
def complete_subst_table():
    global subst_table

    # TODO 3.1 sort the monograms frequence table by the frequency

    # TODO 3.2 fill in the missing letters from the substitution table by
    # associating the sorted frequence dictionary with the given monograms

# this is magic stuff used in main
def adjust():
	global subst_table
	subst_table['Y'] = 'B'
	subst_table['E'] = 'L'
	subst_table['L'] = 'M'
	subst_table['P'] = 'W'
	subst_table['F'] = 'C'
	subst_table['X'] = 'F'
	subst_table['J'] = 'G'
	subst_table['I'] = 'Y'

def decrypt_text(text):
    global subst_table

    # TODO 4 decrypt and print the text using the substitution table


def main():
    with open('msg_ex2.txt', 'r') as myfile:
        text = myfile.read()
    
    analize(text)
    create_subst_table()
    complete_subst_table()
    adjust()
    decrypt_text(text)
    

if __name__ == "__main__":
  main()

