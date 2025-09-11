import streamlit as st
from utils.scoring import calculate_score, get_score_message
from utils.pdf_generator import create_pdf
from utils.card_generator import display_eco_challenge_card
from utils.recipe_guide import create_recipe_guide  # Added import
from data.recommendations import RECOMMENDATIONS
import requests
import time
from PIL import Image
from io import BytesIO

def load_image(url):
    """Load an image from URL with cache prevention"""
    try:
        # Add a random parameter to prevent caching
        cache_buster = f"?cb={hash(url)}-{hash(str(time.time()))}"
        full_url = f"{url}{cache_buster}"
        response = requests.get(full_url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        st.warning(f"Unable to load image: {e}")
        return None

def main():
    if 'responses' not in st.session_state:
        st.warning("Please complete the assessment first!")
        st.button("Start Assessment", on_click=lambda: st.switch_page("pages/01_questionnaire.py"))
        return

    st.title("Your Pollinator-Friendly Cleaning Assessment Results")

    score_level, percentage = calculate_score(st.session_state.responses)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Your Results")
        st.markdown(get_score_message(score_level, percentage))

    with col2:
        image = load_image("https://images.unsplash.com/photo-1556911220-bff31c812dba")
        st.image(image, caption="Natural cleaning products", use_container_width=True)

    st.markdown("---")

    st.header("Recommended Actions")

    recommendations = RECOMMENDATIONS[score_level]

    for rec in recommendations:
        with st.expander(f"🌿 {rec['title']}"):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown(f"**Impact:** {rec['impact']}")
                st.markdown(f"**Effort:** {rec['effort']}")
                st.markdown(f"**Description:** {rec['description']}")

            with col2:
                st.markdown("**Implementation Steps:**")
                for step in rec['implementation']:
                    st.markdown(f"- {step}")

    st.markdown("---")

    # Add Natural Recipes Guide section
    st.header("🧪 Natural Cleaning Recipes")
    st.markdown("""
    Want to make your own eco-friendly cleaning products? Download our comprehensive guide
    with recipes for natural cleaners that are safe for pollinators and effective for your home!
    """)

    if st.button("Download Natural Recipes Guide 📚"):
        recipe_guide = create_recipe_guide()
        st.download_button(
            label="Save Recipe Guide",
            data=recipe_guide,
            file_name="natural_cleaning_recipes.pdf",
            mime="application/pdf"
        )

    st.markdown("---")

    # Add Eco-Challenge Card section
    st.header("Share Your Achievement!")
    st.markdown("""
    Inspire others to make pollinator-friendly choices! Generate your eco-challenge
    card and share your achievement with friends and family.
    """)

    display_eco_challenge_card(score_level, percentage, recommendations)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Download PDF Guide"):
            pdf = create_pdf(score_level, percentage, recommendations)
            st.download_button(
                label="Save PDF",
                data=pdf,
                file_name="pollinator_friendly_guide.pdf",
                mime="application/pdf"
            )

    with col2:
        if st.button("Start Over"):
            st.session_state.clear()
            st.switch_page("main.py")

if __name__ == "__main__":
    main()