// filter always returns an array and item is added to new array if function returns true

// map will always return new array with exact number of items
// filter has similar functionality, will return new array that meets parameters.
// filter uses boolean, returns item to new array if true.

let numbers = [5, 3, -10, 3, -21, 78, -54, -1, 8];
let positive = numbers.filter((num) => num >= 0);
console.log(positive);

// common filter usage and function syntax
let ships = [
	{
		type: 'freighter',
		name: 'falcon',
	},
	{
		type: 'fighter',
		name: 'xwing',
	},
	{
		type: 'bomber',
		name: 'ywing',
	},
	{
		type: 'fighter',
		name: 'tie-fighter',
	},
];

let fighters = ships.filter((ship) => ship.type == 'fighter');
let justNames = fighters.map((fighter) => fighter.name);

console.log(justNames);

// time stamp, creates date object
let timestamp = new Date();
console.log(timestamp);
