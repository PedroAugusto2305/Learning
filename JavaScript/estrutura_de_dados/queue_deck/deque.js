class Deque {
    constructor() {
        this.count = 0;
        this.lowestCount = 0;
        this.items = {};
    }

    // adiciona elemento na frente do deque
    addFront(element) {
        if(this.isEmpty()) {
            this.addBack(element);
        } else if(this.lowestCount > 0) {
            this.lowestCount--;
            this.items[this.lowestCount] = element;
        } else {
            for(let i = this.count; i > 0; i--) {
                this.items[i] = this.items[i - 1];
            }
            this.count++;
            this.lowestCount = 0;
            this.items[0] = element;
        }
    }

    // adiciona elemento no fim do deque
    addBack(element) {
        this.items[this.count] = element;
        this.count++;
    }

    // remove elemento da frente do deque
    removeFront(element) {
        if(this.isEmpty()) {
            return undefined;
        }
        const result = this.items[this.lowestCount];
        delete this.items[this.lowestCount];
        this.lowestCount++;
        return result;
    }

    // remove o último elemento do deque
    removeBack() {
        if (this.isEmpty()) {
            return undefined;
          }
          this.count--;
          const result = this.items[this.count];
          delete this.items[this.count];
          return result;
    }

    // verifica o primeiro elemento do deque
    peekFront() {
        if(this.isEmpty()) {
            return undefined;
        }
        return this.items[this.lowestCount];
    }

    // verifica o último elemento do deque
    peekBack() {
        if (this.isEmpty()) {
            return undefined;
          }
          return this.items[this.count - 1];
    } 


    // verifica o tamanho do deque
    size() {
        return this.count - this.lowestCount;
    }

    // verifica se o deque está vazio
    isEmpty() {
        return this.count - this.lowestCount === 0;
    }
    
    // limpa todo o deque
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

export default Deque;