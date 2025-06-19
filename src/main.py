import sys
import re

patterns_list = [
    (r"tralelero|tralala|porcodio|porcoala", "TIPO DE VARIAVEL"),
    (r"lirili|larila", "INICIO E FIM DE ESTRUTURA DE DECISÃO"),
    (r"dunmadin", "INICIO DE LAÇO CONTADO"),
    (r"tung|sahur", "INÍCIO E FIM DE LAÇO DE REPETIÇÃO"),
    (r"chimpanzini|batapim", "COMANDO DE ENTRADA E SAÍDA"),
    (r"delimitare|finitini", "DELIMITADORES DE BLOCOS"),
    (r"ssturnita", "COMENTÁRIO"),
    (r"tripi|tropa", "VALORES BOOLEANOS: TRUE, FALSE"),
    (r"[a-z][a-zA-Z0-9]*", "IDENTIFICADORES"),
    (r"\d+", "NÚMEROS INTEIROS"),
    (r"\".*?\"", "STRING"),
    (r"\s+", "ESPAÇOS EM BRANCO"),
    (r"\+|\-|\/|\%|\*", "OPERADORES ARITMÉTICOS"),
    (r"==|!=|>|<|<=|>=", "OPERADORES RELACIONAIS"),
    (r"&&|\|\|", "OPERADORES LÓGICOS"),
    (r"\=", "ATRIBUIÇÃO"),
    (r";", "FIM DE INSTRUÇÃO")
]
# a verificação devera ocorrer da seguinte forma iremos analizar o inicio do arquivo e verificar o pattern se encontrado indicar junto com sua linha correspondente e remover, entao vai para o proximo pattern
def lex_anal(arch):
    tokens = []
    line = 1
    while arch:
        punch = False
        for pattern, desc in patterns_list:
            match = re.match(pattern, arch)
            if match:
                tokens.append((match.group(0), desc, line))
                if arch[match.end():].startswith("\n"):
                    line += 1
                arch = arch[match.end():]
                punch = True
                break
        if not punch:
            raise ValueError(f"Unrecognized token in input: {arch[:20]}")
    for token in tokens:
        print(f"{token[0]} - {token[1]} (Line {token[2]})\n")

def main():
    if len(sys.argv) > 1:
        archive = sys.argv[1]
    with open(archive, "r", encoding="utf-8") as file:
        fl = file.read()
    print(fl)
    print("\n--------------\n")
    lex_anal(fl)

if __name__ == "__main__":
    main()