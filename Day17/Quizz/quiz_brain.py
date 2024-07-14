

class QuizBrain:
    def __init__(self, q_bank):
        self.question_no = 0
        self.question_list = q_bank
        self.score = 0

    def still_has_ques(self):
        return self.question_no< len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input (f"Q {self.question_no}: {curr_question.text} (True/False)? ")
        self.check_ans(ans, curr_question.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You are Correct!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The Correct Answer was {correct_ans}")
        print(f"Your Current Score is {self.score}/{self.question_no}")
        print("\n")
