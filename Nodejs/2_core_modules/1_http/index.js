const http = require('http');

const PORT = 3000;

const server = http.createServer((req, res) => {
    res.write('Hello HTTP')
    res.end();
})

server.listen(PORT, () => {
    console.log(`Servidor rodando na porta: ${PORT}`);
})