# chatbot_app.py

import streamlit as st
from mistralai import Mistral

# Clé API Mistral et modèle
api_key = "19uJi51E8tUsWiH8ysAqhE6GB9awZMSI"
model = "mistral-large-latest"

# Initialisation du client Mistral
client = Mistral(api_key=api_key)

# Fonction pour générer des réponses sous forme de poésie
def generate_response(user_input):
    try:
        # Ajouter une instruction pour générer une réponse poétique
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "Répondez toujours sous forme de vers poétiques, peu importe la question posée."
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ]
        )
        # Récupération de la réponse du modèle
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de la génération de la réponse : {str(e)}"

# Titre de l'application
st.title("Chatbot Poétique avec Streamlit et Mistral")
st.write("Bienvenue sur l'interface de chatbot poétique. Posez-moi des questions et je vous répondrai en vers !")

# Sauvegarde de l'historique des conversations
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Formulaire pour saisir la question
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

# Si une question est posée, générer la réponse poétique et l'ajouter à l'historique
if submit_button and user_input:
    response = generate_response(user_input)
    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Affichage de l'historique des échanges
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")
