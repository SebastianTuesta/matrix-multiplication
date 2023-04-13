"""File for MatrixInteger class
"""

from __future__ import annotations
from typing import List, Union

class MatrixInteger:
    """Matrix class where all elements are Integer
    """
    def __init__(self, data: List[List[int]]) -> None:
        """__init__ metor

        Args:
            data (List[List[int]]): data that is going to fill the matrix (all integers)
        """

        assert isinstance(data, list), "Data is not a list of list of Integers"
        assert all(isinstance(item, list) for item in data), \
            "Data is not a list of list of Integers"
        assert all([isinstance(l_i, int) for l_i in item] for item in data), \
            "Data is not a list of list of Integers"

        self.n_rows = len(data)
        n_cols = len(data[0])
        self.n_cols = n_cols

        for data_i in data[1:]:
            assert len(data_i) == n_cols, "Not valid matrix, not same cols length accross rows"
        self.matrix = data

    def __add__(self, matrix_b: MatrixInteger) -> MatrixInteger:
        """method that sum two matrix with same n_cols and n_rows

        Args:
            matrix_b (MatrixInteger): matrix with which self class is going to add.
              It must have the same n_cols and n_rows as self class

        Returns:
            MatrixInteger: sum of two matrices
        """
        assert isinstance(matrix_b, MatrixInteger), \
            "matrix_b must be a object of MatrixInteger class"
        assert self.n_cols == matrix_b.n_cols and self.n_rows == matrix_b.n_rows, \
            "The two object MatrixInteger must have same columns and rows"

        result = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]

        for n_row in range(self.n_rows):
            for n_col in range(self.n_cols):
                result[n_row][n_col] = self.matrix[n_row][n_col] + matrix_b.matrix[n_row][n_col]

        return MatrixInteger(result)

    def scalar_multiplication(self, scalar: int) -> MatrixInteger:
        """Scalar multiplication

        Args:
            scalar (int): scalar number

        Returns:
            MatrixInteger: Matrix plus scalar
        """
        assert isinstance(scalar, int), "scalar must be integer"

        result = [[elem*scalar for elem in rows] for rows in self.matrix]
        return result

    def matrix_multiplication(self, matrix_b: MatrixInteger) -> Union[List[int], MatrixInteger]:
        """Multiplication between two matrices.
            N_cols of matrix_a, must be the same as n_rows of matrix_b

        Args:
            matrix_b (MatrixInteger): Matrix which self class will be multiplied

        Returns:
            Union[List[int], MatrixInteger]: Matrix plus matrix
        """
        assert isinstance(matrix_b, MatrixInteger), \
            "matrix_b must be a object of MatrixInteger class"
        assert self.n_cols == matrix_b.n_rows, \
            "Columns of matrix_a must be the same as the row of the matrix_b"

        result = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*matrix_b.matrix)] \
                  for A_row in self.matrix]
        print("result: ", result)
        return result

    def __mul__(self, scalar_or_matrix_b: Union[int, MatrixInteger]) -> \
        Union[List[int], MatrixInteger]:
        """Matrix multiplication or matrix plus scalar, depend of arg datatype

        Args:
            scalar_or_matrix_b (Union[int, MatrixInteger]): Matrix or scalar

        Returns:
            Union[List[int], MatrixInteger]: Multiplication of matrices or 
                matrix plus scalar, depend of arg datatype
        """
        assert isinstance(scalar_or_matrix_b, (int, MatrixInteger)), "Invalid operator"

        if isinstance(scalar_or_matrix_b, int):
            return MatrixInteger(self.scalar_multiplication(scalar_or_matrix_b))
        return MatrixInteger(self.matrix_multiplication(scalar_or_matrix_b))

    def __rmul__(self, scalar_or_matrix_b: Union[int, MatrixInteger]) -> \
        Union[List[int], MatrixInteger]:
        """Matrix multiplication or matrix plus scalar, depend of arg datatype

        Args:
            scalar_or_matrix_b (Union[int, MatrixInteger]): Matrix or scalar

        Returns:
            Union[List[int], MatrixInteger]: Multiplication of matrices or 
                matrix plus scalar, depend of arg datatype
        """
        assert isinstance(scalar_or_matrix_b, (int, MatrixInteger)), "Invalid operator"

        if isinstance(scalar_or_matrix_b, int):
            return MatrixInteger(self.scalar_multiplication(scalar_or_matrix_b))
        return MatrixInteger(self.matrix_multiplication(scalar_or_matrix_b))


    def transpose(self) -> MatrixInteger:
        """Tranpose

        Returns:
            MatrixInteger: Transpose. The n_rows and n_cols are inverted
        """
        result = [[0 for _ in range(self.n_rows)] for _ in range(self.n_cols)]

        for n_col in range(self.n_cols):
            for n_row in range(self.n_rows):
                result[n_col][n_row] = self.matrix[n_row][n_col]

        return MatrixInteger(result)

    def __getitem__(self, key: int) -> Union[list, int]:
        """__getitem__ overwrite

        Args:
            key (int): key

        Returns:
            Union[list, int]: list or int, depends on key
        """
        return self.matrix[key]

    def __repr__(self) -> str:

        result = "["

        for n_row in range(self.n_rows):
            result += "["
            for n_col in range(self.n_cols):
                result += str(self.matrix[n_row][n_col]) + " "

            result = result[:-1]
            result += ']\n'

        result = result[:-1] + "]"
        return result

    def __str__(self):
        """__str__ overwrite

        Returns:
            str: print result
        """
        result = "["

        for n_row in range(self.n_rows):
            result += "["
            for n_col in range(self.n_cols):
                result += str(self.matrix[n_row][n_col]) + " "

            result = result[:-1]
            result += ']\n'
        result = result[:-1] + "]"
        return result

    def __eq__(self, other: MatrixInteger) -> bool:
        """_eq_

        Args:
            other (MatrixInteger): Other matrix

        Returns:
            bool: comparasion
        """
        if not isinstance(other, MatrixInteger):
            return NotImplemented
        return self.matrix == other.matrix
    