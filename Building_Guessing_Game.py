secret_number = float(9)
guess_number = ""
guess_count = 0
guess_limit = 3
out_guess = False
while secret_number != guess_number and not(out_guess):
    if guess_count < guess_limit:
        guess_number = float(input("Enter the guess number = "))
        guess_count= guess_count +1
        print("you are left with ", guess_limit - guess_count)
    else:
        out_guess = True
if out_guess:
    print("YOU LOSE")
else:
    print("YOU WIN")

