class ProgrammingLanguage:
    '''
    Input: code file's name, with extension
    Task: save the file name, extract the programming language of the code
    '''
    def __init__(self, file_name: str):
        self.__filename = file_name
        # Extract the programming language of the code
        self.__language = str(self.__filename).split(".")[-1]
    
    # Get the file name
    def get_name(self):
        return self.__filename
    
    # Set new file name
    def set_name(self, name):
        self.__filename = name

    # Get the programming language
    def get_language(self):
        return self.__language

    # Read the code file, return code as string
    def read_file(self):
        with open(str(self.__filename), 'r') as f:
            file_text = f.read()
        return file_text