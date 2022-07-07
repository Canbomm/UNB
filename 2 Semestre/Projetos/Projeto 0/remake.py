# funcao que mostra a grade horaria
def printa_grade(grade,espacamento):
    # definindo divisao
    divisao = "+---------------+" + (("-"*espacamento) + "+")*7

    # organizando os dias da semana
    dias_semana = "|               |"
    semana = ["Dom","Seg","Ter","Qua","Qui","Sex","Sab"]
    for dia_semana in semana:
        dias_semana += (" " + dia_semana + ((espacamento-4)*" ") + "|")
    
    # terminando cabecalho
    cabecalho = [divisao,dias_semana,divisao]
    
    # formatando a grade
    grade_formatada = []
    for chave in grade:
        print(chave)
    
    # finalmente printando a grade
    for linha in cabecalho:
        print(linha)
    for linha in grade_formatada:
        print(grade_formatada)

# funcao que verifica se o input esta correto
def verificador(lista,dicionario,espacamento,limites):   
    # tratando os horarios pro modelo ideal: DTH. D = Dia, T = Turno, H = Horario
    horarios = pega_horario(lista[2:],limites)
    # caso o pega_horario encontre algo de errado ele retorna None
    if horarios == None:
        return False,None,espacamento
    
    # verificando se algum horario ja existe caso o usuario queira adicionar
    if lista[0] == "+":
        for horario in horarios:
            if dicionario.get(horario) != None:
                # se caiu aqui o usuario quer adicionar um horario que ja existe
                return False,None,espacamento

    # mudando o espacamento caso necessario, o +2 sao os espacos que vem antes e depois do nome da materia
    tamanho_mat = len(lista[1]) + 2
    if tamanho_mat > espacamento:
        espacamento = tamanho_mat
    
    # retornando True pois tudo foi um sucesso, horarios e espacamento
    return True,horarios,espacamento

# funcao que separa os horarios
def pega_horario(codigos,limites):
    # definindo uma lista para armazenar os horarios tratados
    tratados = []

    # fazendo um for para caso receba mais de um turno
    for horario in codigos:
        # Garantindo que tenha apenas uma letra por horario
        pos_letra = -1

        # encontrando a letra que representa o turno
        for index,caractere in enumerate(horario):
            if caractere == "M" or caractere == "T" or caractere == "N":
                if pos_letra == -1:
                    pos_letra = index
                    turno_atual = caractere
                else:
                    # se entrou aqui, e porque tem mais de uma letra portanto o input ta errado
                    return None
        # se entrar no prox if, e porque percorreu o for inteiro e nao encontrou um turno valido
        if pos_letra == -1:
            return None
        
        # montando os horarios do jeito ideal

        # dias_horarios e uma lista cujo primeiro elemento representa os dias da semana e o segundo os horarios
        dias_horarios = horario.split(turno_atual)
        # fazendo a juncao
        for dia in dias_horarios[0]:
            # verificando se o dia da semana esta correto
            if int(dia) > 7 or int(dia) < 1:
                return None
            for horario in dias_horarios[1]:
                # verificando se o horario nao passou dos limites
                limite = limites.get(turno_atual)
                if int(horario) > limite or int(horario) < 1:
                    return None
                tratados.append(dia + turno_atual + horario)
    # retornando horarios tratados, aqui tudo ocorreu com o esperado
    return tratados

# funcao que adiciona horario
def adiciona_horario(grade,horarios,materia):
    for horario in horarios:
        grade[horario] = materia
    return grade

# funcao que remove horario
def remove_horario(grade,horarios,materia):
    # salvando caso aconteca alguma coisa
    grade_inical = grade

    # removendo os horarios
    for horario in horarios:
        # conferindo se a materia esta correta
        if grade[horario] == materia:
            grade[horario] = None
        else:
            return False,grade_inical
    return True, grade

# definindo variaveis iniciais
grade = {}
espacamento = 4
limites_turnos = {"M":5,"T":6,"N":4}

# loop que le input
while True:
    # pegando input
    entrada = input()
    processada = entrada.split(" ")

    # tratamento de entrada

    if processada[0] == "?":
        # mostra grade horaria
        printa_grade(grade,espacamento)
    
    # adicionando ou removendo horarios
    elif processada[0] == "+":
        # adiciona horario
        verificacao = verificador(processada,grade,espacamento,limites_turnos)
        espacamento = verificacao[2]
        if verificacao[0]:
            grade = adiciona_horario(grade,verificacao[1],processada[1])
        else:
            print(f"!({entrada})")
    elif processada[0] == "-":
        # remove horario
        verificacao = verificador(processada,grade,espacamento,limites_turnos)
        espacamento = verificacao[2]
        if verificacao[0]:
            # removeu e uma lista com 2 itens, caso o primeiro de False, o nome da materia esta errado
            # o segundo item do removeu e so a grade mesmo
            removeu = remove_horario(grade,verificacao[1],processada[1])
            if not removeu[0]:
                print(f"!({entrada})")
            else:
                grade = removeu[1]
        else:
            print(f"!({entrada})")
    
    # encerrando loop
    else:
        break
