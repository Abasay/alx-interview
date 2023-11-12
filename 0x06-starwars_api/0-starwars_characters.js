#!/usr/bin/node

const request = require('request');
const process = require('process');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

const options = {
  url,
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'alx-student'
  }
};

request(options, async (err, resp, body) => {
  if (err) return console.error(err);

  const characters = JSON.parse(body).characters;
  // await queue result until they resolve in order
  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (err, res, body) => {
        if (err) return console.error(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
