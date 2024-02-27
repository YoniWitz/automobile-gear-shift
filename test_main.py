
import unittest
from data_analysis import avg_speed_by_model, recurring_error
from main import main

change_in_gear_file_name = "log_change_in_gear.json"
gear_error_file_name = "log_error.json"
gear_error_for_test_file_name = "log_error_for_test.json"

class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        main(change_in_gear_file_name, gear_error_file_name)

    def test_avg_1(self):
        #arrange
        expectedResult = 56.333333333333336

        #act
        result = avg_speed_by_model(change_in_gear_file_name, "Subaru")
        
        #assert
        self.assertEqual(result, expectedResult)

    def test_avg_2_return_aero_if_model_doesnt_exist(self):
        #arrange
        expectedResult = 0

        #act
        result = avg_speed_by_model(change_in_gear_file_name, "doesntexist")

        #assert
        self.assertEqual(result, expectedResult)

    def test_recurring_error(self):
        #arrange
        expected_length = 0

        #act
        result = recurring_error(gear_error_file_name)

        #assert
        self.assertEqual(len(result), expected_length)

    def test_recurring_error_returns_one_value(self):
        #arrange
        expected_length = 1

        #act
        result = recurring_error(gear_error_for_test_file_name)

        #assert
        self.assertEqual(len(result), expected_length)