import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test19(self):
        input = """
    Function: main
    Body:
    For (i=1,i>10,1) Do 
    EndFor.
    Break;
    EndBody.
    """
        expect = "Error on line 4 col 14: >"
        self.assertTrue(TestParser.checkParser(input, expect, 319))