document.addEventListener("DOMContentLoaded", function () {
    displayMessage("Bot", "👋 Welcome to the Movie Bot! How can I help you today?");
    showAvailableGenres();
});

function sendMessage(userInput) {
    if (!userInput) {
        userInput = document.getElementById("user-input").value.trim();
        if (userInput === "") return;
    }

    displayMessage("You", userInput);

    fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ genre: userInput })  // Sending user input as "genre"
    })
    .then(response => response.json())
    .then(data => {
        if (data.recommendations) {
            displayMessage("Bot", `🎬 Recommended movies: ${data.recommendations.join(", ")}`);
        } else {
            displayMessage("Bot", data.error);
        }
        // Ask if the user needs further assistance and show genre options again
        setTimeout(() => {
            displayMessage("Bot", "📌 Anything else I can help with?");
            showAvailableGenres();
        }, 1000);
    })
    .catch(error => {
        displayMessage("Bot", "⚠️ Error fetching recommendations.");
        console.error("Error:", error);
    });

    document.getElementById("user-input").value = ""; // Clear input field
}

function displayMessage(sender, message) {
    let chatBox = document.getElementById("chat-box");
    let msgElement = document.createElement("p");
    msgElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(msgElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showAvailableGenres() {
    let genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi"];
    let chatBox = document.getElementById("chat-box");

    let buttonContainer = document.createElement("div");
    buttonContainer.style.marginTop = "10px";

    genres.forEach(genre => {
        let button = document.createElement("button");
        button.textContent = genre;
        button.style.margin = "5px";
        button.onclick = function () {
            sendMessage(genre);
        };
        buttonContainer.appendChild(button);
    });

    chatBox.appendChild(buttonContainer);
}

