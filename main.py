# Crossword_Scrathcer_Optimize 

from cgi import test


def quicksort_letters(letters: dict[str, int]) -> list[str]:

    letter_items = letters.items()
    letter_list = [(i[0], i[1]) for i in letter_items]

    return quicksort_letter_H(letter_list)

def quicksort_letter_H(letters: list[(str, int)]) -> list[str]:
    
    if (len(letters) <= 1):
        return letters

    pivot = letters[-1][1]
    x = 0
    for i in range(len(letters)-1):
        if letters[i][1] < pivot:
            temp = letters[x]
            letters[x] = letters[i]
            letters[i] = temp
            x += 1

    temp = letters[x]
    letters[x] = letters[-1]
    letters[-1] = temp

    lista = quicksort_letter_H(letters[0:x])
    listb = quicksort_letter_H(letters[x+1:])
            
    return  lista + [letters[x]] + listb

# Board is an object representing the board containing the words
# on a crossword scratcher
class Board:

    # The class is constructed by having the user input the words contained in the crossword board
    def __init__(self, word_count: int = 5, letter_count: int = 10):

        self.words: list[str] = [input("Enter word number %d: "% a) for a in range(1, word_count+1)]
        self.letter_count = letter_count
        self.letters_occ: list[str] = []
        self.letters_osw: list[str] = []
        self.uncovered_words_occ = 0
        self.uncovered_words_osw = 0

        self.optmize_char_count()        
        #self.optimize_small_words()


    # optimize_char_count computes the best letters by counting the total amount of letter 
    # and choosing the most common ones
    def optmize_char_count(self) -> None:

        character_occurence: dict[str, int] = {}

        # the program will go through every word and count the total number of each letters
        for word in self.words:
            for char in word:
                if char in character_occurence.keys():
                    character_occurence[char] += 1
                else:
                    character_occurence[char] = 1

        # the letters are sorted by recurrence in increasing order
        sorted_list = quicksort_letters(character_occurence)

        # the most occuring characters are set as the "optimal letters" in decreasing order
        for i in range(1, self.letter_count+1):
            self.letters_occ.append(sorted_list[-i][0])


        for i in self.words:
            flag = True
            for j in i:
                if (j not in self.letters_occ):
                    flag = False
                    break

            if flag:
                self.uncovered_words_occ += 1
                
        

    
    # optimize_small_words computes the best letters by choosing letters that would complete
    # small words as to complete as many words as possible
    def optimize_small_words(self) -> None:
        pass

    
def main():
    test_board = Board(int(input("How many words are there? ")),18)
    print("The optimal letters are: ", test_board.letters_occ)
    print("There are %d words that have been uncovered with those letters"% test_board.uncovered_words_occ)

    pass

if __name__ == "__main__":
    main()