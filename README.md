# AnalisadorLexico-IBR
Linguagem desenvolvida para a matéria de compiladores, ela é baseada nos Brainrots italianos onde basicamente alteramos as palavras comuns de um programa para o nome de alguns Brainrots italianos.
Em seguida estaremos definindo as especificações da linguagem.
## Tipos de dados
|Tipo|IBR|
|---|---|
|inteiro|tralalero|
|float|tralala
|caracter|porcodio|
|boolean|porcoala|
## Operadores
|Tipo do operador|Símbolos|Exemplos|
|---|---|---|
Aritméticos|+,-,*,/,%| a + b, x * 2
Relacionais| ==, !=, >, <, <=, >=| a == b, x >= 10
Lógicos| && (e), \|\|(ou)|
## Identificadores
- Devem começar com uma letra minúscula.
- Podem conter letras (maiúsculas e minúsculas) e números.
- Não pode haver espaços ou separadores no meio do identificador.

    |Exemplo|Válido|
    |---|---|
    |variavel1|sim|
    |contador|sim|
    |resultadoFinal|sim|
    |1variavel|não|
    |Resultado|não|


# Preparação para execução do analisador léxico
Para rodar o analisador crie o ambiente virtual para poder instalar todos os requisitos necessários:
```
python -m venv venv
```
E para ativar o ambiente rode o seguinte script:
```
.\venv\Script\activate
```
E então instalar os requisitos:
```
pip install requirements.txt
```