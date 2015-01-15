# -*- coding: utf-8 -*-

#Json
import simplejson as json2
import json

#Time
import datetime

#String
import re

ARCHIVO_SALIDA_PERU = '../../files/output_presume_peru.json'
ARCHIVO_SALIDA_CHILE = '../../files/output_presume_chile.json'
ARCHIVO_SALIDA_NONE = '../../files/output_presume_none.json'

ARCHIVOS_ENTRADA = [
    "../../files/output_timezone_null.json"
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

    output_presume_peru = open(ARCHIVO_SALIDA_PERU, 'wb')
    output_presume_chile = open(ARCHIVO_SALIDA_CHILE, 'wb')
    output_presume_none = open(ARCHIVO_SALIDA_NONE, 'wb')

    for in_file in ARCHIVOS_ENTRADA:

        print "Procesando archivo: " + in_file

        with open(in_file,'r') as f:
            lines = f.readlines()
        
        for line in lines:

            var_json        = json.loads(line)

            try:
                if (re.search('#vamosperu', var_json["text"], re.IGNORECASE)):
                    output_presume_peru.write(to_JSON(var_json))
                    continue

                if (re.search(ur'#vamosperú', var_json["text"], re.IGNORECASE)):
                    output_presume_peru.write(to_JSON(var_json))
                    continue

                if (re.search('vamos peru', var_json["text"], re.IGNORECASE)):
                    output_presume_peru.write(to_JSON(var_json))
                    continue

                if (re.search(ur'vamos perú', var_json["text"], re.IGNORECASE)):
                    output_presume_peru.write(to_JSON(var_json))
                    continue

                if (re.search('#vamoschile', var_json["text"], re.IGNORECASE)):
                    output_presume_chile.write(to_JSON(var_json))
                    continue

                if (re.search('vamos chile', var_json["text"], re.IGNORECASE)):
                    output_presume_chile.write(to_JSON(var_json))
                    continue

                output_presume_none.write(to_JSON(var_json))
            except:
                pass

    output_presume_peru.close()
    output_presume_chile.close()
    output_presume_none.close()

    print "...Fin del procesamiento"
    print


main()

