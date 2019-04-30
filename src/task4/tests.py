import unittest
from task4.run import accum


class TestTask(unittest.TestCase):

    def test_accum(self):
        self.assertEqual(accum("abcd"), "A-Bb-Ccc-Dddd")
        self.assertEqual(accum("RqaEzty"), "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")
        self.assertEqual(accum("cwAt"), "C-Ww-Aaa-Tttt")
        self.assertEqual(accum(""), "")
        self.assertRaises(Exception, accum, 126)
