const http = require('http');

const ships = [
	{
		name: 'x-wing',
		type: 'fighter',
	},
	{
		name: 'tie-fighter',
		type: 'fighter',
	},
	{
		name: 'y-wing',
		type: 'bomber',
	},
];
const server = http.createServer((req, res) => {
	res.writeHead(200, {
		'Content-Type': 'application/json',
	});
	res.write(JSON.stringify(ships));
	res.end('Sent. Check the network!');
});

server.listen(8000, () => {
	console.log(`Running on Port ${8000}`);
});
