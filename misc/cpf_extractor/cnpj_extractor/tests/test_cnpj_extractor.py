#!/usr/bin/env python

"""Tests for `cnpj_extractor` package."""

import pytest
import pandas as pd
from cnpj_extractor import cnpj_extractor
from pandas.testing import assert_frame_equal

with open("tests/test_file.txt", "r") as f:
    text = f.read()

def test_that_it_get_cnpjs():
    expected = ["20.247.212/0001-85", "03.435.599/0002-65", "34.846.750/0001-09"]
    result = cnpj_extractor.get_cnpjs(text)

    assert expected == result


def test_that_it_get_cnpjs_for_all_files():
    expected = pd.read_csv("tests/expected_cnpj_df.csv")
    result = cnpj_extractor.get_cnpjs_from_folder("tests")
    assert_frame_equal(expected, result, check_dtype=False)

def test_cnpj_checker():
    expected = True
    result = cnpj_extractor.check_cnpj('53.612.734/0001-98')
    assert expected == result

    expected = False
    result = cnpj_extractor.check_cnpj('53.612.734/0001-99')
    assert expected == result

