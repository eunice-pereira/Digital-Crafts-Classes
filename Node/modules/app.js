/*Make a node application that will supply html content based on the page parameter in the query string using the http module.
(bonus) Make the response send full valid html document without writing the top and bottom sections more than once. (IE make re-usable code)
(Extra Bonus) Add additional content based on any additional parameters in the quesy string.
*/

const http = require('http');
const fs = require('fs');
const port = 8000;
const makeHeading = require('./modules/makeHeading');
const generateContent = require('./modules/generateContent');

const serveCSS = (req, res) => {
	fs.readFile =
		('./favicon.png',
		(err, data) => {
			if (err) {
				res.writeHead(404);
				res.end();
			}
			res.end(data);
		});
};

const server = http.createServer((req, res) => {
	res.writeHead(200);

	if (req.url === '/favicon.png') return serveFavicon(res);

	const url = new URL(req.headers.host + req.url);
	let page = url.searchParams.get('page');
	let count = url.searchParams.get('count');
	let additional = [];

	url.searchParams.forEach((value, name) => {
		additional.push(`<li>${name}:${value}</li>`);
	});
	let heading = makeHeading(page);
	let foo = 'You are awesome';
	let wrapper = generateContent({
		page,
		heading,
		count,
		additional,
		foo,
	});
	res.write(wrapper);
	res.end();
});
server.listen(port);
