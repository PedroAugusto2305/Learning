const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000; // variável de ambiente

// render HTML
const basePath = path.join(__dirname, "templates");

// verbo get básico
app.get("/", (req, res) => {
  res.sendFile(`${basePath}/index.html`);
});

app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
