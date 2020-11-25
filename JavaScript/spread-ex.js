// Create an array of letters and create an array of numbers.
//Using the spread operator create an array of the values of the letters first then the numbers.
//Make another array with the numbers first.

let numbers = [1, 2, 3, 4, 5];
let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];

let newArr = [letters, ...numbers];

// Using the spread operator when possible do the following:
// Create a new array adding at least 2 more cars.
// From that new array return another array removing any cars made before 2018.
// Create a new array with a 2010 ford focus added to the begining.
// Create a new array of the cars sorted by date without changing the original cars array.

const cars = [
	{
		make: 'Chevy',
		model: 'Corvette',
		year: 2019,
	},
	{
		make: 'Ford',
		model: 'Mustang',
		year: 2018,
	},
	{
		make: 'Tesla',
		model: 'Model 3',
		year: 2020,
	},
	{
		make: 'GMC',
		model: 'h2',
		year: 2010,
	},
];

let update = {...car,
	make: 'honda',
	model: 'accord',
	year: '2014',
});
let updatedCars = cars.map(update);
console.log(updatedCars);
