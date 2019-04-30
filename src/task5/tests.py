import unittest
from task5.run import  createfirsth, names, birthofchild, Man, Woman


class TestTask(unittest.TestCase):
    def test_createfirsth(self):
        firstpeople = createfirsth()
        self.assertIsInstance(firstpeople[0], Man)
        self.assertIsInstance(firstpeople[1], Woman)

    def test_names(self):
        people = createfirsth()
        self.assertEqual(names(people), ("Adam", "Eva"))

    def test_birthofchild(self):
        people = createfirsth()
        child = birthofchild(people, "Pepinka", "Pepa", 1999, "Bohušice")
        self.assertTrue(isinstance(child, Woman) or isinstance(child, Man))