# -*- coding: utf-8 -*-

#Json
import simplejson as json2
import json

#Time
import datetime

ARCHIVO_SALIDA_LOCATION = '../files/output_location_noRT.json'
ARCHIVO_SALIDA_NO_LOCATION = '../files/output_no_location_noRT.json'

ARCHIVOS_ENTRADA = [
    "../files/output_time.json"
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

    count_noRT = 0
    count_RT = 0
    count_location = 0
    count_no_location = 0
    count_total = 0
    count_except = 0
    no_location = False

    for in_file in ARCHIVOS_ENTRADA:

        print "Procesando archivo: " + in_file

        with open(in_file, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            
            try:
                var_json = json.loads(line)
                count_total += 1

                if ((var_json["coordinates"] != None) or (var_json["geo"] != None) or (var_json["place"] != None)):
                    output_location.write(to_JSON(var_json))
                    count_location += 1
                    count_noRT += 1
                    no_location = True
                else:
                    no_location = False
                    if var_json["retweeted_status"] != None:
                        count_RT += 1
                        continue
                    #output_no_location.write(to_JSON(var_json))
                    #count_no_location += 1
                    #count_noRT += 1
            except:
                if not no_location:
                    count_except += 1
                    output_no_location.write(to_JSON(var_json))
                    count_no_location += 1
                    count_noRT += 1
                pass

    output_location.close()
    output_no_location.close()

    print "...Fin del procesamiento"
    print count_noRT, count_RT, count_except
    print count_location, count_no_location
    print count_total

main()

