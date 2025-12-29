import sys

from utils import lex_anal

__version__ = "1.0.0"

def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python main.py <caminho_do_arquivo>")

    archive = sys.argv[1]
    flag = sys.argv[2] if len(sys.argv) > 2 else "c"


    with open(archive, "r", encoding="utf-8") as file:
        fl = file.read()

    tokens = lex_anal(fl)

    if flag == "f":
        archive_name = archive.split("\\")[-1].split(".")[0] + "_out.txt"
        with open(f"{archive_name}", "w", encoding="utf-8") as out_file:
            if not tokens:
                out_file.write("Nenhum token encontrado.\n")
            else:
                for token in tokens:
                    val = token[0]
                    if val == "\n":
                        val = "\\n"
                    elif val == "\t":
                        val = "\\t"
                    elif val == " ":
                        val = "' '"
                    out_file.write(f"[ {val}  -  {token[1]}  -  Linha {token[2]} ]\n")
        print(f"Tokens escritos em {archive_name} no diretório atual.")
        
    else:
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