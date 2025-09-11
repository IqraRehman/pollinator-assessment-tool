import streamlit as st
from PIL import Image
import requests
import time
from io import BytesIO

st.set_page_config(
    page_title="Pollinator-Friendly Cleaning Practices",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed"  # Start with collapsed sidebar for better layout
)

# Load custom CSS (with error handling for deployment)
try:
    with open('.streamlit/custom.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    # CSS file not found - app will work without custom styles
    pass

def load_image(url):
    """Load an image from URL with error handling and cache prevention"""
    try:
        # Add a random parameter to prevent caching
        cache_buster = f"?cb={hash(url)}-{hash(str(time.time()))}"
        full_url = f"{url}{cache_buster}"
        response = requests.get(full_url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        st.warning(f"Unable to load image: {e}. Using placeholder content instead.")
        return None

def main():
    st.title("🐝 Pollinator-Friendly Cleaning Assessment")

    # Top section with introduction and start button
    col1, col2 = st.columns([4, 2])  # Adjusted ratio for better layout

    with col1:
        st.markdown("""
        ## Welcome to Your Eco-Friendly Cleaning Journey!

        Discover how your cleaning practices affect local pollinators and learn simple ways to make a positive impact. Our assessment will help you:

        - 📊 Evaluate your current cleaning practices
        - 🎯 Get a personalized eco-score
        - 📝 Receive custom recommendations
        - 📱 Generate a shareable action guide

        Join thousands of others in making their homes safer for pollinators!
        """)

        # Custom button styling with animations
        st.markdown("""
        <style>
        .start-button {
            background-color: #4CAF50;
            color: white;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            width: 100%;
            text-align: center;
            margin: 2rem 0;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .start-button:hover {
            background-color: #45a049;
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            transform: translateY(-2px);
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("Start Assessment ➡️", use_container_width=True):
            st.balloons()  # Add a fun animation effect
            st.switch_page("pages/01_questionnaire.py")

    with col2:
        # Updated to a proper bee image
        bee_image = load_image("https://images.unsplash.com/photo-1558618666-fcd25c85cd64")
        if bee_image:
            st.image(bee_image, caption="Honey bee pollinating flowers", use_container_width=True)

    st.markdown("---")

    # Middle section with impact information
    st.header("Why Your Cleaning Choices Matter")

    impact_cols = st.columns(3)

    with impact_cols[0]:
        st.markdown("""
        ### 🏠 Home Impact
        Your cleaning choices directly affect:
        - Indoor air quality
        - Water runoff
        - Local soil health
        - Pollinator habitats
        """)

    with impact_cols[1]:
        st.markdown("""
        ### 🌿 Environmental Benefits
        Making changes helps:
        - Protect bee populations
        - Support biodiversity
        - Reduce chemical pollution
        - Preserve ecosystems
        """)

    with impact_cols[2]:
        st.markdown("""
        ### 🌍 Community Impact
        Your actions inspire:
        - Neighbor awareness
        - Local conservation
        - Collective change
        - Habitat protection
        """)

    st.markdown("---")

    # Bottom section with success stories
    st.header("Success Stories")
    story_cols = st.columns(2)

    with story_cols[0]:
        garden_image = load_image("https://images.unsplash.com/photo-1416879595882-3373a0480b5b")
        if garden_image:
            st.image(garden_image, caption="Thriving garden with pollinators", use_container_width=True)
        st.markdown("""
        ### "Small Changes, Big Impact"
        After switching to eco-friendly cleaning products, local gardeners reported 
        a 60% increase in pollinator activity in their gardens!
        """)

    with story_cols[1]:
        community_image = load_image("https://images.unsplash.com/photo-1464207687429-7505649dae38")
        if community_image:
            st.image(community_image, caption="Pollinator-friendly community garden", use_container_width=True)
        st.markdown("""
        ### "Community in Action"
        A neighborhood's collective switch to pollinator-friendly practices led to
        the return of native butterfly species within just one season!
        """)

if __name__ == "__main__":
    main()