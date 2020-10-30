"""Main module."""
import re

def get_cnpjs(text):
    """
    Given a string, extract all CNPJs in it

    Arguments
        text: A string of text which might contain a CNPJ

    Returns
        cnpjs: A list of all CNPJs in the string

    """

    pattern = r'\d{2}\.\d{3}\.\d{3}/\d{4}\-\d{2}'
    match = re.findall(pattern, text)
    cnpjs = match
    
    return(cnpjs)