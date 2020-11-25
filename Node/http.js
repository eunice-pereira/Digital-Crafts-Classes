// creating module
// const { resolve6 } = require('dns');
const http = require('http');

const htmlContent = `
      <!DOCTYPE html>
      <html>
          <head>
              <title>HTML Content from Node</title>
          </head>
          <body>
              <h1>This is a full HTML document!</h1>
              <ul>
                  <li>It's Valid!</li>
                  <li>It's From Node!</li>
                  <li>It's Just a String!</li>
              </ul>
              <script>
                  console.log("It's like magic")
              </script>
          </body>
      </html>
  `;

const server = http.createServer((req, res) => {
	// setting status code
	res.statusCode = 200;
	// ends response to client & sends data in argument
	res.end(htmlContent);
});

server.listen(8000, () => {
	console.log('The server is up and running.');
});
