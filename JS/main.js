
var fs = require('fs');
var async = require('async');


// Hello World
// console.log('hello world');

function getFileContents(filePath) {
    return fs.readFileSync(filePath, 'utf-8').toString();
};

function decode(msg, key) {
    map = key.split(/\r?\n/);
    // var dict_map = {};
    var dict_map_r = {};
    for(var i in map){
        key_pair = map[i].split(":")
        // dict_map[key_pair[0]] = key_pair[1];
        dict_map_r[key_pair[1]] = key_pair[0];
    }
    newMsg = ""
    for(var j in msg){
        newMsg += dict_map_r[msg[j]];
    }
    return newMsg;
}


async.waterfall(
    [
        function(callback){
            msg = getFileContents('message.txt');
            key = getFileContents('key.txt');
            callback(null, msg, key);
        },
        function(msg, key, callback){
            result = decode(msg, key);
            callback(null, result);
        },
    ], 
    function (err,result) {
        console.log(result);
    }
);

const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});


