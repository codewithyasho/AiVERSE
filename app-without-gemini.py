'''
Streamlit App for AIVerse - Multi AI Agents Platform
USING PYTHON 3.11.9
'''

import streamlit as st
from pathlib import Path
import time

from src.crew import AIVerseCrew
from src.gemma_client import run_gemma


# ================= Page Configuration =================
st.set_page_config(
    page_title="AIVerse - One Window. 6 Perspectives.",
    page_icon="🤖",
    layout="wide",
)

# ================= Custom CSS =================
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(135deg, #A855F7 0%, #EC4899 50%, #F59E0B 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}
.tagline {
    font-size: 1.5rem;
    color: #A855F7;
    text-align: center;
    font-style: italic;
}
.agent-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 10px;
    color: white;
    text-align: center;
}
.stButton>button {
    width: 100%;
    background-color: #A855F7;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================= Session State =================
defaults = {
    "crew_running": False,
    "deepseek_response": None,
    "openai_response": None,
    "gemini_response": None,
    "llama_response": None,
    "qwen_response": None,
    "kimik2_response": None,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ================= Header =================
st.markdown('<div class="main-header">AiVERSE</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">One Window. 6 Perspectives.</div>',
            unsafe_allow_html=True)
st.write("")


# ================= Input =================
col1, col2 = st.columns([2, 1])

with col1:
    query = st.text_input(
        label="Enter your question",
        placeholder="Ask Your Question Here...",
        label_visibility="collapsed"
    )

with col2:
    run_button = st.button(
        "SUBMIT",
        type="primary",
        disabled=st.session_state.crew_running
    )


# ================= Run Agents =================
if run_button and query:
    st.session_state.crew_running = True
    for k in defaults:
        if k != "crew_running":
            st.session_state[k] = None

    with st.spinner("6 AI Agents are analyzing your question..."):
        try:
            progress_bar = st.progress(0)
            status_text = st.empty()

            # ---- DeepSeek / OpenAI / etc (CrewAI) ----
            status_text.text("🟣 DeepSeek Agent: Processing...")
            progress_bar.progress(15)

            crew_instance = AIVerseCrew()
            inputs = {"query": query}

            status_text.text("🟢 OpenAI GPT Agent: Analyzing...")
            progress_bar.progress(30)

            # ---- Gemma (DIRECT, NO CrewAI) ----
            status_text.text("🔵 Google Gemma Agent: Thinking...")
            progress_bar.progress(45)

            gemma_prompt = f"""
Explain the following in a simple, beginner-friendly way with examples:

{query}
"""
            st.session_state.gemini_response = run_gemma(gemma_prompt)

            # ---- Continue CrewAI agents ----
            status_text.text("🔴 Meta Llama Agent: Responding...")
            progress_bar.progress(60)

            status_text.text("🟠 Alibaba Qwen Agent: Processing...")
            progress_bar.progress(75)

            status_text.text("🟡 Moonshot Kimi K2 Agent: Finalizing...")
            progress_bar.progress(85)

            crew_instance.crew().kickoff(inputs=inputs)

            # ---- Read CrewAI outputs ----
            paths = {
                "deepseek_response": "outputs/deepseek-task.md",
                "openai_response": "outputs/openai-gpt-task.md",
                "llama_response": "outputs/meta-llama3-task.md",
                "qwen_response": "outputs/alibaba-qwen-task.md",
                "kimik2_response": "outputs/kimi-k2-task.md",
            }

            for key, file in paths.items():
                path = Path(file)
                if path.exists():
                    with open(path, "r", encoding="utf-8") as f:
                        st.session_state[key] = f.read()

            progress_bar.progress(100)
            status_text.text("✅ All AI agents have responded!")
            time.sleep(1)

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
            st.exception(e)

        finally:
            st.session_state.crew_running = False


elif run_button and not query:
    st.warning("⚠️ Please enter a question before submitting.")


# ================= Display Results =================
if any([
    st.session_state.deepseek_response,
    st.session_state.openai_response,
    st.session_state.gemini_response,
    st.session_state.llama_response,
    st.session_state.qwen_response,
    st.session_state.kimik2_response
]):
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🟣 DeepSeek",
        "🟢 OpenAI GPT",
        "🔵 Google Gemma",
        "🔴 Meta Llama",
        "🟠 Alibaba Qwen",
        "🟡 Kimi K2"
    ])

    def render(tab, title, content, filename):
        with tab:
            if content:
                st.markdown(
                    f'<div class="agent-card"><h4>{title}</h4></div>', unsafe_allow_html=True)
                st.markdown(content)
                st.download_button(
                    "⬇️ Download",
                    content,
                    file_name=filename,
                    mime="text/markdown"
                )
            else:
                st.info("Response will appear here.")

    render(tab1, "DeepSeek", st.session_state.deepseek_response, "deepseek.md")
    render(tab2, "OpenAI GPT", st.session_state.openai_response, "openai.md")
    render(tab3, "Google Gemma", st.session_state.gemini_response, "gemma.md")
    render(tab4, "Meta Llama 3", st.session_state.llama_response, "llama.md")
    render(tab5, "Alibaba Qwen", st.session_state.qwen_response, "qwen.md")
    render(tab6, "Kimi K2", st.session_state.kimik2_response, "kimi.md")


# ================= Footer =================
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#666;">
Powered by DeepSeek, OpenAI, Google Gemma, Meta Llama, Alibaba Qwen & Moonshot Kimi K2
</div>
""", unsafe_allow_html=True)
