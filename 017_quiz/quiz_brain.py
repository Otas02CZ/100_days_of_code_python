
from question_model import Question

class QuizBrain:
    
    def __init__(self, given_questions : list[Question]) -> None:
        self.question_number : int = 0
        self.questions_list : list[Question] = given_questions
        self.score : int = 0

    def next_question(self) -> None:
        question : str = self.questions_list[self.question_number].text
        correct_answer : str = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_answer : str = input(f"Q.{self.question_number} {question} (True/False): ")
        self.check_answer(user_answer, correct_answer)
    
    def check_answer(self, user_answer : str, correct_answer : str) -> None:
        if correct_answer.lower() == user_answer.lower():
            print(f"You are right, the answer is {correct_answer}")
            self.score += 1
        else:
            print(f"Unfortunately no, the correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
    
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.questions_list)