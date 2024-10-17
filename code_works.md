<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analyse des Publications</title>
    <link rel="stylesheet" href="/static/clone_X.css">
</head>
<body>
    <div class="container">
        <textarea id="publication" placeholder="Quoi de neuf ?"></textarea>
        <button id="send-btn">Publier</button> <!-- Changement du bouton -->
    </div>

    <div id="popup" class="hidden">
        <p id="popup-message"></p>
        <button id="confirm-btn">Oui</button>
        <button id="cancel-btn">Non</button>
    </div>

    <div id="response-container"></div> <!-- Ajouté pour afficher les réponses -->

    <script src="/static/clone_X.js"></script>
</body>
</html>
-------------------------------------------------------

body {
    font-family: Arial, sans-serif;
    background-color: #3f2424;
    color: #f5f5f5; /* Meilleure lisibilité avec un texte clair */
    margin: 0;
    padding: 0;
}

.container {
    width: 90%;
    max-width: 500px; /* Limite la largeur maximale à 500px */
    margin: 50px auto;
    text-align: center;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Ajout d'une ombre pour le style */
}

textarea {
    width: 100%;
    height: 150px;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    border: 1px solid #ccc;
    font-size: 1rem; /* Taille de police pour une meilleure lisibilité */
    resize: vertical; /* Permet de redimensionner le textarea verticalement uniquement */
}

button {
    padding: 10px 20px;
    background-color: #1da1f2;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem; /* Taille de police légèrement plus grande */
    transition: background-color 0.3s ease; /* Transition fluide pour l'effet hover */
}

button:hover {
    background-color: #0d8ae9; /* Couleur plus sombre au survol pour effet visuel */
}

#response-container {
    margin-top: 20px;
    text-align: left;
    font-size: 1.2em;
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 5px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    color: #333;
}

.hidden {
    display: none;
}

#popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    z-index: 1000;
}

#popup button {
    margin: 5px;
}


