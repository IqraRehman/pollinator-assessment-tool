import streamlit as st
import qrcode
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64

class EcoChallengeCard:
    def __init__(self):
        self.card_width = 800
        self.card_height = 600
        self.primary_color = "#4CAF50"
        self.background_color = "#FFFFFF"
        self.text_color = "#262730"

    def create_qr_code(self, url):
        """Generate QR code for the assessment URL"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color=self.text_color, back_color=self.background_color)

        # Convert to RGB mode for compatibility with the main image
        qr_image = qr_image.convert('RGB')

        # Resize QR code to desired dimensions
        qr_size = (150, 150)
        qr_image = qr_image.resize(qr_size)
        return qr_image

    def generate_card(self, score_level, percentage, key_achievements):
        """Generate a shareable eco-challenge card"""
        # Create base image
        card = Image.new('RGB', (self.card_width, self.card_height), self.background_color)
        draw = ImageDraw.Draw(card)

        # Add decorative elements
        draw.rectangle([(0, 0), (self.card_width, 60)], fill=self.primary_color)
        draw.rectangle([(0, self.card_height-60), (self.card_width, self.card_height)], fill=self.primary_color)

        # Add title
        title = "Pollinator Protector Achievement"
        draw.text((self.card_width//2, 30), title, fill=self.background_color, anchor="mm")

        # Add score
        score_text = f"Eco-Score: {percentage:.1f}%"
        draw.text((self.card_width//2, 120), score_text, fill=self.text_color, anchor="mm")

        # Add achievements
        y_position = 200
        for achievement in key_achievements:
            draw.text((40, y_position), f"✓ {achievement}", fill=self.text_color)
            y_position += 40

        # Add QR code
        qr_image = self.create_qr_code("https://pollinator-friendly-cleaning.repl.co")
        qr_pos = (self.card_width - 190, self.card_height - 210)  # Adjusted position
        card.paste(qr_image, qr_pos)

        # Add call to action
        cta_text = "Scan to take the assessment!"
        draw.text((self.card_width - 115, self.card_height - 40), 
                 cta_text, fill=self.background_color, anchor="mm")

        # Convert to bytes for Streamlit
        buffered = BytesIO()
        card.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return buffered.getvalue()

def display_eco_challenge_card(score_level, percentage, recommendations):
    """Display and provide sharing options for the eco-challenge card"""
    card_generator = EcoChallengeCard()

    # Extract key achievements from recommendations
    key_achievements = [
        f"{rec['title']}: {rec['impact']} Impact" 
        for rec in recommendations[:3]
    ]

    # Generate card
    card_image = card_generator.generate_card(score_level, percentage, key_achievements)

    # Display card
    st.image(card_image, caption="Your Eco-Challenge Card", use_container_width=True)

    # Download button
    st.download_button(
        label="Download Card 📥",
        data=card_image,
        file_name="eco_challenge_card.png",
        mime="image/png"
    )

    # Share text
    share_text = f"""
    🌿 I just scored {percentage:.1f}% on the Pollinator-Friendly Cleaning Assessment!
    Join me in protecting our pollinators by making eco-friendly cleaning choices.
    Take the assessment: https://pollinator-friendly-cleaning.repl.co
    #PollinatorProtector #EcoFriendly #SaveTheBees
    """

    # Copy share text button
    st.text_area("Share your achievement!", share_text, height=150)
    if st.button("Copy Share Text 📋"):
        st.toast("Share text copied to clipboard!", icon="📋")