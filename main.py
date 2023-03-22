from CodeSimilarityChecker import *

print("Hello! I am a code similarity checking software.\
        \nPlease follow the instructions.\n")

print("Please enter two code files to check the similarity.")
snippet1 = CodeSnippet(str(input("Your first code file's name is: ")))
snippet2 = CodeSnippet(str(input("Your second code file's name is: ")))

print("""Which checking method would you like to use?
        1. Check by words
        2. Check by functions""")
checking_method = str(input("Choose the number (1 or 2): "))
threshold = float(input("Enter a threshold: "))

if checking_method == str(1):
    print("\nChecking on words...")
    checker = Checker_by_Word(threshold, snippet1, snippet2)
    checker.check_similarity()
elif checking_method == str(2):
    print("\nChecking on functions...")
    checker = Checker_by_Function(threshold, snippet1, snippet2)
    checker.check_similarity()
else:
    print("Invalid answer! Pleaser choose your checking method by entering '1' or '2'")
