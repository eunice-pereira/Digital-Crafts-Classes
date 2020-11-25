// Node is built on callbacks and asynchronous execution.
//Prevents the whole system being 'blocked'

// 'throw' below says 'if there is an error reading the file, let the system know and shout out the error'
const fs = require('fs');

fs.readFile('stuff.json', 'utf8', (err, data) => {
	if (err) throw err;
	let output = JSON.parse(data);
	output.forEach((data) => {
		console.log(`${data.name} is ${data.age} years old!`);
	});
});

// blocking piece of code below. should not be used except for loading initial data as program launches

// let data = fs.readFileSync('stuff.json', 'utf8');
// let dataArr = JSON.parse(data);
