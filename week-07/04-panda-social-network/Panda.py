import re


class Panda:
    """docstring for Panda"""

    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def set_email(self, email):
        if(re.match(r"[^@]+@[^@]+\.[^@]+", email)):
            return True
        else:
            return False

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        if self.__gender == "male":
            return True

        return False

    def isFemale(self):
        if self.__gender == "female":
            return True
        return False

    def __str__(self):
        return "{}".format(self.__name)

    def __eq__(self, panda):
        if self.__name == panda.get_name() and\
                self.__email == panda.get_email() and\
                self.__gender == panda.get_gender():
            return True
        return False

    def __hash__(self):
        return hash(self.__email)

