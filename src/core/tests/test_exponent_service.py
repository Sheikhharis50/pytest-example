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
        ("_input", "_expected_result"),
        [
            ((2, 2), [1, 2]),
            ((-1, -1), []),
            ((-1, 2), []),
            ((2, -1), []),
        ],
    )
    def test_get_exponents(self, mocker, _input, _expected_result):
        mocker.patch(
            "core.services.ExponentService._store_exponents",
            return_value=_expected_result,
        )
        _actual_result = ExponentService.get_exponents(*_input)

        assert _actual_result == _expected_result


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
        ((2, -1), []),
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
