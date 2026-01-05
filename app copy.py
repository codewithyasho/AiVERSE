'''
Streamlit App for AIVerse - Multi AI Agents Platform
USING PYTHON 3.11.9
'''

import streamlit as st
import os
from pathlib import Path
from src.crew import AIVerseCrew
import time

# Page configuration
st.set_page_config(
    page_title="AIVerse - One Window. 6 Perspectives.",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #6366F1;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .tagline {
        font-size: 1.5rem;
        color: #8B5CF6;
        text-align: center;
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #6366F1;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #4F46E5;
    }
    .output-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #6366F1;
    }
    .agent-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'crew_running' not in st.session_state:
    st.session_state.crew_running = False
if 'deepseek_response' not in st.session_state:
    st.session_state.deepseek_response = None
if 'openai_response' not in st.session_state:
    st.session_state.openai_response = None
if 'gemini_response' not in st.session_state:
    st.session_state.gemini_response = None
if 'llama_response' not in st.session_state:
    st.session_state.llama_response = None
if 'qwen_response' not in st.session_state:
    st.session_state.qwen_response = None
if 'kimik2_response' not in st.session_state:
    st.session_state.kimik2_response = None

# Header
st.markdown('<div class="main-header">AIVerse</div>',
            unsafe_allow_html=True)
st.markdown('<div class="tagline">One Window. 6 Perspectives.</div>',
            unsafe_allow_html=True)
# st.markdown('<div class="sub-header">Get answers from 6 different AI models simultaneously - DeepSeek, OpenAI, Gemini, Llama, Qwen & Kimi K2</div>', unsafe_allow_html=True)


# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Ask Your Question")
    query = st.text_input(
        label="Enter your question", placeholder="How can AI transform the future of education?", label_visibility="collapsed")

with col2:
    run_button = st.button("Send", type="primary",
                           disabled=st.session_state.crew_running)

# Run the crew
if run_button and query:
    st.session_state.crew_running = True
    st.session_state.deepseek_response = None
    st.session_state.openai_response = None
    st.session_state.gemini_response = None
    st.session_state.llama_response = None
    st.session_state.qwen_response = None
    st.session_state.kimik2_response = None

    with st.spinner("6 AI Agents are analyzing your question..."):
        try:
            # Create progress indicators
            progress_container = st.container()
            with progress_container:
                # st.subheader("Loading AI Responses...")
                progress_bar = st.progress(0)
                status_text = st.empty()

                # Update progress - DeepSeek
                status_text.text(
                    "🟣 DeepSeek Agent: Processing your query...")
                progress_bar.progress(15)

                # Run the crew
                inputs = {"query": query}
                crew_instance = AIVerseCrew()

                # Update progress - OpenAI
                status_text.text(
                    "🟢 OpenAI GPT Agent: Analyzing...")
                progress_bar.progress(30)

                # Update progress - Gemini
                status_text.text(
                    "🔵 Google Gemini Agent: Thinking...")
                progress_bar.progress(45)

                # Update progress - Llama
                status_text.text(
                    "🔴 Meta Llama Agent: Responding...")
                progress_bar.progress(60)

                # Update progress - Qwen
                status_text.text(
                    "🟠 Alibaba Qwen Agent: Processing...")
                progress_bar.progress(75)

                # Update progress - Kimi K2
                status_text.text(
                    "🟡 Moonshot Kimi K2 Agent: Finalizing...")
                progress_bar.progress(85)

                # Execute the crew
                result = crew_instance.crew().kickoff(inputs=inputs)

                # Update progress - Reading files
                # status_text.text("📂 Collecting all responses...")
                # progress_bar.progress(90)

                # Read the generated files
                deepseek_path = Path("outputs/deepseek-task.md")
                openai_path = Path("outputs/openai-gpt-task.md")
                gemini_path = Path("outputs/google-gemini-task.md")
                llama_path = Path("outputs/meta-llama3-task.md")
                qwen_path = Path("outputs/alibaba-qwen-task.md")
                kimik2_path = Path("outputs/kimi-k2-task.md")

                if deepseek_path.exists():
                    with open(deepseek_path, 'r', encoding='utf-8') as f:
                        st.session_state.deepseek_response = f.read()

                if openai_path.exists():
                    with open(openai_path, 'r', encoding='utf-8') as f:
                        st.session_state.openai_response = f.read()

                if gemini_path.exists():
                    with open(gemini_path, 'r', encoding='utf-8') as f:
                        st.session_state.gemini_response = f.read()

                if llama_path.exists():
                    with open(llama_path, 'r', encoding='utf-8') as f:
                        st.session_state.llama_response = f.read()

                if qwen_path.exists():
                    with open(qwen_path, 'r', encoding='utf-8') as f:
                        st.session_state.qwen_response = f.read()

                if kimik2_path.exists():
                    with open(kimik2_path, 'r', encoding='utf-8') as f:
                        st.session_state.kimik2_response = f.read()

                progress_bar.progress(100)
                status_text.text("All 6 AI agents have responded!")
                time.sleep(1)

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.exception(e)

        finally:
            st.session_state.crew_running = False

