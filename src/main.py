import sys

from utils import lex_anal

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