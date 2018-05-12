#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import linha_do_tempo

grafico = """
digraph {
	/*rankdir=LR;*/
	concentrate = True;
	node[shape=plaintext,fontsize=16];

"""
import eventos
import economia

#economia.classicos()
import reformas
economia.classicos()
economia.marxistas()
economia.neoclassicos()
economia.keynesianos()
economia.neoliberais()
eventos.guerras()
eventos.invencoes()

#inclui linha do tempo
grafico += linha_do_tempo.sequencia_de_datas()
#inclui o autor
grafico += linha_do_tempo.definir_obras()
#ranqueia os itens por data
#ranqueia os eventos por data
grafico += linha_do_tempo.ranquear_por_data()
grafico+= "}"

print grafico
