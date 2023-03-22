# Check similarity tools

## Member of group 2:
    Trần Văn Độ
    Lê Quang Dũng
    Nguyễn Ngọc Tú
    Nguyễn Duy Anh

## Classes in project
- Class **ProgrammingLanguage**:
```
Input: code file's name, with extension.
Task: save the file name, extract the programming language of the code
```

- Class **CodeSnippet**: Inherit from class **ProgrammingLanguage**
```
Task: Get lists of words or methods
```

- Class **Checker**: Compare 2 codes, take Code 1 as root
```
Input:  threshold: threshold for accepting similarity
        snippet1: Object CodeSnippet của code 1
        snippet2: Object CodeSnippet của code 2
Task: Compare 2 codes and show the result
```

- Class **Checker_by_Word**: Inherit *\_\_init\_\_* and other methods from the class Checker
```
Task: Compare by counting the number of similar words between 2 codes,
remove the keywords available in the programming language.
```

- Class **Checker_by_Function**: Inherit *\_\_init\_\_* and other methods from the class Checker
```
Task: Compare by counting the number of similar properties and methods between 2 codes
```

## Files in project
- *ProgrammingLanguage.py*: stores class **ProgrammingLanguage**
- *CodeSnippet.py*: stores class **CodeSnippet**
- *CodeSimilarityChecker.py*: stores class **Checker**, **Checker_by_Word**, **Checker_by_Function**
- *test.py*: testy code. Check the similarity between code1.py and code2.py
- *main.py*: The tool's command line interface
