from medalhas import obter_pais_por_id


def consultas(medalhas, paises):
	cabecalho = "\n **** Consultas e Estatisticas **** \n"
	menu_consulta = " 1 - Medalhas por Pais \n 2 - Medalhas por Continente \n"\
	" 3 - Paises Sem Medalhas \n 0 - Voltar" \
	 "\n opcao >>> "

	while True:
		opcao = input(cabecalho + menu_consulta)

		if opcao == 0:
			return
		elif opcao == 1:
			medalhas_por_pais(medalhas, paises)
		elif opcao == 2:
			medalhas_por_continente(medalhas, paises)
		elif opcao == 3:
			paises_sem_medalhas(medalhas, paises)
		else:
			print 'Opcao invalida.'


def medalhas_por_pais(medalhas, paises):

	for pais in paises:
		qtd_ouro = qtd_medalha_por_pais(medalhas, pais['id'], 'Ouro')
		qtd_prata = qtd_medalha_por_pais(medalhas, pais['id'], 'Prata')
		qtd_bronze = qtd_medalha_por_pais(medalhas, pais['id'], 'Bronze')
		print '%s -> Ouro: %d -> Prata: %d -> Bronze: %d' % (pais['nome'], qtd_ouro, qtd_prata, qtd_bronze )


def qtd_medalha_por_pais(medalhas, pais_id, tipo_medalha):
	qtd = 0
	for medalha in medalhas:
		if medalha['pais_id'] == pais_id and medalha['medalha'] == tipo_medalha:
			qtd += 1

	return qtd


def medalhas_por_continente(medalhas, paises):
	continentes = ['AMERICA', 'EUROPA', 'ASIA', 'OCEANIA', 'AFRICA']

	for continente in continentes:
		qtd_ouro = qtd_medalha_por_continente(medalhas, paises, continente, 'Ouro')
		qtd_prata = qtd_medalha_por_continente(medalhas, paises, continente, 'Prata')
		qtd_bronze = qtd_medalha_por_continente(medalhas, paises, continente, 'Bronze')
		print '%s -> Ouro: %d -> Prata: %d -> Bronze: %d' % (continente, qtd_ouro, qtd_prata, qtd_bronze )


def qtd_medalha_por_continente(medalhas, paises, continente, tipo_medalha):
	qtd = 0

	for medalha in medalhas:
		pais = obter_pais_por_id(medalha['pais_id'], paises)
		if pais['continente'] == continente and medalha['medalha'] == tipo_medalha:
			qtd += 1

	return qtd

def paises_sem_medalhas(medalhas, paises):

	nomes_paises_medalhistas = paises_com_medalhas(medalhas, paises)

	for pais in paises:
		if pais['nome'] not in nomes_paises_medalhistas:
			print "%s" % pais['nome']



def paises_com_medalhas(medalhas, paises):
	lista_nomes_paises_medalhista = []
	for medalha in medalhas:
		pais = obter_pais_por_id(medalha['pais_id'], paises)
		if pais['nome'] not in lista_nomes_paises_medalhista:
			lista_nomes_paises_medalhista.append(pais['nome'])

	return lista_nomes_paises_medalhista
