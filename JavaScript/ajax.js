const request = new XMLHttpRequest();
request.onreadystatechange = (evt) => {
	let req = evt.target;
	if (req.readyState !== 4) return;
	if (req.status === 200) console.log(req.response);
};
request.open('GET', './samples/test.txt');
request.send();
