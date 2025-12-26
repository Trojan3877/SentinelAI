import streamlit as st
import requests
import time

st.set_page_config(
    page_title="Sentinel AI Dashboard",
    layout="wide"
)

st.title("🛡️ Sentinel AI — Live Inference Dashboard")

API_URL = st.text_input(
    "FastAPI Inference Endpoint",
    "http://localhost:8000/infer"
)

prompt = st.text_area(
    "Enter Prompt",
    "Explain transformer attention in simple terms."
)

if st.button("Run Inference"):
    with st.spinner("Running LLM inference..."):
        start = time.time()
        response = requests.post(
            API_URL,
            json={"text": prompt}
        )
        latency = time.time() - start

    if response.status_code == 200:
        st.success("Inference Complete")
        st.markdown("### Model Output")
        st.write(response.json()["response"])
        st.metric("Latency (seconds)", round(latency, 2))
    else:
        st.error("Inference failed")

st.divider()

st.subheader("📊 System Status")
st.info("GPU-backed inference • Prometheus metrics enabled • MLflow tracking active")
