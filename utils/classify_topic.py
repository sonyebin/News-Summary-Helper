from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_classifier():
    try:
        classifier = pipeline("text-classification",
                              model="classla/multilingual-IPTC-news-topic-classifier",
                              device=-1, max_length=512, truncation=True)
    except Exception as e:
        raise RuntimeError(f"분류 모델 로딩에 실패했습니다 : {e}")

    return classifier


def detect_topic(text):
    classifier = load_classifier()
    result = classifier(text)[0]["label"]
    return result
