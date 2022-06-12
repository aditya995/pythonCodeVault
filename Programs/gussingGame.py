import random as rn

answer = rn.randint(1, 10)
count = 3
start = 1
end = 10
while count:
    try:
        guess = int(input(f"Guess between {start}~{end}\n"))
        # print(answer)
        count -= 1
        if start <= guess and end >= guess:
            if guess == answer:
                print("Your guess is correct")
                break
            else:
                print("Your guess is wrong")
        else:
            print("Out of bound")
    except ValueError:
        print("Please give integer number")
