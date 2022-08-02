# Make a two-player Rock-Paper-Scissors game.

while(1):
    p1 = input("Player 1! Throw your hand! (R)ock, (P)aper or (S)cissors: ").lower()
    p2 = input("Player 2! Throw your hand! (R)ock, (P)aper or (S)cissors: ").lower()
    if (p1 == "r" and p2 == "s") or (p1 == "p" and p2 == "r") or (p1 == "s" and p2 == "p"):
        print("Player 1 wins")
    elif (p2 == "r" and p1 == "s") or (p2 == "p" and p1 == "r") or (p2 == "s" and p1 == "p"):
        print("Player 2 wins")
    elif p1 not in ["r","p","s"] or p2 not in ["r","p","s"]:
        print("One of you didn't type R, P or S")
    else:
        print("You tied")
    again = input("Do you want to try again? y/N ").lower()
    if again == "n" or again == "":
        break