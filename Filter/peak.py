# -*- coding: utf-8 -*-
import csv
import heapq
import sys

DELIMITER = ','

def main():

	try:
		N = int(sys.argv[1])
	except:
		print "Modo correcto de ejecucion:"
		print "> python peak.py NUMERO_DE_PICOS"
		sys.exit()

	print "Cantidad de picos hallados: " + str(N)

	with open("../files/rate_march_all.csv", 'rb') as csvfile:
		lines = csv.reader(csvfile, delimiter=DELIMITER, quotechar="'")

		minutes = {}

		for line in lines:
			minutes[int(line[0])] = int(line[1])

		ret = heapq.nlargest(N ,minutes, key=minutes.get)

		minimo = min(minutes.keys())
		maximo = max(minutes.keys())

		for pico in ret:
			valor = minutes[pico]

			inicio = pico
			ant = inicio

			while ((inicio >= minimo) and (minutes[inicio] <= minutes[ant])):
				ant = inicio
				inicio = inicio - 1
				if (inicio == 1899 ):
					inicio = 1859

			inicio = pico
			aft = inicio

			while ((inicio <= maximo) and (minutes[inicio] <= minutes[aft])):
				aft = inicio
				inicio = inicio + 1

				if (inicio == 1860 ):
					inicio = 1900

			print "Pico: " + str(pico) +") " + str(ant) + " - " + str(aft)	

main()