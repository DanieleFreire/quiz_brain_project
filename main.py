from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_q = Question(item['question'], item['correct_answer'])
    # print(new_q.text)
    # print(new_q.answer)
    # question_bank.append(new_q.text)
    # question_bank.append(new_q.answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")