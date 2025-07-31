
async function fetchWeather() {
    const city = document.getElementById("cityInput").value;
    if (!city) {
        alert("Please enter a city name.");
        return;
    }
    const response = await fetch("/api/weather", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city })
    });
    const data = await response.json();
    const div = document.getElementById("weatherResult");

    if (data.error) {
        div.innerText = "Error: " + data.error;
    } else {
        div.innerHTML = `
            <h3>Weather in ${data.city}</h3>
            <p>Temperature: ${data.temperature} °C</p>
            <p>Description: ${data.description}</p>
            <p>Humidity: ${data.humidity}%</p>
        `;
    }
}
