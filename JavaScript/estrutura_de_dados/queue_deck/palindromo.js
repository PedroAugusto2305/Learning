import Deque from "./deque.js";

function palidromeChecker(aString) {
  if (
    aString === undefined || aString === null || (aString !== null && aString.length === 0)) {
        return false;
  }

  const deque = new Deque();
  const lowerString = aString.toLowerCase(' ').split().join('');
  let isEqual = true;
  let firstChar, lastChar;
  for(let i = 0; i < lowerString.length; i++) {
    deque.addBack(lowerString.charAt(i));
  }
  while(deque.size() > 1 && isEqual) {
    firstChar = deque.removeFront();
    lastChar = deque.removeBack();
    if(firstChar !== lastChar) {
        isEqual = false;
    }
  }
  return isEqual;
}

console.log('a', palidromeChecker('a'));
console.log('aa', palidromeChecker('aa'));
console.log('kayak', palidromeChecker('kayak'));
console.log('level', palidromeChecker('level'));
console.log('Was it a car or a cat I saw', palidromeChecker('Was it a car or a cat I saw'));
console.log('Step on no pets', palidromeChecker('Step on no pets'));
