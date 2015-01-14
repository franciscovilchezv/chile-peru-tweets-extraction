# -*- coding: utf-8 -*-

#Json
import simplejson as json2
import json

#Time
import datetime

ARCHIVO_SALIDA_HORA = '../../files/output_time.json'

ARCHIVOS_ENTRADA = [
    "../../files/peruvschile_stream.json",
    "../../files/peruvschile_stream2.json",
    "../../files/peruvschile_stream3.json"
]

INICIO_PARTIDO = datetime.datetime.strptime("Fri Oct 10 18:00:00 +0000 2014",'%a %b %d %H:%M:%S +0000 %Y')
FIN_PARTIDO = datetime.datetime.strptime("Fri Oct 10 20:00:00 +0000 2014",'%a %b %d %H:%M:%S +0000 %Y')

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

    id_array = {}

    output = open(ARCHIVO_SALIDA_HORA, 'wb')


    for in_file in ARCHIVOS_ENTRADA:

        print "Procesando archivo: " + in_file

        with open(in_file,'r') as f:
            lines = f.readlines()
        
        for line in lines:
            
            try:
                var_json        = json.loads(line)

                if not(var_json["id_str"] in id_array.keys()):

                    id_array[var_json["id_str"]] = True
                    
                    # Le resto 5 horas por que no se, asi toca.
                    var_json["created_at"] = datetime.datetime.strptime(var_json["created_at"],'%a %b %d %H:%M:%S +0000 %Y') - datetime.timedelta(hours=5)

                    if ((var_json["created_at"] > INICIO_PARTIDO) and (var_json["created_at"] < FIN_PARTIDO)):
                        var_json["created_at"] = str(var_json["created_at"])
                        output.write(to_JSON(var_json))
                    else:
                        pass
            except:
                pass


    output.close()

    print "...Fin del procesamiento"
    print


main()

