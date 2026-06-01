import streamlit as st
import time

st.set_page_config(page_title="Universo Red Moon & Scarlett - Rafael Lessa", page_icon="🌙", layout="centered")

# --- MENU LATERAL (SELEÇÃO DA OBRA) ---
st.sidebar.title("📚 Universo Literário")
st.sidebar.markdown("Selecione a obra que deseja ler e ambientar:")

# O menu agora reflete os títulos exatos das suas três novels
novel_selecionada = st.sidebar.radio(
    "Obras Disponíveis:",
    [
        "🌌 Scarlett's Sun Ellipse [2056]",
        "📕 The Red Moon Archive [2006]",
        "🏹 The Red Moon Archive: A Second Chance [Ano 60]"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("✍️ **Autor:** Rafael Lessa")

# --- ESTRUTURA DINÂMICA DO SITE ---

if novel_selecionada == "🌌 Scarlett's Sun Ellipse [2056]":
    
    st.title("🌌 Scarlett's Sun Ellipse")
    st.caption("Ano 2056 — O Mistério Espiritual do Eclipse Escarlate")
    st.markdown("---")
    
    st.markdown("#### 🎵 Trilha Sonora (Cyberpunk / Sobrenatural)")
    clima_musica = st.text_area(
        "Descreva o clima da música para este capítulo:", 
        placeholder="Ex: Synthwave sombrio com batida pesada de trap geek e um piano misterioso no fundo..."
    )
    
    if st.button("Compor Trilha de 2056 ⚡", key="btn_2056", use_container_width=True):
        with st.spinner("Sintonizando as frequências do Eclipse de 2056..."):
            time.sleep(2)
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
            
    st.markdown("---")
    st.subheader("📝 Capítulo 1: Sob o Céu Sangrento")
    st.markdown("""
    *Em 2056, a tecnologia alcançou o ápice, mas o mundo parou quando o Sol foi obscurecido por uma sombra escarlate. Não era um fenômeno astronômico comum. O início do Scarlett's Sun Ellipse trouxe de volta o que a ciência tentou trancar no passado...*
    
    Os neons da metrópole falhavam enquanto os primeiros sinais espirituais começavam a se manifestar através das telas digitais.
    """)

elif novel_selecionada == "📕 The Red Moon Archive [2006]":
    
    st.title("📕 The Red Moon Archive")
    st.caption("Ano 2006 — O Início dos Registros da Lua Vermelha")
    st.markdown("---")
    
    st.markdown("#### 🎵 Trilha Sonora (Anos 2000 / Investigação)")
    clima_musica = st.text_area(
        "Descreva o clima da música para este capítulo:", 
        placeholder="Ex: Rock alternativo nostálgico, estilo Linkin Park ou trilhas clássicas de mistério de anime..."
    )
    
    if st.button("Compor Trilha de 2006 ⚡", key="btn_2006", use_container_width=True):
        with st.spinner("Abrindo os arquivos secretos de 2006..."):
            time.sleep(2)
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", format="audio/mp3")
            
    st.markdown("---")
    st.subheader("📝 Capítulo 1: O Primeiro Manifesto")
    st.markdown("""
    *Os registros começaram cinquenta anos antes do eclipse, no outono de 2006. Quando a Lua Vermelha subiu ao céu, o primeiro arquivo foi aberto. Nós não sabíamos o que estávamos catalogando, apenas que o mundo nunca mais seria o mesmo.*
    """)

else:
    st.title("🏹 The Red Moon Archive: A Second Chance")
    st.caption("Ano 60 — A Linha Temporal Alternativa da Antiguidade")
    st.markdown("---")
    
    st.markdown("#### 🎵 Trilha Sonora (Épica / Fantasia Ancestral)")
    clima_musica = st.text_area(
        "Descreva o clima da música para este capítulo:", 
        placeholder="Ex: Música orquestral épica com coros dramáticos, violinos intensos e tambores de guerra..."
    )
    
    if st.button("Compor Trilha do Ano 60 ⚡", key="btn_60", use_container_width=True):
        with st.spinner("Invocando a melodia das legiões..."):
            time.sleep(2)
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", format="audio/mp3")
            
    st.markdown("---")
    st.subheader("📝 Prólogo: O Retorno de Dois Mil Anos")
    st.markdown("""
    *Sob o céu do Ano 60, as regras da física de 2006 não se aplicavam. Diante do avanço dos impérios antigos e do brilho implacável da Lua Vermelha, a oportunidade de reescrever a história inteira se abria. Era a nossa segunda chance.*
    """)
    
