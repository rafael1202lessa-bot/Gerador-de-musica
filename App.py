import streamlit as st
import time

# Configurando a página para o estilo Leitura/Novel
st.set_page_config(page_title="Novel Studio IA", page_icon="📖", layout="centered")

st.title("📖 Minha Light Novel - Estúdio Secreto")
st.markdown("---")

# --- SEÇÃO 1: O GERADOR DE TRILHA SONORA ---
st.subheader("🎵 Trilha Sonora do Capítulo")
st.caption("Descreva o clima da música para acompanhar a leitura deste capítulo.")

# Opções para guiar a IA musical
clima_musica = st.text_area(
    "Comandos para a IA de música:", 
    placeholder="Ex: Uma música triste de piano que se transforma em um rock épico com guitarras no final, estilo abertura de anime..."
)

if st.button("Compor Trilha Sonora ⚡", use_container_width=True):
    if clima_musica.strip() != "":
        with st.spinner("🧑‍🎤 A IA está compondo a melodia para a sua história..."):
            # Simulação do tempo de resposta da API de Áudio
            time.sleep(3) 
            
            st.success("🎧 Trilha Sonora carregada com sucesso para este capítulo!")
            # Player de áudio que o leitor vai dar o play antes de começar a ler
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", format="audio/mp3")
    else:
        st.warning("Digite o clima da música para a IA começar a compor!")

st.markdown("---")

# --- SEÇÃO 2: A HISTÓRIA (SUA NOVEL) ---
st.subheader("📝 Capítulo 1: O Despertar do Fragmento")

# Aqui você pode escrever a sua história direto usando Markdown.
# Use o bloco abaixo para colocar o texto do seu personagem original!
st.markdown("""
> *“As luzes da cidade futurista piscavam através da janela quebrada, mas os olhos dele só conseguiam focar no brilho azul que emanava da sua própria mão...”*

O silêncio do quarto foi quebrado pelo som dos passos metálicos no corredor. Ele sabia que eles estavam vindo. Não havia mais tempo para fugir, nem para se esconder. O poder que ele tentou ocultar por tantos anos finalmente tinha acordado...

*— Se eles querem o fragmento... — sussurrou, fechando o punho com força enquanto a energia estalava como trovão. — Vão ter que vir buscar.*
""")

# --- MENU LATERAL ---
st.sidebar.title("🗂️ Menu da Novel")
st.sidebar.selectbox("Escolha o Capítulo:", ["Prólogo", "Capítulo 1: O Despertar", "Capítulo 2: Em Breve..."])
st.sidebar.markdown("---")
st.sidebar.markdown("✍️ **Autor:** Rafael Lessa")
