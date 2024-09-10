import streamlit as st

st.set_page_config(
    page_title="Site GPT Home",
    page_icon="🤖",
)


with st.sidebar:
    st.link_button("Open Git", "https://github.com/JangSeonguk/Site_GPT")
    choice = st.selectbox(
        "Choose what you want to use.",
        (
            "Home",
            "Code",
        ),
    )

SITEGPT_PATH = "pages/Site_GPT.py"

with open(SITEGPT_PATH, "r", encoding="utf-8") as file:
    site_code = file.read()

if choice == "Code":
    st.subheader("아래 코드는 Site GPT 페이지에 대한 소스 코드입니다.")
    st.code(site_code, language="python")

else:
    st.markdown(
        """
    # Home
                
    :red[**Site GPT**]에 오신 것을 환영합니다.

    웹사이트에 대해 궁금한 내용이 있다면 Site GPT의 챗봇에게 질문해보세요.

    """
    )
