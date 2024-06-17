const http = require('http');

const PORT = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 400;
  res.setHeader('Content-type', 'text/html');
  res.end('<h1>Olá, este é meu primeiro server com HTML!</h1>')
})

server.listen(PORT, () => {
    console.log(`Servidor rodando na porta: ${PORT}`);
})