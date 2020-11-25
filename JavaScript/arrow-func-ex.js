// Write an arrow function that accepts a number as an argument and
//multiplies that number by itself and returns the value.

const arrowFunc = (5) => {
	console.log(arrowfunc() * 5);
};

// Write an arrow function that has 2 arguments. Add the two arguments and console.log the results.
const myFunc = (a, b, c, d) => {
	return (a + b + c) / d;
};

//Write an array of names using forEach loop through the array and
//have the callback function be an arrow function that prints will print the index +1 and then the name.

let arr = ['eunice', 'dc students', 'dylan'];
arr.forEach((name, idx) => console.log(`${idx + 1}. ${name}`));
