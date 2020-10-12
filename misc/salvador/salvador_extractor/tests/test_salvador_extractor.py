#!/usr/bin/env python

"""Tests for `salvador_extractor` package."""

import pytest
from salvador_extractor import salvador_extractor

with open("tests/test_deal.txt", "r") as f:
    test_deal = f.read()


def test_content():

    deal = salvador_extractor.gazetteDeal(test_deal)

    expected = test_deal
    result = deal.filetext

    assert result == expected


def test_process():

    deal = salvador_extractor.gazetteDeal(test_deal)
    
    deal.get_process()
    
    expected = "6567/2020"
    result = deal.process

    assert result == expected


def test_company():

    deal = salvador_extractor.gazetteDeal(test_deal)
    
    deal.get_company()
    
    expected = "PMH PRODUTOS MÉDICOS HOSPITALARES LTDA"
    result = deal.company

    assert result == expected
