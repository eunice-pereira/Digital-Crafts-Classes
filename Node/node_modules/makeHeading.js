const makeHeading = (page) => {
	let heading;
	switch (page) {
		case 'about':
			heading += `<h1>This is about!<h1>`;
			break;
		case 'contact':
			heading += `<h1>This is contact</h1>`;
			break;
		case 'foo':
			heading += '<h1>Check this out</h1>';
		default:
			heading += `<h1>This is Home</h1>`;
	}
	return heading;
};
module.exports = makeHeading;
