def ValidadorCodigo(texto):
    # primeiro termo é um + ou -
    if not (ord(texto[0]) == 43 or ord(texto[0]) == 45):
        return False
    # verifica se o segundo termo e um espaco
    if not texto[1] == " ":
        return False
    # verifica se os 3 primeiros termos são letras
    for i in range(2,5):
        e = texto[i]
        e = ord(e)
        if not (e >= 65 and e <= 90):
            return False
    # verifica se o codigo está composto por números
    for i in range(5,9):
        e = texto[i]
        e = ord(e)
        if not (e >= 48 and e <= 57):
            return False
    if not (ord(texto[9]) >= 65 and ord(texto[9]) <= 90):
        return False
    if not texto[10] == " ":
        return False
    return True

def PegaHorario(texto):
    # transforma os horarios em uma lista
    texto = texto[11:].split()
    for horario in texto:
        # index da letra
        for l in horario:
            l = ord(l)
            if l >= 65 and l <= 90:
                h_dia_semana = chr(l)
        # h_ind_t = index do horário que contém o turno.
        h_ind_t = horario.find(h_dia_semana)
        # pegando os dias da semana e os horarios
        h_dias_semana = horario[:h_ind_t]
        h_tempos = horario[h_ind_t+1:]
        print(f"Temos aula na {h_dias_semana} no periodo da {horario[h_ind_t]} nos tempos: {h_tempos}")

lista_de_horarios_exemplo = ['2M5', '4M5', '2T1', '4T1']
lista_de_horarios_exemplo = ['246T23']

# definindo a grade horária
g_divisao = "+---------------+----------+----------+----------+----------+----------+----------+"
g_espacamento_interno = " "*10
g_cabecalho = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"
GradeHorária = [g_divisao,g_cabecalho,g_divisao]

# fazendo o loop
while True:
    # input
    inputs = input()
    # criterio de parada
    if inputs == "tchau":
        break
    # mostrador de grade
    if inputs == "?":
        for e in GradeHorária:
            print(e)
    # checa o input OBS TA FALTANDO O VALIDADOR DE HORARIO
    else:
        if not ValidadorCodigo(inputs):
            print(f"!({inputs})")
        else:
            # a parte do codigo ta funcionando
            PegaHorario(inputs)
