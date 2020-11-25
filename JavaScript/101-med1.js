// ex 1. Write a madlib function, which is given a name and a subject.
//It will return ( not print) a new string: ( name )'s favorite subject in school is (subject).

function madlib(name, subject) {
	console.log(`${name}'s favorite subject in school is ${subject}`);
}
madlib('eunice', 'science');

// ex. 2 Tip Calculator
/*Write a function tipAmount that is given the bill amount and the level of service (one of good, fair and poor) 
and returns the dollar amount for the tip. 
Based on: good -> 20% fair -> 15% bad -> 10% */

function tipAmount(bill, service) {
	if (service == 'good') {
		tip = bill * 0.2;
	} else if (service == 'fair') {
		tip = bill * 0.15;
	} else if (service == 'bad') {
		tip = bill * 0.1;
	}
	console.log(`The tip amount is ${tip}.`);
}

// ex. 3
/* Write a function totalAmount that takes the same arguments as tipAmount 
except it returns the total as the tip amount plus the bill amount. 
This function may make use of tipAmount as a sub-task. */

function tipAmount(bill, service) {
	if (service == 'good') {
		total = bill + bill * 0.2;
	} else if (service == 'fair') {
		total = bill + bill * 0.15;
	} else if (service == 'bad') {
		total = bill + bill * 0.1;
	}
	console.log(`The total amount is ${total}.`);
}
tipAmount(30, 'fair');
