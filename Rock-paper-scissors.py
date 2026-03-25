"""
A simple Rock, Paper, Scissors game where the computer always wins."""

print("=" * 40)
print("Rock, Paper, Scissors Game")
print("=" * 40)
print("""
    ===       =============     =     =
   =====      =============      =   =
  =======     =============        =
  =======     =============      =   = 
   =====      =============     =      =
    ===       =============    =        =

      """)
user_answer = input("Rock, Paper, Scissors ? ")

if user_answer == "Rock" or user_answer == "rock":
    print("Computer answer is : Paper")
    print("Computer wins !")
elif user_answer == "Paper" or user_answer == "paper":
    print("Computer answer is : Scissors")
    print("Computer wins !")
elif user_answer == "Scissors" or user_answer == "scissors":
    print("Computer answer is : Rock")
    print("Computer wins !")
else:
    print("Invalid input. Please choose Rock, Paper, or Scissors.")

print("=" * 40)
print("DEFEAT !")
print("Thank you for playing !")



