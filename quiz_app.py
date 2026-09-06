import json



with open("ace/questions.json", "r") as file:
  data = json.load(file)


score = 0

for i in data:
  print(f"{i['question']}")
  for k in i["options"]:
    print(f"{k}")
  print("\n\n\n\n")
  main = input("enter your answer\n:")
  if main == i["answer"]:
    print("correct answer")
    score += 1
print(f"your score is {score}")
  
  