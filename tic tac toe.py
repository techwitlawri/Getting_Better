from tic import draw_board, check_turn,check_for_win
import os
if __name__=="__main__":
  spot={1:'1', 2:'2', 3:'3', 4:'4',5:'5',
          6:'6', 7:'7',8:'8',9:'9'}
  # draw_board(spot)
  playing = True
  complete= False
  turn=0
  last_turn = -1
  print('Hello!!!,This is a Tic Tac Toe game.')

  while playing:
      
      os.system('cls' if os.name =='nt'else 'clear')
      draw_board(spot)
      if last_turn== turn:
          print('this spot has already been picked, pls pick another spot')
      last_turn=turn
      print('Hello!!!,This is a Tic Tac Toe game.')
      print('Only Two Players Are Allowed. ')
      print('player' + str((turn%2)+1) +" "'turn: pls pick your spot or q to quit')
      # get input from the player
      choice=input()
      if choice=='q':
          playing=False
          #  check if player has picked from 1-9
      elif str.isdigit(choice) and int(choice) in spot:
          if not spot[int(choice)] in {'X','O'}:
            turn+=1
            spot[int(choice)]=check_turn(turn)
      if check_for_win(spot): playing, cpmplete = False, True
      if turn > 8: playing = False

  # os.system('cls' if os.name =='nt'else 'clear')
  # draw_board(spot)
  if complete:
      if check_turn(turn)=='X': print('player 1 wins!!!')
      else: print('player 2 Wins!!')  
  else:
      print('It  Tie')
  print('Thank you for playing!!!')       


  # spot[1] ='x'
  # print('second draw')
  # draw_board(spot)