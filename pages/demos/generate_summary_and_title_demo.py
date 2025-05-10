import streamlit as st
from utils.summaryNewsTest import summary_news      # 요약문 생성
from utils.generateTitleTest import generate_title  # 제목 생성


def run():
    st.title("📝 본문 내용 요약문 및 제목 생성 Demo")

    text = st.text_area("뉴스 본문을 입력하세요", height=300)

    if st.button("Generate"):
        if not text.strip():
            st.warning("텍스트를 입력해주세요.")
        else:
            with st.spinner("생성 중입니다..."):
                summary = summary_news(text)
                title = generate_title(summary)
                if summary == "error1":
                    st.warning("언어 감지에 실패하였습니다 (지원 언어: 영어, 한국어)")
                elif summary == "error2":
                    st.warning("지원하는 언어가 아닙니다 (지원 언어: 영어, 한국어)")
                else:
                    st.success("✅ 생성 완료 !")
                    st.write(title)
                    st.write(summary)
