import streamlit as st

# Page Title
st.title("🎬 About Movies Bot Project")
st.divider()

# Project Overview
st.markdown("""
The **Movies Bot Project** is an AI-powered chatbot designed to assist users in exploring movies effortlessly. By leveraging advanced **Natural Language Processing (NLP)** techniques, the bot provides tailored movie recommendations, detailed movie information, and curated lists across various genres and languages.

The user-friendly interface, built with **Streamlit**, ensures seamless interaction, allowing users to search for movies, get actor or director-specific suggestions, and explore trending titles with ease.
""")

# Project Breakdown
st.subheader("🔍 Project Features:")
st.markdown("""
- **Natural Language Understanding**:
    - Identifies user intents such as:
        - Searching for movies by name, year, or actor.
        - Exploring Hollywood, Bollywood, South Indian, or Korean films.
        - Trending movies and curated recommendations.
    - Provides accurate and context-aware responses based on user input.

- **Interactive and Accessible Interface**:
    - Built using **Streamlit** for real-time interaction.
    - Dynamic response generation with user-focused design.

- **Database Integration**:
    - A rich dataset of movies including:
        - Titles, release years, genres, actors, and trending status.
    - Pre-trained models for entity extraction and intent classification.
""")

# Dataset Section
st.subheader("📊 Dataset:")
st.markdown("""
The dataset used for training includes:
- **Intents**:
    - Search movies by name, actor, or genre.
    - Fetch trending movies or curated lists.
- **Entities**:
    - Movie details like name, year, or actor.
    - Categories like Bollywood, Hollywood, etc.
- **Text Input**:
    - User queries like _"Find me a Bollywood movie"_ or _"Show trending movies this year"_.
""")

# NLP and AI Techniques
st.subheader("🤖 NLP and AI Techniques:")
st.markdown("""
The bot leverages:
- **Natural Language Processing (NLP)**:
    - Intent classification using **Logistic Regression** or **Neural Networks**.
    - Entity recognition for extracting movie names, years, or genres.
- **Model Training**:
    - Training on labeled datasets of intents and patterns.
    - Fine-tuned for accurate predictions and responses.
""")

# Streamlit Interface
st.subheader("💻 Streamlit Interface:")
st.markdown("""
The **Streamlit** interface provides:
- A **text input box** for user queries.
- A **response area** for the bot's answers, such as:
    - Trending movies: _"The top trending movies are Oppenheimer, Barbie, and The Marvels."_
    - Movie details: _"Inception (2010), directed by Christopher Nolan, is a must-watch!"_
    - Actor-based suggestions: _"Movies featuring Robert Downey Jr.: Iron Man, Sherlock Holmes."_
""")

# Conclusion
st.subheader("✅ Conclusion:")
st.markdown("""
The **Movies Bot Project** demonstrates the potential of combining **NLP** with an intuitive UI for creating a smart and user-friendly movie assistant.

### Key Highlights:
- Successfully trained a model for intent recognition and response generation.
- Built a robust and accessible interface using **Streamlit**.
- Opened opportunities for future enhancements, such as:
    - Expanding the movie database.
    - Adding voice input and responses.
    - Supporting multilingual interactions for global accessibility.

This project represents a significant step forward in creating AI-based entertainment solutions.
""")

# Footer
st.markdown("""
---
🎥 Movies Bot | Developed by ("Mr.Rushikesh Girase")
""")
