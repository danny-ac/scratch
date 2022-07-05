from sre_constants import ASSERT_NOT
from src.add_something import AddSomething


class TestAddSomething:
    """Test the AddSomething Class."""

    def test_add_one_on(self):
        input_value = 2
        expected_value = 3
        actual_value = AddSomething.add_one_on(input_value)
        assert expected_value == actual_value
    
    def test_add_one_onto_2_is_not_4(self):
        input_value = 2
        expected_value = 4
        actual_value = AddSomething.add_one_on(input_value)
        assert expected_value != actual_value