let myArr = ['a', 'b', 'c'];
console.log(myArr[0]);

// add to end of array
myArr.push('d');

console.log(myArr);

// remove index
let removed = myArr.pop();
console.log(removed);
console.log(myArr);

// unshift adds to beginnig of array
myArr.unshift('z');
console.log(myArr);

// for loops with arrays

for (let i = 0; i < myArr.length; i++) {
	console.log(myArr[i]);
}

myArr.forEach(function (letter, idx) {
	console.log(letter, idx);
});

// shift removes from front of array

let firstItem = myArr.shift();
console.log(firstItem);
console.log(myArr);
