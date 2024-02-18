    #!/usr/bin/node

    const request = require('request');

    const movieId = process.argv[2];
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, function (error, response, body) {
    if (error) {
        console.error('Error:', error);
    } else {
        const filmData = JSON.parse(body);
        const characters = filmData.characters;
        characters.forEach(characterUrl => {
        request(characterUrl, function (error, response, body) {
            if (error) {
            console.error('Error:', error);
            } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            }
        });
        });
    }
    });
