var fs = require("fs");
var async = require('async');



function getFileContents(filePath) {
    return fs.readFileSync(filePath, 'utf-8').toString();
};



function decodeArray(arr,key) {
    decodedMessage = "";
    let file = getFileContents("key.txt");
    let message = getFileContents("message.txt");
    filedict = file.split(/\r?\n/);
    realdict = {}
    for (let index = 0; index < filedict.length; index++) {
        pair = filedict[index].split(":");
        realdict[pair[1]] = pair[0];
        
    }


    for (let index = 0; index < message.length; index++) {
        decodedMessage = decodedMessage + realdict[message[index]]
        
    }
console.log(decodedMessage)
    // for (let index = 0; index < message.length; index++) {
    //     // message = message.replace(message[index],dict[message[index]])
    //     console.log(message[index])
    //     // console.log(message)
        
    // }
    // console.log(dict)
    // message = message.replace("m",dict[m])
    // console.log(message)
}

decodeArray();