import unittest
from exercicio3 import _executa_xn_, martingal
import numpy as np


## exercicio 3:

class TestExercicio3(unittest.TestCase):
    
    def test_exercicio3_xn(self):
        """
        Testa se a variável aleatória está bem cmportada
        """
        expected = [0.5, 1.5]
        result = _executa_xn_()
        self.assertTrue(result in expected)
        
    def test_exercicio3_martingal(self):
        meu_martingal = martingal()
        expected = [0.5, 1.5]
        result = next(meu_martingal)
        self.assertTrue(result in expected)
        
        
if __name__ == '__main__':
    unittest.main()