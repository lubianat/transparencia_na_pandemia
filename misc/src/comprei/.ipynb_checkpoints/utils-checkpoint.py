import pandas as pd
import numpy as np
import pprint 
import os

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.decomposition import TruncatedSVD

import matplotlib.pyplot as plt
from IPython.display import clear_output
import seaborn as sns


def plot_corpus(corpus):
    """
    
    Plots a 2D representation of the corpus.
    
    Args:
        corpus: A list of text documents, each in a separate string. 
        
   
    """
    print( 'there are ' + str(len(corpus)) + " matches" + '\n')
    vectorizer = TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('portuguese'))
    X = vectorizer.fit_transform(corpus)
    SVD = TruncatedSVD(n_components=2).fit(X)
    data2D = SVD.transform(X)
    
    plt.scatter(data2D[:,0], data2D[:,1])
    plt.show()
    
def print_tipos():
        print("""
     Tipos possíveis:
     1 - compra     
     2 - reparo
     3 - aviso de convocação para licitação
     4 - registro de preços
     5 - licitação fracassada
     6 - outro    
    """)
    
def descrever_tipo(classes):
    
    tipo2name= {"1" : "compra",
        "2" : "reparo",
        "3" : "aviso de licitação",
        "4" : "registro de preços",
        "5" : "licitação fracassada",
        "6" : "outro",
        "-1": "não anotado"}
    
    return([tipo2name[k] for k in classes])
        
    
    
    
def plot_corpus_with_labels(df, filename):
    print_tipos()
    g = sns.scatterplot(x="d1", y="d2",
              hue="labels",
              data=df);

    plot = g.get_figure()
    plot.savefig(filename)
    
    
def classificar(df):
    """
    
    
    Args
        A dataframe with columns for text and id
        
    Returns
        dict: A dictionary with the user defined classes.
        
    
    
    """
    classes = {}
    for i, row in df.iterrows():
        classes[row["id"]] = "unlabeled"
        

    for i, row in df.iterrows():
        print(row["text"])
        print_tipos()
        counter = " - " + str(i+1) + "/" + str(len(classes)) 
        message = "Qual é o tipo que mais se aproxima desse snippet?" + counter
        class_of_snippet = input(message)

        classes[row["id"]] = class_of_snippet
        clear_output()

        if input('continuar?(y/n)') == 'n':
            break
                
    
    return(classes)
    print(classes)
    
def get_2d_representation(file_content_splitted):
    vectorizer = TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('portuguese'))
    X = vectorizer.fit_transform(file_content_splitted)
    SVD = TruncatedSVD(n_components=2).fit(X)
    data2D = SVD.transform(X)
    return(data2D)
