questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["  A. Paris", "  B. London", "  C. Berlin", "  D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["  A. Spanish", "  B. Portuguese", "  C. English", "  D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["  A. 1", "  B. 2", "  C. 3", "  D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["  A. Harper Lee", "  B. Mark Twain", "  C. J.K. Rowling", "  D. Ernest Hemingway"],
        "answer": "A"
    }
]
score=0
while True:
  print(questions[0]['prompt'])
  for option in questions[0]['options']:
    print(option)
  answer=input('enter the write answer A to D:')
  if answer=='A':
    print('right answer👏🏻👏🏻')
    score+=1
  else:
    print('wrong answer❌❌')
  print(questions[1]['prompt'])
  for option in questions[1]['options']:
    print(option)
  answer=input('enter the write answer A to D:')
  if answer=='B':
    print('right answer👏🏻👏🏻')
    score+=1
  else:
    print('wrong answer❌❌')
  print(questions[2]['prompt'])
  for option in questions[2]['options']:
    print(option)
  answer=input('enter the write answer A to D:')
  if answer=='B':
    print('right answer👏🏻👏🏻')
    score+=1
  else:
    print('wrong answer❌❌')
  print(questions[3]['prompt'])
  for option in questions[3]['options']:
    print(option)
  answer=input('enter the write answer A to D:')
  if answer=='A':
    print('right answer👏🏻👏🏻')
    score+=1
  else:
    print('wrong answer❌❌')

  print(f'you finished, your score is:{score}/4')
  break
  