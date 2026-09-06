import json



with open("questions.json", "r") as file:
  data = json.load(file)


score = 0

for number,i in enumerate(data, 1):
  print(f"Q {number}/{len(data)}")
  print(f"{i['question']}")
  for k in i["options"]:
    print(f"{k}")
  print("\n\n\n\n")
  main = input("enter your answer\n:")
  if main == i["answer"]:
    print("correct answer")
    score += 1
  else:
    print(f"the correct answer is {i['answer']}")

if score < 5:
  print(f"your score is {score}")
  print("fail")
elif score >= 5 and score <= 8:
   print(f"your score is {score}")
   print("performed well")
elif score >= 9:
  print(f"your score is {score}")
  print("performed excellent")