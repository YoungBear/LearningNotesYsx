var fs = require("fs");

fs.readFile('input.txt', function (err, data) {
    if (err) {
        console.log(err.stack);
	return;
        //return console.error(err);
    }
    console.log(data.toString());
});

console.log("程序执行结束!");
