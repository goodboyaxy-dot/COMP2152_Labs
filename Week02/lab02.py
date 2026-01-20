import random
choices = ['rock', 'paper', 'scissors']

playerChoice = input("Enter your choice (1=rock, 2=paper, 3=scissors): ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("error: choice must be between 1 and 3")
else:
    coputerChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice - 1]
    computerChoiceIndex = choices[coputerChoice - 1]

    print("Player choice:", playerChoiceIndex)
    print("Computer choice:", computerChoiceIndex)

    # Determine the winner using if-elif-else statements
    if playerChoiceIndex == computerChoiceIndex:
        print("It's a tie!")
    elif playerChoiceIndex == 0 and computerChoiceIndex == 2:
        print("rock beats scissors- you win!")
    elif playerChoiceIndex == 1 and computerChoiceIndex == 0:
        print("paper beats rock- you win!")
    elif playerChoiceIndex == 2 and computerChoiceIndex == 1:
        print("scissors beats paper- you win!")
    else:
        print("you lose!")