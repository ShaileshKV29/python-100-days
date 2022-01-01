from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

questions = QuizBrain(question_bank)

while questions.still_has_questions():
    questions.next_question()

# print(question_bank)
print("You have completed the quiz")
print(f"Your final score is {questions.score}/{questions.question_number}")
