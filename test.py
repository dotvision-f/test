from CodeSimilarityChecker import *

snippet1 = CodeSnippet('code1.py')
snippet2 = CodeSnippet('code2.py')

print("Checking by words")
checker = Checker_by_Word(0.7, snippet1, snippet2)
checker.check_similarity()

print()
print("Checking by functions")

checker2 = Checker_by_Function(0.7, snippet1, snippet2)
checker2.check_similarity()