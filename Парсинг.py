name = input ("enter way to file ")
dic=dict()
with open(name, 'r') as f:
    for str in f:
        if str[0]!='#' and str[0]!='\n' and str[0]!=';':
            listtime=str.split("#",1)
            move=listtime[0]
            move=move.replace('\n','')
            move=move.split(" ",1) 
            if len(move)==1:
                move.append('none')
            dic[move[0]]=move[1] 
flag=True     
while flag:
    command=input('Введите запрос в формате(get param ...): ')
    s=command.split()
    for key in dic:
        if s[2]==key:
            if dic[key]!='null':
                print(key,':',dic[key])
            else:
                print(key,':','none')
    while True:
        str_cont=input('Continue?(Y/N): ')
        if str_cont.lower()=='y':
            break;
        elif str_cont.lower()=='n':
            flag=False
            break