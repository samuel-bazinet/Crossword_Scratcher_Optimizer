# Crossword Scratcher Optimizer
A program that computes the best letters to have in a crossword scratcher (Will not help you win more often)

## About

This program takes in the words and the number of letters available on a crossword scratcher card. It then calculates a set of letters that will uncover the most words. While this will not make you win anymore games, it can let you know which set of letters would have given you that prize.

## Current Features

* You can give it the number of words on the board
* You can give it the number of letters that can be used
* It will give you two set of numbers that were found using two algorithms
* It will tell you the number of words that can be uncovered with those letters
* Comprehensive GUI to make the use of the program easier

## Future Features

* Let the user have multiple boards set to a single set of letters
* Find and use a more optimal algorithm to maximize the amount of words that can get uncovered
* Add a crossword scratcher "maker" (the program will generate a set of letters that will limit the amount of words uncovered)

## How to Run

*The executable is in the .exe format, so make sure that you machine can run them*

1. Pull this git repository to your machine 
2. Go to the directory conataining the .py files
3. Click on the Run shortcut
    * If the shortcut does not work, enter the dist folder and click on gui.exe to run the program
4. Enter the words in the crossword in the leftmost text box
5. Press the Enter/Return key on your keyboard to add it to the list
6. Enter the number of letters that are available to the scratch in the topmost text box
7. Press on one of the button saying *Algorithm* on them to get the optimal letters 
    * The letters will appear in the list under those buttons
8. Press clear if you want to try a different set of words