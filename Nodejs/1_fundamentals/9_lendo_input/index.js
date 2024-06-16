const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
})

readline.question("Qual a sua linguagem favorita? ", (lang) => {
    if(lang == "Python") {
        console.log("Isso nem é linguagem!")
    } else {
        console.log(`A minha linguagem preferida é: ${lang}`);
    }
    readline.close();
})
