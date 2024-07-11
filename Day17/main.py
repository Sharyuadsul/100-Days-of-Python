from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    new_q = Question(item["question"], item["correct_answer"])
    question_bank.append(new_q)

# print(question_bank)
# print(question_bank[0].text)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_ques():
    quiz_brain.next_question()

print("You have Completed your Quiz!!")
print(f"You have score of: {quiz_brain.score}/{len(question_bank)}")
