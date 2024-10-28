import streamlit as st
import base64

# Inicializa a lista de dispositivos no estado da sessão, se ainda não estiver
if 'dispositivos' not in st.session_state:
    st.session_state.dispositivos = []

# Configurações da página
st.set_page_config(
    page_title="SafetyDevices",  # Título da página que aparecerá na aba do navegador
    page_icon="Frame 3.png",  # Ícone da página (pode ser um emoji ou um caminho para uma imagem)
    layout="centered",  # Pode ser "centered" ou "wide"
)

def main():
    st.image("Frame 3.png",width = 150,use_column_width=True)
    st.title("Central de Monitoramento")
    st.write("visualize e gerencie seus dispositivos!")
    # Menu para navegação
    page = st.sidebar.selectbox("Menu", ["Home", "Adicionar Dispositivo", "Configurar Dispositivo","ajuda & suporte"])

    if page == "Home":
        display_devices()
    elif page == "Adicionar Dispositivo":
        add_device()
    elif page == "Configurar Dispositivo":
        configure_device()
    elif page == "ajuda & suporte":
        Help_suporte()

def display_devices():
    st.subheader("Dispositivos Configurados")

    if st.session_state.dispositivos:
        # Criar colunas para cada dispositivo
        cols = st.columns(len(st.session_state.dispositivos))
        
        for i, dispositivo in enumerate(st.session_state.dispositivos):
            with cols[i]:
                st.write(f"### {dispositivo['nome']}")
                st.write(f"**ID:** {dispositivo['id']}")
                st.success(f"Status: {dispositivo['status']}")  # Exibindo status como variável
    else:
        st.write("Nenhum dispositivo configurado.")

def add_device():
    st.header("Adicionar Novo Dispositivo")
    nome = st.text_input("Nome do Dispositivo", placeholder="Ex: Sensor Escritório")
    dispositivo_id = st.text_input("ID do Dispositivo", placeholder="Insira o ID")

    # Campo para a localização
    localizacao = st.text_input("Localização", placeholder="Ex: Casa, Trabalho, etc.")

    # Botão de adicionar dispositivo
    if st.button("Adicionar Dispositivo"):
        if nome and dispositivo_id and localizacao:
            st.session_state.dispositivos.append({
                "nome": nome,
                "id": dispositivo_id,
                "localizacao": localizacao,
                "status": "Atualizado"  # Definindo o status como "Atualizado"
            })
            st.success(f"Dispositivo '{nome}' adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos!")

def configure_device():
    st.header("Configurar Dispositivo")
    
    if st.session_state.dispositivos:
        dispositivo_selecionado = st.selectbox("Escolher Dispositivo", [d["nome"] for d in st.session_state.dispositivos])
        
        for dispositivo in st.session_state.dispositivos:
            if dispositivo["nome"] == dispositivo_selecionado:
                st.write(f"### Configurações para {dispositivo['nome']}")
                st.write(f"**ID:** {dispositivo['id']}")
                st.write(f"**Localização:** {dispositivo['localizacao']}")
                st.write(f"**Status:** {dispositivo['status']}")
                novo_limite = st.slider("Definir limite de alerta (ppm)", 0, 300, 100)
                st.success(f"Limite de alerta ajustado para {dispositivo['nome']} em {novo_limite} ppm.")
    else:
        st.write("Nenhum dispositivo configurado.")
def Help_suporte():
    st.header("Ajuda & suporte")
    st.title("Central de Monitoramento")
    st.write("Visualize e gerencie dispositivos de detecção de fumaça.")
    

# Rodar o app
if __name__ == "__main__":
    main()
