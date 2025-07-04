import sys
import re

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


# ========== Análise Léxica ==========
# Função que realiza a análise léxica do arquivo de entrada
def lex_anal(arch):
    tokens = []
    line = 1
    while arch:
        for pattern, desc in patterns_list:
            match = re.match(pattern, arch)
            if match:
                tokens.append((match.group(0), desc, line))
                if tokens[-1][0] == "\n":
                    line += 1
                arch = arch[match.end():]
                break
            
    return tokens

def main():
    if len(sys.argv) > 1:
        archive = sys.argv[1]
    with open(archive, "r", encoding="utf-8") as file:
        fl = file.read()

    tokens = lex_anal(fl)

    if tokens:
        print("Tokens encontrados:")
        for token in tokens:
            val = token[0]
            if val == "\n":
                val = "\\n"
            elif val == "\t":
                val = "\\t"
            elif val == " ":
                val = "' '"
            print(f"[ \033[34m{val}\033[0m  -  \033[32m{token[1]}\033[0m  -  \033[35mLinha {token[2]}\033[0m ]")

if __name__ == "__main__":
    main()