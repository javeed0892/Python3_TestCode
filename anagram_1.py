#Here we are initialize the number of arrays as 256
No_Of_CHARS =256

#function to check where the both string are anagram or not.

def aranagram(str1, str2):

    #lnitialize all valve to 0.
    count1 = [0] * No_Of_CHARS
    count2 = [0] * No_Of_CHARS
    for i in str1:
        count1[ord(i)] += 1
    for i in str2:
        count2[ord(i)] += 1
    #here we need to compare the both string
    if len(str2) != len(str1):
        return 0
    #compare count arrays
    for i in range(No_Of_CHARS):
        if count1[i] != count2[i]:
            return 0
        return 1
str1 = "geeksforgeeks"
str2 = "geeksgeeksfor"
if aranagram(str1, str2):
    print("here are strings")
else:
    print("we not")




