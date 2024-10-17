from flask import Flask, request, jsonify, render_template
from prompt import *  # Importer le prompt spécifique
import requests
import json

app = Flask(__name__)

# Configuration du client LLM
class CompletionResponse:
    def __init__(self, data):
        self.content = data['content']
        self.id_slot = data['id_slot']
        self.stop = data['stop']
        self.model = data['model']
        self.tokens_predicted = data['tokens_predicted']
        self.tokens_evaluated = data['tokens_evaluated']
        self.generation_settings = data['generation_settings']
        self.prompt = data['prompt']
        self.truncated = data['truncated']
        self.stopped_eos = data['stopped_eos']
        self.stopped_word = data['stopped_word']
        self.stopped_limit = data['stopped_limit']
        self.stopping_word = data['stopping_word']
        self.tokens_cached = data['tokens_cached']
        self.timings = data['timings']

    def get_content(self):
        return self.content

class CompletionClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post_completion(self, prompt, temperature=0.7, n_predict=200, stop=None):
        # Préparer les paramètres de requête pour le modèle LLM
        payload = {
            "prompt": prompt,
            "temperature": temperature,
            "n_predict": n_predict,
            "stop": stop if stop is not None else [],
        }

        # Faire la requête POST vers le modèle LLM
        response = requests.post(f"{self.base_url}/completion", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Initialisation du client pour communiquer avec le modèle LLM
client = CompletionClient("http://127.0.0.1:8080")
systemPrompt = prompt_agent_deterctor  # Prompt de base

# Route pour servir la page HTML (frontend)
@app.route("/")
def home():
    return render_template("index.html")

# Route pour analyser la publication
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    publication = data.get('publication', '')

    if not publication:
        return jsonify({"error": "No publication provided"}), 400

    # Créer le prompt complet et envoyer au modèle LLM
    fullPrompt = systemPrompt + publication + "\nSamSam:"
    result = client.post_completion(prompt=fullPrompt, temperature=0.7, n_predict=200, stop=["Utilisateur:"])
    
    # Traiter la réponse du modèle
    response = CompletionResponse(result)
    SamSamResponse = response.get_content().strip()

    # Vérifier si le contenu est inapproprié
    inappropriate = any(word in SamSamResponse for word in ["haine", "racisme", "terrorisme", "niques"])

    return jsonify({
        "response": SamSamResponse,
        "inappropriate": inappropriate
    })

if __name__ == "__main__":
    app.run(debug=True)
