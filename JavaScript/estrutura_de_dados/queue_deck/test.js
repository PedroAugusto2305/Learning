import Queue from "./queue.js";

function hotPotato(elementList, num) {
    const queue = new Queue();
    const elimitatedList = [];

    for(let i = 0; i < elementList.length; i++) {
        queue.enqueue(elementList[i]);
    }

    while(queue.size() > 1) {
        for(let i = 0; i < num; i++) {
            queue.enqueue(queue.dequeue());
        }
        elimitatedList.push(queue.dequeue());
    }
    return {
        elimitatedList: elimitatedList,
        winner: queue.dequeue()
    };
}

const names = ['John', 'Jack', 'Camila', 'Ingrid', 'Carl'];
const result = hotPotato(names, 7);
result.elimitatedList.forEach(name => {
    console.log(`${name} was eliminated from the Hot Potato game.`);
});

console.log(`The winner is: ${result.winner}`);
