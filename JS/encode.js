var fs = require("fs");
var async = require('async');

function getFileContents(filePath) {
    return fs.readFileSync(filePath, 'utf-8').toString();
};

function shuffleArr(array) {
    return array.slice().sort(() => Math.random() - 0.5);
}

function buildTranslation(arr1,arr2) {
    // these arrays are the same length, that is why I used
    // arr1.length in the for loop, will error out if the user
    // supplies arrays that are of different sizes, need to account
    // for that test case. The user should only be able to upload a key
    // that is 26 characters.
    let dict_map = {};
    for (let index = 0; index < arr1.length; index++) {
        dict_map[arr1[index]] = arr2[index];
    }
    return dict_map;
}

function encode(msg) {
    // TODO:
    //     Add space character to this dictionary, map space:space
    let alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
                    "q","r","s","t","u","v","w","x","y","z"];
    let cipher = shuffleArr(alphabet);
    let input= getFileContents("input.txt").toLowerCase();

    let mapping = buildTranslation(alphabet,cipher);
    //console.log(mapping);
    let result = "";
    for (let index = 0; index < input.length; index++) {

        cur = mapping[input.charAt(index)];
        //console.log(input.charAt(index) + cur);
        if (cur != undefined)
        {
            result+=cur;
        }
        else
        {
            result+= " ";
        }
        // console.log(cur);
    }
    console.log(input);
    console.log(result);
    // TODO:
    //     Save both files to disc



}

encode();