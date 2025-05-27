from transformers import pipeline

classifier = pipeline("text-classification", model="classla/multilingual-IPTC-news-topic-classifier",
                      device=-1, max_length=512, truncation=True)


def detect_topic(text):
    result = classifier(text)[0]["label"]
    return result