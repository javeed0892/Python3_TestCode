is_Going = False
is_NotGoing = False
is_Maybe = True
if is_Going and is_Maybe:
    print("Take the house keys with you")
elif is_NotGoing:
    print("we can watch the tv")
elif is_Maybe or is_Going:
    print("if you wait i will come with you")