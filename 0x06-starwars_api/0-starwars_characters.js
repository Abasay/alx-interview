#!/usr/bin/node

const request = require('request');
const process = require('process');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`

const options = {
    url: url,
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8',
        'User-Agent': 'alx-student'
    }
};

request(options, (err, resp, body) => {
    let res = JSON.parse(body);
    let characters = res.characters

    try{
	if (!characters) {
	    console.log('No characters found for this movie')
	} else {
	    for (let elem = 0; elem < characters.length; elem++) {
		request(characters[elem], (err, resp, body) => {
		    let characterRes = JSON.parse(body);
		    console.log(characterRes.name);
		});
	    };
	}
    } catch (err){
	console.log('No characters');
    }
});
