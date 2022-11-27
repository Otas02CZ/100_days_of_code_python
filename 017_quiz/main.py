

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank : list = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz : QuizBrain = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have reached the end of the quiz. :D")
print(f"Your score is {quiz.score}/{quiz.question_number}")