
import unittest
from data_analysis import avg_speed_by_model
from main import main



class MainTest(unittest.TestCase):
    #def setUp(self):
        

    def test_project_runs(self):
        #arrange
        change_in_gear_file_name = "change_in_gear.json"
        gear_error_file_name = "log_error.json"
        model = "Subaru"
        #main(change_in_gear_file_name, gear_error_file_name)

        #act
        avg_speed_by_model(change_in_gear_file_name, model)

        #assert
        self.assertTrue(True)