#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from linha_do_tempo import Autor

def classicos():
	Autor("Adam Smith",1723, 1790, [
		("Teoria dos Sentimentos Morais",1759),
		("A riqueza das Nações", 1776)])
	Autor("David Ricardo",1772,1823,[
		("The High Price of Bullion, a Proof of the Depreciation of Bank Notes", 1810),
		("Essay on the Influence of a Low Price of Corn on the Profit of Stock", 1815),
		("On the Principles of Political Economy and Taxation", 1817)
		] );
	Autor("John Stuart Mill", 1806, 1873, [
		("Sistema de Lógica Dedutiva", 1843),
		("Princípios de Economia Política",  1848),
		("A Liberdade", 1859),
		("Utilitarismo", 1861),
		("O Governo Representativo", 1861),
		("Sujeição das mulheres", 1869),
	])

def marxistas():
	Autor("Karl Marx",1818,1883, [
		("A questão judaica", 1843),
		("A Ideologia Alemã",1846), 
		("O Manifesto do Partido Comunista",1848),
		("O 18 brumário de Luís Bonaparte", 1852),
		("O Capital",1867),
		("A guerra civil na França", 1871),
		])

def neoclassicos():
	Autor("Léon Walras", 1834, 1910, [
		("Elementos de Economia Pura", 1874),
	])
	Autor("William Stanley Jevons", 1835, 1882, 
		[
		("General Mathematical Theory of Political Economy", 1859),
		("A Serious Fall in the Value of Gold, Edward Stanford.", 1863),
		("Pure Logic; or, the Logic of Quality apart from Quantity", 1864),
		("The Coal Question", 1865),
		("The Substitution of Similars, The True Principle of Reasoning", 1869),
		("Elementary Lessons on Logic", 1870),
		("The Theory of Political Economy", 1871),
		("Principles of Science", 1874),
		("Money and the Mechanism of Exchange", 1875),
		("A Primer on Political Economy", 1878),
		("Studies in Deductive Logic", 1880),
		("The State in Relation to Labour", 1882),
		]
	)
	Autor("Carl Menger", 1840, 1921, [
		("Principles of Economics¹", 1871 ),
		("Investigations into the Method of the Social Sciences with Special Reference to Economics", 1883 ),
		("The Errors of Historicism in German Economics", 1884 ),
		("The Theory of Capital", 1888 ),
		("Money", 1892 ),
		])
	Autor("Alfred Marshall", 1842, 1924, [
		("The Economics of Industry (with Mary Paley Marshall)", 1879 ),
		("The Pure Theory of Foreign Trade: The Pure Theory of Domestic Values", 1879.1 ),
		("Principles of Economics", 1890 ),
		("Industry and Trade", 1919 ),
	])

def institucionalistas():
	Autor("Thorstein Veblen", 1857, 1929, [
		("The Theory of the Leisure Class", 1899),
		("The Theory of Business Enterprise", 1904),
		("The Instinct of Workmanship", 1914),
		("Imperial Germany and the Industrial Revolution", 1915),
		("The Higher Learning in America", 1918),
		("Absentee Ownership", 1923)]
		)
	Autor("Max Weber", 1864, 1920, [
		("A história das companhias comerciais na idade média", 1889),
		("O direito agrário romano e sua significação para o direito público e privado", 1891),
		("O Estado Nacional e a Política Econômica", 1895),
		#("A objetividade do conhecimento na ciência política e na ciência social", 1904),
		("A ética protestante e o espírito do capitalismo", 1904),
		("A situação da democracia burguesa na Rússia", 1905),
		#("A transição da Rússia a um regime pseudoconstitucional", 1905),
		("As seitas protestantes e o espírito do capitalismo", 1906),
		("Sobre algumas categorias da sociologia compreensiva", 1913),
		#("Ensaios Reunidos de Sociologia da Religião", 1920),
		#("Parlamento e Governo na Alemanha reordenada", 1917),
		("A ciência como vocação", 1917),
		("O sentido da neutralidade axiológica nas ciências políticas e sociais", 1918),
		#("Conferência sobre o Socialismo", 1918),
		#("A política como vocação", 1919),
		("História Geral da Economia", 1919),
		#("Economia e Sociedade", 1921),
	])

def keynesianos():
	Autor("John Maynard Keynes", 1883, 1946, [
		("As consequências econômicas da paz", 1919),
		("The end of laissez-faire", 1926),
		("Tratado sobre a moeda",1930),
		("Teoria geral do emprego, do juro e da moeda",1936),
	
	])

def neoliberais():
	Autor("Friedrich Hayek", 1899, 1992, [
		("Monetary Theory and the Trade Cycle", 1929),
		("Prices and Production", 1931),
		("Monetary Nationalism and International Stability", 1937),
		("Profits, Interest and Investment - and other essays on the theory of industrial fluctuations", 1939),
		("O caminho da servidão", 1944),
		("Individualism and Economic Order", 1948),
		("The Counter-Revolution of Science: Studies on the Abuse of Reason", 1952),
		("The Constitution of Liberty", 1960),
		("Studies in Philosophy, Politics and Economics", 1967),
		("A Tiger by the Tail", 1972),
		("Law, Legislation and Liberty", 1973),
		("Denationalisation of Money", 1976),
		("New Studies in Philosophy, Politics, Economics and the History of Ideas", 1978),
		("1980s Unemployment and the Unions", 1980),
		("The Fatal Conceit: The Errors of Socialism", 1989),
	])
