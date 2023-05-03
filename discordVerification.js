var psd = require("psd-api");
var isStudent;
var token = "MTA5OTQxMjIzNDE1NDgwMzIxMQ.G29Z9y.ELsat-sHg5CeJtYNEerYKuc3NF3whikjRioo4o";

var callback = function(student) {    
    if ((student == null) || (String(student.Name) == "undefined") ){
        isStudent = false;
        console.log('false');
    }
    else{
        isStudent = true;
        console.log('true');
    }
};

const fs = require('fs');

const data = fs.readFileSync('userID.txt', 'utf8');

psd.get({userID: data}, callback);


