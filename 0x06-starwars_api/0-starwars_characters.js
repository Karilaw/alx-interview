#!/usr/bin/node

const request = require('request');

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error('Invalid status code: ' + response.statusCode));
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function getCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, async function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      for (let i = 0; i < characters.length; i++) {
        const name = await getCharacterName(characters[i]);
        console.log(name);
      }
    }
  });
}

const movieId = process.argv[2];
getCharacters(movieId);
