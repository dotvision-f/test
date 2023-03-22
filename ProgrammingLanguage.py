class ProgrammingLanguage:
    '''
    Input: tên file code, có kèm extension
    Task: lưu tên file, suy ra ngôn ngữ lập trình của file code
    '''
    def __init__(self, file_name: str):
        self.__filename = file_name
        # Lưu 
        self.__language = str(self.__filename).split(".")[-1]
    
    def get_name(self):
        return self.__filename
    
    def set_name(self, name):
        self.__filename = name

    def get_language(self):
        return self.__language

    def read_file(self):
        with open(str(self.__filename), 'r') as f:
            file_text = f.read()
        return file_text