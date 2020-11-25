export const element = (tag, options = {}) => {
	//{} allows for default value
	let el = document.createElement(tag);
	return el;
};
// j query returns arrays
export const getEl = (query) => {
	let el = document.querySelectorAll(query);
	if (el.length == 0) return null; //didint find anything
	if (el.length == 1) return el[0];
	return el;
};
