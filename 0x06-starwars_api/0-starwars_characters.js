#!/usr/bin/node

const request = require('request');

function fetchCharacter(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

async function fetchAndPrintCharacters(movieId) {
  try {
    const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
    const filmResponse = await new Promise((resolve, reject) => {
      request(filmUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const characters = filmResponse.characters;
    for (const characterUrl of characters) {
      const characterName = await fetchCharacter(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

const movieId = process.argv[2];
fetchAndPrintCharacters(movieId);
