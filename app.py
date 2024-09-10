import streamlit as st

st.set_page_config(
    page_title="Quiz_GPT Home",
    page_icon="🤖",
)


with st.sidebar:
    st.link_button(
        "Open Git", "https://github.com/JangSeonguk/Quiz_GPT/blob/main/app.py"
    )
    choice = st.selectbox(
        "Choose what you want to use.",
        (
            "Welcome Home",
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
    # Hello!
                
    Welcome to **Quiz GPT**

    Quiz GPT allows you to create quizzes from Wikipedia or documents that you have.

    """
    )
