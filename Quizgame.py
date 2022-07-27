print("welcome to the Quiz game :)" )

answer = input("do you wanna play? ")
if answer.lower() != "yes":
	quit()
else:
	print("let's play! ")
	score = 0
print("who is prime minister of Nepal? ")
answer = input()
if answer.lower() == "sher bahadur deuba":
	print("correct!")
	score+=1
else:
	print("incorrect")
	
	
print("who is mahanayak of nepal? ")
answer = input()
if answer.lower() == "rajesh hamal":
	print("correct!")
	score+=1
else:
	print("incorrect")
	
print("who is first female president of nepal? ")
answer = input()
if answer.lower() == "bidhya devi bhandari":
	print("correct!")
	score+=1
else:
	print("incorrect")

print("who is know as comedian politics leader of nepal? ")
answer = input()
if answer.lower() == "kp oli":
	print("correct!")
	score +=1
else:
	print("incorrect")
	
print("what is the full form of LMAO? ")
answer = input()
if answer.lower() == "laughing my ass off":
	print("correct!")
	score+=1
else:
	print("incorrect")
	
print("your score is",score)
print("you got",score/5*100,"%")


	