elif run_button and not query:
    st.warning("⚠️ Please enter a question before getting AI responses.")

# Display results
if any([st.session_state.deepseek_response, st.session_state.openai_response, st.session_state.gemini_response,
        st.session_state.llama_response, st.session_state.qwen_response, st.session_state.kimik2_response]):
    # st.markdown("---")
    # st.header("🌐 AI Responses")
    st.write("")  # Spacing

    # Create tabs for the outputs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🟣 DeepSeek",
        "🟢 OpenAI GPT",
        "🔵 Google Gemini",
        "🔴 Meta Llama",
        "🟠 Alibaba Qwen",
        "🟡 Kimi K2"
    ])

    with tab1:
        if st.session_state.deepseek_response:
            st.markdown(
                '<div class="agent-card"><h4>DeepSeek</h4></div>', unsafe_allow_html=True)
            st.markdown(st.session_state.deepseek_response)
            st.download_button(
                label="⬇️ Download DeepSeek Response",
                data=st.session_state.deepseek_response,
                file_name="deepseek-response.md",
                mime="text/markdown",
                key="download_deepseek"
            )
        else:
            st.info("DeepSeek response will appear here after generation.")

    with tab2:
        if st.session_state.openai_response:
            st.markdown(
                '<div class="agent-card"><h4>OpenAI GPT</h4></div>', unsafe_allow_html=True)
            st.markdown(st.session_state.openai_response)
            st.download_button(
                label="⬇️ Download OpenAI Response",
                data=st.session_state.openai_response,
                file_name="openai-gpt-response.md",
                mime="text/markdown",
                key="download_openai"
            )
        else:
            st.info("OpenAI response will appear here after generation.")

    with tab3:
        if st.session_state.gemini_response:
            st.markdown(
                '<div class="agent-card"><h4>Google Gemini</h4></div>', unsafe_allow_html=True)
            st.markdown(st.session_state.gemini_response)
            st.download_button(
                label="⬇️ Download Gemini Response",
                data=st.session_state.gemini_response,
                file_name="google-gemini-response.md",
                mime="text/markdown",
                key="download_gemini"
            )
        else:
            st.info("Gemini response will appear here after generation.")

    with tab4:
        if st.session_state.llama_response:
            st.markdown(
                '<div class="agent-card"><h4>Meta Llama 3</h4></div>', unsafe_allow_html=True)
            st.markdown(st.session_state.llama_response)
            st.download_button(
                label="⬇️ Download Llama Response",
                data=st.session_state.llama_response,
                file_name="meta-llama3-response.md",
                mime="text/markdown",
                key="download_llama"
            )
        else:
            st.info("Llama response will appear here after generation.")

    with tab5:
        if st.session_state.qwen_response:
            st.markdown(
                '<div class="agent-card"><h4>Alibaba Qwen 3</h4></div>', unsafe_allow_html=True)
            st.markdown(st.session_state.qwen_response)
            st.download_button(
                label="⬇️ Download Qwen Response",
                data=st.session_state.qwen_response,
                file_name="alibaba-qwen-response.md",
                mime="text/markdown",
                key="download_qwen"
            )
        else:
            st.info("Qwen response will appear here after generation.")

    with tab6:
        if st.session_state.kimik2_response:
            st.markdown(
                '<div class="agent-card"><h4>Kimi K2</h4></div>', unsafe_allow_html=True)
            st.markdown(st.session_state.kimik2_response)
            st.download_button(
                label="⬇️ Download Kimi K2 Response",
                data=st.session_state.kimik2_response,
                file_name="kimi-k2-response.md",
                mime="text/markdown",
                key="download_kimik2"
            )
        else:
            st.info("Kimi K2 response will appear here after generation.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>Powered by DeepSeek, OpenAI, Google Gemini, Meta Llama, Alibaba Qwen & Moonshot Kimi K2</p>
    </div>
""", unsafe_allow_html=True)
