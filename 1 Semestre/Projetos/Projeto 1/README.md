## W.I.P ##

O SIGAA é legal, mas poderia ser melhor! E se algumas funcionalidades fossem integradas? Poder gerenciar sua grade horária ou a alocação de salas tornariam a experiência com o sistema muito melhor. Capaz de atender esta demanda, a turma de APC resolveu implementar o vulgarmente conhecido como SAD (☹️) - Sistema de Apoio ao Discente, uma plataforma flexível que proverá soluções para todos!

A primeira funcionalidade a ser criada é a de gerenciamento de grade horária, de modo que a matrícula no próximo semestre ocorra de forma mais fluida. Implemente as seguintes funcionalidades para os comandos indicados:

* \+ COD DTH1 ... DTHn acrescenta a disciplina COD nos horários DTH1,DTH2,…DTHn. Há um espaço entre cada elemento do comando.
* \- COD DTH1 ... DTHn retira a disciplina COD dos horários DTH1,DTH2,…DTHn. Há um espaço entre cada elemento do comando.
* ? mostra a grade horária semanal.
* Hasta la vista, beibe! interrompe a execução do programa.

Todo COD tem o formato XXX####Y, onde XXX identifica a unidade responsável pela oferta, #### o código da disciplina e Y a turma ofertada no horário. Por exemplo, CIC0004B é a turma B disciplina Algoritmos e Programação de Computadores, que é ofertada pelo Departamento de Ciência da Computação. Cada turma é ofertada em horários específicos no formato DTH, onde D define o(s) dia(s) da semana, T o turno e H a(s) hora(s) da(s) aula(s). Por exemplo, 35M12 são aulas as terças (3) e quintas (5), no período da manhã (M), nos horários 1 e 2. A UnB atua nos três turnos: matutino (M), vespertino (T) e noturno (N) - você pode ver mais detalhes no sítio da instituição.

A exibição da grade deve seguir um formato específico de tabela, que apresenta todos os dias da semana, mas somente os horários com matricula registrada. As linhas horizontais são compostas pelo caractere '-'; as verticais pelo '|' e as interseções pelo '+'. A primeira informação apresenta os dias úteis da semana, representados pelas siglas Seg, Ter, Qua, Qui, Sex e Sab, nesta ordem. As demais informações apresentam, cada uma, um dos horários previstos para aula. A primeira coluna apresenta a duração da aula, e as demais os códigos das disciplinas, se houver a matrícula nesse horário. Sempre há pelo menos um espaço entre os caracteres de linha vertical e o conteúdo.

É garantido que o conjunto de instruções fornecidos é sintaticamente correto. Caso não seja possível atualizar a grade, apresente a mensagem: '!(instr)', onde instr é a instrução fornecida. Exemplos de atualizações não permitidas são a adição de disciplinas com choque de horário e a remoção de uma disciplina que não está na grade.