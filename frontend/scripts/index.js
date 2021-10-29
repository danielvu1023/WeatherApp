console.log("hello world")

function getCurrentWeather() {
    fetch(url)
    .then(response.something) // Define response type (JSON, Headers, Status codes)
    .then(data) // get the response type 

    // Practical example
    fetch('https://jsonplaceholder.typicode.com/todos')
    .then(response => response.json())
    .then(data => console.log(JSON.stringify(data)))
}

