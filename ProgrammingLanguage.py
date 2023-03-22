class ProgrammingLanguage:
    '''
    Input: tên file code, có kèm extension
    Output: Code dưới dạng String
    '''
    def __init__(self, file_name: str):
        self.__filename = file_name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__filename = name

    def get_language(self):
        strs = str(self.__filename).split(".")
        return strs[-1]

    def read_file(self):
        with open(str(self.__filename), 'r') as f:
            file_text = f.read()
        return file_text