'use strict';

const rawResultData = document.querySelector('#result-data');
const apiKey = '97ce82a7';

let resultContainer;

function createFilmCard(data) {
    let card = document.createElement('div');

    card.classList.add('film-card');
    card.innerHTML = `<div class="poster">
						<img src="${data['Poster']}" alt="${data['Title']} Poster">
					  </div>
					  <div class="info">
						<div class="row">
							<div class="label">Title</div>
							<div class="value">${data['Title']}</div>
						</div>
						<div class="row">
							<div class="label">Year</div>
							<div class="value">${data['Year']}</div>
						</div>
						<div class="row">
							<div class="label">Rated</div>
							<div class="value">${data['Rated']}</div>
						</div>
						<div class="row">
							<div class="label">Runtime</div>
							<div class="value">${data['Runtime']}</div>
						</div>
						<div class="row">
							<div class="label">Genre</div>
							<div class="value">${data['Genre']}</div>
						</div>
						<div class="row">
							<div class="label">Director</div>
							<div class="value">${data['Director']}</div>
						</div>
						<div class="row">
							<div class="label">Actors</div>
							<div class="value">${data['Actors']}</div>
						</div>
						<div class="row">
							<div class="label">Plot</div>
							<div class="value">${data['Plot']}</div>
						</div>
						<div class="row">
							<div class="label">Awards</div>
							<div class="value">${data['Awards']}</div>
						</div>
						<div class="row">
							<div class="label">imdbRating</div>
							<div class="value">${data['imdbRating']}</div>
						</div>
					  </div>`;

    resultContainer.appendChild(card);
}

async function getFilmInfo(title, year) {
    const apiUrl = `https://www.omdbapi.com/?apikey=${apiKey}&t=${encodeURIComponent(title)}&y=${year}`;
    const response = await fetch(apiUrl);
    const data = await response.json();

    createFilmCard(data);
}

function displayErrorMessage(errorMessage) {
	let error = document.createElement('div');

	error.classList.add('error-message');
	error.innerHTML = `${errorMessage}`

	resultContainer.appendChild(error);
}

if (rawResultData) {
    resultContainer = document.querySelector('.result-container');
    const results = JSON.parse(rawResultData.textContent);

    console.log(results);

    if (results.recommendations) {
	    results.recommendations.forEach((recommendation) => {
	        getFilmInfo(recommendation.title, recommendation.year);
	    });
    } else if (results.error) {
    	displayErrorMessage(results.error);
    }
}
