from ProgrammingLanguage import *

class CodeSnippet(ProgrammingLanguage):
    '''
    Inherit from class ProgrammingLanguage
    Input: code file's name
    Task: Get lists of words or methods
    '''
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.__code = self.read_file()

    # Get the number of properties and methods used in the code
    def get_len_method(self):
        return len(self.get_method())

    # get the code as string
    def get_code(self):
        return self.__code
    
    # Get a list of words in the code
    def get_strings(self):
        code_string_list = str(self.__code).split()
        return code_string_list

    # get a list of all properties và methods in the code
    def get_methods(self):
        list_method = []
        for i in dir(self):
            list_method.append(i)
        return list_method


