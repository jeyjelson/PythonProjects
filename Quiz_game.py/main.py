from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question = q["text"]
    answer = q["answer"]
    new_q = Question(question, answer)
    question_bank.append(new_q)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions:
    quiz_brain.next_q()
