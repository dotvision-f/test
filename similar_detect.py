class code_info:

    def __init__(self, code, language: str):
        self.__code = code
        self.__language = language

    def get_string(self, code):       #return a list of code words
        code_string_list = str(self.__code).split(' ')
        return code_string_list

    def len_code(self, code):
        return len(self.get_string())

    def get_method(self, code):       #return all the methods and functions in the code
        list_method = []
        for i in dir(self.__code):
            list_method.append(i)
        return list_method

    def get_len_method(self, code):
        return len(self.get_method())

    def get_code(self):
        code = self.__code
        return code

    def get_language(self):
        language = self.__language
        return language



class similar_string_check(code_info):

    def __init__(self, code, count):
        self.count = 0
        self.code = code

    def so_sanh(self, phrase):
        phrase = phrase
        a = self.get_string()
        for i in a:
            if i in phrase:
                count += 1
        b = self.len_code()
        if count >= 0.5*b:
            print("Same code source!!")
        return count/b


class method_similar_check(code_info):

    def method_similar(self, code2):
        count = 0
        code2 = code2
        method1 = self.get_method()
        for i in method1:
            if i in code2:
                count += 1
        b = self.get_len_method()
        if count >= 0.6*b:
            print("Same code method!!")
        return count/b

