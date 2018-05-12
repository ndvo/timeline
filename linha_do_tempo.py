#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os

class Autor():
	todos = []
	lista_datas = {}
	def __init__(self, nome, nascimento, morte, obras):
		self.nome = nome
		self.data_nascimento = nascimento
		self.data_morte = morte
		self.obras = []
		self.todos.append(self)
		self.nascimento = "✩ "+str(nome)
		self.morte = "✝ "+str(nome)
		if nascimento in self.lista_datas:
			self.lista_datas[nascimento] += [self.nascimento];
		else:
			self.lista_datas[nascimento] = [self.nascimento];
		if morte in self.lista_datas:
			self.lista_datas[morte] += [self.morte]
		else:
			self.lista_datas[morte] = [self.morte]
		for i in obras:
			self.obras.append(Obra(i[0], self, i[1]))

	def linha_do_tempo(self):
		linha = ""
		for i in self.obras:
			linha+=i.nome+"->"
		linha = linha[:-2]+";"
		return linha
	
	def lista_obras(self):
		lista = """
		/*"""+self.nome+"""*/
		{
			node[shape=box];
		"""
		for i in self.obras:
			lista+=i.nome+";"	
		lista+="""
		}"""

	def datas(self):
		datas_obras = [i.data for i in self.obras]
		datas = [self.data_nascimento, self.data_morte]+datas_obras
		return sorted(datas)

class Obra():
	def __init__(self, nome, autor, data):
		self.nome= nome
		self.autor = autor
		self.data = data
		if data in autor.lista_datas:
			autor.lista_datas[data] += [nome]
		else:
			autor.lista_datas[data] = [nome]

	def __lt__(self, x):
		if self.data < x.data:
			return True
		else:
			return False

class Event():
	todos = []
	def __init__(self, nome, data, limits=None):
		self.nome = nome
		self.data = data
		if not limits or int(self.data) in range(limits[0], limits[1]):
			self.todos.append(self)


def sequencia_de_datas():
	eventos = set(Autor.lista_datas.keys()+[i.data for i in Event.todos])
	resultado = "\n{node[shape=plaintext, fontsize=20]\n\t"
	formato = "{}->"
	for i in sorted(eventos):
		resultado += formato.format(i)
	resultado = resultado[0:-2]
	resultado += "\n}\n"
	return resultado

def definir_obras():
	resultado = ""
	defineobras = "\t{/*Obras*/\n\tnode[shape=box];\n"
	autores = "\n"
	obra_anterior = None
	counter = 0
	lista_de_obras  =  [obra for item in [i.obras for i in Autor.todos] for obra in item]
	for obra in lista_de_obras:
		counter += 1
		defineobras+='\t"'+obra.nome+'";\n'
		if obra_anterior and obra_anterior.autor == obra.autor:
			anterior = obra_anterior.nome
			new_author = False
		else:
			anterior = obra.autor.nascimento
			new_author = True
		autores += '"'+anterior+'"->"'+obra.nome+'"[style=dotted,color=blue,arrowhead=none];\n'
		if new_author and obra_anterior:
			autores += '"'+obra_anterior.nome+'"->"'+obra_anterior.autor.morte+'"[style=dotted,color=blue];\n'
		obra_anterior = obra
	autores += '"'+obra_anterior.nome+'"->"'+obra_anterior.autor.morte+'"[style=dotted,color=blue];\n'
	defineobras+="\t}\n"
	resultado+=defineobras+"\n"+autores+'\n '
	return resultado

def ranquear_por_data(obras = True, eventos = True):
	resultado = ""
	if obras:
		for key,value in Autor.lista_datas.items():
			resultado+="{rank=same;\n"+str(key)+";"
			for i in value:
				resultado += '"'+str(i)+'" '
			resultado+=";\n}\n"
	if eventos:
		for evento in Event.todos:
			resultado+="{rank=same;\n"+str(evento.data)+";"
			for i in value:
				resultado += '"'+str(evento.nome)+'"[style=filled,shape=box,fontsize=20,fillcolor=gray,color=gray] '
			resultado+=";\n}\n"
	return resultado

	

