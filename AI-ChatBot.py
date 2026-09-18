import json;
import os;
import socket;
import urllib.error;
import urllib.request;
from typing import Any;
import streamlit as st;

APP_TITLE = "Auto-Reply-AI"
DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_SYSTEM_PROMPT = (
    "You are a helpful customer support assistant. "
    "Reply clearly, politely, and briefly. If you do not know something, say so."
)
st.set_page_config(page_title=APP_TITLE, page_icon="AI", layout="centered")

def get_secret(name: str, default: str = "") -> str:
    """Read a setting from Streamlit secrets first, then environment variables."""
    try:
        value = st.secrets.get(name)
    except Exception:
        value = None
    return str(value or os.getenv(name, default)).strip()

def demo_reply(message: str) -> str:
    """Return a useful local response when no API key is configured."""
    lowered = message.lower()
    if any(word in lowered for word in ("hello", "hi", "hey")):
        return "Hello! Thanks for reaching out. How can I help you today?"
    if "price" in lowered or "cost" in lowered:
        return "I can help with pricing. Please tell me which product or plan you are asking about."
    if "thank" in lowered:
        return "You are welcome! I am here if you need anything else."
    return (
        "Thanks for your message. This is demo mode because no AI API key is configured. "
        "Add OPENAI_API_KEY in the .env file to enable real AI replies."
    )

def request_ai_reply(
    messages: list[dict[str, str]], api_key: str, model: str, base_url: str
) -> str:
    """Call an OpenAI-compatible chat completion endpoint using Python's standard library."""
    api_key = api_key.strip().strip("\"'\u201c\u201d\u2018\u2019")
    try:
        api_key.encode("ascii")
    except UnicodeEncodeError as error:
        raise RuntimeError(
            "The API key contains an unsupported character. Re-copy the key directly from your provider."
        ) from error
    url = f"{base_url.rstrip('/')}/chat/completions"
    payload = json.dumps(
        {"model": model, "messages": messages, "temperature": 0.7}
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    timeout = (
        300 if base_url.startswith(("http://localhost", "http://127.0.0.1")) else 60
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data: dict[str, Any] = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"AI provider error ({error.code}): {detail}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(
            f"Could not reach the AI provider: {error.reason}"
        ) from error
    except (TimeoutError, socket.timeout) as error:
        raise RuntimeError(
            f"The local model took too long to reply ({timeout} seconds). "
            "Keep Ollama running and try again; the first response can be slow on CPU."
        ) from error
    try:
        return str(data["choices"][0]["message"]["content"]).strip()
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError(
            "The AI provider returned an unexpected response."
        ) from error

def build_messages(system_prompt: str) -> list[dict[str, str]]:
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(
        {"role": item["role"], "content": item["content"]}
        for item in st.session_state.messages
    )
    return messages
st.title(APP_TITLE)
st.caption("A Python AI-Auto-Reply-Assistant.")
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input(
        "API key", value=get_secret("OPENAI_API_KEY"), type="password"
    )
    model = st.text_input("Model", value=get_secret("OPENAI_MODEL", DEFAULT_MODEL))
    base_url = st.text_input(
        "API base URL", value=get_secret("OPENAI_BASE_URL", DEFAULT_BASE_URL)
    )
    system_prompt = st.text_area(
        "Assistant instructions", value=DEFAULT_SYSTEM_PROMPT, height=130
    )
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    if not api_key:
        st.info("Demo mode is active. Add an API key to get real AI replies.")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
prompt = st.chat_input("Type a message to get an automatic reply...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Writing a reply..."):
            try:
                if api_key:
                    reply = request_ai_reply(
                        build_messages(system_prompt), api_key, model, base_url
                    )
                else:
                    reply = demo_reply(prompt)
            except RuntimeError as error:
                st.error(str(error))
                reply = (
                    "I could not generate a reply. Check the settings and try again."
                )
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})