# Crossword_Scrathcer_Optimize 

# Board is an object representing the board containing the words
# on a crossword scratcher
class Board:

    # The class is constructed by having the user input the words contained in the crossword board
    def __init__(self, word_count: int = 5, letter_count: int = 10) -> None:

        self.words: list[str] = self.user_input(word_count) if __name__ == "__main__" else []
        self.letter_count = letter_count
        self.letters_occ: list[str] = []
        self.letters_osw: list[str] = []
        self.uncovered_words_occ = 0
        self.uncovered_words_osw = 0

        if (__name__ == "__main__"):
            self.optmize_char_count()        
            self.optimize_small_words()

    # get_optimal_set computes both algorithms and returns the set with the most words that have been uncovered
    def get_optimal_set(self) -> tuple[list[str], int]:

        self.optmize_char_count()
        self.optimize_small_words()

        if (self.uncovered_words_occ > self.uncovered_words_osw):
            return self.letters_occ, self.uncovered_words_occ
        else:
            return self.letters_osw, self.uncovered_words_osw

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
        sorted_list = self.quicksort_tuple_list(character_occurence)

        # the most occuring characters are set as the "optimal letters" in decreasing order
        for i in range(1, self.letter_count+1):
            self.letters_occ.append(sorted_list[-i][0])


        # We use a loop too find out how many words would be found using those letters
        for i in self.words:
            flag = True
            for j in i:
                # if one of the letters isn't in the "optimized" list, it is set as false and the loop proceeds to the next word
                if (j not in self.letters_occ):
                    flag = False
                    break

            if flag:
                self.uncovered_words_occ += 1
    
    # optimize_small_words computes the best letters by choosing letters that would complete
    # small words as to complete as many words as possible
    def optimize_small_words(self) -> None:
        
        # the quicksort function is used to sort the words by length
        sorted_words = self.quicksort_tuple_list_H([(i, len(i)) for i in self.words])
        counter = 0

        # the letters in the words are checked and added to 
        while (len(self.letters_osw) != self.letter_count) and (counter < len(sorted_words)):

            for i in sorted_words[counter][0]:
                if i not in self.letters_osw:
                    self.letters_osw.append(i)

            counter += 1

        # We use a loop too find out how many words would be found using those letters
        for i in self.words:
            flag = True
            for j in i:
                # if one of the letters isn't in the "optimized" list, it is set as false and the loop proceeds to the next word
                if (j not in self.letters_osw):
                    flag = False
                    break

            if flag:
                self.uncovered_words_osw += 1

    # quicksort_tuple_list is a function that sets up the quicksort_tuple_list_H function 
    # it is meant to sort the letters by occurence
    def quicksort_tuple_list(self, letters: dict[str, int]) -> list[(str, int)]:

        letter_items = letters.items()
        letter_list = [(i[0], i[1]) for i in letter_items]

        return self.quicksort_tuple_list_H(letter_list)

    # quicksort_tuple_list_H sorts a list whose elements are tuples
    # the int compared is the second element in the tuple
    def quicksort_tuple_list_H(self, letters: list[(str, int)]) -> list[(str, int)]:
        
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

        lista = self.quicksort_tuple_list_H(letters[0:x])
        listb = self.quicksort_tuple_list_H(letters[x+1:])
                

        return  lista + [letters[x]] + listb

    # user_input is called when the program is called in CLI mode
    # it makes the user input the words via the CLI
    def user_input(self, word_count: int) -> list[str]:
        return [input("Enter word number %d: "% a) for a in range(1, word_count+1)]

    # gui_input is called by the GUI to input the words into the board
    def gui_input(self, inputs: list[str]):
        self.words = inputs
    
def main() -> None:
    
    test_board = Board(int(input("How many words are there? ")), int(input("How many letters are available? ")))
    print("The optimal letters using occurence are: ", test_board.letters_occ)
    print("There are %d words that have been uncovered with those letters" % test_board.uncovered_words_occ)
    print("The optimal letters using word length are: ", test_board.letters_osw)
    print("There are %d words that have been uncovered with those letters" % test_board.uncovered_words_osw)

if __name__ == "__main__":
    main()