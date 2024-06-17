# Node Fundamentals

## 1. Módulos

### 1.1 O que são?

Os módulos são scripts reaproveitáveis, que utilizamos para criar aplicações NodeJS.
Os módulos são divididos em três categorias: 
- Internos: módulos que o próprio desenvolvedor criou na sua aplicação;
- Core Modules: são módulos que vem com o NodeJS;
- Externos: são módulos que foram criados por outros desenvolvedores e podem ser instalados através do npm.

### 1.2 Módulos Internos

São módulos que foram criados dentro da nossa aplicação, para usarmos esses módulos precisamos exportar a função ou arquivo que compõem o módulo e então importar onde queremos dentro da aplicação. Podemos realizar a importação de duas formas, sendo uma com o ``require`` e outra com o ``import`` que veio junto com o ESmodules.

### 1.3 Export e Import

Com o NodeJS também é possível utilizar o export e import do ES6, que são funcionalidades mais modernas de importação e exportação. Essas funcionalidades possuem mais recursos do que a funcionalidade anterior ```require``. 
Para utilizarmos esse modo de exportação e importação precisamos de algumas configurações sendo elas:

No arquivo JSON precisamos adicionas a seguinte configuração:
````json
{
  "type": "module",
}
````

Após isso poderemos utilizar o ``export`` e o ``import`` em todo nosso projeto.

Abaixo podemos conferir algumas implementações da sintax do ``export`` e do ``import``:

#### Export

````js
function sum(a, b) {
    return a + b;
}

export default sum;
````

````js
export function sum(a, b) {
    return a + b;
}
````

````js
module.exports = {
    sum(a, b) {
        return a + b;
    }
} 
````

#### Import
````js
import <modulo que será importado> from "caminho do módulo";
````

**Obs: podemos importar diversas funções de um mesmo módulo de uma só vez, como vemos abaixo.**
````js
import { <modulo_1>, <modulo_2>, ... } from "caminho do módulo";
````

### 1.4 Core Modules

Os Core Modules são funcionalidades nativas do NodeJS, elas resolvem diversos tipos de problemas como: trabalhar com arquivos, servir aplicações e etc.
Também precisamos importar os Core Modules no projeto, para que possam ser utilizados. 

**Exemplo de um Core Module:**

```js
const path = require('path');

const extension = path.extname("arquivo.pdf");
console.log(extension);

```

No exemplo temos o Core Module Path, que pode ser usado para identificar extensões de arquivos.

### 1.5 Módulos Externos

São os módulos que precisam ser instalados via ``npm``, para instalar esses módulos precisamos inicializar nosso projeto via terminal com o comando ``npm init``. 
A partir daí, todos os módulos ficam mapeados e podemos instalar qualquer módulo via ``npm``.
Quando instalamos os módulos, eles ficam em uma pasta chamada **node_modules** para instalar módulos utilizamos o comando ``npm install <nome_do_modulo>``

## 2. Events

Os eventos são parte fundamental na arquitetura do NodeJS, eles permitem o desenvolvimento de aplicações assíncronas e não bloqueantes. O sistema de eventos do NodeJS é baseado no padrão observador, onde um objeto (emissor) emite os eventos, e os outros objetos (ouvintes) respondem a esses eventos.

### 2.1 Event Loop

O NodeJS executa uma linha por vez, de cima para baixo do código, o event loop nos ajuda a evitar problemas de concorrência, garantindo a execução do código. Precisamos apenas cuidar pccom bloqueios no fluxo, como loops infinitos;

### 2.2 Event Emitter

O Event Emitter se comporta como os eventos do navegador, podemos ativar um código em alguns pontos da aplicação, como o início. É um Core Module chamado events, precisamos instanciar uma class EventEmitter que vem deste módulo, e então podemos utilizá-lo em nossa aplicação.

## Sync e Async

No NodeJS temos duas opções ao executar métodos: 
- Forma síncrona: o código espera ser totalmente executado para prosseguir;
- Forma assíncrona: o código continua progredindo e em um ponto futuro obtém a resposta da execução assíncrona. 

## Erros no NodeJS

Temos duas formas principais para gerar ou evidenciar erros em NodeJS:
- throw: uma froma de encerrar um programa, gerando um novo erro;
- try catch: uma forma de evidenciar algo que deu errado em um bloco de código e exibir a mensagem de erro.
