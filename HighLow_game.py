def HiLogame(predict, points, final):
    restart=True
    while(restart):
        restart= False
        
        while(predict ==1 or predict== 0):
            import random
            from random import randint
            random_num= randint(1,13)
        
            if(predict ==0 and random_num>=1 and random_num<=6):
                print('Number is:',random_num)
                print('You Win')
                final_points= points*2+final            
                print('You have',final_points,'points')
                playagain= input('Play again (yes or no):')
             
                if(playagain == 'yes'):
                    final=final_points
                    print()
                    points= int(input('Enter points to risk:'))
                    predict= int(input('Predict <1-High, 0-Low>'))
                    restart=True
                    
                    break
                else:
                    break
    
            elif(predict==0 ):
                print('Number is:',random_num)
                print('You Loses')
                total_points5= final-points
                print('You have',total_points5,'points')
                playagain= input('Play again (yes or no):')
                if(playagain == 'yes'):
                    final=total_points5
                    print()
                    points= int(input('Enter points to risk:'))
                    predict= int(input('Predict <1-High, 0-Low>'))
                    restart=True
                                        
                    break
                    
                else:
                    break
    
        
            elif(predict==1 and random_num>=8 and random_num<=13):
                print('Number is:',random_num )
                print('You Win')
                total_points4= points*2+final
                print('You have',total_points4,'points')
                playagain= input('Play again (yes or no):')
                if(playagain == 'yes'):
                    
                    final=total_points4
                    print()
                    points= int(input('Enter points to risk:'))
                    predict= int(input('Predict <1-High, 0-Low>'))
                    restart=True
                    
                    break
                            
                else:
                    break

        
            elif(predict==0 or predict==1 and random_num == 7):
                print('Number is:',random_num )
                print('You Win')
                total_points1=final-points
                print('You have',total_points1,'points')
                playagain= input('Play again ( yes or no):')
                if(playagain == 'yes'):
                    final=total_points1
                
                    print()
                    points= int(input('Enter points to risk:'))
                    predict= int(input('Predict <1-High, 0-Low>'))
                    restart=True
                    
                    break
                    
                else:
                    break

        
            elif(predict==1 ):
                print('Number is:',random_num)
                print('You Loses')
                total_points2= final- points
                print('You have',total_points2,'points')
                playagain= input('Play again ( yes or no):')
                if(playagain == 'yes'):
                    final=total_points2
                    
                    print()
                    points= int(input('Enter points to risk:'))
                    predict= int(input('Predict <1-High, 0-Low>'))
                    restart=True
                    
                    break
                else:
                    break
        



print('High Low Game')
print()
print('RULES')
print('Numbers 1 through 6 are low')
print('Numbers 8 through 13 are high')
print('Numbers 7 is neither high or low')
print()
print('You have 1000 points.')
final=1000
print()
points= int(input('Enter points to risk:'))
predict= int(input('Predict <1-High, 0-Low>'))
HiLogame(predict, points,final)
