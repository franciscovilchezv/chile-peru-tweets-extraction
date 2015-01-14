# -*- coding: utf-8 -*-
import json

import string

import unicodedata

import re

DELIMITER = '|'

ARCHIVO_SALIDA = ''

ARCHIVOS_ENTRADA = [
    "../files/*.json"
]

CARACTERES = [
    '“',
    '¿',
    '►',
    '¡',
    '“',
    '”',
    '«',
    '»',
    '´',
    '`',
    '’'
]
CARACTERES_UTF8 = [u'►', u'“', u'”', u'’', u'´', u'`', u'¿', u'¡', u'«', u'»']

class Tweet:

    id_tweet    = None
    id_author   = None
    tweet_original  = None
    body_tweet  = None
    date        = None
    esRT        = None
    estado      = None
    cant_terminos = None


    def __init__(self):
        self.id_tweet    = None
        self.id_author   = None
        self.tweet_original  = None
        self.body_tweet  = None
        self.date        = None
        self.esRT        = None
        self.estado      = None
        self.cant_terminos = None
        

    def load_json(self,post):
        self.id_tweet    = post["id"]
        self.id_author   = post["user"]["id"]

        texto = post["text"].replace('\n',". ")
        texto = texto.replace('\r'," ")

        self.tweet_original = str(texto.encode('utf-8'))

        self.body_tweet  = str(texto.encode('utf-8'))

        self.date        = post["created_at"]

        if ("retweeted_status" in post.keys()) or ("RT" in self.body_tweet.split()):
            self.esRT = 1
        else: 
            self.esRT = 0

        self.estado      = 0 # Sin calificar (se agina automaticamente de acuerdo a las caritas)
        self.cant_terminos = 0 # se asignara el valor correcto luego de la limpieza

    def load_csv(self,post):
        
        #print post

        self.id_tweet    = post[0]
        self.id_author   = post[1]

        texto = post[2].replace('\n',". ")
        texto = texto.replace('\r'," ")

        self.tweet_original = texto
        self.body_tweet  = texto

        self.date        = post[4]
        self.esRT = post[5]
        self.estado = post[6]
        self.cant_terminos = post[7]

    
    def to_CSV(self):
        output = ""
        output += str(self.id_tweet) + DELIMITER
        output += str(self.id_author) + DELIMITER
        output += str(self.tweet_original) + DELIMITER
        output += str(self.body_tweet) + DELIMITER
        output += str(self.date) + DELIMITER
        output += str(self.esRT) + DELIMITER
        output += str(self.estado) + DELIMITER
        output += str(self.cant_terminos) + "\n"

        return output
    

    def to_sequence(self,tipo):

        if(tipo == 1):
            sequence = [self.id_tweet, self.id_author, self.tweet_original, self.body_tweet, self.date, self.esRT, self.estado, self.cant_terminos]
        else:
            sequence = [self.id_tweet, self.id_author, self.tweet_original, self.body_tweet, self.date, self.esRT, str(0)]

        return sequence


def main():

    print "Procesando..."

    output = open(ARCHIVO_SALIDA, 'wb')
    writer = csv.writer(output, delimiter=DELIMITER, quotechar="'")

    output_original = open(ARCHIVO_SALIDA_ORIGINAL, 'wb')
    writer_original = csv.writer(output_original, delimiter=DELIMITER, quotechar="'")

    for in_file in ARCHIVOS_ENTRADA:

        print "Procesando archivo: " + in_file

        with open(in_file,'r') as f:
            lines = f.readlines()


        # Determino la fuente de donde viene (csv, txt)
        fuente = ""
        

        for line in lines:

                if (line[0] == '"'):
                    line = line[1:-3]
                if(len(line) > 10):
                    vector_tweets.append(line)


        vector_tweets_limpio    = limpieza_de_datos(vector_tweets,fuente)
        vector_tweets_sequence  = sequenciar_tweets(vector_tweets_limpio,1)


    print "...Fin del procesamiento"
    print


main()

