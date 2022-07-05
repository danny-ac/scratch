import pytest

from src.add_something import AddSomething


class TestAddSomething:
    """Test the AddSomething Class."""

    @pytest.mark.parametrize(
        "input_value, expected_value",
        [(2, 3), (4, 5), (-1, 0), pytest.param(2, 4, marks=pytest.mark.xfail)],
    )
    def test_add_one_on(self, input_value, expected_value):
        actual_value = AddSomething.add_one_on(input_value)
        assert expected_value == actual_value
