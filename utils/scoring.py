from data.questions import MAX_SCORE

def calculate_score(responses):
    total_score = sum(responses.values())
    percentage = (total_score / MAX_SCORE) * 100

    if percentage < 40:
        return "low", percentage
    elif percentage < 70:
        return "medium", percentage
    else:
        return "high", percentage

def get_score_message(score_level, percentage):
    messages = {
        "low": f"""Your Score: {percentage:.1f}% - There's significant room for improvement, but don't worry!

Your current cleaning practices could be impacting local pollinator populations, but small changes can make a big difference. 
Focus on replacing chemical cleaners with natural alternatives and improving disposal practices.

Remember: Every positive change helps protect our vital pollinator friends! 🐝""",

        "medium": f"""Your Score: {percentage:.1f}% - You're making positive strides!

Your cleaning practices show awareness of pollinator health. You're already helping protect these important creatures!
Some targeted improvements in product choices and outdoor cleaning methods could further increase your impact.

Keep up the great work and explore more pollinator-friendly options! 🦋""",

        "high": f"""Your Score: {percentage:.1f}% - Outstanding pollinator protection!

Your cleaning practices demonstrate excellent awareness of pollinator health. You're a true environmental steward!
Your home is creating a safe haven for these essential creatures.

Share your knowledge and inspire others to make pollinator-friendly choices! 🌺"""
    }
    return messages[score_level]