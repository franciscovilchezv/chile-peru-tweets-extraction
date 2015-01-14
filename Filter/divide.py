# -*- coding: utf-8 -*-

#Json
import simplejson as json2
import json

#Time
import datetime

ARCHIVO_SALIDA_LOCATION = '../../files/output_location.json'
ARCHIVO_SALIDA_NO_LOCATION = '../../files/output_no_location.json'

ARCHIVOS_ENTRADA = [
    "../../files/output_time.json"
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

    output_location = open(ARCHIVO_SALIDA_LOCATION, 'wb')
    output_no_location = open(ARCHIVO_SALIDA_NO_LOCATION, 'wb')


    for in_file in ARCHIVOS_ENTRADA:

        print "Procesando archivo: " + in_file

        with open(in_file,'r') as f:
            lines = f.readlines()
        
        for line in lines:
            
            try:
                var_json        = json.loads(line)
            
                if ((var_json["coordinates"] != None) or (var_json["geo"] != None) or (var_json["place"] != None)):
                    output_location.write(to_JSON(var_json))
                else:
                    output_no_location.write(to_JSON(var_json))
            except:
                pass

            

    output_location.close()
    output_no_location.close()

    print "...Fin del procesamiento"
    print


main()

