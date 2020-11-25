//spread operator is ... can use to concatenate arrays
// does not impact original array

let array1 = [1, 2, 3];
let array2 = [...array1, 4, 5];
console.log(array2);

let me = { firstName: 'Eunice', lastName: 'Eunice', email: 'email@gmail.com' };
let newPerson = { ...me };
newPerson.age = 33;
