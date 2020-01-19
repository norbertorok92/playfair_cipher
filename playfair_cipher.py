
key=input("Enter key: ")
key=key.replace(" ", "") # schimbam " " cu ""
key=key.upper()

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]

result=list() # definim o lista goala
for c in key: 
    if c not in result:
        if c=='J':
            result.append('I') # daca caracterul este J inlocuim cu I
        else:
            result.append(c) # punem la sfarsitul listei caracterul daca nu exista deja in lista

flag=0
for i in range(65,91): # facem un loop peste alfabet (range(65,91) insemnand caractere ASCII UPPERCASE)
    if chr(i) not in result: # daca caracterul nu este deja in lista
        if i==73 and chr(74) not in result: # si daca caracterul este I si J inca nu este in lista
            result.append("I") # punem un I la sfarsitul listei
            flag=1
        elif flag==0 and i==73 or i==74:
            pass
        else:
            result.append(chr(i)) # punem la sfarsitul listei caracterele in ordine alfabetica

k=0
my_matrix=matrix(5,5,0) # initializare matrix 5x5
for i in range(0,5): # facem matrixul
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1
    # matricul va arata cam asa:
    # [['M', 'E', 'T', 'A', 'N'],
    #  ['O', 'B', 'C', 'D', 'F'],
    #  ['G', 'H', 'I', 'K', 'L'],
    #  ['P', 'Q', 'R', 'S', 'U'],
    #  ['V', 'W', 'X', 'Y', 'Z']]

def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Encryption
    msg=str(input("Enter Message: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT: ",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #decryption
    msg=str(input("Enter Cipher Text: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT: ",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption \n 3.EXIT \n What would you like to do? "))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice! ")
