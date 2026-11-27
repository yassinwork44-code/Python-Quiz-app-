import random
words=['java','python','css','sql','html']
chosen_word=words[random.randint(0,len(words)-1)]
print(chosen_word)
word_display=['-' for _ in chosen_word]
attemps=8
index=0
while attemps>0 and '-' in word_display:
  guess=input('enter a letter:').lower()
  if chosen_word[index]==guess:
    print('right letter')
    word_display[index]=guess
    print(' '.join(word_display))
    index += 1
  elif chosen_word[index]!=guess:
    attemps-=1
    print(f'you have {attemps} attempts left')
if '-' not in word_display:
    print('You survived')
    print(f"you found the right word, it's {chosen_word} ✅")
if attemps==0:
    print('you lost❌, you finished you attempts')