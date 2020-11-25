// discussing objects as data types, similar to dictionaries in python

let myObj = {};

let aboutMe = {
	name: 'Clint',
	age: 38,
	tall: false,
};

let searchBy = 'name';

//can treat obj as instance of a class like in Python

console.log(aboutMe.name, aboutMe.age);

// change values
aboutMe.name = 'Eunice Pereira';
aboutMe.age = 33;
console.log(aboutMe);

//add new key
aboutMe.gender = 'Female';
console.log(aboutMe);

// delete a key
delete aboutMe.tall;
console.log(aboutMe);

// loop through objects if you are using for-in

for (key in aboutMe) {
	if (!aboutMe.hasOwnProperty(key)) continue;
	console.log(key, aboutMe[key]);
}
