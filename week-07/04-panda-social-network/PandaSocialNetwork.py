class PandaSocialNetwork:
    """docstring for PandaSocialNetwork"""

    def __init__(self):
        self.__pandas = []

    def add_panda(self, panda):
        if panda in self.__pandas:
            raise ValueError(
                "You can't add a panda,\
                 because it's already in the panda list")
        self.__pandas.append(panda)

    def has_panda(self, panda):
        pass

    def make_friends(self, panda1, panda2):
        pass

    def are_friends(self, panda1, panda2):
        pass

    def friends_of(self, panda):
        pass

    def connection_level(self, panda1, panda2):
        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, panda, gender):
        pass

    def get_pandas_list(self):
        return self.__pandas
