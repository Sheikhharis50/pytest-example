from typing import List


class ExponentService:
    """
    It initializes n resources, stores their exponents, and returns them.
    """

    def __init__(self, n: int, exponent: int) -> None:
        """
        `__init__` is a function that takes in two arguments, `n` and `exponent`, and returns nothing.

        :param n: The number of elements in the array
        :type n: int
        :param exponent: The exponent of the polynomial
        :type exponent: int
        """
        print("[Inside][ExponentService.__init__]")

        self.exponent = exponent
        self.__init__resources__(n)

    def __init__resources__(self, n):
        """
        It creates a list of numbers from 1 to n

        :param n: The number of resources to be created
        """
        print("[Inside][ExponentService.__init__resources__]")

        self.resources = list(map(int, range(1, n + 1)))

    def _calculate_exponent(self, element: int) -> int:
        """
        This function takes an integer as an argument and returns the result of raising that integer to
        the power of the exponent attribute of the class.

        :param element: int
        :type element: int
        :return: The exponent of the element.
        """
        print("[Inside][ExponentService._calculate_exponent]")

        return element**self.exponent

    def _store_exponents(self) -> None:
        """
        > This function stores the exponents of resources.
        """

        print("[Inside][ExponentService._store_exponents]")

        self.resources = list(map(self._calculate_exponent, self.resources))

    @classmethod
    def get_exponents(cls, n: int = 10, exponent: int = 2) -> List[int]:
        """
        > The function `get_exponents` takes a class `cls` and two optional arguments `n` and `exponent`
        and returns a list of `n` exponents of `exponent`

        :param cls: the class that we're calling the method on
        :param n: number of resources, defaults to 10
        :type n: int (optional)
        :param exponent: the exponent of the resource, defaults to 2
        :type exponent: int (optional)
        :return: The exponents of the resources.
        """
        print("[Inside][ExponentService.get_exponents]")

        # initialize n resources
        instance = cls(n, exponent)
        # store exponents of n resources
        instance._store_exponents()

        return instance.resources
