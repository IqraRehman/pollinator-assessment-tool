import streamlit as st
import math

def create_eco_progress_bar(progress_percentage):
    """
    Creates an animated eco-themed progress bar using emojis and custom styling
    """
    # Ensure progress is between 0 and 100
    progress = min(max(progress_percentage, 0), 100)
    
    # Calculate the number of growth stages to show
    total_segments = 10
    filled_segments = math.floor((progress / 100) * total_segments)
    
    # Create growth stages using emojis
    growth_stages = {
        0: "🌱",  # Seed
        1: "🌿",  # Sprout
        2: "🌸",  # Flower
        3: "🦋",  # Butterfly (indicating pollinator presence)
    }
    
    # Custom HTML/CSS for animated progress bar
    progress_html = f"""
    <style>
    @keyframes grow {{
        from {{ width: 0%; }}
        to {{ width: {progress}%; }}
    }}
    
    .progress-container {{
        width: 100%;
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 3px;
        margin: 10px 0;
    }}
    
    .progress-bar {{
        width: {progress}%;
        height: 20px;
        background: linear-gradient(90deg, #4CAF50, #8BC34A);
        border-radius: 7px;
        animation: grow 1.5s ease-out;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10px;
    }}
    
    .growth-indicator {{
        display: flex;
        justify-content: space-between;
        margin-top: 5px;
    }}
    </style>
    
    <div class="progress-container">
        <div class="progress-bar">{progress:.1f}%</div>
    </div>
    <div class="growth-indicator">
    """
    
    # Add growth stage indicators
    for i in range(total_segments):
        stage_index = min(3, i // 3)  # Determine which growth stage to show
        if i < filled_segments:
            progress_html += f'<span>{growth_stages[stage_index]}</span>'
        else:
            progress_html += '<span>⋅</span>'
    
    progress_html += "</div>"
    
    # Display the custom progress bar
    st.markdown(progress_html, unsafe_allow_html=True)
    
    # Add contextual message based on progress
    if progress < 33:
        st.caption("🌱 Just getting started - watch your eco-impact grow!")
    elif progress < 66:
        st.caption("🌿 Growing strong - keep making pollinator-friendly choices!")
    else:
        st.caption("🌸 Almost there - your positive impact is blooming!")
