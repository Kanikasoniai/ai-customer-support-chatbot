
function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    // Show user message
    chatBox.innerHTML += `<div class="user">${message}</div>`;

    input.value = "";

    // Send to backend
    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot">${data.reply}</div>`;
    });
}