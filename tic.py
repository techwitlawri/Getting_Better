def draw_board(spot):
  # board="1|2|3|\n|4|5|6|\n|7|8|9|"
  board=(f"|{spot[1]}|{spot[2]}|{spot[3]}|\n|"
           f"{spot[4]}|{spot[5]}|{spot[6]}|\n|"
           f"{spot[7]}|{spot[8]}|{spot[9]}|")
  print(board)
def check_turn(turn):
  if turn % 2 ==0: return'O'
  else:return 'X'  
def check_for_win(spot):
  # Handle horizronial case
  if (spot[1]==spot[2]==spot[3])\
    or(spot[4]==spot[5]==spot[6])\
    or(spot[7]==spot[8]==spot[9]):
    return True
  # Handle vertical cases
  elif(spot[1]==spot[4]==spot[7])\
    or(spot[2]==spot[5]==spot[8])\
    or(spot[3]==spot[6]==spot[9]):
    return True


  elif(spot[1]==spot[5]==spot[9])\
    or(spot[3]==spot[5]==spot[7]):
    return True

  else: return False