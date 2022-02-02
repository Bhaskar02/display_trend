import streamlit as st
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
from PIL import Image

img = st.file_uploader("upload image", type=["jpg", "png"])
if img:
    test = Image.open(img)
    width, height = test.size  # width is needed for image_to_url()
    if width > MAXIMUM_CONTENT_WIDTH:
        width = MAXIMUM_CONTENT_WIDTH  # width is capped at 2*730 https://github.com/streamlit/streamlit/blob/949d97f37bde0948b57a0f4cab7644b61166f98d/lib/streamlit/elements/image.py#L39
    st.image(img)
    st.write(
        image_to_url(
            image=img,
            width=width,
            clamp=False,
            channels="RGB",
            output_format=img.type,
            image_id=img.id,  # each uploaded file has a file.id
        )
    )
