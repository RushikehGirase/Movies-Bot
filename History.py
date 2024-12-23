import os
import streamlit as st
import csv

def history_section():
    st.title("🕒 Conversation History")
    st.write("Review your past interactions with the Movies Bot below.")

    # Path to the conversation history file
    history_file = 'movie_bot_history.csv'  # Update the file path if needed

    if os.path.exists(history_file):
        st.subheader("📜 Previous Conversations")
        with open(history_file, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader, None)  # Skip the header row

            if header:
                st.markdown(f"**Columns:** {', '.join(header)}")

            # Display each conversation
            for row in csv_reader:
                st.text(f"**User:** {row[0]}")
                st.text(f"**Movies Bot:** {row[1]}")
                st.text(f"**Timestamp:** {row[2]}")
                st.markdown("---")
    else:
        st.warning("⚠️ No conversation history found.")
        st.markdown("""
        - Ensure the file `movie_bot_history.csv` exists in the current directory.
        - The file should be in the following format:
            1. User's message
            2. Movies Bot's response
            3. Timestamp
        """)

    # Optional Footer
    st.markdown("""
    ---
    🎬 Movies Bot | Developed by Rushikesh Girase
    """)

# Run the history section if this file is executed directly
if __name__ == "__main__":
    history_section()
