# -*- coding: utf-8 -*-

#Json
import simplejson as json2
import json

#Time
import datetime

#Division por coordenadas y codigo de pais
ARCHIVO_SALIDA_PERU = '../files/output_coord_peru.json'
ARCHIVO_SALIDA_CHILE = '../files/output_coord_chile.json'
ARCHIVO_SALIDA_OTHER = '../files/output_coord_other.json'
#ARCHIVO_SALIDA_NO_LOCATION = '../files/output_null.json'

ARCHIVOS_ENTRADA = [
    "../files/output_location_noRT.json"
]


def to_JSON(tweet):

    jsonconv = json.dumps(tweet, default=lambda o: o.__dict__, sort_keys=True, indent=4)
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

    output_peru = open(ARCHIVO_SALIDA_PERU, 'wb')
    output_chile = open(ARCHIVO_SALIDA_CHILE, 'wb')
    output_other = open(ARCHIVO_SALIDA_OTHER, 'wb')
    #output_null = open(ARCHIVO_SALIDA_NO_LOCATION, 'wb')

    count_location_PER = 0
    count_location_CHI = 0
    count_other = 0
    count_exception = 0
    count = 0

    for in_file in ARCHIVOS_ENTRADA:

        print "Procesando archivo: " + in_file

        with open(in_file, 'r') as f:
            lines = f.readlines()

        for line in lines:

            try:
                var_json = json.loads(line)
                count += 1

                if var_json["place"]["country"] == "Peru":
                    output_peru.write(to_JSON(var_json))
                    count_location_PER += 1
                elif var_json["place"]["country"] == "Chile":
                    output_chile.write(to_JSON(var_json))
                    count_location_CHI += 1
                else:
                    output_other.write(to_JSON(var_json))
                    count_other += 1
            except:
                count_exception += 1
                print var_json["text"]
                print var_json["coordinates"]["coordinates"]
                pass

    output_peru.close()
    output_chile.close()
    output_other.close()

    print "...Fin del procesamiento"
    print count_location_PER, count_location_CHI, count_other
    print count, count_exception


main()

