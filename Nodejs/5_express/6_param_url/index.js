const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000; // variável de ambiente

// render html
const basePath = path.join(__dirname, "templates");

app.get("/users/:id", (req, res) => {
  const id = req.params.id;

  console.log(`Estamos buscando pelo usuário: ${id}`);
  res.sendFile(`${basePath}/users.html`)
})


// verbo get básico para acessar a rota principal
app.get("/", (req, res) => {
  res.sendFile(`${basePath}/index.html`);
});

app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
