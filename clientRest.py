import requests
import json
import tkinter as tk
from prompt import *


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

    def __repr__(self):
        return f"CompletionResponse(model={self.model}, content={self.content[:50]}...)"

    def get_content(self):
        return self.content

    def get_generation_settings(self):
        return self.generation_settings

    def get_timings(self):
        return self.timings

    # Add more methods as needed to manipulate or access data

class CompletionClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post_completion(self, prompt, temperature=0.8, dynatemp_range=0.0, dynatemp_exponent=1.0,
                        top_k=40, top_p=0.95, min_p=0.05, n_predict=-1, n_keep=0, stream=False,
                        stop=None, tfs_z=1.0, typical_p=1.0, repeat_penalty=1.1, repeat_last_n=64,
                        penalize_nl=True, presence_penalty=0.0, frequency_penalty=0.0, penalty_prompt=None,
                        mirostat=0, mirostat_tau=5.0, mirostat_eta=0.1, grammar=None, json_schema=None,
                        seed=-1, ignore_eos=False, logit_bias=None, n_probs=0, min_keep=0,
                        image_data=None, id_slot=-1, cache_prompt=False, system_prompt=None,
                        samplers=None):
        # Construct the payload
        payload = {
            "prompt": prompt,
            "temperature": temperature,
            "dynatemp_range": dynatemp_range,
            "dynatemp_exponent": dynatemp_exponent,
            "top_k": top_k,
            "top_p": top_p,
            "min_p": min_p,
            "n_predict": n_predict,
            "n_keep": n_keep,
            "stream": stream,
            "stop": stop if stop is not None else [],
            "tfs_z": tfs_z,
            "typical_p": typical_p,
            "repeat_penalty": repeat_penalty,
            "repeat_last_n": repeat_last_n,
            "penalize_nl": penalize_nl,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "penalty_prompt": penalty_prompt,
            "mirostat": mirostat,
            "mirostat_tau": mirostat_tau,
            "mirostat_eta": mirostat_eta,
            "grammar": grammar,
            "json_schema": json_schema,
            "seed": seed,
            "ignore_eos": ignore_eos,
            "logit_bias": logit_bias if logit_bias is not None else [],
            "n_probs": n_probs,
            "min_keep": min_keep,
            "image_data": image_data if image_data is not None else [],
            "id_slot": id_slot,
            "cache_prompt": cache_prompt,
            "system_prompt": system_prompt,
            "samplers": samplers if samplers is not None else ["top_k", "tfs_z", "typical_p", "top_p", "min_p", "temperature"]
        }

        # Send the POST request
        response = requests.post(f"{self.base_url}/completion", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

client = CompletionClient("http://127.0.0.1:8080")
systemPrompt = prompt5

def envoyer_msg():
    msg = entree_msg.get()
    if msg:
        zone_chat.configure(state='normal')
        zone_chat.insert(tk.END, "Oussema: " + msg + "\n")
        entree_msg.delete(0, tk.END)

        fullPrompt = systemPrompt + msg + "\nSamSam:"
        result = client.post_completion(prompt=fullPrompt, temperature=0.7, n_predict=200, stop=["Oussema:"])
        response = CompletionResponse(result)
        SamSamResponse = response.get_content().strip()
        zone_chat.insert(tk.END, "SamSam: " + SamSamResponse + "\n")
        zone_chat.configure(state='disabled')



def envoyer_msg_event(event):
    envoyer_msg()

#Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Chat avec SamSam")

#Création des widgets
zone_chat = tk.Text(fenetre, state='disabled', width=80, height=20, wrap='word')
entree_msg = tk.Entry(fenetre, width=80)
bouton_envoyer = tk.Button(fenetre, text="Envoyer", command=envoyer_msg)
entree_msg.bind("<Return>", envoyer_msg_event)

#Placement des widgets
zone_chat.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entree_msg.grid(row=1, column=0, padx=10, pady=10)
bouton_envoyer.grid(row=1, column=1, padx=10, pady=10)

#Lancement de la boucle principale
fenetre.mainloop()


