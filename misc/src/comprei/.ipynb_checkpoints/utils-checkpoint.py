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
import pandas as pd
import seaborn as sns


def get_2d_representation(file_content_splitted):
    vectorizer = TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('portuguese'))
    X = vectorizer.fit_transform(file_content_splitted)
    SVD = TruncatedSVD(n_components=2).fit(X)
    data2D = SVD.transform(X)
    return(data2D)



def plot_corpus(file_content_splitted):
    n_matches = str(len(file_content_splitted))
    print( 'there are ' + n_matches + " matches")
    print('\n')
    vectorizer = TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('portuguese'))
    X = vectorizer.fit_transform(file_content_splitted)
    SVD = TruncatedSVD(n_components=2).fit(X)
    data2D = SVD.transform(X)
    plt.scatter(data2D[:,0], data2D[:,1])
    plt.show()
    
def print_tipos():
        print("""
     Tipos possíveis:
     1 - compra (de ventilador ou acessório)
     2 - reparo/manutenção (de ventilador ou acessório)
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
        "6" : "outro"}
    
    return([tipo2name[k] for k in classes])
        
    
    
    
def plot_corpus_with_classes(df, filename):
    print_tipos()
    g = sns.scatterplot(x="d1", y="d2",
              hue="classes",
              data=df);

    plot = g.get_figure()
    plot.savefig(filename)
    
    
def classificar(file_content_splitted):
    classes = []

    if input('classificar?(y/n)') == 'y':
        for i in file_content_splitted:
            print(i)
            print_tipos()
            class_of_snippet = input("Qual é o tipo que mais se aproxima desse snippet?")

            classes.append(class_of_snippet)
            clear_output()
    
    return(classes)
    print(classes)