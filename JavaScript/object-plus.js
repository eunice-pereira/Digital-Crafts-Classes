// operator to output what data type an item is.

console.log(typeof 'yes'); //string
console.log(typeof new String('yes')); // object

/* instanceof is an operator that will compare value with a given object to
check if indeed is instance of object */

'yes' instanceof Object; //false
new String('yes') instanceof Object; // true

let myString = 'yes';
let anotherString = new String('yes');

console.log(myString, myString.length);
console.log(anotherString, anotherString.length);

// function is a type of object. in JS called first class objects.
function Animal() {}
let rainbow = Animal(); //undefined

//creating new instance
rainbow = new Animal();
console.log(rainbow); //sintace of Animal

// object oriented - like creating a class in Python
// 'this' is a keyword, like 'self' in Python
function Animal(type, name, noise) {
	this.name = name;
	this.type = type;
	this.noise = noise;
	this.makeNoise = function () {
		console.log(this.name + 'says' + this.noise);
	};
}

let shadow = new Animal('cat', 'Shadow', 'groowwww');
console.log(shadow.name);
console.log(shadow.makeNoise);

/* prototypes are mechanism by which JS objects inherits features from one another. 
acts as a template object that inherits methods and properties form 
can be used to add methods to existing constructors */

Animal.prototype.makeNoise = function () {
	console.log(this.name + 'says' + this.noise);
};
