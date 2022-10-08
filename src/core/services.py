from typing import List


class ExponentService:
    """
    It initializes n resources, stores their exponents, and returns them.
    """

    def _init_resources(self, n: int, exponent: int):
        """
        This function initializes the resources list with the numbers from 1 to n, and sets the exponent
        to the value of the exponent parameter.

        :param n: the number of resources
        :type n: int
        :param exponent: The exponent of the power function
        :type exponent: int
        """
        print("[Inside][ExponentService._init_resources]")

        self.resources = [ele for ele in range(1, n + 1)]
        self.exponent = exponent

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

    def _store_exponents(self) -> List[int]:
        """
        > This function stores the exponents of resources and
        returns a list of exponents.
        """

        print("[Inside][ExponentService._store_exponents]")

        self.resources = list(map(self._calculate_exponent, self.resources))
        return self.resources

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

        instance = cls()
        # initialize n resources
        instance._init_resources(n, exponent)
        # store exponents of n resources
        return instance._store_exponents()
