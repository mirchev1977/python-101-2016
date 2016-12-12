import unittest
from Panda import Panda
from PandaSocialNetwork import PandaSocialNetwork


class TestPanda(unittest.TestCase):
    """docstring for TestPanda"""

    def test_hash(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        dictionary = {}
        dictionary['panda'] = panda
        self.assertEqual(str(dictionary['panda']), 'Ivo')

    def test_set_email(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(panda.set_email("ivo@pandamail.com"), True)
        self.assertEqual(panda.set_email("ivo@pandamail"), False)

    def test_add_panda(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        soc_net = PandaSocialNetwork()
        soc_net.add_panda(panda)
        lst = soc_net.get_pandas_list()
        panda1 = lst[0]
        self.assertEqual(str(panda1), 'Ivo')

        try:
            soc_net.add_panda(panda)
        except ValueError:
            bra = 'this is an error'
            self.assertEqual(bra, 'this is an error')


if __name__ == '__main__':
    unittest.main()
