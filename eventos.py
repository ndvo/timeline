#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from linha_do_tempo import Event


def invencoes(limites = None):
	lista = [
		(1774, "Barco a vapor"),
		(1811, "Prensa a vapor"),
		(1825, "Linha Férrea"),
		(1885, "Automóvel"),
		(1903, "Avião"),
		(1913, "Linha de Montagem Ford T"),
		(1876, "Telefone"),
	]
	create_events(lista, limites)

def guerras(limites=None):
	lista= [
		(1861, "Guerra Civil Americana"),
		(1914, "I Guerra Mundial"),
		(1939, "II Guerra Mundial"),
	]
	create_events(lista, limites)

def acontecimentos(limites=None):
	lista=[
		(1969, "Apolo 11 pousa na Lua"),
		]
	create_events(lista, limites)





def create_events(lista,limites):
	if not limites:
		from linha_do_tempo import Autor
		datas_obras = [obra.data for item in [i.obras for i in Autor.todos] for obra in item]
		limites = (min(datas_obras),max(datas_obras))
	for i in lista:
		if not limites or (i[0] >= limites[0] and i[0] <= limites[1]):
			Event(i[1], i[0])


