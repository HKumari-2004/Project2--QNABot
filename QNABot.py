import re
import random

# Q&A Pairs containing questions and answers
qa_pairs = {
    "application process": {
        "question": "Could you provide more information about the application process, including any specific requirements or deadlines?",
        "answer": "For the application process, you'll typically need to submit transcripts, test scores, essays, and letters of recommendation. Deadlines vary by institution, so be sure to check the specific requirements for each college you're applying to."
    },
    "financial aid": {
        "question": "I'm curious about the financial aid options available for students. Can you tell me more about scholarships, grants, and other forms of financial assistance?",
        "answer": "Financial aid options can include scholarships, grants, work-study programs, and student loans. It's important to fill out the Free Application for Federal Student Aid (FAFSA) to determine your eligibility for federal financial aid, and to check with each college's financial aid office for additional opportunities."
    },
    "campus life": {
        "question": "What is campus life like at your institution? Are there any notable clubs, organizations, or events that students typically participate in?",
        "answer": "Campus life varies by institution but often includes a vibrant mix of clubs, organizations, and events. These can range from academic clubs to cultural organizations to intramural sports teams. Many colleges also host social events, guest speakers, and cultural festivals throughout the year."
    },
    "academic programs": {
        "question": "I'm interested in learning more about the academic programs offered at your college. Could you provide an overview of the majors, minors, and specializations available?",
        "answer": "Our college offers a wide range of academic programs, including majors, minors, and specializations across various fields of study. Some popular areas of study include STEM (Science, Technology, Engineering, and Mathematics), humanities, social sciences, business, and the arts. You can explore specific programs on our website or by contacting the academic advising office."
    },
    "student support services": {
        "question": "How does your college support student success? Are there resources available for academic advising, career counseling, or mental health services?",
        "answer": "We offer a range of student support services to help students succeed academically, professionally, and personally. These may include academic advising, career counseling, tutoring services, wellness programs, and mental health resources. Our goal is to provide comprehensive support to help students thrive during their college experience."
    },
    "housing options": {
        "question": "What are the housing options for students? Can you tell me about on-campus dormitories, off-campus housing, and any special accommodations available?",
        "answer": "Our college provides a variety of housing options for students, including on-campus dormitories, apartment-style housing, and off-campus accommodations. On-campus housing typically offers amenities such as dining halls, laundry facilities, and social spaces. Special accommodations may be available for students with disabilities or specific needs. For more information, you can contact the housing office."
    },
    "internship opportunities": {
        "question": "Are there opportunities for students to participate in internships or co-op programs? I'm interested in gaining practical work experience while studying.",
        "answer": "Yes, our college values experiential learning and offers various opportunities for students to gain practical work experience through internships, co-op programs, research projects, and community engagement initiatives. These experiences can help students apply classroom knowledge to real-world settings and develop valuable skills for their future careers."
    },
    "study abroad programs": {
        "question": "Do you offer study abroad programs for students? I'm eager to explore opportunities for international education and cultural immersion.",
        "answer": "Yes, we offer study abroad programs that allow students to explore new cultures, languages, and academic opportunities around the world. These programs may range from short-term exchanges to semester-long immersion experiences. Studying abroad can be a transformative experience that enhances your academic and personal growth."
    },
}

# Fun facts about college life
fun_facts = [
    "Did you know? The first college in the United States, Harvard, was established in 1636.",
    "Fun fact: The average student changes their major three times during college!",
    "Here's an interesting fact: College students spend about 30% of their time sleeping.",
    "Did you know? The longest lecture ever delivered was 138 hours long, given by Dr. Richard F. Taflinger at East Carolina University in 2007.",
    "Fun fact: The word 'quiz' originated in the late 18th century, when a Dublin theater owner bet he could introduce a new word into the English language within 24 hours.",
]

# Farewell messages
farewell_messages = [
    "Thank you for chatting with me! If you have any more questions in the future, feel free to come back.",
    "It was great talking to you! Have a fantastic day!",
    "Goodbye for now! Remember, I'm here to help anytime you need assistance.",
    "Until next time! Take care and best of luck with your college journey.",
]

# Empty lists to store conversation history and user information
conversation_history = []


def greet():
    """Welcome message."""
    print("Welcome to the College Q&A Bot! I'm here to assist you with any questions you have about college life.")
    print("To personalize your experience, could you please provide your name?")
    user_name = input("Your name: ")
    print(f"Great, thanks, {user_name}! Feel free to ask me anything about college Admission and Procedures.")


def handle_question(question):
    """Handle user's question and provide an appropriate response."""
    if "fun fact" in question.lower():
        return random.choice(fun_facts)
    
    for keyword, qa_pair in qa_pairs.items():
        if re.search(keyword, question, re.IGNORECASE):
            return qa_pair["answer"]

    return "I'm not sure I understand that question. Could you rephrase it or ask something else?"


def main():
    """Main function to run the Q&A bot."""
    greet()
    while True:
        question = input("You: ")
        answer = handle_question(question)
        print("Bot:", answer)
        conversation_history.append((question, answer))

        # Check if the user wants to end the conversation
        if question.lower() in ["goodbye", "bye", "quit"]:
            print(random.choice(farewell_messages))
            break


if __name__ == "__main__":
    main()
