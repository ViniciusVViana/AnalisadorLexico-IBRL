patterns_list = [
    # Comentários
    (r"saturnita.*", "COMENTARIO"),

    # Quebra de linha e espaços
    (r"\n", "QUEBRA DE LINHA"),
    (r"\t", "TABULACAO"),
    (r" ", "ESPACO"),

    # Palavras-chave
    (r"tralelero|tralala|porcodio|porcoala", "TIPO DE VARIAVEL"),
    (r"lirili|larila", "INICIO E FIM DE ESTRUTURA DE DECISAO"),
    (r"dunmadin", "INICIO DE LACO CONTADO"),
    (r"tung|sahur", "INICIO E FIM DE LACO DE REPETICAO"),
    (r"chimpanzini", "COMANDO DE SAIDA"),
    (r"batapim", "COMANDO DE ENTRADA"),
    (r"delimitare|finitini", "DELIMITADOR DE BLOCO"),
    (r"tripi|tropa", "VALOR BOOLEANO"),

    # Identificadores (após palavras-chave)
    (r"[a-z][a-zA-Z0-9]*", "IDENTIFICADOR"),

    # Literais
    (r"\d+\.\d+", "NUMERO REAL"),
    (r"\d+", "NUMERO INTEIRO"),
    (r"\".*?\"", "STRING"),
    (r"'.*?'", "CARACTERE"),

    # Operadores
    (r"\+|\-|\*|\/|\%", "OPERADOR ARITMETICO"),
    (r"==|!=|>=|<=|>|<", "OPERADOR RELACIONAL"),
    (r"\&\&|\|\|", "OPERADOR LOGICO"),
    (r"=", "ATRIBUICAO"),
    (r";", "FIM DE INSTRUCAO"),

    # Captura qualquer outro caractere (erro léxico)
    (r".", "TOKEN INVALIDO"),
]