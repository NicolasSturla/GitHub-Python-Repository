from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

# juego de preguntas y respuestas pregrabadas que lleva el puntaje. 
    
for question in question_data:
    question_text = question['text']
    question_answer= question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while QuizBrain.still_has_questions(quiz):
    quiz.next_question()

print("You have complete the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")