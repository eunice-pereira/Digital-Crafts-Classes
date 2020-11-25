let generateContent = ({ page, heading, additional, count }) => {
	return `
        <!DOCTYPE html>
        <html>
            <head><title>My Selection:${page}</title><head>
            <link rel="stylesheet" href="style.css" type="text/css"/> 
            <body>
                ${navigation}
                ${heading}
                The count is  ${count || 0}. 
                <ul>
                    ${additional.join('')}
                <ul>
                <footer>
                    copyleft 2020
                <footer> 
            </body>
        </html>
    `;
};
module.exports = generateContent;
