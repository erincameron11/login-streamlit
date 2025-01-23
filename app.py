# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st # for UI
# import streamlit_authenticator as stauth # for login authentication
# import yaml # for config.yaml
# from yaml.loader import SafeLoader
# Import external file
from helpers import *


# ------------------------------------ APP ------------------------------------
def main():
    """
    Main method to run the application.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """   
    # Change the title and favicon of the app in the browser
    st.set_page_config(page_title='Login', page_icon=":closed_lock_with_key:")
    
    # App title
    st.title(":closed_lock_with_key: Login")
    st.write(f"*Erin Cameron &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; [GitHub](https://github.com/erincameron11/login-streamlit)*")
    st.divider()

    login()


# ------------------------------------ RUN THE APP ------------------------------------
if __name__ == "__main__":
    main()