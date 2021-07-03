#Here we are creating a dictionrie inside a dictionrie there we will be having key value.
monthConversions = {
    "jan": "January",
    "Feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}
monthConversions["lvu"] = "love"#adding key value to the dictionary.
del monthConversions ["lvu"]
print(len(monthConversions))
for item in monthConversions:
    if "nov" in monthConversions:
        print("Key found")
        break
    else:
        print("Key not found")

