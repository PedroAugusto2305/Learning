// pilha => LIFO (Last In First Out)

class Stack {
  constructor() {
    this.items = [];
  }

  // adicionando elemento
  push(element) {
    this.items.push(element);
  }

  // removendo elemento
  pop() {
    return this.items.pop();
  }

  // verificando o elemento do topo da pilha
  peek() {
    // o ultimo do array pode ser obtido com o length - 1
    return this.items[this.items.length - 1];
  }

  // verificando se a pilha está vazia
  isEmpty() {
    return this.items.length == 0;
  }

  // verificando o tamanho da pilha
  size() {
    return this.items.length;
  }

  // limpando os elementos da pilha
  clear() {
    this.items = [];
  }
}

const stack = new Stack();

console.log(stack.isEmpty());
stack.push(5);
stack.push(8);
console.log(stack.peek());
stack.push(11);
console.log(stack);
console.log(stack.size());
console.log(stack.isEmpty());
stack.push(15);
stack.pop();
stack.pop();
console.log(stack.size());
