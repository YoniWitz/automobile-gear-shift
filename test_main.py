
import unittest
from data_analysis import avg_speed_by_model
from main import main

change_in_gear_file_name = "log_change_in_gear.json"
gear_error_file_name = "log_error.json"
test_data = "test_data.json"

class MainTest(unittest.TestCase):
    def setUp(self):
        main(change_in_gear_file_name, gear_error_file_name)

    def test_avg(self):
        avg_speed_by_model(change_in_gear_file_name, "Subaru")