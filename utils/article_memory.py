import streamlit as st


# 생성된 요약 결과들 세션에 저장
def save_article(title, summary, topic, lang):
    if title is None:  # 정상적으로 생성된 요약문만 저장되도록
        return

    if "generated_articles" not in st.session_state:
        st.session_state.generated_articles = []

    st.session_state.generated_articles.append({
        "title": title,
        "summary": summary,
        "topic": topic,
        "lang": lang
    })


def show_similar_articles(current_topic, current_summary):
    if "generated_articles" not in st.session_state:
        return

    similar_articles = [
        article for article in st.session_state.generated_articles
        if article["topic"] == current_topic and article["summary"] != current_summary
    ]

    if similar_articles:
        st.write("---")
        st.subheader(f"같은 분야({current_topic})의 기사들")
        for article in similar_articles:
            with st.expander(f"**{article['title']}**"):
                st.write(article["summary"])
