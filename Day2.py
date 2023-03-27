# CODE
d= ['a', 'e', 'i', 'o', 'u']
s = str(input("Enter character: "))

if s.isalpha():
    if s.lower() in d:
        print("{} is vovel.".format(s))
    else:
        print("{} is consonant.".format(s))
else:
    print("Input is not a character.")

    
#CASE 1:-
# INPUT:
Enter character: e
# OUTPUT: 
e is vovel.

#CASE 2:-
#INPUT:
Enter character: w
# OUTPUT:
w is consonent.
