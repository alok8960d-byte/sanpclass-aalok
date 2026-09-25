import streamlit as st

def style_background_home():
    st.markdown(
        """
        <style>
        .stApp {
            background: #BDDDFC !important;
        }
        .stApp div[data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            padding: 1.5rem !important;
            border-radius: 5rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background: #E0E3FF !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Streamlit top bar, menu and footer */
        #MainMenu,
        header,
        footer {
            visibility: hidden;
        }

        /* Main content container */
        .block-container {
            padding-top: 1.5rem !important;
        }

        /* H1 Heading */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        /* H2 Heading */
        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        /* Other text */
        h3,
        h4,
        p {
            font-family: 'Outfit', sans-serif !important;
        }

        /* Primary Button */
        button {
            border-radius: 1.5rem !important;
            background: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        /* Secondary Button */
        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        /* Tertiary Button */
        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover{
            transform: scale(1.05)
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
