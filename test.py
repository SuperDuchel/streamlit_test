import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()



if st.session_state["authentication_status"]:
    # Le bouton de déconnexion
    with st.sidebar:
        authenticator.logout("Déconnexion")
        choix = st.radio('Bienvenue root', ['Acceuil', 'Les photos de mes animaux'])

    if choix == 'Acceuil':
        st.header('Bienvenue sur ma page')
        st.image(r'data:image/jpeg;base64,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')
    else:
        st.header('Bienvenue dans l album de mes animaux')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("mon chat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("mon chien")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("mon hibou")
            st.image("https://static.streamlit.io/examples/owl.jpg")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')





  
