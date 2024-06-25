class Queue {
    constructor() {
        this.count = 0;
        this.lowestCount = 0;
        this.items = {};
    }

    // adiciona elemento no final da fila
    enqueue(element) {
        this.items[this.count] = element;
        this.count++;
    }

    // remove elemento da fila
    dequeue() {
        if(this.isEmpty()) {
            return undefined;
        }
        const result = this.items[this.lowestCount];
        delete this.items[this.lowestCount];
        this.lowestCount++;
        return result;
    }

    // verifica o primeiro elemento da fila
    peek() {
        if(this.isEmpty()) {
            return undefined;
        }
        return this.items[this.lowestCount];
    }

    // verifica o tamanho da fila
    size() {
        return this.count - this.lowestCount;
    }

    // verifica se a fila está vazia
    isEmpty() {
        return this.count - this.lowestCount === 0;
    }
    
    // limpa toda a fila
    clear() {
        this.items = {};
        this.count = 0;
        this.lowestCount = 0;
    }

    toString() {
        if(this.isEmpty()) {
            return '';
        }
        let objString = `${this.items[this.lowestCount]}`;
        for(let i = this.lowestCount + 1; i < this.count; i++) {
            objString = `${objString}, ${this.items[i]}`
        }
        return objString;
    }
}

export default Queue;