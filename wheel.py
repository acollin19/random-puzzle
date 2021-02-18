
import math
import random

# Use the random module to return random strings from the puzzles list
# Used randrange not randint because its strings inside the list and not integers
def get_random_puzzle(puzzles):
    puzzle=puzzles[random.randrange(len(puzzles))]
    
    return puzzle  
    
def count_occurrences_of_letter(puzzle, letter):
# Counting how many times a letter appears in the puzzle
# Using counter to increase the value every time the same letter is found in the puzzle
    counts=0
    for i in puzzle:
        if i==letter:
            counts=counts+1
            
    return counts
    
  
def check_puzzle_compatibility(puzzle, blanks, puzzle2):
# If the length of the first puzzle and second puzzle dont match return False
    if len(puzzle)!=len(puzzle2):
        return False
    else:
        '''
            Go through each letter in the puzzle and if the letter int the list of booleans
            are match and the letters in the puzzle 1 and 2 dont match return False
            So otherwise it would be True.
        '''
        for letter in range(len(puzzle)):
            if blanks[letter]==True and puzzle[letter]!=puzzle2[letter]:
                return False
        return True


def get_best_compatible_puzzle(puzzle, blanks, letter, puzzles):
# Two variable to compare the lowest occurences and empty string
    lowest_num=len(puzzle)
    puzzle_low=''
    for puzzle2 in puzzles:
# If the 
        if check_puzzle_compatibility(puzzle, blanks, puzzle2):
            if count_occurrences_of_letter(puzzle2, letter) <= lowest_num:
                puzzle_low=puzzle2
                lowest_num=count_occurrences_of_letter(puzzle2, letter)
# Returns None if it can't swap with another puzzle   
    if puzzle_low=='':
        return None
    else:
# Returns empty string if the number of occurences dont match the second puzzle 
        return puzzle_low

def get_starting_blanks(puzzle):
# Setting variable to equal the list of strings in puzzle   
    starting_blanks=list(puzzle)
# Values in range of the length of the puzzle will be equal to the list of the puzzle     
    for i in range(0,len(puzzle)):
        starting_blanks[i]=starting_blanks[i]==" "
    
    return starting_blanks 
    

def blanks_to_string(blanks, puzzle):
    newlist=""
    for character in range(len(blanks)):
# if user enters the wrong character it returns underscore
        if blanks[character] == False:
            newlist+="_"
        else:
# if user inputs correct character it will return the value to the new string
            newlist+=puzzle[character]
      
    return newlist


def update_blanks(blanks, puzzle, letter):
#  For every letter that matches in the puzzle, if it matches to the letter then it changes the blank to True
    for match in range(len(puzzle)):
        if puzzle[match]==letter:
            blanks[match]=True
                

def check_if_game_won(blanks):
# For every guess that is true in blanks 
    for won in blanks:
# If there are still some that arent guessed then return False
        if won!=True:
            return False
# If all letter are found return True
    return True
    

# Depending on user input 1 or 2, the play function will take in the True
# or False boolean argument to play the regular game or the misfortune game.
def play(misfortune):
    '''
    Parameter: a boolean indicating whether or not the special variant should be played.
    This function will let the player play the game.
    '''
    
    puzzles = [
        "TO BE OR NOT TO BE",
        "TO ME NO CAT IS IN",
        "WALKING ON SUNSHINE",
        'TALKING ON IMESSAGE',
        "BE READY AT NOON",
        "HE READS AT CAMP",
        "NO SHADE ON MOON",
        "HE RAN TO THE VAN", 
        "HE GOT ME ONE CAN",
        "OLD MAN WAS HOT",
        "THE DOG WAS CUT",
        "MAD MAN HAD CAT",
        "THE CELL IS BROKEN",
        "SHE FELL AT CAMPUS"  
    
    ]
    
    num_correct_guesses, num_incorrect_guesses = 0, 0
    
    puzzle = get_random_puzzle(puzzles)
    puzzles.remove(puzzle)
    
    blanks = get_starting_blanks(puzzle)
    
    print("Here is your phrase:")
    print(blanks_to_string(blanks, puzzle))
        
    winner = False
    while not winner:
        letter = ''
        while not letter.isalpha():
            letter = input("Enter a letter (a - z or A - Z): ")
            letter = letter.upper()
        
        letter_present = count_occurrences_of_letter(puzzle, letter) > 0
        if letter_present and misfortune:
            new_puzzle = get_best_compatible_puzzle(puzzle, blanks, letter, puzzles)
            if new_puzzle not in [None, puzzle]:
                puzzles.remove(new_puzzle)
                puzzle = new_puzzle
                letter_present = count_occurrences_of_letter(puzzle, letter) > 0
                print("Muahaha.")
        
        if letter_present:
            update_blanks(blanks, puzzle, letter)
            num_correct_guesses += 1
        else:
            num_incorrect_guesses += 1
        
        print(blanks_to_string(blanks, puzzle))
        winner = check_if_game_won(blanks)
    
    print("Thanks for playing!")
    print("You had {} correct and {} incorrect guesses.".format(num_correct_guesses, num_incorrect_guesses))

         
def menu():
#  Printing the introductory messages and asking for user to input an option
    print("Welcome to Wheel of(Mis)Fortune!")
    print("Guess the phrase, one letter at a time.")
    print("What would you like to do?")
    print("1) Play a game of Wheel of Fortune")
    print("2) Play a game of Wheel of Misfortune")
    print("3) Exit")
    user_input=int(input())
# If user inputs 1 the regular game will play as the play function takes in False argument    
    if user_input==1:
        play(False)
# If user inputs 2 the misfortune game will play as play function takes True argument                
    elif user_input==2:
        play(True)
# If user inputs 3 the game will end             
    elif user_input==3:
        print("See ya!")
# If the user inputs 4 the menu will reprint so they can input a new option             
    else:
        print("Invalid input.")
        menu()        
    
    
if __name__ == '__main__':
    menu()
