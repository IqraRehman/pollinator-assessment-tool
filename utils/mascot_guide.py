import streamlit as st
import random

class PollinatorMascot:
    def __init__(self):
        self.name = "Buzzy"
        self.messages = {
            'welcome': [
                "Hi! I'm Buzzy, your friendly pollinator guide! 🐝",
                "Ready to make your home more pollinator-friendly? Let's get started! 🌺",
                "I'm excited to help you create a safer environment for my friends! 🦋"
            ],
            'progress': [
                "You're doing great! Keep going! 🌱",
                "Every small change helps us pollinators thrive! 🌿",
                "I'm buzzing with excitement at your progress! 🐝"
            ],
            'completion': [
                "Wow! You're becoming a real pollinator protector! 🌸",
                "Together, we're making the world better for pollinators! 🦋",
                "Thank you for helping create safer spaces for us! 🐝"
            ]
        }
        
        self.tips = {
            'cleaning_products': "Did you know? Some cleaning products contain chemicals that can harm pollinators even through indirect contact!",
            'outdoor_practices': "Fun fact: The best time to clean outdoors is early morning or evening when we're less active!",
            'indoor_practices': "Quick tip: Natural ventilation not only saves energy but also helps protect us pollinators!"
        }

    def display_mascot(self, message_type='welcome'):
        # Custom CSS for the mascot container
        st.markdown("""
        <style>
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        .mascot-container {
            background-color: #f0f8ff;
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            border: 2px solid #4CAF50;
            animation: float 3s ease-in-out infinite;
        }
        .mascot-message {
            font-size: 1.1em;
            color: #2E7D32;
        }
        </style>
        """, unsafe_allow_html=True)

        # Display random message from the appropriate category
        message = random.choice(self.messages[message_type])
        st.markdown(f"""
        <div class="mascot-container">
            <div class="mascot-message">
                {message}
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_tip(self, section):
        if section in self.tips:
            st.info(f"🐝 Buzzy's Tip: {self.tips[section]}")

    def celebrate_progress(self, progress):
        if progress >= 100:
            self.display_mascot('completion')
        elif progress > 0:
            self.display_mascot('progress')
        else:
            self.display_mascot('welcome')
