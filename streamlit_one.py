#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 17:25:18 2025

@author: ananyaashahi
"""

import random
import streamlit as st

st.set_page_config(page_title="Legal Case Classifier (Prototype)", layout="wide")

st.title("Legal Case Classifier (Prototype)")
st.caption("Skeletal demo: accepts text and returns a random classification (no real model yet).")

with st.sidebar:
    st.header("Options")
    scope = st.radio("Analyze", ["Summary only", "Full text"], index=0)
    model_name = st.selectbox(
    "Model",
    [
        "BERT (placeholder)",
        "RoBERTa (placeholder)",
        "DistilBERT (placeholder)",
        "Legal-BERT (placeholder)"
    ],
    index=3  # Default selection is Legal-BERT
)
    show_expl = st.checkbox("Show explanation (top terms)", value=True)

col1, col2 = st.columns([1, 1.1])

with col1:
    text = st.text_area("Paste case summary or text", height=220, placeholder="Paste a short case summary here…")
    submitted = st.button("Classify Case")

def dummy_predict(_text: str):
    labels = ["Employee", "Independent Contractor", "Undetermined"]
    label = random.choice(labels)
    confidence = round(random.uniform(0.51, 0.98), 2)
    top_terms = random.sample(
        ["degree of control", "supervision", "tools provided", "independent agreement",
         "payment structure", "work schedule", "location control", "equipment ownership"], k=3
    )
    return label, confidence, top_terms

with col2:
    st.subheader("Result")
    if submitted:
        if not text.strip():
            st.warning("Please enter some text to classify.")
        else:
            label, conf, top_terms = dummy_predict(text)
            st.markdown(f"**Predicted Class:** {label}")
            st.progress(int(conf * 100))
            st.markdown(f"**Confidence:** {int(conf * 100)}%")
            if show_expl:
                st.markdown("**Top contributing phrases (placeholder):**")
                for term in top_terms:
                    st.write(f"- {term}")
            st.caption("Note: This is a skeletal demo returning random results. No real model is loaded yet.")

st.divider()
st.caption("For academic demonstration only. This page simulates a future mobile workflow.")
