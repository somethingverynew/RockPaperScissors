import random
from typing import Counter

# Import random is an important moduel for the computer to choose a random value (options)

# This is "options" to pick from representing the choices
# Options is reprsented by the choices
options = ('rock', 'paper', 'scissors')

# The running statement is set to true so the game can have a running loop
running = True

# This will count the number of wins, losses, and ties
print()

# Here i added a counter to keep track of the number of wins, losses, and ties
# Its current value is set to 0
wins = 0
losses = 0
ties = 0

# I decided to add ASCII art to make the game more interesting and fun!
# ASCII art representation for "rock"
rock_art = """
ROCK!!!
                       ░░░░░░░░░░░░░         
                ░░░░░░░░░░░░░░░░░░░░░░       
            ░░░▒▒▒▒▒▒▒▒░▒░▒▒░░░░░░░▒▒▒▒░     
          ░░▒░░░▒▒▒▒▒▒░░░░░░░░░░░▒▒▒░░▒▒▒░   
         ░░░▒▒░░▒▒▒▒▒░▒░░░░░▒░░░░▒▒▒▒▒▒▒▒▒▒  
       ░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▓▓▒  
     ░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒  
   ░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▒▓▓▒░ 
  ░▒▒░░░░░░░▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▓▓▓▓░ 
 ░▒▒▒▒░░▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▒░
 ▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒
░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▓▓███▓▓▓█▒ 
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒░      
    ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒░               
          ░░▒▒▒▒▒▒▒▒▒▒░                      
"""
# ASCII art representation for "paper"
paper_art = """
PAPER!!!

░░░░░░░░▒▒▒▒░░░░░░░░░░░░▒░▒░░▒░░░   
░░░▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒░░▒░░▒▒▒░   
 ▒░░░░░░▒▒▒▒▒░░░▒▒▒▒▒▒▒░░░▒░░▒░▒░   
 ░░▒▒░░░░▒░░░░░░░░░░░░░░░░▒░░▒░▒    
 ▒░░░░░░░░░░▒▒▒░░░░░░░░░░░▒░░▒░▒    
░▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒░░░░▒▓░   
░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒    
░░▒▒▒▒▒▒░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▒░   
░░░░▒░▒░░░░░░░░░░░░▒▒▒░░ ░░▒▒▒▒▒░   
░░ ▒▒▒░░░░░░░░░▒░▒▒▒▒░░ ░░░░▒▒▒▒░   
 ░░▒▒░░░▒▒▒▒▒▒░░░░░░░░ ▒▒░░░▒▒▒▒▒   
░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒░▒░░░▒▒░░░▒▒▒▒▒░   
░▒▒░▒▒▒▒▒▒▒░░░▒░░▒░░░░▒▒▒░▒▒▒▒▒▒▒   
░▒░░░▒▒▒▒░░░░░ ░░▒▒▒▒▒▒░░░▒▒▒▒▒▒░   
 ░░░░░▒▒░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒░▒    
 ░░░░░░▒░░░▒▒▒░░░░░░░░░░░▒▒▒▒▒░░░   
 ░░░░░░▒░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒    
░░░░░░░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░    
░▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒░░  ░░░░░░░   
"""
# ASCII art representation for "scissors"
scissors_art = """         
SCISSORS!!!
 
        ▒█         ▒█         
        ▓░█       ░▒▒▒        
        ▓░░▒      ▓░▓░        
        ░▓░▓░    ▓░░▒         
         ▒░░▓   ░▒░▓░         
         ░█░░▓ ░▓░▒▓          
          ░▒░░▒▓░░▓           
           ▓░░▓▒░▒▒           
            ▓░░▒░▒            
            ░▒▒▒█░            
            ▒░▒░░▒            
           ▓▓▓▒▒▒▓▓           
          █▓▓▓▒▒▓▓▓█          
     ░░▒▒▓▓▓▓█  █▓▓▓▓▒▒▒░░    
  ▒▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▒  
 ▓▓▓▒░ ░▓▓▓▓▒    ▒▓▓▓▓░  ▒▓▓▓ 
░▓▓▒    ▓▓▓▓      ▓▓▓▓    ▒▓▓▒
▒▓▓░    ▓▓█░      ░█▓▓░   ░▓▓▒
░▓▓▓▒░▒▓▓▓░         ▓▓▓▓▒▓▓▓█░
  ▒█▓▓▓▓▓            ▒▓▓▓▓█░  
"""
# Here the player will be welcomed to the game
print("Welcome to Rock, Paper, Scissors!")

# Here is the start of the running loop and start of the game
while running:

# This assigns a current value for both the player and the computer
# The player will not have a value until they pick one of the options
# The computer will randomly pick one of the options
    player = None
    computer = random.choice(options)

# Here if the player does not correctly type one of the options
# The program will ask them to pick again
    while player not in options:
      player = input('Select either (rock, paper, or scissors): ')
      if player not in options:
        print("Invalid entry.")

# So this is for when the results of what both the player and computer picked
# And would be displayed on the screen with ASCII art
# This is for rock
    if player == "rock":
      print("You chose:\n" + rock_art)
    if computer == "rock":
      print("Computer chose:\n" + rock_art)
# This is for paper
    if player == "paper":
      print("You chose:\n" + paper_art)
    if computer == "paper":
      print("Computer chose:\n" + paper_art)
# This is for scissors
    if player == "scissors":
      print("You chose:\n" + scissors_art)
    if computer == "scissors":
      print("Computer chose:\n" + scissors_art)

# This is all of the possible outcomes of the game
    if player == computer:
      print("It's a tie!")
# This is where the win losses and ties are added to the counter      
      ties += 1
    elif player == "rock" and computer == "scissors" or \
    player == "paper" and computer == "rock" or \
    player == "scissors" and computer == "paper":
      print("You win!")
      wins += 1
    else:
      print("You lose!")
      losses += 1 
    print (f"wins: {wins} losses: {losses} ties: {ties}")
  
# Ask the user if they want to play again
# If they say yes, the game will loop again
# Also as the same as before, if the player does not type one of the options
# It will ask them to pick again
    play_again = input("Would you like to play again? (yes/no): ")
    while play_again.lower() not in ['yes', 'no']:
      print("Invalid entry.")
      play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() != "yes":

# If they say no, the program will end by closing the running loop
      running = False

# Once the running loop is over, the program will say goodbye 
# And thank the player for playing and end the program
print("""
░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░
░░████████████░░░█████████████████░░░░░""")
print("Thank you for playing!")
print("Have a wonderful day!")