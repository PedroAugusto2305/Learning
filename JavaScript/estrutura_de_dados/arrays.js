// criando um array
let daysOfWeek = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  
  for (let i = 0; i < daysOfWeek.length; i++) {
    console.log(daysOfWeek[i]);
  }
  
  // acessando elementos do array
  const fib = [];
  fib[1] = 1;
  fib[2] = 2;
  
  for (let i = 3; i < 20; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  for (let i = 1; i < fib.length; i++) {
    console.log(fib[i]);
  }
  
  // adicionando um elemento no final do array
  let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  console.log(numbers);
  
  numbers[numbers.length] = 10;
  console.log(numbers);
  
  // usando o metodo push
  numbers.push(11);
  console.log(numbers);
  
  numbers.push(12, 13);
  console.log(numbers);
  
  // inserindo elemento na primeira posição
  Array.prototype.insertFirstPosition = function (value) {
    for (let i = this.length; i >= 0; i--) {
      this[i] = this[i - 1];
    }
    this[0] = value;
  };
  
  numbers.insertFirstPosition(-1);
  console.log(numbers);
  
  // usando o metodo unshift
  numbers.unshift(-2);
  console.log(numbers);
  numbers.unshift(-4, -3);
  console.log(numbers);
  
  // remover elementos do final do array
  numbers.pop();
  console.log(numbers);
  
  // remover elemento do inicio do array
  for (let i = 0; i < numbers.length; i++) {
    numbers[i] = numbers[i + 1];
  }
  
  console.log(numbers);
  
  Array.prototype.reIndex = function (myArray) {
    const newArray = [];
    for (let i = 0; i < myArray.length; i++) {
      if (myArray[i] !== undefined) {
        newArray.push(myArray[i]);
      }
    }
    return newArray;
  };
  
  // remove a primeira posição manualmente e executa o reIndex
  Array.prototype.removeFirstPosition = function () {
    for (let i = 0; i < this.length; i++) {
      this[i] = this[i + 1];
    }
    return this.reIndex(this);
  };
  
  numbers = numbers.removeFirstPosition();
  
  console.log(numbers);
  
  numbers.shift();
  console.log(numbers);
  
  // adicionando ou removendo elementos em uma posição especifica
  // removendo
  numbers.splice(5, 3);
  console.log(numbers);
  // adicionando
  numbers.splice(5, 0, 4, 5, 6); // quando passamos o 0 no argumento, significa que não queremos remover nada, mas sim adicionar.
  console.log(numbers);
  
  // arrays bidimensionais
  let averageTemp = [
    [72, 75, 79, 79, 81, 81],
    [81, 79, 75, 73, 73],
  ];
  
  // iterando pelos elementos do array bidimensional
  function printMatrix(myMatrix) {
    for (let i = 0; i < myMatrix.length; i++) {
      for (let j = 0; j < myMatrix[i].length; j++) {
        console.log(myMatrix[i][j]);
      }
    }
  }
  printMatrix(averageTemp);
  
  // arrays multidimensionais
  const matrix3x3x3 = [];
  
  for (let i = 0; i < 3; i++) {
    matrix3x3x3[i] = [];
    for (let j = 0; j < 3; j++) {
      matrix3x3x3[i][j] = [];
      for (let z = 0; z < 3; z++) {
        matrix3x3x3[i][j][z] = i + j + z;
      }
    }
  }
  
  for (let i = 0; i < matrix3x3x3.length; i++) {
    for (let j = 0; j < matrix3x3x3[i].length; j++) {
      for (z = 0; z < matrix3x3x3[i][j].length; z++) {
        console.log(matrix3x3x3[i][j][z]);
      }
    }
  }
  
  // juntando arrays
  const zero = 0;
  const positiveNumbers = [1, 2, 3];
  const negativeNumbers = [-3, -2, -1];
  
  let mergeArray = negativeNumbers.concat(zero, positiveNumbers);
  console.log(mergeArray);
  
  // funções de iteração
  // metodo every
  
  // function isEven(x) {
  //     console.log(x);
  //     return x % 2 === 0 ? true : false;
  // }
  
  let newNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
  
  // simplificando a função isEven
  const isEven = (x) => x % 2 === 0;
  console.log(newNumbers.every(isEven));
  
  // metodo some
  console.log(newNumbers.some(isEven));
  
  // metodo forEach
  newNumbers.forEach((x) => console.log(x % 2 === 0));
  
  // metodo map
  const myMap = newNumbers.map(isEven);
  console.log(myMap);
  
  // metodo filter
  const evenNumbers = newNumbers.filter(isEven);
  console.log(evenNumbers);
  
  // metodo reduce
  console.log(newNumbers.reduce((previous, current) => previous + current));
  
  // iterando com o laço for...of
  
  for (const n of newNumbers) {
    console.log(n % 2 === 0 ? "even" : "odd");
  }
  
  // usando o objeto @@iterator
  
  let iterator = newNumbers[Symbol.iterator]();
  console.log(iterator.next().value);
  console.log(iterator.next().value);
  console.log(iterator.next().value);
  console.log(iterator.next().value);
  console.log(iterator.next().value);
  
  iterator = newNumbers[Symbol.iterator]();
  for (const n of iterator) {
    console.log(n);
  }
  
  // entries, keys e values de array
  
  let aEntries = newNumbers.entries();
  console.log(aEntries.next().value);
  console.log(aEntries.next().value);
  console.log(aEntries.next().value);
  
  aEntries = newNumbers.entries();
  for (const n of aEntries) {
    console.log(n);
  }
  
  const aKeys = newNumbers.keys();
  console.log(aKeys.next());
  console.log(aKeys.next());
  console.log(aKeys.next());
  
  const aValues = newNumbers.values();
  console.log(aValues.next());
  console.log(aValues.next());
  console.log(aValues.next());
  
  // metodo from
  let numbers2 = Array.from(newNumbers);
  let evens = Array.from(newNumbers, (x) => x % 2 == 0);
  
  // metodo Array.of
  
  let numbers3 = Array.of(1);
  let numbers4 = Array.of(1, 2, 3, 4, 5, 6);
  
  // o codigo anterior é o mesmo que:
  // let numbers3 = [1]
  // let numbers4 = [1, 2, 3, 4, 5, 6];
  
  // fazendo copia usando esse metodo
  let numbersCopy = Array.of(...newNumbers);
  
  console.log(numbersCopy);
  
  // metodo fill
  console.log(numbersCopy.fill(1, 3, 5));
  
  let ones = Array(6).fill(1);
  console.log(ones);
  
  // metodo copyWithin
  
  let copyArray = [1, 2, 3, 4, 5, 6];
  copyArray.copyWithin(1, 3, 5);
  
  console.log(copyArray);
  
  // ordenação
  
  console.log(newNumbers.reverse());
  console.log(newNumbers.sort((a, b) => a - b));
  
  // codigo anterior pode ser representado por:
  
  // function compare(a, b) {
  //   if (a < b) {
  //     return -1;
  //   }
  //   if(a > b) {
  //     return 1;
  //   }
  //   // a deve ser igual a b
  //   return 0;
  // }
  
  // numbers.sort(compare);
  
  const friends = [
    { name: "John", age: 30 },
    { name: "Ana", age: 20 },
    { name: "Chris", age: 25 },
  ];
  
  function comparePerson(a, b) {
    if (a.age < b.age) {
      return -1;
    }
    if (a.age > b.age) {
      return 1;
    }
    return 0;
  }
  
  console.log(friends.sort(comparePerson));
  
  // ordenando strings
  
  let names = ["Ana", "ana", "john", "John"];
  console.log(
    names.sort((a, b) => {
      if (a.toLowerCase() < b.toLowerCase()) {
        return -1;
      }
      if (a.toLowerCase() > b.toLowerCase()) {
        return 1;
      }
      return 0;
    })
  );
  
  console.log(names.sort((a, b) => a.localeCompare(b)));
  
  const names2 = ["Maève", "Maeve"];
  
  console.log(names2.sort((a, b) => a.localeCompare(b)));
  
  // Pesquisa
  console.log(newNumbers.indexOf(10));
  console.log(newNumbers.indexOf(100));
  
  newNumbers.push(10);
  console.log(newNumbers.lastIndexOf(10));
  console.log(newNumbers.lastIndexOf(100));
  
  // metodos find e findIndex
  
  let numbersIndex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
  
  function mutipleOf13(element, index, array) {
    return element % 13 == 0;
  }
  
  console.log(numbersIndex.find(mutipleOf13));
  console.log(numbersIndex.findIndex(mutipleOf13));
  
  // metodo includes
  
  console.log(numbersIndex.includes(15));
  console.log(numbersIndex.includes(20));
  
  // convertendo array em string
  
  console.log(numbersIndex.toString());
  const numbersString = numbersIndex.join('-');
  console.log(numbersString);