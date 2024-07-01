const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000; // variável de ambiente

// render html
const basePath = path.join(__dirname, "templates");


// middleware
const checkAuth = function(req, res, next) {
  req.authStatus = true;

  if(req.authStatus) {
    console.log("Está logado, pode continuar!")
    next();
  } else {
    console.log("Não está logado, faça login para continuar")
  }
}

app.use(checkAuth);

// verbo get básico para acessar a rota principal
app.get("/", (req, res) => {
  res.sendFile(`${basePath}/index.html`);
});

app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
