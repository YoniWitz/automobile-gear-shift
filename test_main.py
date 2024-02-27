
import unittest
from data_analysis import avg_speed_by_model
from main import main

change_in_gear_file_name = "log_change_in_gear.json"
gear_error_file_name = "log_error.json"
test_data = "test_data.json"

class MainTest(unittest.TestCase):
    def setUp(self):
        #arrange
        main(change_in_gear_file_name, gear_error_file_name)

    def test_avg_1(self):
        expectedResult = 56.333333333333336
        #act
        result = avg_speed_by_model(change_in_gear_file_name, "Subaru")
        print(result)
        #assert
        self.assertEquals(result, expectedResult)

    def test_avg_2(self):
        expectedResult = 0
        #act
        result = avg_speed_by_model(change_in_gear_file_name, "doesntexist")

        #assert
        self.assertEqual(result, expectedResult)