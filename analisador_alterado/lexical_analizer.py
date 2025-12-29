# -*- coding: utf-8 -*-
#lexical_analizer.py
import re

# ---------------------------------------------
# Palavras reservadas da linguagem Saturnita 🪐
# ---------------------------------------------
RESERVED = {
    "tralalero", "tralala", "porcodio", "porcoala",
    "lirili", "larila",
    "dunmadun", "tung", "sahur",
    "chimpanzini", "batapim",
    "delimitare", "finitini",
    "tripi", "tropa",
    "saturnita"
}

# ---------------------------------------------
# Lista de padrões regulares (em ordem de prioridade)
# ---------------------------------------------
patterns_list = [
    # Comentários
    (r"saturnita.*", "COMENTARIO"),

    # Quebra de linha e espaços
    (r"\n", "QUEBRA DE LINHA"),
    (r"\t", "TABULACAO"),
    (r" ", "ESPACO"),

    # Palavras-chave (devem vir antes dos identificadores)
    (r"tralalero|tralala|porcodio|porcoala", "TIPO DE VARIAVEL"),
    (r"lirili|larila", "INICIO E FIM DE ESTRUTURA DE DECISAO"),
    (r"dunmadun", "INICIO DE LACO CONTADO"),
    (r"tung|sahur", "INICIO E FIM DE LACO DE REPETICAO"),
    (r"chimpanzini", "COMANDO DE SAIDA"),
    (r"batapim", "COMANDO DE ENTRADA"),
    (r"delimitare|finitini", "DELIMITADOR DE BLOCO"),
    (r"tripi|tropa", "VALOR BOOLEANO"),

    # Identificadores (variáveis)
    (r"[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFICADOR"),

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

# ---------------------------------------------
# Mapeamento entre categorias e tokens do parser
# ---------------------------------------------
TOKEN_MAP = {
    "TIPO DE VARIAVEL": "tralalero",  # todas mapeiam para o token 'tralelero'
    "NUMERO INTEIRO": "valor_inteiro",
    "NUMERO REAL": "valor_real",
    "STRING": "string",
    "CARACTERE": "caractere",
    "VALOR BOOLEANO": "VALOR_BOOL",
    "IDENTIFICADOR": "id",
    "OPERADOR ARITMETICO": None,  # usa o próprio símbolo (+, -, etc.)
    "OPERADOR RELACIONAL": None,
    "OPERADOR LOGICO": None,
    "ATRIBUICAO": "=",
    "FIM DE INSTRUCAO": ";",
}

# ---------------------------------------------
# Função principal de análise léxica
# ---------------------------------------------
def lex_anal(code):
    tokens = []
    line = 1

    while code:
        matched = False
        for pattern, token_type in patterns_list:
            match = re.match(pattern, code)
            if match:
                matched = True
                lexeme = match.group(0)
                code = code[match.end():]

                # Ignora espaços, tabs e quebras de linha (exceto para contagem)
                if token_type == "QUEBRA DE LINHA":
                    line += 1
                    break
                elif token_type in ["ESPACO", "TABULACAO"]:
                    break

                # Reporta erro léxico
                elif token_type == "TOKEN INVALIDO":
                    print(f"⚠️ Erro léxico na linha {line}: caractere inválido '{lexeme}'")
                    break

                # Comentário (ignora)
                elif token_type == "COMENTARIO":
                    break

                # Geração de tokens normais
                else:
                    if lexeme in RESERVED:
                        # Palavra reservada: o token é o próprio lexema
                        tokens.append(lexeme)
                    else:
                        mapped = TOKEN_MAP.get(token_type)
                        if mapped:
                            tokens.append(mapped)
                        elif mapped is None:
                            # operadores, etc. -> usa o próprio lexema
                            tokens.append(lexeme)
                        else:
                            tokens.append(token_type)
                    break

        if not matched:
            print(f"⚠️ Erro léxico na linha {line}: caractere inesperado '{code[0]}'")
            code = code[1:]
    return tokens

