import unittest
from exercicio1 import exercicio1
from exercicio3 import _executa_xn_, martingal
from util import validar_matriz
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
        
    def test_validar_matriz(self):
        matrix = np.array([[1,0],[0,1]])
        validar_matriz(matrix, 2)
        self.assertTrue(True)
        
    def test_validarmatriz_tamanhoErrado(self):
        matrix = np.array([[1,2,3,4],[1,2,3,4]])
        try:
            validar_matriz(matrix, 2)
        except ArithmeticError:     
            pass
        except Exception:
            self.fail()
        else:
            self.fail()
        
    
    def test_validarmatriz_NaoEstocastica(self):
        matrix = np.array([[1,0],[1,1]])
        try:
            validar_matriz(matrix, 2)
        except ArithmeticError:     
            pass
        except Exception:
            self.fail()
        else:
            self.fail()
            
    def test_validarmatriz_exercicio1(self):
        matrix = np.matrix([[1/3, 0, 2/3, 0, 0],[1/4,1/2,1/4,0,0],[1/2, 0, 1/2, 0, 0], [0, 0, 0, 0, 1],[0,0,0,2/3,1/3]])
        validar_matriz(matrix, 5)
        self.assertTrue(True)
    
    def test_exercicio1_dadosexercico1(self):
        P = np.matrix([[1/3, 0, 2/3, 0, 0],[1/4,1/2,1/4,0,0],[1/2, 0, 1/2, 0, 0], [0, 0, 0, 0, 1],[0,0,0,2/3,1/3]])
        i, j, epsilon = 1,1,0.1
        exercicio1(P, i, j, epsilon)
        self.assertTrue(True)
        
        
if __name__ == '__main__':
    unittest.main()