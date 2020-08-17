// Get chat group slug
const chat_group_slug = JSON.parse(document.getElementById('chat_group_slug').textContent);
const username = JSON.parse(document.getElementById('username').textContent);

// Create a new websocket connection with the server
const chat_socket = new WebSocket(
    // Url for the websocket connection 
    `ws://${window.location.host}/ws/chat/${chat_group_slug}`
);

// Receive message from server
chat_socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    var author = "other";
    if (data.username == username) {
        author = "self";
    }
    // Escape message
    data.message = data.message.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
    
    // Add message HTML to chat log
    $('#chat-log-container').append(
        `
        <div class="chat-message-wrapper">
            <div class="chat-message chat-message-${author}">${data.message}</div>
        </div>
        `
    );

    // Scroll to the bottom of chat log
    $('#chat-log-container').scrollTop($('#chat-log-container')[0].scrollHeight);
};

// Send data to server
document.querySelector('#chat-message-submit').onclick = function(event) {
    const input_field = document.querySelector('#chat-message-input');

    if (input_field.value != '') {
        // Convert username message to json and send it to server
        chat_socket.send(
            JSON.stringify(
                {
                    'message': input_field.value
                }
            )
        );

        // Clear input field
        input_field.value = '';
    }
};

// Run when websocket disconnects from the server
chat_socket.onclose = function(event) {
    console.error('WebSocket closed unexpectedly');
};