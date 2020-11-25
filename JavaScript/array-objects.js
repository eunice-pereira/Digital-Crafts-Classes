//Make an array of ship objects (at least 3). Each ship needs a name, topSpeed, acceleration, and cargo capacity.

let ships = [
	{
		name: 'Ship1',
		topSpeed: 2000,
		acceleration: 500,
		cargoCapacity: 1000,
	},
	{
		name: 'Ship2',
		topSpeed: 3000,
		acceleration: 700,
		cargoCapacity: 4000,
	},
	{
		name: 'Ship3',
		topSpeed: 4000,
		acceleration: 600,
		cargoCapacity: 3000,
	},
];

//console.log the name and top speed of the 2nd ship.

console.log(ships[1].name, ships[1].topSpeed);

//loop through the array and print out every stat in a key:value style.

ships.forEach(function (ship) {
	console.log('******');
	for (key in ships) {
		console.log(key, ':', ships[key]);
	}
	console.log('*****');
});

//(Bonus) sort the array by the ship with the fastest speed and console log it out.

ships.sort(function (a, b) {
	return a.topSpeed - b.topSpeed;
});
console.log(ships);
