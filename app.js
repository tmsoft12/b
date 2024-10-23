const socket = new WebSocket('ws://192.168.180.131:8000'); // Raspberry Pi IP address

// When the connection is open, update status
socket.addEventListener('open', function (event) {
    document.getElementById('status').innerText = 'Connected to the WebSocket server';
});

// When a message is received, update the data on the page
socket.addEventListener('message', function (event) {
    const message = event.data;

    if (message.startsWith('Temperature:')) {
        document.getElementById('temperature').innerText = message;
    } else if (message.startsWith('Humidity:')) {
        document.getElementById('humidity').innerText = message;
    } else if (message.startsWith('Motion detected!')) {
        document.getElementById('motionStatus').innerText = message; // Hereket algylandy
        setTimeout(() => {
            document.getElementById('motionStatus').innerText = 'Hereket ýok.'; // 5 sekuntdan soň hereket ýok diýmek
        }, 5000); // 5000 milisegunde 5 sekunt
        document.getElementById('status').innerText = message;
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