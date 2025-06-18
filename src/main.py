import sys



def main():
    if len(sys.argv) > 1:
        archive = sys.argv[1]
    with open(archive, "r", encoding="utf-8") as file:
        fl = file.read()
    print(fl)

if __name__ == "__main__":
    main()