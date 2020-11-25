// ex 1.
//Write a function that accepts 3 arguments and returns the value of all the items added together.

function printNumbers(x, y, z) {
	return x + y + z;
}
console.log(printNumbers(1, 2, 3));

//ex 2.
//Write a function that has an anonymous function as the first argument and a number as the second argument.
//the anonymous function needs to console.log something.
//Have the first function count from 0 to the number that the second argument is.
//After it is done counting have it call the anonymous function.
//call the function again with a different function as the argument.

const varFunc = function () {
	console.log('Random sentence.');
};

function newFunction(anonymousFunc, number) {
	let i = 0;
	while (i <= number) {
		console.log(i);
		i++;
	}
	anonymousFunc();
}

// newFunction(varFunc, 5)

// newFunction(function()

// ex. 3
