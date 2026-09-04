
expenses = [
    {
        "amount": 250,
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": 100,
        "category": "Travel",
        "description": "Metro"
    },
    {
        "amount": 150,
        "category": "Food",
        "description": "Snacks"
    },
    {
        "amount": 500,
        "category": "Shopping",
        "description": "T-shirt"
    },
    {
        "amount": 80,
        "category": "Travel",
        "description": "Auto"
    }
]



while True:

    print("=====EXPENSE TRACKER=====")
    main = input("1.add expense \n2.view expense \n3.show summary \n4.exit \n\nenter your choice:")

    if main == "1":
        print("add your expense")
        try:
          amount = int(input("enter your amount \n:"))
        except ValueError:
           print("please enter valid number !!")
           continue
        if amount <= 0:
            print("you can't add amount equal to or less than 0")
            continue
        category = input("enter your category \n:")
        description = input("enter description \n:") 
        expense = {
            "amount" : amount,
            "category" : category,
            "description" : description
        }
        expenses.append(expense)
    elif main == "2":
        for i in expenses:
            print(f"amount : {i['amount']} category : {i['category']} description : {i['description']}")
    elif main == "3":
        category_total = {}
        highest_category = ""
        highest_amount = 0
        total = 0
        for i in expenses:
          total = i["amount"] + total
        for i in expenses:
          if i["category"] in category_total:
            category_total[i["category"]] += i["amount"]  #if category existed add amount its amount to category total
          else: 
            category_total[i["category"]] = i["amount"]  #if category doen't existed in category_total then add category as well as amount to dictionary category_total
        for category, amount in category_total.items():
           if amount > highest_amount:
              highest_amount = amount
              highest_category = category
        print("====SUMMARY====")
        print(f"total expense amount is ${total}")
        for i, j in category_total.items():
          print(f"category : {i} | total {j}")
        print(f"highest spending catgory is {highest_category} \nhighest amount spent is ${highest_amount}")


    elif main == "4":
       print("thanks for using my program")
       print("name : MOHD ATHAR \ncourse : BCA \nsection : EB")
       break


    