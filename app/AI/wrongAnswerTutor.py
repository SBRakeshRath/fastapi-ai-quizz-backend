def wrong_answer_tutor_prompt(input_data, relevant_context):
    
    
    question = input_data.question
    user_wrong_answer = input_data.user_wrong_answer
    correct_answer = input_data.correct_answer
    
    prompt  = f"""
        You are an encouraging, expert tutor. 
        The student was asked: "{question}"
        The correct answer is: "{correct_answer}"
        The student incorrectly guessed: "{user_wrong_answer}"

        Here is the exact excerpt from the video transcript that explains this topic:
        ---
        {relevant_context}
        ---

        Explain WHY the student's answer is wrong, and teach them the correct concept using ONLY the provided transcript excerpt. 
        Keep your tone friendly, concise, and helpful. Output a clean text paragraph without any markdown formatting.
        """
        
    return prompt