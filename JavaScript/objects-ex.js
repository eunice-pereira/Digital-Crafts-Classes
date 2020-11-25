// ex 1. Create an object called 'spaceship'.
// give it the following keys with whatever values seems reasonable to you. speed,acceleration, passangers, fuel.

let spaceship = {
	speed: 500,
	acceleration: 600,
	passengers: 20,
	fuel: 100,
};

// ex 2. Using the spaceship object above add a payload key after the object has been created. (just give it a number)
spaceship.payload = 50;
console.log(spaceship);

// ex 3. Using the same object above, lower the amount of fuel by 1 / 3.
spaceship.fuel = spaceship.fuel - spaceship.fuel / 3;
console.log(spaceship.fuel);

// ex. 4 loop through the object and give a message to the console like the one below for every property in the object

// use if statement in larger objects, best practice to get in habit now
for (key in spaceship) {
	if (!spaceship.hasOwnProperty(key)) continue;
	console.log(key, ':', spaceship[key]);
}
