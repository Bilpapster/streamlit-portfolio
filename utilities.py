import streamlit as st

def rotate_image():
    from PIL import Image, ExifTags

    image = Image.open("ANN_3747.JPG")

    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = image._getexif()

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)

    # image = image.rotate(90)
    image.save("ROTATED_ANN_3747.JPG")

@st.cache_data(ttl=3600)
def render_about_information():
    left, right = st.columns([4, 1])

    with left:
        st.write("Hello traveller :wave: :flying_saucer:,")
        st.title("I'm Vasileios Papastergios,")
        st.write("a Computer Scientist with a passion for delivering data-centric, impactful solutions.")
    with right:
        st.image("Vasileios Papastergios.png")

@st.cache_data(ttl=3600)  # Cache images for 1 hour (=3600 seconds)
def get_images():
    images = dict()
    images['open_discussion_1'] = "assets/images/Vasileios Papastergios - DAR YE Camp 1.png"
    images['open_discussion_2'] = "assets/images/Vasileios Papastergios - DAR YE Camp 2.png"
    images['farewell_1'] = "assets/images/Vasileios Papastergios - Farewell comments 1.jpg"
    images['farewell_2'] = "assets/images/Vasileios Papastergios - Farewell comments 2.jpg"
    images['outdoor_cooking'] = "assets/images/Vasileios Papastergios - DAR YE Camp 3.png"
    images['love_nature'] = "assets/images/Vasileios Papastergios - DAR YE Camp 4.png"
    images['endurance'] = "assets/images/Vasileios Papastergios - DAR YE Camp 5.png"
    images['bill_builder'] = "assets/images/Vasileios Papastergios - DAR YE Camp 6.png"
    images['skouras_group_photo'] = "assets/images/Vasileios Papastergios - Skouras Camp 1.jpg"
    images['skouras_instructor'] = "assets/images/Vasileios Papastergios - Skouras Camp 2.JPG"
    return images

def switch(tab):
    return f"""<script>
    var tabGroup = window.parent.document.getElementsByClassName("stTabs")[0]
    var tab = tabGroup.getElementsByTagName("button")
    tab[{tab}].click()</script>
    """