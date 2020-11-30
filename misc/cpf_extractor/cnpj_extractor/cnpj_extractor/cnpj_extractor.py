"""Main module."""
import re
import pandas as pd
from itertools import zip_longest 
import glob 
 
# Code adapted from https://wiki.python.org.br/Cnpj 
# There may be license issues. If there is a problem, we
# will readily change the code.
def check_cnpj(cnpj: str) -> bool:
    """ 
    Method to validate brazilian cnpjs
    Tests:
    
    >>> print Cnpj().validate('61882613000194')
    True
    >>> print Cnpj().validate('61882613000195')
    False
    >>> print Cnpj().validate('53.612.734/0001-98')
    True
    >>> print Cnpj().validate('69.435.154/0001-02')
    True
    >>> print Cnpj().validate('69.435.154/0001-01')
    False
    """
    # defining some variables
    lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4 , 3, 2]
    lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # cleaning the cnpj
    cnpj = cnpj.replace( "-", "" )
    cnpj = cnpj.replace( ".", "" )
    cnpj = cnpj.replace( "/", "" )

    # finding out the digits
    verificadores = cnpj[-2:]
    
    # verifying the lenght of the cnpj
    if len( cnpj ) != 14:
        return False
    
    # calculating the first digit
    soma = 0
    id = 0
    for numero in cnpj:
        
        # to do not raise indexerrors
        try:
            lista_validacao_um[id]
        except:
            break
            
        soma += int( numero ) * int( lista_validacao_um[id] )
        id += 1
    
    soma = soma % 11
    if soma < 2:
        digito_um = 0
    else:
        digito_um = 11 - soma
    
    digito_um = str( digito_um ) # converting to string, for later comparison
    
    # calculating the second digit
    # suming the two lists
    soma = 0
    id = 0
    
    # suming the two lists
    for numero in cnpj:
        
        # to do not raise indexerrors
        try:
            lista_validacao_dois[id]
        except:
            break
        
        soma += int( numero ) * int( lista_validacao_dois[id] )
        id += 1
    
    # defining the digit
    soma = soma % 11
    if soma < 2:
        digito_dois = 0
    else:
        digito_dois = 11 - soma
    
    digito_dois = str( digito_dois )

    # returnig
    return bool( verificadores == digito_um + digito_dois )


def get_cnpjs(text: str) -> list:
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


def get_cnpjs_from_path(path: str) -> pd.DataFrame:
    """
    Given a path, extract all CNPJs in the .txt files in it

    Arguments
        path: A path to folder with .txts
        which might contain a CNPJ

    Returns
        cnpjs_df: A pandas DataFrame with 3 columns: filenames, for file names, cnpj, and cnpj count 

    """

    # Find all *.txt files in the directory 
    file_name_list = glob.glob(path + "/"+ '*.txt') 
    cnpjs_holder = {}

    for each_file in file_name_list:
        with open(each_file, "r") as f:
            text = f.read()
        cnpjs = get_cnpjs(text)
        cnpjs_holder[each_file] = cnpjs

    # From https://stackoverflow.com/questions/50751184/pandas-dataframe-from-dictionary-of-list-values
    cnpjs_df = pd.DataFrame([(key, var) for (key, L) in cnpjs_holder.items() for var in L], 
                 columns=['key', 'variable'])
    cnpjs_df.columns = ['text', 'cnpj']

    # From https://stackoverflow.com/questions/35584085/how-to-count-duplicate-rows-in-pandas-dataframe
    cnpjs_df = cnpjs_df.groupby(cnpjs_df.columns.tolist()).size().reset_index().rename(columns={0:'count'})
    
    return(cnpjs_df)