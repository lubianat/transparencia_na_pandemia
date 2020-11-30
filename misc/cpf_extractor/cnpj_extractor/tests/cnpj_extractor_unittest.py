import pandas as pd
from cnpj_extractor import cnpj_extractor
from pandas.testing import assert_frame_equal
import unittest  

class TestThings(unittest.TestCase):

    def setUp(self):
        with open("tests/test_file.txt", "r") as f:
            self.text = f.read()
        return super().setUp()

    def test_that_it_get_cnpjs(self):
        expected = ["20.247.212/0001-85", "03.435.599/0002-65", "34.846.750/0001-09"]
        result = cnpj_extractor.get_cnpjs(self.text)
        self.assertEqual(expected, result)
    
    def test_that_it_get_cnpjs_for_all_files(self):
        expected = pd.read_csv("tests/expected_cnpj_df.csv")
        result = cnpj_extractor.get_cnpjs_from_path("tests")
        assert_frame_equal(expected, result, check_dtype=False)

    def test_cnpj_checker(self):
        expected = True
        result = cnpj_extractor.check_cnpj('53.612.734/0001-98')
        assert expected == result

        expected = False
        result = cnpj_extractor.check_cnpj('53.612.734/0001-99')
        assert expected == result


if __name__ == '__main__':
    unittest.main()
