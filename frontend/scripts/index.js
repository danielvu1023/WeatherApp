const weatherSearchForm = document.getElementById("searchWeather");

weatherSearchForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let cityNameInputValue = "";
  let searchOptionValue;

  // Get cityName
  cityNameInputValue = document.getElementById("CityNameInput").value;
  if (cityNameInputValue.length == 0) {
    alert("City name can not be blank");
  } else {
    if (
      !document.getElementById("SearchCurrentWeather").checked &&
      !document.getElementById("SearchForecastWeather").checked
    ) {
      alert("Please select a weather option");
    } else {
      if (document.getElementById("SearchCurrentWeather").checked) {
        getCurrentWeather(cityNameInputValue).then((data) => {
          if (data.statusCode == 200) {
            buildCurrentWeatherCard(
              data.weatherData.cityName,
              data.weatherData.temperature
            );
          } else {
            alert(data.data.message);
          }
        });
      } else {
        getWeatherForecast(cityNameInputValue).then((data) => {
          if (data.statusCode == 200) {
            console.log(data);
            buildWeatherForecastCard(
              data.weatherData.cityName,
              data.weatherData.forecastList
            );
          } else {
            alert(data.data.message);
          }
        });
      }
    }
  }
});

function getCurrentWeather(cityName) {
  return fetch(`http://127.0.0.1:5000/weather/current/${cityName}`).then(
    (response) => response.json()
  );
}

function getWeatherForecast(cityName) {
  return fetch(`http://127.0.0.1:5000/weather/forecast?q=${cityName}`).then(
    (response) => response.json()
  );
}

function buildCurrentWeatherCard(cityName, temperature) {
  const today = new Date();
  const card = `<div class="card">
    <div class="cardContainer">
      <h4 class="cardTitle"><b>${cityName}</b></h4>
        <div id="cardRow">
          <p class="cardContent">Temperature: ${temperature}°F </p>
          <p class="cardContent">Date: ${today.toLocaleDateString()} </p>
        </div>
    </div>
  </div>`;

  document
    .getElementById("weatherResultsContainer")
    .insertAdjacentHTML("afterbegin", card);
}

function buildWeatherForecastCard(cityName, forecast) {
  const card = `<div class="card">
    <div class="cardContainer">
      <h4 class="cardTitle">
        <b>${cityName}</b>
      </h4>
      <div id="cardRow">
      </div>
    </div>
  </div>`;
  document
    .getElementById("weatherResultsContainer")
    .insertAdjacentHTML("afterbegin", card);
  for (const date in forecast) {
    const cardContent = `<div class="contentContainer">
      <p class="cardContent">Avg Temp: ${forecast[date]}°F </p>
      <p class="cardContent">Date: ${date} </p>
      </div>`;
    document
      .getElementById("cardRow")
      .insertAdjacentHTML("beforeend", cardContent);
  }
}

