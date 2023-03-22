from ProgrammingLanguage import *

class CodeSnippet(ProgrammingLanguage):
    '''
    Kế thừa từ class ProgrammingLanguage
    Input: tên file Code.
    Output: 
    '''
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.__code = self.read_file()
        self.__language = self.get_language()

    def get_string(self):
        code_string_list = str(self.__code).split()
        return code_string_list

    def __len__(self):
        return len(self.get_string())

    def get_len_method(self):
        return len(self.get_method())

    def get_code(self):
        code = self.__code
        return code
    
    def get_method(self):       #return all the methods and functions in the code
        list_method = []
        for i in dir(self):
            list_method.append(i)
        return list_method

    def get_code(self):
        return self.__code
