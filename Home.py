import streamlit as st

def home_section():
    st.title("🎥 Movies Bot Home 🏠")
    st.write("Welcome to the Movies Bot! Ask me anything about movies and explore various sections.")



# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    home_section()  # Display the home section content dynamically

with col2:
    # Add a movie-related image or icon
    st.image("chatbot\Pages\Image.webp", width=250)

# Chat button
st.markdown("""
    ### Ready to Explore Movies? 
""")
st.button(
    label="Start Chatting 🎬", 
    help="Click to begin your movie exploration journey!"
)
