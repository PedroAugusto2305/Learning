const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000; // variável de ambiente

const basePath = path.join(__dirname, "templates");

app.get("/", (req, res) => {
  res.sendFile(`${basePath}/index.html`);
});

app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
