print("Welcome to AI Quiz Generator")

score = 0

file = open("questions.txt", "r")

questions = file.readlines()

for line in questions:
    data = line.strip().split("|")

    question = data[0]
    correct_answer = data[1]

    print("\n" + question)

    answer = input("Your Answer: ")

    if answer.lower() == correct_answer.lower():
        print("Correct Answer!")
        score = score + 1
    else:
        print("Wrong Answer!")
        print("Correct Answer is:", correct_answer)

print("\nFinal Score:", score, "/", len(questions))

save = open("scores.txt", "a")

save.write("Score: " + str(score) + "/" + str(len(questions)) + "\n")

save.close()