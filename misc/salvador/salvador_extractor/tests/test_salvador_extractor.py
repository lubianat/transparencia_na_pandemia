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


def test_company_id():

    deal = salvador_extractor.gazetteDeal(test_deal)
    
    deal.get_company_id()
    
    expected = "00.740.696/0001-92"
    result = deal.company_id

    assert result == expected


def test_object():

    deal = salvador_extractor.gazetteDeal(test_deal)
    
    deal.get_object()
    
    expected = """Aquisição de Kit para Laboratório: Teste rápido IGM/IGG para coronavirus, para garantir
-o atendimento do Laboratório Central / SMS, no combate ao COVID-19, conforme CI DGAS / LAB.
-CENTRAL Nº 033/2020
-"""
    result = deal.object

    assert result == expected

def test_date():

    deal = salvador_extractor.gazetteDeal(test_deal)
    
    deal.get_date()
    
    expected = "25/05/2020"
    result = deal.date

    assert result == expected

def test_value():

    deal = salvador_extractor.gazetteDeal(test_deal)
    
    deal.get_value()
    
    expected = "4.375.000,00"
    result = deal.date

    assert result == expected