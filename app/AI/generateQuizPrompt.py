

def generate_quiz_prompt(transcript_text, num_quizzes):
    prompt = prompt = f"""
        You are an expert tutor. Read the following transcript and generate exactly {num_quizzes} multiple-choice questions 
        based on the core concepts taught in the text. Ensure the questions are challenging but fair.
        
        Transcript:
        {transcript_text}
        """
        
    return prompt