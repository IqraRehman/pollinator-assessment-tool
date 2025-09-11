import streamlit as st
from data.questions import QUESTIONS
from utils.progress_bar import create_eco_progress_bar
from utils.mascot_guide import PollinatorMascot

def init_session_state():
    if 'responses' not in st.session_state:
        st.session_state.responses = {}
    if 'current_section' not in st.session_state:
        st.session_state.current_section = list(QUESTIONS.keys())[0]
    if 'mascot' not in st.session_state:
        st.session_state.mascot = PollinatorMascot()

def display_question(question, key):
    st.markdown(f"**{question['question']}** ℹ️")
    st.caption(question['tooltip'])

    options = [opt['text'] for opt in question['options']]
    selected = st.radio("Select one:", options, key=f"radio_{key}")

    score = next(opt['score'] for opt in question['options'] if opt['text'] == selected)
    return score

def main():
    st.title("🧹 Cleaning Practices Assessment")

    init_session_state()
    mascot = st.session_state.mascot

    # Calculate progress percentage
    progress = (len(st.session_state.responses) / 
               sum(len(section) for section in QUESTIONS.values()) * 100)

    # Show mascot with appropriate message based on progress
    mascot.celebrate_progress(progress)

    # Use the animated eco-progress bar
    create_eco_progress_bar(progress)

    current_section = st.session_state.current_section

    # Show Buzzy's tip for the current section
    mascot.show_tip(current_section)

    for i, question in enumerate(QUESTIONS[current_section]):
        key = f"{current_section}_{i}"
        score = display_question(question, key)
        st.session_state.responses[key] = score

        st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if current_section != list(QUESTIONS.keys())[0]:
            if st.button("⬅️ Previous Section"):
                current_index = list(QUESTIONS.keys()).index(current_section)
                st.session_state.current_section = list(QUESTIONS.keys())[current_index - 1]
                st.rerun()

    with col2:
        if current_section != list(QUESTIONS.keys())[-1]:
            if st.button("Next Section ➡️"):
                current_index = list(QUESTIONS.keys()).index(current_section)
                st.session_state.current_section = list(QUESTIONS.keys())[current_index + 1]
                st.rerun()
        else:
            if st.button("View Results ➡️"):
                st.switch_page("pages/02_recommendations.py")

if __name__ == "__main__":
    main()