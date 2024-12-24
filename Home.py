import streamlit as st

# Function for the chatbot search section
def chat_with_bot():
    st.subheader("🎬 Let's Talk Movies!")
    st.write("Type your movie-related query below.")

    user_input = st.text_input("Enter your movie preferences or questions:")
    if user_input:
        # Placeholder for the chatbot's response
        st.write(f"🔍 Searching for movies related to: {user_input}")
        # Add the actual chatbot logic or movie recommendation logic here.

# Home page function
def home_section():
    # Adding a title with an image
    col1, col2 = st.columns([1, 3])

    # Add an image in the first column
    with col1:
        st.image("chatbot/image.webp", use_container_width=True)  # Updated parameter

    # Add the title in the second column
    with col2:
        st.title("🎥 Movies Recommendation Bot")
        st.write(
            """
            Your personal assistant for discovering amazing movies!  
            - Get personalized recommendations.  
            - Find details about your favorite movies.  
            - Explore genres, ratings, and cast.  
            """
        )

    # Add a fancy divider
    st.markdown("---")

    st.subheader("✨ Features:")
    st.write(
        """
        - **Personalized Recommendations:** Based on your preferences.  
        - **Detailed Information:** Genres, cast, ratings, and more.  
        - **Interactive Chat:** Ask questions and get instant answers.  
        """
    )

    # Add a button to start chatting
    if st.button("🚀 Start Chatting"):
        st.session_state["current_page"] = "chat"

# Main app logic
if __name__ == "__main__":
    # Initialize session state
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "home"

    # Navigation logic
    if st.session_state["current_page"] == "home":
        home_section()
    elif st.session_state["current_page"] == "chat":
        chat_with_bot()
