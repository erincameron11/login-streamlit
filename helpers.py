# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st # for UI
import streamlit_authenticator as stauth # for login authentication
import yaml # for config.yaml
from yaml.loader import SafeLoader


# ------------------------------------ HELPER FUNCTIONS ------------------------------------
def login():
    """
    Method to authenticate login attempts.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """   
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Pre-hash all plain text passwords one time
    stauth.Hasher.hash_passwords(config['credentials'])
    update_config_file(config)

    # Create an Authenticate object (returns the credentials dict with hashed passwords)
    authenticator = stauth.Authenticate(
        config['credentials'],
        auto_hash = False # Since pre-hashing is completed above
    )

    # Create a login widget
    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

    # Authenticate users
    if st.session_state['authentication_status']:
        authenticator.logout()
        st.write(f'Welcome, *{st.session_state["name"]}*')
    elif st.session_state['authentication_status'] is False:
        st.error('Username or password is incorrect')
    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')


def update_config_file(config):
    """
    Method to update the config.yaml file.

    Parameters
    ----------
    config : config.yaml file contents

    Returns
    -------
    None
    """   
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)