from random import randint
import random
restart= True


board=[]
mines=[]
r_list=[]
c_list=[]
p_list=[]
#These are different list functions that are used to store information
count=0
num=0
nnumber=0
n=0
row = 0
col= 0
#The different function that would be used as a count system 
board= [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
#This is a list function and also the outline of the board game 

print("   0  1  2  3")
value=0
for row in  (board):
    print (value, row)
    value+=1
#this for statment prints the 4 by 4 board and outlines the x and y values
    
for i in range (1):
  number= random.randint(0,3)
print(number)

  

for x in range(number):
    row= random.randint(0,3)
    r_list.append(row)
    col= random.randint(0,3)
    c_list.append(col)
#this for statment would store random numbers for the rows and columns. These random numbers for the col. and rows would be where the mines would be   
print( r_list)
print(c_list)
    
for k in range (0,3):
  for j in range (0,3):
    board_number= k,j
    p_list.append(board_number)

#this for statment would generate coordinate points and would be stored in the function called p_list
while True:
  if count == number:
    break
  else:
    x=c_list [count]
    y=r_list[count]
    point= x, y
  
    mines.append (point)
    count+=1
#this while statment would recall the random numbers stored into the list function called c_list and r_list
#also this function would join the two random points and they would be the coordinat point where the mines would be on the board and these points would be placed in the function list called mines

  
while True:
  user_row= int(input('Row:'))
  user_col= int(input('Column:'))
  num=0
#the user is going to be ask to choise their value of the row and column which would be the user point
  if user_col>4 or user_row>4:
    break 
  user_point= user_col, user_row

#this if statement would make sure the values the user inputs is present on the game board
#also the users input of their chosen row and column are put together and are called user_point
  for i in mines:
      #this for statment would check each value in the mines list
    if user_point == i:
        n+= 1
  if n==1:
      print("You are on a mine")
    #this statment would print and the game would end because the person point is where the mine is at 
    break

  elif user_point!= mines:
    for i in r_list:
      if i== (user_row+1) or i == (user_row-1):
        num+=1
    for j in c_list:
      if j== (user_col +1) or j== (user_col -1):
          num+=1
#so, if the user_point doesnt equal to any of the mine point then these for and if statment would check if thereis any mines around the coordinat point the user picked 

    board[user_col][user_row]= num
    print("   0  1  2  3")
    value=0
    for row in  (board):
        print (value, row)
        value+=1
            
#this for statment would re print the the 4 by 4 board however, it would add the amount of mines around the point 
        
   
