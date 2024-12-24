import streamlit as st

def socials_section():
    st.title("Follow Me On Social Media")
    
    st.markdown("""
    Connect with me on various platforms!  
    Here are the links to my social media profiles and other platforms where I share my work:

    - [GitHub](https://github.com/desalebhavesh)  
    - [LinkedIn](https://www.linkedin.com/in/bhavesh-desale-950239233/)  
    

    Feel free to reach out to me for collaborations, questions, or just to connect!  
    Stay updated with my latest content by following me on these platforms.
    """)

# Call the socials_section function to display the content
if __name__ == "__main__":
    socials_section()

# Custom CSS for styling
st.markdown("""
    <style>
    h1 {
        color: #D97757;
    }
    h2 {
        color: #6B7280;
    }
    .socials-link {
        color: #3498db;
        text-decoration: none;
    }
    .socials-link:hover {
        color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Movies Search Chatbot")

# Subheading
st.subheader("Connect with me on various platforms!")
