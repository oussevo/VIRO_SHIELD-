document.getElementById("send-btn").addEventListener("click", function() { // Corrigé à send-btn
    const publication = document.getElementById("publication").value;

    if (publication.trim() === "") {
        alert("Veuillez écrire quelque chose avant d'envoyer.");
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ publication: publication })
    })
    .then(response => response.json())
    .then(data => {
        const responseContainer = document.getElementById("response-container");

        if (data.inappropriate) {
            responseContainer.innerHTML = `<p style="color:red;">Attention: Contenu inapproprié détecté.</p>`;
        } else {
            responseContainer.innerHTML = `<p>SamSam: ${data.response}</p>`;
        }
    })
    .catch(error => console.error('Erreur:', error));
});
