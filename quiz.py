import streamlit as st

user_option = st.radio(
    label='Amount',
    options=[10, 20, 30]
)

st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 32px;
}
    </style>
    """, unsafe_allow_html=True)

if user_option == 30:
    st.info("you made the right choice")
