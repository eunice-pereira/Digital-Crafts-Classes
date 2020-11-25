// use arrow function same way. Remove function keyword, add fat arrow after argument
const myArrowFunc = (foo) => {
	console.log(foo);
};
myArrowFunc('look new method');

// using return keyword is explicit return
const returnStuff = (arg) => {
	return 'stuff' + arg;
};

let result = returnStuff('my text');
console.log(result);

// implicit return is when a value is returned from a func w/o using return keyword

const newFunc = (arg) => 'stuff' + arg;

let result = newFunc('my text');
console.log(result);
