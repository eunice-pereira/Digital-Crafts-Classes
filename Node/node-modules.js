const os = require('os');

const getInfo = () => {
	console.log(os.platform(), os.homedir(), os.hostname());
};

console.log(Object.keys(os));

// print amount of free memory in system/ network Interfaces, and user info
const getMoreInfo = () => [os.freemem(), os.networkInterfaces(), os.userInfo()];

let results = getMoreInfo();
console.log(results);
