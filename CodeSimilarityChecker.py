from CodeSnippet import *
from abc import ABC, abstractmethod

# Dictionary các từ khoá có sẵn trong các ngôn ngữ lập trình
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
    ###
    '''So sánh CodeSnippet2, lấy CodeSnippet1 làm gốc'''
    def __init__(self, threshold, snippet1, snippet2):
        self.threhold = threshold
        self.snippet1 = snippet1
        self.snippet2 = snippet2
    
    def show_result(self, scale):
        print(f"Similarity {scale*100}%")
        if scale >= self.threhold:
            print("2 code snippets are similar")
        else: 
            print("2 code snippets are dissimilar")

    def check_similairy(self):
        pass


class Checker_by_Word(Checker):
    '''So sánh bằng cách đếm số từ giống nhau giữa 2 CodeSnippet,
    Loại bỏ các từ khoá có sẵn trong ngôn ngữ lập trình.
    '''
    def __init__(self, threshold, snippet1, snippet2):
        super().__init__(threshold, snippet1, snippet2)

    def check_similarity(self):
        count = 0
        lens = len(self.snippet2.get_strings())
        if self.snippet1.get_language() != self.snippet2.get_language():
            print("The 2 codes are different in language. They can't check similarity")
        else:
            for i in self.snippet2.get_strings():
                if i in dict[snippet1.get_language()]:
                    lens -= 1
                elif i in self.snippet1.get_strings():
                    count +=1
        scale = count/lens

        self.show_result(scale)
class Checker_by_Function(Checker):
    '''
    So sánh bằng cách đếm số properties và methods tương tự nhau được sử dụng trong Code
    '''
    def __init__(self, threshold, snippet1, snippet2):
        super().__init__(threshold, snippet1, snippet2)

    def check_similarity(self):
        count = 0
        if self.snippet1.get_language() != self.snippet2.get_language():
            print("The 2 codes are different in language. They can't check similarity")
        else:
            for i in self.snippet2.get_methods():
                if i in self.snippet1.get_methods():
                    count +=1
        scale = count/len(self.snippet2.get_methods())

        self.show_result(scale)

# Test

snippet1 = CodeSnippet('codeSnippet1.py')
snippet2 = CodeSnippet('codeSnippet2.py')

print("Check word")
checker = Checker_by_Word(0.7, snippet1, snippet2)
checker.check_similarity()

print()
print("Check function")

checker2 = Checker_by_Function(0.7, snippet1, snippet2)
checker2.check_similarity()
