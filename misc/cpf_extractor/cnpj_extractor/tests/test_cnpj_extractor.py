#!/usr/bin/env python

"""Tests for `cnpj_extractor` package."""

import pytest
from cnpj_extractor import cnpj_extractor

with open("tests/test_file.txt", "r") as f:
    text = f.read()

def test_that_it_get_cnpjs():
    print(text)
    expected = ["20.247.212/0001-85", "03.435.599/0002-65", "34.846.750/0001-09"]
    result = cnpj_extractor.get_cnpjs(text)

    assert expected == result