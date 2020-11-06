"""Main module."""
import re
import pandas as pd

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


def get_cnpjs_from_folder(folder):
    """
    Given a folder, extract all CNPJs in the .txt files in it

    Arguments
        folder: A path to a folder with .txts
        which might contain a CNPJ

    Returns
        cnpjs_df: A pandas DataFrame with 3 columns: filenames, for file names, cnpj, and cnpj count 

    """

    from itertools import zip_longest 
    import glob 
 
    # Find all *.txt files in the directory 
    file_name_list = glob.glob(folder + "/"+ '*.txt') 
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