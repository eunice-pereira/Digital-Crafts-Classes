const fs = require('fs');
let ships = JSON.parse(fs.readFileSync('ship-data.json'));

// let ships = [
// 	{
// 		type: 'Freighter',
// 		speed: 'medium',
// 		cargo: 'large',
// 		payload: 'low',
// 	},
// 	{
// 		type: 'Fighter',
// 		speed: 'fast',
// 		cargo: 'none',
// 		payload: 'medium',
// 	},
// 	{
// 		type: 'Bomber',
// 		speed: 'slow',
// 		cargo: 'none',
// 		payload: 'high',
// 	},
// ];

//adding item to ship

let newShip = {
	type: 'speeder',
	speed: 'Fast',
	cargo: 'none',
	payload: 'none',
};
// ships.push(newShip);
// console.log(ships);

// fs.writeFile('ship-data.json', JSON.stringify(ships), 'utf8', (err) => {
// 	if (err) throw err;
// 	console.log('The JSON file has been written');
// });

const addShip = (newShip) => {
	ships.push(newShip);
	fs.writeFile('ship-data.json', JSON.stringify(ships), (err) => {
		if (err) throw err;
		console.log('new ship data saved');
	});
};
addShip(newShip);
