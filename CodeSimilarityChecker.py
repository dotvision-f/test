from CodeSnippet import *
from abc import ABC, abstractmethod

# Dictionary of keywords available in programming languages
dict = {"py": ["class", "def", "if", "else", "is", "not", "for", "while",\
                "import", "print", "True", "False", "and", "or", "as",\
                "assert", "await", "async", "del", "elif", "break",\
                "continue", "except", "finally", "from", "global", "in",\
                "lambda", "nonlocal", "pass", "raise", "try", "with", "yield"
              ],
        "java": ["Abstract", "Assert", "Break", "Case", "Catch", "Char",\
                 "Class", "Const", "Continue", "Default", "Else", "Enum",\
                 "If", "Import", "Package", "Private", "Protected", "Public",\
                 "Return", "Short", "Static", "Super", "Switch",\
                 "Synchronized", "This", "Throw", "Transient", "Try",\
                 "Void", "Volatile", "While"
                ],
        "c": ["auto", "break", "case", "char", "const", "continue", "default",\
              "do", "double", "else", "enum", "extern", "float", "for", "goto",\
              "if", "int", "long", "register", "return", "short", "signed",\
              "sizeof", "static", "struct", "switch", "typedef", "union",\
              "unsigned", "void", "volatile", "while"
             ],
        "cpp": ["auto", "double", "int", "struct", "break", "else", "long",\
                "switch", "case", "enum", "register", "typedef", "char",\
                "extern", "return", "union", "const", "float", "short",\
                "unsigned", "continue", "for", "signed", "void", "default",\
                "goto", "sizeof", "volatile", "do", "if", "static", "while",\
               ]}

class Checker:
    '''Compare 2 codes, take Code 1 as root
    Input:  threshold: threshold for accepting similarity
            snippet1: Object CodeSnippet của code 1
            snippet2: Object CodeSnippet của code 2
    Task: Compare 2 codes and show the result
    '''
    def __init__(self, threshold, snippet1, snippet2):
        self.threhold = threshold
        self.snippet1 = snippet1
        self.snippet2 = snippet2
    
    # Show similarity and compare with threshold
    def show_result(self, scale):
        print(f"Similarity {scale*100}%")
        if scale >= self.threhold:
            print("2 code snippets are similar")
        else: 
            print("2 code snippets are dissimilar")

    # Evaluate the similarity
    # having some diffrent comparisons
    def check_similairy(self):
        pass


class Checker_by_Word(Checker):
    '''Inherit __init__ and other methods from the class Checker
    Task: Compare by counting the number of similar words between 2 codes,
            remove the keywords available in the programming language.
    '''
    def __init__(self, threshold, snippet1, snippet2):
        super().__init__(threshold, snippet1, snippet2)

    # Evaluate the similarity
    def check_similarity(self):
        count = 0
        lens = len(self.snippet2.get_strings())
        if self.snippet1.get_language() != self.snippet2.get_language():
            print("The 2 codes are different in language. They can't check similarity")
        else:
            for i in self.snippet2.get_strings():
                if i in dict[self.snippet1.get_language()]:
                    lens -= 1
                elif i in self.snippet1.get_strings():
                    count +=1
        scale = count/lens

        # Show result
        self.show_result(scale)

class Checker_by_Function(Checker):
    '''Inherit __init__ and other methods from the class Checker
    Task: Compare by counting the number of similar properties and methods,
    '''
    def __init__(self, threshold, snippet1, snippet2):
        super().__init__(threshold, snippet1, snippet2)

    # Evaluate the similarity
    def check_similarity(self):
        count = 0
        if self.snippet1.get_language() != self.snippet2.get_language():
            print("The 2 codes are different in language. They can't check similarity")
        else:
            for i in self.snippet2.get_methods():
                if i in self.snippet1.get_methods():
                    count +=1
        scale = count/len(self.snippet2.get_methods())

        # Show result
        self.show_result(scale)

