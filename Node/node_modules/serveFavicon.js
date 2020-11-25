const serveFavicon = (req, res) => {
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
