wrong_answer_counter=0
flag=True
while flag:
	num_1=int(input("pervoe"))
	num_2=int(input("vtoroe"))
	command=input('input command:')
	if command=='+':
		print(num_1+num_2)
	elif command=='-':
		print(num_1-num_2)
	elif command=='/':
		print(num_1+num_2)
	elif command=='*':
		print(num_1*num_2)
	else:
		print('error')
		wrong_answer_counter+=1;
	while True:
		command=input('Conti? Y/N')
		if command=='N' or command=='n':
			flag=False
			break
		elif command=='Y'or command=='y':
			wrong_answer_counter=0
			break
		else:
			print("error")
			wrong_answer_counter+=1
			if wrong_answer_counter==3:
				flag=False
				print('too much error! Goodbye')
				break


