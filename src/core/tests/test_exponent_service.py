import random
from dataclasses import dataclass
from typing import Sequence

import pytest
from django.test import TestCase

from core.services import ExponentService

"""
Django with Pytest Approaches

- I have tried we can only utilize fixture benefit
  of pytest this way but only with driver class.
"""


"""
# =================================================
# Approach # 01 
# =================================================
"""


@dataclass
class FixtureData:
    _input: Sequence[int]
    _expected_result: Sequence[int]


class ExponentServiceApproachOneTests(TestCase):
    def setUp(self) -> None:
        self.fd = {
            "positive": FixtureData((2, 2), [1, 4]),
            "negative": FixtureData((-2, -2), []),
        }
        return super().setUp()

    def test_get_exponents_with_positive_values(self):
        _input, _expected_result = self.fd["positive"].__dict__.values()
        _actual_result = ExponentService.get_exponents(*_input)

        self.assertEqual(_actual_result, _expected_result)

    def test_get_exponents_with_negative_values(self):
        _input, _expected_result = self.fd["negative"].__dict__.values()
        _actual_result = ExponentService.get_exponents(*_input)

        self.assertEqual(_actual_result, _expected_result)


"""
# =================================================
# Approach # 02
# =================================================
"""


@pytest.fixture(scope="session")
def _input():
    return [(2, 2), (-1, -1)]


@pytest.fixture(scope="session")
def _expected_result():
    return [[1, 4], []]


@pytest.fixture(scope="class")
def exponent_service_fixtures(request, _input, _expected_result):
    request.cls._input = _input
    request.cls._expected_result = _expected_result


@pytest.mark.usefixtures("exponent_service_fixtures")
class ExponentServiceApproachTwoTests(TestCase):
    def test_get_exponents_with_positive_values(self):
        _input, _expected_result = self._input[0], self._expected_result[0]
        _actual_result = ExponentService.get_exponents(*_input)

        self.assertEqual(_actual_result, _expected_result)

    def test_get_exponents_with_negative_values(self):
        _input, _expected_result = self._input[1], self._expected_result[1]
        _actual_result = ExponentService.get_exponents(*_input)

        self.assertEqual(_actual_result, _expected_result)


"""
# =================================================
"""

"""
Pytest Approaches

- if we use this approaches we can get all the features of pytest.
- Moreover, Saleor is using the second approach.
- But i think first approach will be more preferable for us
  because of our current code and it will take minimal change.

"""


"""
# =================================================
# Approach # 03
# =================================================
"""


class TestExponentService:
    """
    Pytest finds both `test_` prefixed functions. There is no need to subclass anything,
    but make sure to prefix your class with Test otherwise the class will be skipped.
    """

    @pytest.mark.parametrize(
        ("_input", "_expected_initialization"),
        [
            ((2, 2), [1, 2]),
            ((-1, -1), []),
            ((-1, 2), []),
            ((2, -1), [1, 2]),
        ],
    )
    def test_should_define_service(self, _input, _expected_initialization):
        instance = ExponentService(*_input)

        assert instance.resources == _expected_initialization

    def test_should_not_define_service(self):
        with pytest.raises(TypeError) as e:
            ExponentService()

        assert "required positional argument" in str(e.value)

    @pytest.mark.parametrize(
        ("_input", "_expected_result"),
        [
            ((2, 2), [1, 2]),
            ((-1, -1), []),
            ((-1, 2), []),
            ((2, -1), [1, 2]),
        ],
    )
    def test_get_exponents(self, mocker, _input, _expected_result):
        mocker.patch(
            "core.services.ExponentService._store_exponents", return_value=None
        )

        _actual_result = ExponentService.get_exponents(*_input)

        assert _actual_result == _expected_result

    @pytest.mark.parametrize(
        ("_input", "_initial", "_expected_result"),
        [
            ((2, 2), [1, 2], [4, 4]),  # Positive values
            ((-1, -1), [], []),  # Negative values
            ((-1, 2), [], []),  # Negative number of values with positive exponent
            (
                (2, -1),
                [1, 2],
                [4, 4],
            ),  # Positive number of values with negative exponent
        ],
    )
    def test_store_exponents(self, mocker, _input, _initial, _expected_result):
        mocker.patch(
            "core.services.ExponentService._calculate_exponent", return_value=4
        )
        instance = ExponentService(*_input)

        assert instance.resources == _initial
        instance._store_exponents()
        assert instance.resources == _expected_result

    @pytest.mark.parametrize(
        ("_exponent_input", "_input", "_expected_result"),
        [
            (0, 1, 1),  # Zero exponent
            (2, 2, 4),  # Positive exponent
            (-1, 2, 0.5),  # Negative exponent
            (100, 2, 1_267_650_600_228_229_401_496_703_205_376),  # Large exponent
        ],
    )
    def test_calculate_exponent(self, _exponent_input, _input, _expected_result):
        instance = ExponentService(n=random.randint(1, 100), exponent=_exponent_input)

        assert instance._calculate_exponent(_input) == _expected_result


"""
# =================================================
# Approach # 04
# =================================================
"""


@pytest.mark.parametrize(
    ("_input", "_expected_result"),
    [
        ((2, 2), [1, 2]),
        ((-1, -1), []),
        ((-1, 2), []),
        ((2, -1), [1, 2]),
    ],
)
def test_get_exponents(mocker, _input, _expected_result):
    mocker.patch(
        "core.services.ExponentService._store_exponents",
        return_value=_expected_result,
    )
    _actual_result = ExponentService.get_exponents(*_input)

    assert _actual_result == _expected_result


"""
# =================================================
"""
