#!/usr/bin/env python

"""Tests for `cpf_extractor` package."""

import pytest
from cpf_extractor import cpf_extractor

with open("tests/test_file.txt", "r") as f:
    text = f.read()

def test_that_it_get_cnpjs():
    cpf_extractor.get_cnpjs(text)
    cpjs = ["20.247.212/0001-85", "03.435.599/0002-65", "34.846.750/0001-09"]
    """."""
    assert 4 == 5