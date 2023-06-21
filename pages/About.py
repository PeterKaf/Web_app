import streamlit as st
from PIL import Image


message = """This application is designed to assist you in staying organized and on top of your work.
With its intuitive interface, you can effortlessly manage your tasks by adding, editing, and marking them as complete.

The app prioritizes your most urgent tasks, ensuring that they are prominently displayed at the top of your list.
In situations where multiple tasks share the same deadline, the app intelligently considers their priorities to determine the order in which they are presented."""

image = Image.open("about_image.png")

# Define the desired width and height for the resized image
desired_width = 300
desired_height = 600
# Resize the image
resized_image = image.resize((desired_width, desired_height))

# Display the resized image
col1, col2, col3 = st.columns(3)
with col2:
    st.image(resized_image)
st.subheader("")
st.header("About:")
st.write(message)
