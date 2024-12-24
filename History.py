# history.py

# Preloaded chat history as a sample
preset_history = [
    "You: Recommend me a good sci-fi movie.",
    "Bot: I recommend 'Inception' or 'Interstellar'. Both are great sci-fi movies with amazing storytelling.",
    "You: Who directed 'Interstellar'?",
    "Bot: 'Interstellar' was directed by Christopher Nolan.",
]

# File path for storing chat history (optional, for persistence)
history_file = "chat_history.txt"

def load_history():
    """Load chat history from a file, or use the preset history if the file doesn't exist."""
    try:
        with open(history_file, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return preset_history  # Use preset history as fallback

def save_history(chat_line):
    """Save a new chat line to the history file."""
    with open(history_file, 'a') as file:
        file.write(chat_line + "\n")

def display_chat_history(st, chat_history):
    """Display the chat history on the Streamlit app."""
    st.write("### Chat History:")
    for chat in chat_history:
        st.write(chat.strip())

        
        # history.py
def history_section():
    # Your code for the history section
    return "This is the history section!"
