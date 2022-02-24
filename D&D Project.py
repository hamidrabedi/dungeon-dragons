import random
import msvcrt
import os
import math
from termcolor import colored


def creatboeard(Size: int) -> list:
	The_Board = []
	for i in range(Size):
		for j in range(Size):
			The_Board.append((i, j))
	return The_Board


def moveplayer(Position: tuple, Choice: str, Size: int) -> tuple:

	Poslist = list(Position)
	if Choice == b's':
		Poslist[1] += 1
	elif Choice == b'a':
		Poslist[0] -= 1
	elif Choice == b'd':
		Poslist[0] += 1
	elif Choice == b'w':
		Poslist[1] -= 1
	print("\n")
	if Poslist[0] > Size-1:
		print("You just hit the wall Brotha!!!")
		Poslist[0] -= 1
		print("Press any key to continue")
		msvcrt.getch()
	if Poslist[1] > Size-1:
		print("You just hit the wall Brotha!!!")
		Poslist[1] -= 1
		print("Press any key to continue")
		msvcrt.getch()
	if Poslist[0] < 0:
		print("You just hit the wall Brotha!!!")
		Poslist[0] += 1
		print("Press any key to continue")
		msvcrt.getch()
	if Poslist[1] < 0:
		print("You just hit the wall Brotha!!!")
		Poslist[1] += 1
		print("Press any key to continue")
		msvcrt.getch()

	return tuple(Poslist)


def movedragon(Position: tuple, player_P: tuple, Size: int) -> tuple:
	Poslist = list(Position)
	X1, Y1 = player_P
	X2, Y2 = Position
	Temp1 = abs(Y2 - Y1)
	Temp2 = abs(X2 - X1)
	Float_Distance = math.sqrt((Temp1**2)+(Temp2**2))

	temp_dragon_position = Poslist.copy()
	Player_Dragon_Distance = [Position[0]-player_P[0], Position[1]-player_P[1]]
	ChanceToGetCloseToPlayer = random.randint(1, 100)

	if 3 < Float_Distance < 4 or Float_Distance == 3:
			if ChanceToGetCloseToPlayer < 41:
				if abs(Player_Dragon_Distance[0]) >= abs(Player_Dragon_Distance[1]):
					if Player_Dragon_Distance[0] > 0:
						Poslist[0] -= 1
					else:
						Poslist[0] += 1
				elif Player_Dragon_Distance[1] > 0:
						Poslist[1] -= 1
				else:
					Poslist[1] += 1
	elif 2 < Float_Distance < 3 or Float_Distance == 2:
			if ChanceToGetCloseToPlayer < 61:
				if abs(Player_Dragon_Distance[0]) >= abs(Player_Dragon_Distance[1]):
					if Player_Dragon_Distance[0] > 0:
						Poslist[0] -= 1
					else:
						Poslist[0] += 1
				elif Player_Dragon_Distance[1] > 0:
						Poslist[1] -= 1
				else:
					Poslist[1] += 1
	elif 0<Float_Distance<2 or Float_Distance==1: 
			if ChanceToGetCloseToPlayer<81:
				if abs(Player_Dragon_Distance[0])>= abs(Player_Dragon_Distance[1]):
					if Player_Dragon_Distance[0]>0:
						Poslist[0]-=1
					else:
						Poslist[0]+=1
				elif Player_Dragon_Distance[1]>0:
						Poslist[1]-=1
				else:
					Poslist[1]+=1

	if temp_dragon_position==Poslist:
		if ChanceToGetCloseToPlayer>20:
			while True:          
					x=random.randint(1,4)
					if x==1:
						if Poslist[1]!=0:
							Poslist[1]-=1
							break
					elif x==2:
						if Poslist[0]!=Size-1:
							Poslist[0]+=1
							break
					elif x==3:
						if Poslist[1]!= Size-1:
							Poslist[1]+=1
							break
					elif x==4:
						if Poslist[0]!=0:
							Poslist[0]-=1
							break    
					print(Poslist)
		else:
			if abs(Player_Dragon_Distance[0])>= abs(Player_Dragon_Distance[1]):
				if Player_Dragon_Distance[0]>0:
						Poslist[0]-=1
				else:
						Poslist[0]+=1
			elif Player_Dragon_Distance[1]>0:
						Poslist[1]-=1
			else:
					Poslist[1]+=1


	
	
	return tuple(Poslist) 

