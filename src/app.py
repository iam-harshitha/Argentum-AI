import streamlit as st
from loader import load_and_chunk_pdf
from rag import RAGRetriever
from llm import query_llama3

retriever = RAGRetriever()

# Streamlit Page Setup
st.set_page_config(page_title="Argentum-AI", layout="centered")
st.title("💼 Argentum-AI: Regulated Financial Assistant")

# Sidebar Instructions
st.sidebar.header("📘 Instructions")
st.sidebar.markdown("1. Upload a financial PDF document.\n2. Ask any investment-related question.\n3. Get context-aware, compliant answers.")

# Load PDF
uploaded_file = st.file_uploader("📄 Upload your financial PDF", type="pdf")
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    chunks = load_and_chunk_pdf("temp.pdf")
    if chunks:
        retriever.build_index(chunks)
        st.session_state.index_loaded = True
        st.success("✅ PDF processed and indexed.")

# Session states
if "messages" not in st.session_state:
    st.session_state.messages = []
if "index_loaded" not in st.session_state:
    st.session_state.index_loaded = False

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
if st.session_state.index_loaded:
    user_input = st.chat_input("Ask a financial question...")
    if user_input:
        # Store user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").markdown(user_input)

        # Retrieve context
        context_chunks = retriever.retrieve(user_input)
        context = "\n".join(context_chunks)
        context = context[:3000]
        
        # Prepare prompt
        prompt = f"""
        You are a regulated AI financial assistant. Based only on the provided context, answer in a short, concise, and professional manner (5-10 lines max).

        Context:
        {context}

        Question: {user_input}
        Answer:
        """

        # Generate and show answer
        with st.spinner("💬 Generating answer..."):
            assistant_response = query_llama3(prompt).strip()

        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.chat_message("assistant").markdown(assistant_response)

# Apply custom styling
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .stChatMessage.user div {
            background-color: #1e90ff !important;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stChatMessage.assistant div {
            background-color: #4CAF50 !important;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stTextInput>div>input, .stTextArea>div>textarea {
            background-color: #333 !important;
            color: white !important;
            border-radius: 5px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)