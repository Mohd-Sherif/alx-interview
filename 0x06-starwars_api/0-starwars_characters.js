#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the film data based on the movie ID
request(url, (error, response, body) => {
  if (error) {
    console.error("Error fetching movie:", error);
    return;
  }
  
  // Check if response status code is not 200
  if (response.statusCode !== 200) {
    console.error("Failed to retrieve the movie. Please check the movie ID.");
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Fetch each character name sequentially
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error("Error fetching character:", charError);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
