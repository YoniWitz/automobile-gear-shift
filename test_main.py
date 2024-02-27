
import unittest
#from data_analysis import avg_speed_by_model
from main import main



class MainTest(unittest.TestCase):
    #def setUp(self):
        

    def test_project_runs(self):
        #arrange
        change_in_gear_file_name = "log_change_in_gear.json"
        gear_error_file_name = "log_error.json"
        model = "Subaru"

        #act
        main(change_in_gear_file_name, gear_error_file_name)

        #assert
        self.assertTrue(True)