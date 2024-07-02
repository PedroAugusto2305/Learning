# javaScript Moderno (ES6+)

## O que é?

## Compatibilidade


## Template Literals

É uma forma de declarar strings, foi introduzida na versão ES6+, utilizaremos o acento grave **``**. As Template Strings permitem a interpolação de strings e quebra de linha automática, com ela podemos adicionar variáveis de forma mais clara e organizada em trechos de string.

**Syntax:**

````js
let lang = "JavaScript"

let str = `Essa linha será
    quebrada automaticamente
    e essa quebrará e terá um espaço no começo.
    Resultado de uma expressão: ${2 + 2}
    Eu gosto muito de ${lang}.`
````

## Arrow Functions

É uma forma diferente de escrever funções anônimas. Não utilizamos o termo **function** mas sim utilizamos uma `=>` após os parâmetros. Não possui os próprios `this`, `arguments`, `super` e `new.target`.
Também permite retornar diretamente uma expressão, caso seja uma função de uma única linha como vemos abaixo na sintaxe.

**Syntax:**

````js
const sum = (a, b) => {
    return a + b;
}

const multiply = (a, b) => a * b;

const double = n => n * 2;
````