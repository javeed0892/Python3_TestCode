read_file = open("C:\\Users\\skjav\\PycharmProjects\\pythonProject\\TestPythoin\\read.txt", "r+")
lenght_file = len(read_file.readlines())
#print(lenght_file)
read_file.write("\n78  TI                      F  SMALL LETTER THORN ")
if lenght_file != 95:
     print("Here you go ")
else:
    print("Here is leght = ", lenght_file)
read_file.close()
