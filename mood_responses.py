def mood_response(mood):
    if mood.lower() == 'happy':
        return "Great to hear that you're happy!"
    elif mood.lower() == 'sad':
        return "I'm sorry to hear that you're feeling sad."
    elif mood.lower() == 'excited':
        return "That's fantastic! Excitement is contagious."
    elif mood.lower() == 'angry':
        return "Take a deep breath. It's okay to feel angry sometimes."
    else:
        return "I'm not sure how to respond to that mood. Let's try again later."
