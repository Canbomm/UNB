with open("ENM20211.csv", encoding="UTF-8") as arquivo:
    cabecalho = (next(arquivo)).rstrip()
    for linha in arquivo:
        dados = (linha.rstrip()).split(",")
        lixo = dados.pop(3),dados.pop(5),dados.pop(6),dados.pop(4)
        
        # criando o dic_carga
        docente,carga = (dados[3]).split("(")
        docente = docente[:-1]
        carga = int(carga[:-2])
            
        codigo = dados[0]
        disciplina = dados[1]
        turma = (f"Turma {dados[2]}")
        alunos = (f"{dados[4]} alunos")

        