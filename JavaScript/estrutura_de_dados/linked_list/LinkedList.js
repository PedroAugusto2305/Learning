import defaultEquals from "../utils.js";
import { Node } from "../models/linked_list_models.js";

export default class LinkedList {
  constructor(equalsFn = defaultEquals) {
    this.count = 0; // armazena o número de elementos que temos na lista
    this.head = undefined; // o head é a referência ao primeiro elemento, por isso armazenamos com o this em uma variável
    this.equalsFn = equalsFn; // comparação de igualdade entre os elementos da lista
  }

  // adicionar um novo elemento no final da lista
  push(element) {
    const node = new Node(element); // criando um novo node passando element como seu valor
    let current; // variável que aponta para o item atual da lista

    // o último nó da lista sempre terá um valor undefined ou null como o próximo elemento
    if (this.head == null) {
      // se o head aponta para undefined ou null a lista está vazia
      this.head = node; // então adicionamos o primeiro elemento na lista, então o próximo elemento node será automaticamente undefined
    } else {
      // se a lista não estiver vazia então vamos adicionar um elemento no próximo nó que estiver vazio
      current = this.head; // o current é a referência ao primeiro elemento da lista
      while (current.next != null) {
        // {5} obtém o último elemento da lista
        current = current.next;
      }
      current.next = node; // ligamos o ponteiro next ao nó que deve ser adicionado ao final da lista.
    }
    this.count++; // agora vamos incrementar o tamanho da listas
  }

  // inserir um novo elemento em uma posição específica da lista
  insert(element, position) {}

  // retorna um elemento que está em uma posição específica da lista, se não estiver, retorna undefined
  getEelementAt(index) {}

  // remove elemento da lista
  remove(element) {}

  // devolve o índice de um elemento da lista, se o elemento não estiver na lista retorna -1
  indexOf(element) {}

  // remove um item de uma posição específica da lista
  removeAt(index) {
    // verificar valores fora do intervalo
    if (index >= 0 && index < this.count) { // {1} verificaremos se o index é válido que pode ser 0 até count - 1, se não for válida retorna undefined
      let current = this.head; //{2} referência ao primeiro elemento da lista
      // remove o primeiro item
      if (index === 0) { // {3} vamos remover o primeiro elemento da lista apontando o head para o segundo elemento da lista
        this.head = current.next;
      } else {
        let previous; // {4} elemento que está antes de current
        for (let i = 0; i < index; i++) { // {5} vamos iterar pelos nós da lista ligada até chegar na posição desejada
          previous = current; // {6} faremos uma referência ao elemento que estiver antes de current
          current = current.next; // {7} a variável current sempre fará referência ao elemento atual da lista que estivermos percorrendo com esse laço
        }
        // faz a ligação de previous com o next de current: pula esse elemento para removê-lo
        previous.next = current.next; // {8} remove o nó current ligando o previous.next ao current.next
      }
      this.count--; // {9}
      return current.element; 
    }
    return undefined; // {10}
  }

  // retorna true se a lista ligada não tiver nenhum elemento, false se o tamanho da lista for maior que 0
  isEmpty() {}

  // retorna o número de elemento da lista, é semelhante à propriedade length do array
  size() {}

  // retorna uma representação em string da lista ligada.
  toString() {}
}
