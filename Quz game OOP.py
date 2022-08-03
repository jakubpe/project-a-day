import random


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class Game:
    def __init__(self, library):
        self.game_data = library
        self.score = 0
        self.question_number = 0

    def still_have_q(self):
        return self.question_number < len(self.game_data)

    # def random_question(self):
    #     question = random.choice(self.game_data)
    #     print(question.text)
    #     print(question.answer)
    #     if input("Provide answer: ") == question.answer:
    #         self.score += 1
    #         print("Good answer, current score is: {}".format(self.score))
    #         return True
    #     else:
    #         print("Game over, your score is: {}".format(self.score))
    #         return False

    def next_question(self):
        answer = input("Q.{}: ".format(str(self.question_number + 1)) + self.game_data[self.question_number].text +
                       " True/False: ")
        if answer == self.game_data[self.question_number].answer:
            self.score += 1
            self.question_number += 1
            print("Great, your current score is: {}".format(self.score))
        else:
            print("Wrong")
            self.question_number += 1

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it "
             "home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a "
             "state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# new = Question("2+3=5", True)
# print(new.text)
# print(new.answer)
# print(len(question_data))
question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))
# print(question_bank[0].text)
# print(question_bank[0].answer)
game = Game(question_bank)
# while game.random_question():
#     pass
while game.still_have_q():
    game.next_question()
print("Your final score is {}".format(game.score))
