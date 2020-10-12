"""Main module."""
import re

class gazetteDeal():
    """
    A class to describe a deal in a municipal gazette.

    Attributes:
       filetext: A string containing the text of the deal
       process: A string containing the process number
       company: A string containing the name of the company that got the deal
    """

    def __init__(self, filetext):
        self.filetext = filetext
        self.process = ""

    def get_process(self):
        pattern = r'PROCESSO Nº: ([0-9/]+)'
        
        text = self.filetext
        match = re.findall(pattern, text)

        self.process = match[0]

    def get_company(self):
        pattern = r'CONTRATADA: ([a-zA-Z à-úÀ-Ú]+)'
        
        text = self.filetext
        match = re.findall(pattern, text)

        self.company = match[0]

