// Create an array of at least 6 todo items with each todo having keys, id, todo, status, deadline (timestamp).
// Make at least one date before today.
// Limit the status to "complete","in-progress","todo"
// Using filter, create an array of only the complete items.
// Using find, get the soonest todo item that has a status of "todo".
// using filter get an array of all of the past due items.

let timestamp = new Date();
let items = [
	{
		id: 'JS',
		priority: 'high',
		status: 'in-progress',
		deadline: new Date(11 / 5 / 2020),
	},
	{
		id: 'udemy',
		priority: 'high',
		status: 'in-progress',
		deadline: new Date(1 / 15 / 2019),
	},
	{
		id: 'blog',
		priority: 'medium',
		status: 'todo',
		deadline: timestamp,
	},
	{
		id: 'gym',
		priority: 'high',
		status: 'complete',
		deadline: timestamp,
	},
];

let todo = items.find((task) => task.status == 'todo');

let pastDue = items.filter((task) => new Date(task.deadline).getTime());

let progress = items.filter(
	(item) => new Date(item.deadline).getTime() < Date.now()
);
console.log(progress);
