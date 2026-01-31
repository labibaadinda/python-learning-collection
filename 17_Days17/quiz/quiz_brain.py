class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
    def next_question(self):
        # retrieve pertanyaan saat ini berdasarkan nomor urut
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # menanyakan pertanyaan kepada pengguna
        user_answer = input(f"Q{self.question_number}: {current_question.text}? (True/False) ")
        return user_answer

    def check_score(self, user_answer):
        current_question = self.question_list[self.question_number - 1]
        real_answer = current_question.answer
        if user_answer.lower() == real_answer.lower():
            self.score += 1

        print(f"The correct answer was: {real_answer}")
        print(f"Your Score: {self.score}/{self.question_number}")
        print("\n")













