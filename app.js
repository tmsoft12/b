const socket = new WebSocket('ws://192.168.100.187:8000');

// When the connection is open, update status
socket.addEventListener('open', function (event) {
    document.getElementById('status').innerText = 'Connected to the WebSocket server';
});

// When a message is received, update the data on the page
socket.addEventListener('message', function (event) {
    const message = event.data;

    // Check if the message contains temperature or humidity information
    if (message.startsWith('Temperature:')) {
        document.getElementById('temperature').innerText = message; // Update temperature
    } else if (message.startsWith('Humidity:')) {
        document.getElementById('humidity').innerText = message; // Update humidity
    } else {
        document.getElementById('status').innerText = message; // Display any error messages
    }
});

// Handle errors
socket.addEventListener('error', function (event) {
    document.getElementById('status').innerText = 'Error connecting to the server';
    document.getElementById('status').style.color = 'red';
});

// Handle connection close
socket.addEventListener('close', function (event) {
    document.getElementById('status').innerText = 'Disconnected from the WebSocket server';
    document.getElementById('status').style.color = 'red';
});