"""file for test MatrixInteger class
"""
import pytest
from src.matrix_integer import MatrixInteger

class TestMatrixInteger:
    """Test class for MatrixIntger methods
    """
    @pytest.mark.parametrize("matrix, _str", [
        (MatrixInteger([[1],[2],[3]]), \
        "[[1]\n[2]\n[3]]"),
        (MatrixInteger([[5]]), \
        "[[5]]")
    ])
    def test_str(self, matrix, _str):
        """Test function for __str__ method
        """
        assert str(matrix) == _str, "Fail test_str"
    
    @pytest.mark.parametrize("matrix, key, elem", [
        (MatrixInteger([[1,2],[2,3],[3,4]]), \
         1,
        [2,3]),
        (MatrixInteger([[1,2],[2,3],[3,4]]), \
         slice(1,3),
        [[2,3],[3,4]]),
    ])
    def test_get_item(self, matrix, key, elem):
        """Test function for __get_item method
        """
        assert matrix[key] == elem, "Fail test_get_item"

    @pytest.mark.parametrize("matrix_a, matrix_b", [
        (MatrixInteger([[1,2],[2,3],[3,4]]), \
        MatrixInteger([[1,2,3],[2,3,4]])
        ),
    ])
    def test_tranpose(self, matrix_a, matrix_b):
        """Test function for transpose method
        """
        assert matrix_a.transpose() == matrix_b, "Fail transpose"

    @pytest.mark.parametrize("matrix_a, scalar_or_matrix_b, result", [
        (MatrixInteger([[1,2],[2,3],[3,4]]), \
        3,
        MatrixInteger([[3,6],[6,9],[9,12]])
        ),
        (MatrixInteger([[1,2]]), \
        MatrixInteger([[1],[2]]),
        MatrixInteger([[5]])
        ),

    ])
    def test_mult(self, matrix_a, scalar_or_matrix_b, result):
        """Test function for transpose method
        """
        assert matrix_a*scalar_or_matrix_b == result, "Fail mult"

    @pytest.mark.parametrize("matrix_a, matrix_b, result", [
        (MatrixInteger([[1,2],[2,3],[3,4]]), \
        MatrixInteger([[3,6],[6,9],[9,12]]),
        MatrixInteger([[4,8],[8,12],[12,16]])
        )
    ])
    def test_add(self, matrix_a, matrix_b, result):
        """Test function for transpose method
        """
        assert matrix_a + matrix_b == result, "Fail add"
