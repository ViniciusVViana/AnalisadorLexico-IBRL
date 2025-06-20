import sys
import re
import textwrap

patterns_list = [
    (r"tralelero|tralala|porcodio|porcoala", "TIPO DE VARIAVEL"),
    (r"lirili|larila", "INICIO E FIM DE ESTRUTURA DE DECISÃO"),
    (r"dunmadin", "INICIO DE LAÇO CONTADO"),
    (r"tung|sahur", "INÍCIO E FIM DE LAÇO DE REPETIÇÃO"),
    (r"chimpanzini", "COMANDO DE SAÍDA DE DADO"),
    (r"batapim", "COMANDO DE ENTRADA DE DADO"),
    (r"delimitare|finitini", "DELIMITADORES DE BLOCOS"),
    (r"saturnita", "COMENTÁRIO"),
    (r"tripi|tropa", "VALORES BOOLEANOS: TRUE, FALSE"),
    (r"[a-z][a-zA-Z0-9]*", "IDENTIFICADORES"),
    (r"\d+", "NÚMEROS INTEIROS"),
    (r"\d+\.\d+", "NÚMEROS PONTO FLUTUANTE"),
    (r"\".*?\"", "STRING"),
    (r"\n", "QUEBRA DE LINHA"),
    (r"    ", "TABULAÇÃO"),
    (r"\s", "ESPAÇOS EM BRANCO"),
    (r"\+|\-|\/|\%|\*", "OPERADORES ARITMÉTICOS"),
    (r"==|!=|>|<|<=|>=", "OPERADORES RELACIONAIS"),
    (r"&&|\|\|", "OPERADORES LÓGICOS"),
    (r"\=", "ATRIBUIÇÃO"),
    (r";", "FIM DE INSTRUÇÃO")
]

class TokenInvalido(Exception):
    def __init__(self, message):
        super().__init__(message)

# a verificação devera ocorrer da seguinte forma iremos analizar o inicio do arquivo e verificar o pattern se encontrado indicar junto com sua linha correspondente e remover, então vai para o proximo pattern
def lex_anal(arch):
    tokens = []
    exceptions = []
    line = 1
    while arch:
        punch = False
        for pattern, desc in patterns_list:
            match = re.match(pattern, arch)
            if match:
                tokens.append((match.group(0), desc, line))
                if tokens[-1][0] == "\n":
                    line += 1
                arch = arch[match.end():]
                punch = True
                break
        if not punch:
            # quero que mostre a linha atual e a proxima linha
            exceptions.append(f"Não foi possível reconhecer este token, verifique a escrita: { textwrap.wrap(arch, width=20)[0] } ... na linha {line}")
            arch = arch[1:]  # Remove o primeiro caractere inválido
    return tokens, exceptions

def main():
    if len(sys.argv) > 1:
        archive = sys.argv[1]
    with open(archive, "r", encoding="utf-8") as file:
        fl = file.read()

    tokens, exceptions = lex_anal(fl)

    if tokens:
        print("Tokens encontrados:")
        for token in tokens:
            print(f"{token[0]} - {token[1]} (Linha {token[2]})")
    if exceptions:
        try:
            raise TokenInvalido("\n\t\t".join(exceptions))
        except TokenInvalido as e:
            print("\t\t\t\t\t\t\t\t\t     ↓")
            print(f"Token inválido: {e}")
            print("\t\t\t\t\t\t\t\t\t     ↑")

if __name__ == "__main__":
    main()