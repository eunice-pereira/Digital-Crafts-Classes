// ex. 4
/* Write a function printNumbers which is given a start number and an end number. 
It will print the numbers from one to the other, one per line.
Write two versions of the above function. One using a while loop and the other using a for loop. */

function printNumbers(start, end) {
	for (i = start; i < end; i++) console.log(i);
}

function printNumbers2(start, end) {
	while ((i = start && i < end)) {
		i++;
		console.log(i);
	}
}

// ex. 5
/*
Write a function printSquare which is given a size and prints a square of that size using asterisks.
*/

// function printSquare(size) {
// 	let i = 0;
// 	while (i < size) {
// 		let ow = '';
// 		j = 0;
// 		while (j < size) {
// 			row += '*';
// 			j++;
// 		}
// 	}
// }
// another solution
const printSquare = function (v) {
	let s = '-'.repeat(v) + '\n';
	console.log(s.repeat(v));
};

// ex. 6 Banner
/* Write a function printBanner which is given some text and prints a banner with a border surrounding the text. 
The border has to stretch to the length of the text. */

function printBanner(text) {
	let l = text.length;
	let s = '';
	for (let i = 0; i < l + 2; i++) s += '-';

	console.log(s);
	console.log('-' + text + '-');
	console.log(s);
}
printBanner('This is Eunice');
