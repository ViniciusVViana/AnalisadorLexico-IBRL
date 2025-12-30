import re

from .pattern_util import patterns_list

# ========== Análise Léxica ==========
# Função que realiza a análise léxica do arquivo de entrada
def lex_anal(arch):
    tokens = []
    line = 1
    while arch:
        for pattern, desc in patterns_list:
            match = re.match(pattern, arch)
            if match:
                # verificar se a variavel ja foi declarada
                if match.group(0) in [token[0] for token in tokens] and desc == "id" and tokens[-2][1] == "TIPO_DE_VARIAVEL":
                    raise NameError(f"Erro léxico: Identificador '{match.group(0)}' já declarado na linha {line}.")
                tokens.append((match.group(0), desc, line))
                if tokens[-1][0] == "\n":
                    line += 1
                arch = arch[match.end():]
                break
    return tokens