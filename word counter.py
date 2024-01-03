a=input("Enter the paragraph to count the number of words: ")
b=len(a.split())
if b==0 :
    print("Invalid input, empty input.")
    print(b)
else:
    print("Number of Words in the Given Para:- ", b)