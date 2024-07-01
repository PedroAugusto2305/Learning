import express from "express";

const app = express();
const PORT = 3000; // variável de ambiente

app.get("/", (req, res) => {
  res.send("Olá Mundo!");
});

app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
