from Classes_Object import person

p2 = person ("john", 34, "M", "Az")
p3 = person.added_information("kevin", 34, "M", "Az", "Yes", True)
print(p2.name)
print(p3.name + p3.address, p3.is_criminal_history)