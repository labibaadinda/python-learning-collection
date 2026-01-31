from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# question_bank = [
#     Question(q['text'], q['answer'])
#     for q in question_data
# ]
#
# for question in question_bank:
#     question.display()

question_bank = []
for question in question_data:
    question_text = question['text']
    answer = question['answer']
    question_bank.append(Question(question_text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_answer = quiz.next_question()
    quiz.check_score(user_answer)

print("You've completed the quiz")
print(f"Your dinal score was: {quiz.score}/{quiz.question_number}")





