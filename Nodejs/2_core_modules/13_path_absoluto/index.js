const path = require("path");

// path absoluto
console.log(path.resolve("test.txt"));

// formar path
const midFolder = "relatorios";
const fileName = "pedro.txt";
const finalPath = path.join("/", "arquivos", midFolder, fileName);

console.log(finalPath);
