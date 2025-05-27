import streamlit as st


def run():
    st.title("저장된 기사 목록")
    articles = st.session_state.get("generated_articles", [])

    if not articles:
        st.info("아직 저장된 기사가 없습니다.")
        return

    st.sidebar.header('세부사항 선택')
    lang = st.sidebar.selectbox('언어 선택', ['전체', '한국어', '영어'])
    lang_map = {'전체': None, '한국어': 'ko', '영어': 'en'}
    selected_lang = lang_map[lang]
    selected_topic = st.sidebar.selectbox('분야 선택',
                                 ['전체', 'education', 'human interest', 'society', 'sport', 'crime, law and justice',
                                  'disaster, accident and emergency incident', 'arts, culture, entertainment and media',
                                  'politics',
                                  'economy, business and finance', 'lifestyle and leisure', 'science and technology',
                                  'health', 'labour', 'religion', 'weather', 'environment', 'conflict, war and peace'])

    def filter_condition(article, lang, topic):
        # 언어 필터 적용
        if lang is None or lang == article.get("lang"):
            lang_filter = True
        else:
            lang_filter = False
        # 분야 필터 적용
        if topic == "전체" or topic == article.get("topic"):
            topic_filter = True
        else:
            topic_filter = False

        return lang_filter and topic_filter

    filtered_articles = [a for a in articles if filter_condition(a, selected_lang, selected_topic)]

    if not filtered_articles:
        st.info("조건에 맞는 기사가 없습니다.")
    else:
        st.write(f"총 {len(filtered_articles)}개의 기사 결과")
        for idx, article in enumerate(filtered_articles):
            with st.container(border=True):
                st.write(f"**{article['title']}**")
                st.write(article['summary'])
                st.write(f"분야: `{article['topic']}` | 언어: `{article['lang']}`")

                delete_button = st.button(label="삭제", key=idx, use_container_width=True)
                if delete_button:
                    st.session_state.generated_articles.remove(article)
                    st.rerun()
