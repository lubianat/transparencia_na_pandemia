#!/usr/bin/env python

"""Tests for `salvador_extractor` package."""

import pytest
from salvador_extractor import salvador_extractor


def test_content():

    deal = salvador_extractor.gazetteDeal("test")

    expected = "test"
    result = deal.filetext

    assert result == expected


def test_process():

    deal = salvador_extractor.gazetteDeal("""
    -PROCESSO Nº: 6567/2020
    -
    """)
    
    deal.get_process()
    
    expected = "6567/2020"
    result = deal.process

    assert result == expected

