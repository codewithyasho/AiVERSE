'''
Streamlit App for AIVerse - Multi AI Agents Platform
USING PYTHON 3.11.9
'''

import streamlit as st
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from google_client import google_agent
from agents import agents
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
        font-weight: 900;
        background: linear-gradient(135deg, #A855F7 0%, #EC4899 50%, #F59E0B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .tagline {
        font-size: 1.5rem;
        color: #A855F7;
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
        background-color: #A855F7;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #9333EA;
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
st.markdown('<div class="main-header">AiVERSE</div>',
            unsafe_allow_html=True)
st.markdown('<div class="tagline">One Window. 6 Perspectives.</div>',
            unsafe_allow_html=True)
st.markdown("")


# Main content
col1, col2 = st.columns([2, 1])

with col1:
    query = st.text_input(
        label="Enter your question", placeholder="Ask Your Question Here...", label_visibility="collapsed")

with col2:
    run_button = st.button("SUBMIT", type="primary",
                           disabled=st.session_state.crew_running)

# Helper function to run each agent


def run_agent(name, fn):
    try:
        return name, fn()
    except Exception as e:
        return name, "Can't process the request...CHECK FOR NEXT RESPONSE ->"


# Run the crew
if run_button and query:
    st.session_state.crew_running = True
    st.session_state.deepseek_response = None
    st.session_state.openai_response = None
    st.session_state.gemini_response = None
    st.session_state.llama_response = None
    st.session_state.qwen_response = None
    st.session_state.kimik2_response = None

    with st.spinner("6 AI Agents are analyzing your question in parallel..."):
        try:
            # Create progress indicators
            progress_container = st.container()
            with progress_container:
                progress_bar = st.progress(0)
                status_text = st.empty()

                status_text.text(
                    "🚀 Launching all 6 AI agents simultaneously...")
                progress_bar.progress(10)

                # Define all agent tasks
                tasks = [
                    ("DeepSeek", lambda: agents(
                        model="ollama:deepseek-v3.1:671b-cloud", query=query)),
                    ("OpenAI", lambda: agents(
                        model="ollama:gpt-oss:120b-cloud", query=query)),
                    ("Qwen", lambda: agents(model="groq:qwen/qwen3-32b", query=query)),
                    ("Llama", lambda: agents(
                        model="groq:llama-3.3-70b-versatile", query=query)),
                    ("Kimi", lambda: agents(
                        model="groq:moonshotai/kimi-k2-instruct-0905", query=query)),
                    ("Google", lambda: google_agent(prompt=query)),
                ]

                # Run all agents in parallel
                progress_bar.progress(20)
                status_text.text("⚡ All agents are processing in parallel...")

                responses = {}
                completed = 0
                total_agents = len(tasks)

                with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
                    futures = [executor.submit(run_agent, name, fn)
                               for name, fn in tasks]

                    for future in as_completed(futures):
                        name, result = future.result()
                        responses[name] = result
                        completed += 1

                        # Update progress
                        progress_value = 20 + \
                            int((completed / total_agents) * 70)
                        progress_bar.progress(progress_value)
                        status_text.text(
                            f"✅ {completed}/{total_agents} agents completed - {name} just finished!")
                        time.sleep(0.3)

                # Map responses to session state
                st.session_state.deepseek_response = responses.get(
                    "DeepSeek", "No response")
                st.session_state.openai_response = responses.get(
                    "OpenAI", "No response")
                st.session_state.qwen_response = responses.get(
                    "Qwen", "No response")
                st.session_state.llama_response = responses.get(
                    "Llama", "No response")
                st.session_state.kimik2_response = responses.get(
                    "Kimi", "No response")
                st.session_state.gemini_response = responses.get(
                    "Google", "No response")

                progress_bar.progress(100)
                status_text.text(
                    "🎉 All 6 AI agents have responded successfully!")
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
