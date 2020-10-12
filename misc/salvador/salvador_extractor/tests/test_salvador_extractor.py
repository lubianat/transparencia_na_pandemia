#!/usr/bin/env python

"""Tests for `salvador_extractor` package."""

import pytest
from salvador_extractor import salvador_extractor

def test_content():

    deal = salvador_extractor.gazetteDeal("test")

    expected = "test"
    result = deal.filetext

    assert result == expected

