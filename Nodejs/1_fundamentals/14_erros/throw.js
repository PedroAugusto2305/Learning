const x = "10";

// checar se x é um número, se não for está errado

if(!Number.isInteger(x)) {
    throw new Error("O valor de x não é um número inteiro!");
}

console.log("Continuando o código...");