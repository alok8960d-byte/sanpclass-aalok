import streamlit as st

def footer_home():
    logo_url= "https://logos.textgiraffe.com/user-gen/logo-name/500614735-designstyle-cartoon-l.png"

    st.markdown(
        f"""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 2rem;
        ">
        <p style="font-weight:bold; color: black;"> Created with ❤️ by</p>
        <img src="{logo_url}" style="max-height: 70px;" />
        </div>
        """,
        unsafe_allow_html=True,
)