def showboard(Board: list , Size: int,Position: tuple):
	Player_here=False
	print(" _",end="")
	print(" _"*(Size-1))
	Counter_while=0  
	while Counter_while!=Size:
		for i in range(Size+1):
			if i !=Size:
				if Position== (i,Counter_while):    
					print("|",end="")
					print(colored("X", "cyan"),end= "")
				else: 
					print("|_",end="")             
			else:
				print("|",end= "\n")
		Counter_while+=1

def getrandom(Board_Size: int) -> tuple :
	X= random.randint(0,Board_Size-1)
	Y= random.randint(0,Board_Size-1)
	Position= (X, Y)
	return Position

def playervsdragon(Player_pos: tuple , Dragon_Pos: tuple):
	if Player_pos==Dragon_Pos:
		os.system('cls')
		print("Whoops!\nDragon just ate you!\n You lost! ")
		print("\n1.Play Again \n2.Quit the game\n")
		
		while True:
			Choose=msvcrt.getch()
			if Choose==b'1':
				main()
			elif Choose==b'2':
				exit(0)   

def iswinner(Door: tuple , Player_Position: tuple):
	if Door==Player_Position:
		os.system('cls')
		print("GG WP!\n Congrats You Won!! ")
		print("\n1.Play Again \n2.Quit the game\n")
		
		while True:
			Choose=msvcrt.getch()
			if Choose==b'1':
				main()
			elif Choose==b'2':
				exit(0)   

def distance(Player_position: tuple, dragon_position: tuple) ->str:
	X1, Y1= Player_position
	X2, Y2= dragon_position
	Temp1= abs(Y2- Y1)
	Temp2= abs(X2- X1)
	Distance=math.sqrt((Temp1**2)+(Temp2**2))
	Distance_int= Distance
	Alert= str()
	if 3<Distance<4 or Distance==3:
		Alert= "Dragon is close to you !"
	elif 3>Distance>2 or Distance==2:
		Alert= "Its getting CLOSER !!!"
	elif 2>Distance>0  or Distance==1:
		Alert= "DANGER !! DANGER !!"
	return Alert     

def smartdragon():
	pass

def extralife():
	os.system('cls')
	print("You have been eaten by the dragon ! \n But you have an extra life!")
	print("This is your last chance!")
	msvcrt.getch()

def main():
	while True:
		os.system('cls')
		print("Welcome To D&D")
		Board_Size= input("whats the size of the board?  ")
		if Board_Size.isnumeric() and Board_Size!= '0':
			Board_Size=int(Board_Size)
			break


	Player_Position= getrandom(Board_Size)
	Dragon_Position= getrandom(Board_Size)
	DoorofHeaven= getrandom(Board_Size)
	Game_board=creatboeard(Board_Size )
	Extra_Life_Position= getrandom(Board_Size)
	Extra_Life= False

	while True:
		os.system('cls')
		
		while True:
			os.system('cls')     
			showboard(Game_board, Board_Size, Player_Position)
			print(colored("Whats your move? (Use WASDA) :  ",'green'))
			print(colored(distance(Player_Position, Dragon_Position),"red","on_yellow"),end='\n')
			print(Extra_Life_Position)
			Player_Choice= msvcrt.getch()
			Player_Position_temp= Player_Position
			Player_Position= moveplayer(Player_Position, Player_Choice,Board_Size)		
					
			if Player_Position_temp!=Player_Position:
				if Player_Position==Extra_Life_Position:
					os.system('cls')
					showboard(Game_board, Board_Size, Player_Position)
					Extra_Life= True	
					print(colored("You just got an Extra Life !!!" ,"red","on_green"))
					msvcrt.getch()
					Extra_Life_Position= 0
				break

		if Player_Position==Dragon_Position:
			if Extra_Life:
				extralife()
				Extra_Life= False
				Player_Position= getrandom(Board_Size)
			else:	
				playervsdragon(Player_Position, Dragon_Position)
		Dragon_Position=movedragon(Dragon_Position,Player_Position,Board_Size)
		iswinner(DoorofHeaven, Player_Position)
		if Player_Position==Dragon_Position:
			if Extra_Life:
				extralife()
				Extra_Life= False
				Player_Position= getrandom(Board_Size)
			else:	
				playervsdragon(Player_Position, Dragon_Position)


if __name__=="__main__":
	main()
