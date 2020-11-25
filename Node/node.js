// Node can run any JS code that does not require DOM or browser.

// ex. 1 console.log from 1 to 100 using node.

// for (i = 0; i <= 100; i++) {
// 	console.log(i);
// }

// create a function that accepts a string as an argument.
//have the program write to the terminal "the cow says {value supplied}"
// call the function 3 times with 3 different strings as the argument.

let myFunc = (a) => console.log(`The cow says ${a}`);
myFunc('moo');
myFunc("I'm excited for the holidays!");
myFunc('eat more plants');

// using the array below, create a new array of just the names using map in node.js
let people = [
	{ name: 'batman', powers: 'none' },
	{ name: 'iron man', power: 'rich' },
	{ name: 'The Hulk', powers: 'being green' },
	{ name: 'Superman', powers: 'Being an Alien' },
];
let names = people.map((people) => {
	return people.name;
});
console.log(names);
