// write content to a file + add content to file
//cannot write file from server to front-end (site)
// this is writing to location that node is running from,
//even if request comes from an outside source (like a browser)

const fs = require('fs');
let lockfile = false; //prevents file overwrite

// writing content - first create, then add string (could be anything)
const writeFile = () => {
	// if file is not locked...
	if (!lockfile) {
		// lock file
		lockfile = true;

		// write file
		fs.writeFile('myFile.txt', 'Hello Node!', 'utf8', (err) => {
			if (err) throw err;

			// done writing..unlock the file
			lockfile = false;
			console.log('The file has been saved');
		});
	} else {
		// if file is locked, tell user file is locked
		console.log('the file is locked.');
	}
};
writeFile();
