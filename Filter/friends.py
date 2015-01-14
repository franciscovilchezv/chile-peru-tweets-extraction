# -*- coding: utf-8 -*-

#Json
import simplejson as json2
import json

#Time
import datetime

#Tweepy
import tweepy
from tweepy import OAuthHandler

ARCHIVO_SALIDA_FRIENDS = '../../files/output_friends.json'

ARCHIVOS_ENTRADA = [
    "../../files/output_no_location.json"
]

def to_JSON(tweet):
    jsonconv = json.dumps(tweet, default=lambda o: o.__dict__, sort_keys=True, indent = 4)

    jsonconv = jsonconv.replace('\n','')
    jsonconv = jsonconv.replace('  ','')
    jsonconv = jsonconv.replace('   ','')
    jsonconv = jsonconv.replace('    ','')
    jsonconv = jsonconv.replace('     ','')
    jsonconv = jsonconv.replace('      ','')
    jsonconv = jsonconv.replace('       ','')

    texto = json2.dumps(jsonconv, separators=(',',':'), sort_keys=True)

    texto = texto.decode('string_escape')
    texto = texto[1:-1]
    return str(texto + "\n")

def main():

    print "Procesando..."

    output_friends = open(ARCHIVO_SALIDA_FRIENDS, 'wb')
    
    auth = tweepy.OAuthHandler('2L6jkxYvo7tCZsi48Bu6hGFFt', 'S7vLdLhhfWSsE8c5QVW3eVRXFS02OQRh2GQABurCG3kjeiqxEV')
    auth.set_access_token('393819808-JQa3Flxu0e43qErgm3zt7iRetREqvdbpkBRmrnzK', 'ffSh4Ra9QpPo8T4JLl03V664MCQj8pIzO2zd3cbXTrqt1')

    api = tweepy.API(auth)

    user = api.get_user("@christy080995")

    ids = []

    for page in tweepy.Cursor(api.friends, screen_name="christy080995").pages():
        ids = []
        ids.extend(page)
        #print ids
        for friend in ids:
            print friend.screen_name





    for in_file in ARCHIVOS_ENTRADA:

        print "Procesando archivo: " + in_file

        with open(in_file,'r') as f:
            lines = f.readlines()
        
        for line in lines:
            
            try:
                var_json        = json.loads(line)
  
            except:
                pass

            

    output_friends.close()

    print "...Fin del procesamiento"
    print


main()

