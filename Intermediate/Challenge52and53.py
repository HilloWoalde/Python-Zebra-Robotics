questions = []
answers = []
answer = ""
correct = 0
tot_quests = 0
score = 0.0

fileing = open("QuestionaireforChallenge53.txt", "r")
lines = fileing.readlines()
for i in range(0, len(lines)):
    if (i % 2) == 0:
        questions.append(lines[i].strip()) 
    else:
        answers.append(lines[i].strip())
print(questions)
print(answers)
print("You will now be quizzed")
for i in range(0, len(questions)):
    if input(questions[i]) == answers[i]:
        correct += 1
score = (correct/len(questions)*100)
print(str(score)+"%")
