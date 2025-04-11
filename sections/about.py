import streamlit as st
from social_media_icons import SocialMediaIcons


def get_about_section():
    # render_about_information()
    # st.header("About me")
    # header_underline()
    st.markdown("""Computer Scientist with expertise in Data Quality, Artificial Intelligence, and Big Data Management. Passionate about leveraging technology to drive innovative, impactful solutions to real-life challenges. Skilled in analytical problem-solving, and cross-functional collaboration. Currently serving as a Research Data Engineer at [Datalab AUTh](https://datalab.csd.auth.gr/), under the supervision of [Prof. Anastasios Gounaris](https://datalab-old.csd.auth.gr/~gounaris/).""")
    get_contact_section()
    st.info("Want to learn more about me? Feel free to explore other sections of this website using the tabs above.")


def get_contact_section():
    social_media_links = [
        "mailto:bilpapster@gmail.com",
        "https://www.linkedin.com/in/bilpapster/",
        "https://www.github.com/bilpapster/",
    ]
    social_media_icons = SocialMediaIcons(social_media_links)
    # st.header("Contact")
    # header_underline()
    st.write("Feel free to contact me via email, connect with me on LinkedIn or follow me on GitHub:")
    # st.divider()
    social_media_icons.render()