def translation (phase):
    translation = ""
    for letter in phase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

            return translation

print(translation(input("Eneter the phase:")))
